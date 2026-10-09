"""Dependency-free structural regression checks for the photo-cel-studio Skill.

These tests verify documentation contracts, not image-generation quality.
Actual image edits must be evaluated with tests/scenarios.md.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODES = (
    "urban-cinematic", "quiet-dramatic", "dynamic-action", "youth-energetic",
    "sci-fi-industrial", "everyday-still-life", "landscape-cinematic",
    "pet-character", "vehicle-mechanical", "architecture-graphic",
    "portrait-character", "food-lifestyle", "macro-nature", "interior-atmosphere",
)
ATMOSPHERES = ("neon-night", "golden-hour", "rainy", "snowy", "misty", "backlit")
REFERENCES = (
    "source-analysis", "preservation-rules", "cel-style-grammar", "scene-modes",
    "atmosphere-selection", "prompt-construction", "quality-gates",
)
DEFAULTS = {
    "style_strength": "balanced",
    "identity_lock": "high",
    "background_policy": "simplify",
    "composition_policy": "source-guided",
    "scene_mode": "auto",
    "atmosphere_profiles": "auto",
    "aspect_ratio": "original",
    "typography": "none",
    "output": "single-frame",
    "revision_mode": "new-concept",
}
MODE_HEADINGS = (
    "When to use", "Source cues", "Composition strategy", "Linework", "Palette",
    "Shadow grammar", "Background policy", "Preservation guardrails",
    "Negative constraints", "Quality checks",
)
ATMOSPHERE_HEADINGS = (
    "When to use", "Source evidence", "Lighting strategy", "Palette",
    "Rendering grammar", "Compatibility", "Preservation guardrails",
    "Negative constraints", "Quality checks",
)


def read(relative: str) -> str:
    path = ROOT / relative
    assert path.is_file(), f"Missing required file: {relative}"
    return path.read_text(encoding="utf-8")


def headings(text: str):
    return set(re.findall(r"^#{2,4}\s+(.+)$", text, re.M))


class SkillContractTests(unittest.TestCase):
    def test_entrypoint_has_valid_frontmatter(self):
        text = read("SKILL.md")
        self.assertRegex(text, r"\A---\n[\s\S]+?\n---\n")
        self.assertIn("name: photo-cel-studio", text.split("---", 2)[1])
        self.assertRegex(text.split("---", 2)[1].lower(), r"description:.*(photo|photograph).*(cel|animation)")

    def test_default_preset_matches_spec(self):
        text = read("presets/default.yaml")
        pairs = dict(re.findall(r"^([a-z_]+):\s*([\w-]+)\s*$", text, re.M))
        for k, v in DEFAULTS.items():
            self.assertEqual(pairs.get(k), v, k)
        self.assertEqual(set(pairs), set(DEFAULTS))

    def test_required_reference_files_exist(self):
        entry = read("SKILL.md")
        for ref in REFERENCES:
            path = f"references/{ref}.md"
            read(path)
            self.assertIn(path, entry)

    def test_initial_modes_are_registered(self):
        registry = read("references/scene-modes.md")
        for mode in MODES:
            self.assertIn(f"modes/{mode}.md", registry, mode)
            read(f"modes/{mode}.md")
        paths = re.findall(r"modes/([a-z-]+)\.md", registry)
        self.assertTrue(set(MODES).issubset(set(paths)))

    def test_mode_extension_schema(self):
        for file in [*(f"modes/{m}.md" for m in MODES), "templates/mode-template.md"]:
            self.assertTrue(set(MODE_HEADINGS).issubset(headings(read(file))), file)

    def test_registry_has_neutral_fallback(self):
        registry = read("references/scene-modes.md").lower()
        self.assertIn("neutral fallback", registry)
        self.assertIn("without editing", registry)
        self.assertIn("skill.md", registry)

    def test_everyday_still_life_covers_animals(self):
        body = read("modes/everyday-still-life.md").lower()
        self.assertIn("fish", body)
        self.assertIn("animal", body)
        self.assertIn("count", body)

    def test_photo_category_routing_samples(self):
        registry = read("references/scene-modes.md").lower()
        for cue in ("landscape", "cat", "car", "architecture", "portrait", "food",
                    "flower", "interior", "pet vs", "action vs"):
            self.assertIn(cue, registry, cue)

    def test_six_atmospheres_are_registered(self):
        registry = read("references/atmosphere-selection.md")
        scene = read("references/scene-modes.md")
        for profile in ATMOSPHERES:
            self.assertIn(f"atmospheres/{profile}.md", registry)
            read(f"atmospheres/{profile}.md")
            self.assertNotIn(f"modes/{profile}.md", scene)

    def test_atmosphere_extension_schema(self):
        for file in [*(f"atmospheres/{p}.md" for p in ATMOSPHERES),
                     "templates/atmosphere-template.md"]:
            self.assertTrue(set(ATMOSPHERE_HEADINGS).issubset(headings(read(file))), file)

    def test_atmosphere_observation_only_auto(self):
        text = read("references/atmosphere-selection.md").lower()
        for token in ("source evidence", "zero profiles", "explicit user", "no invented"):
            self.assertIn(token, text)

    def test_atmosphere_compatibility(self):
        text = read("references/atmosphere-selection.md")
        self.assertIn("neon-night + rainy", text)
        self.assertIn("golden-hour + backlit", text)
        self.assertIn("neon-night + golden-hour", text)

    def test_atmosphere_registry_is_extensible(self):
        text = read("references/atmosphere-selection.md")
        for token in ("atmospheres/<id>.md", "registry", "without editing", "SKILL.md"):
            self.assertIn(token, text)

    def test_preservation_policy_handles_overlapping_groups(self):
        text = read("references/preservation-rules.md").lower()
        for token in ("overlap", "count", "individual", "hand"):
            self.assertIn(token, text)

    def test_prompt_policy_avoids_invented_text(self):
        text = read("references/prompt-construction.md").lower()
        for token in ("invented text", "brands", "reference image", "one primary"):
            self.assertIn(token, text)

    def test_master_lock_contract(self):
        text = read("references/preservation-rules.md").lower()
        for token in ("master-lock", "approved", "unchanged", "pixel-perfect"):
            self.assertIn(token, text)

    def test_readme_covers_usage_and_expansion(self):
        text = read("README.md").lower()
        for token in ("install", "codex", "photo-cel-studio", "adding a mode",
                      "atmosphere", "no image", "limitations"):
            self.assertIn(token, text)

    def test_no_fake_example_metadata(self):
        text = read("references/prompt-construction.md").lower()
        self.assertIn("no invented dates", text)
        self.assertIn("no logos", text)

    def test_image_tool_required_for_actual_output(self):
        text = read("SKILL.md").lower()
        self.assertIn("available image-edit", text)
        self.assertIn("do not claim", text)

    def test_single_input_stays_one_frame_not_collage(self):
        entry = read("SKILL.md").lower()
        prompt = read("references/prompt-construction.md").lower()
        gate = read("references/quality-gates.md").lower()
        for text in (entry, prompt, gate):
            self.assertIn("no collage", text)
            self.assertIn("single source", text)

    def test_lighting_not_reinvented_for_style(self):
        prompt = read("references/prompt-construction.md").lower()
        gate = read("references/quality-gates.md").lower()
        self.assertIn("invented shadows", prompt)
        self.assertIn("invented shadows", gate)

    def test_workflow_can_load_only_selected_modes(self):
        text = read("SKILL.md").lower()
        self.assertIn("on demand", text)
        self.assertIn("0–2", text)


if __name__ == "__main__":
    unittest.main()
