"""Actual export checks; these do not establish artistic quality."""
from pathlib import Path
import hashlib
import importlib.util
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "export_frame.py"


def write_png(path, width, height):
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    rows = (b"\x00" + bytes((70, 88, 104)) * width) * height
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b""))


class ExportFrameTests(unittest.TestCase):
    def module(self):
        self.assertTrue(SCRIPT.is_file(), "Fixed output requires the export helper")
        spec = importlib.util.spec_from_file_location("export_frame", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_original_ratio_and_no_upscaling(self):
        module = self.module()
        for source, edge, expected in (((1024, 1536), 540, (360, 540)), ((1536, 1024), 540, (540, 360)), ((1000, 1000), 540, (540, 540)), ((320, 200), 540, (320, 200)), ((1920, 1280), 960, (960, 640)), ((1536, 1024), 0, (1536, 1024))):
            with self.subTest(source=source, edge=edge):
                self.assertEqual(module.scaled_size(*source, edge), expected)

    @unittest.skipUnless(shutil.which("sips"), "Actual resampling requires macOS sips")
    def test_actual_export_dimensions_and_native_preservation(self):
        module = self.module()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name, size, edge, expected in (("portrait", (1024, 1536), 540, (360, 540)), ("landscape", (1536, 1024), 540, (540, 360)), ("square", (700, 700), 540, (540, 540)), ("small", (320, 200), 540, (320, 200)), ("native", (1536, 1024), 0, (1536, 1024)), ("override", (1920, 1280), 960, (960, 640))):
                with self.subTest(name=name):
                    source, output = root / f"{name}.png", root / f"{name}-delivery.png"
                    write_png(source, *size)
                    before = hashlib.sha256(source.read_bytes()).digest()
                    result = subprocess.run([sys.executable, str(SCRIPT), str(source), str(output), "--max-edge", str(edge)], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(module.read_png_size(output), expected)
                    self.assertEqual(hashlib.sha256(source.read_bytes()).digest(), before)

    def test_rejects_overwriting_native_and_existing_delivery(self):
        self.module()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source, output = root / "native.png", root / "existing.png"
            write_png(source, 10, 10)
            write_png(output, 12, 12)
            original, existing = source.read_bytes(), output.read_bytes()
            for args in ((str(source), str(source)), (str(source), str(output)), (str(source), str(root / "bad.png"), "--max-edge", "-1")):
                result = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)
                self.assertEqual(result.returncode, 2)
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(output.read_bytes(), existing)

    @unittest.skipUnless(shutil.which("sips"), "JPEG fixture requires macOS sips")
    def test_jpeg_native_converts_to_png_without_modification(self):
        module = self.module()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            fixture, source, output = root / "fixture.png", root / "native.jpg", root / "delivery.png"
            write_png(fixture, 800, 1200)
            subprocess.run([shutil.which("sips"), "-s", "format", "jpeg", str(fixture), "--out", str(source)], check=True, capture_output=True)
            before = source.read_bytes()
            result = subprocess.run([sys.executable, str(SCRIPT), str(source), str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(module.read_png_size(output), (360, 540))
            self.assertEqual(source.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
