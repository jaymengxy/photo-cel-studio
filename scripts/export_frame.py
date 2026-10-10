"""Export generated frames as PNG at a verified long edge; retain the native."""
from pathlib import Path
import argparse
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile


def read_png_size(path):
    with Path(path).open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[8:16] != b"\x00\x00\x00\rIHDR":
        raise ValueError("Input/output must be a generated PNG frame")
    width, height = struct.unpack(">II", header[16:24])
    if not width or not height:
        raise ValueError("PNG dimensions must be positive")
    return width, height


def scaled_size(width, height, max_edge):
    if min(width, height) <= 0 or max_edge < 0:
        raise ValueError("Dimensions must be positive and max edge must be nonnegative")
    if max_edge == 0 or max(width, height) <= max_edge:
        return width, height
    ratio = max_edge / max(width, height)
    return max(1, round(width * ratio)), max(1, round(height * ratio))


def read_image_size(path):
    try:
        return read_png_size(path), True
    except ValueError:
        sips = shutil.which("sips")
        if not sips:
            raise RuntimeError("sips is required for non-PNG native conversion; native retained")
        result = subprocess.run([sips, "-g", "pixelWidth", "-g", "pixelHeight", str(path)], capture_output=True, text=True)
        width = re.search(r"pixelWidth:\s*(\d+)", result.stdout)
        height = re.search(r"pixelHeight:\s*(\d+)", result.stdout)
        if result.returncode or not width or not height:
            raise ValueError("Native format is unsupported by sips; use an available converter, native retained")
        size = int(width.group(1)), int(height.group(1))
        if min(size) <= 0:
            raise ValueError("Native dimensions must be positive")
        return size, False


def export_frame(source, output, max_edge=540):
    source, output = Path(source).resolve(), Path(output).resolve()
    if source == output:
        raise ValueError("Delivery must be separate from the native input")
    if output.exists():
        raise ValueError("Delivery already exists; choose a new output path")
    if output.suffix.lower() != ".png":
        raise ValueError("Delivery filename must end in .png")
    original, source_is_png = read_image_size(source)
    expected = scaled_size(*original, max_edge)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="cel-export-", dir=output.parent) as folder:
        temporary = Path(folder) / "delivery.png"
        if expected == original and source_is_png:
            shutil.copyfile(source, temporary)
        else:
            sips = shutil.which("sips")
            if not sips:
                raise RuntimeError("sips is unavailable; native retained, reduced delivery not created")
            try:
                command = [sips, "-s", "format", "png"]
                if expected != original:
                    command.extend(["-Z", str(max_edge)])
                subprocess.run([*command, str(source), "--out", str(temporary)], check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as exc:
                raise RuntimeError(f"sips export failed: {exc.stderr.strip()}") from exc
        actual = read_png_size(temporary)
        if any(abs(a - e) > 1 for a, e in zip(actual, expected)) or max(actual) != max(expected):
            raise RuntimeError(f"Unexpected exported dimensions: {actual}, expected {expected}")
        with output.open("xb") as destination, temporary.open("rb") as generated:
            shutil.copyfileobj(generated, destination)
    return {"native": str(source), "delivery": str(output), "width": actual[0], "height": actual[1], "max_edge": max_edge, "upscaled": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--max-edge", type=int, default=540, help="Long edge in pixels; 0 retains native size")
    args = parser.parse_args()
    try:
        result = export_frame(args.source, args.output, args.max_edge)
    except (OSError, ValueError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
