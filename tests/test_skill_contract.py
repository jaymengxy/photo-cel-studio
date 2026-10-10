"""Dependency-free structural regression checks for the photo-cel-studio Skill.

These tests verify documentation contracts, not image-generation quality.
Actual image edits must be evaluated with tests/scenarios.md.
"""
from pathlib import Path
from fnmatch import fnmatchcase
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
    "cel_style_profile": "mature-ova",
    "profile_intensity": "high",
    "palette_character": "cool-restrained",
    "surface_texture": "subtle-analog",
    "delivery_long_edge": "profile-default",
    "retain_native": "true",
    "delivery_format": "png",
}
PROFILES = (
    "mature-ova", "clean-modern-cel", "urban-noir-cel",
    "industrial-mecha-cel", "warm-daily-ova",
)
PROFILE_HEADINGS = (
    "Profile ID", "When to use", "Visual intent", "Linework", "Color palette",
    "Shadow grammar", "Background painting", "Character and object treatment",
    "Material / analog finish", "Compatible Scene Modes", "Atmosphere compatibility",
    "Preservation guardrails", "Negative constraints", "Quality checks",
)
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
    def test_mature_method_is_discoverable_and_delivery_is_profile_scoped(self):
        profile = read("profiles/mature-ova.md")
        self.assertIn("references/mature-cel-render.md", profile)
        method = read("references/mature-cel-render.md")
        for token in ("540", "native", "gray-blue", "one connected shadow", "daylight", "master-lock"):
            self.assertIn(token, method.lower())
        registry = read("references/cel-era-profiles.md")
        self.assertRegex(registry, r"(?m)^\| mature-ova \| high \| cool-restrained \| subtle-analog \| 540 \|$")
        self.assertRegex(registry, r"(?m)^\| clean-modern-cel \| medium \| clear-bright \| none \| native \|$")
        self.assertIn("delivery_long_edge", read("references/prompt-construction.md"))
        self.assertIn("Delivery Gate", read("references/quality-gates.md"))

    def test_ci_covers_v02_development_branch(self):
        workflow = read(".github/workflows/validate-skill.yml")
        branch_list = re.search(r"(?m)^\s+branches:\s*\[(.+)\]\s*$", workflow)
        self.assertIsNotNone(branch_list)
        patterns = [value.strip().strip('\"\'') for value in branch_list.group(1).split(',')]
        for branch in ("main", "design/photo-cel-studio-v0.1", "feat/photo-cel-studio-v0.2"):
            self.assertTrue(any(fnmatchcase(branch, pattern) for pattern in patterns), branch)

    def test_default_profile_is_mature_ova(self):
        preset = read("presets/default.yaml")
        self.assertRegex(preset, r"(?m)^cel_style_profile: mature-ova$")
        registry = read("references/cel-era-profiles.md").lower()
        self.assertIn("unspecified", registry)
        self.assertIn("mature-ova", registry)
        self.assertIn("including vehicles", registry)

    def test_profile_registry_exists(self):
        registry = read("references/cel-era-profiles.md")
        self.assertIn("references/cel-era-profiles.md", read("SKILL.md"))
        for field in ("Profile ID", "File", "Suitable scenes", "Visual target",
                      "Auto priority", "Scene Mode pairing", "Atmosphere compatibility",
                      "Conflict handling"):
            self.assertIn(field, registry)

    def test_five_profiles_exist(self):
        registry = read("references/cel-era-profiles.md")
        for profile in PROFILES:
            with self.subTest(profile=profile):
                read(f"profiles/{profile}.md")
                self.assertIn(f"profiles/{profile}.md", registry)

    def test_skill_requires_exactly_one_profile(self):
        entry = read("SKILL.md").lower()
        self.assertIn("exactly one cel style profile", entry)
        self.assertIn("profiles/<id>.md", entry)
        self.assertIn("on demand", entry)
        self.assertIn("only the selected", entry)

    def test_profile_schema_consistency(self):
        registry = read("references/cel-era-profiles.md")
        registered = set(re.findall(r"profiles/([a-z0-9-]+)\.md", registry))
        self.assertTrue(set(PROFILES).issubset(registered))
        for profile in sorted(registered):
            body = read(f"profiles/{profile}.md")
            with self.subTest(profile=profile):
                self.assertIn(f"# {profile}\n", body)
                self.assertTrue(set(PROFILE_HEADINGS).issubset(headings(body)))
                for heading in PROFILE_HEADINGS:
                    section = re.search(rf"(?ms)^## {re.escape(heading)}\n(.+?)(?=^## |\Z)", body)
                    self.assertIsNotNone(section, heading)
                    self.assertTrue(section.group(1).strip(), heading)
                self.assertNotRegex(body, r"\b(?:TBD|TODO)\b|\[Insert|<profile-id>")
        self.assertTrue(set(PROFILE_HEADINGS).issubset(headings(read("templates/profile-template.md"))))

    def test_profile_registry_is_extensible(self):
        registry = read("references/cel-era-profiles.md")
        for token in ("profiles/<id>.md", "templates/profile-template.md", "registry row",
                      "tests", "without editing", "SKILL.md"):
            self.assertIn(token, registry)
        # Future IDs are resolved from the registry, not an entrypoint enumeration.
        entry = read("SKILL.md")
        for profile in PROFILES[1:]:
            self.assertNotIn(profile, entry)

    def test_vehicle_mode_mentions_profile_recommendation(self):
        mode = read("modes/vehicle-mechanical.md").lower()
        for token in ("mature-ova", "industrial-mecha-cel", "recommend", "explicit",
                      "wheel geometry", "front fork", "handlebar", "engine block",
                      "frame structure", "headlight", "suspension", "mechanical perspective"):
            self.assertIn(token, mode)

    def test_negative_constraints_block_modern_glossy_anime(self):
        mature = read("profiles/mature-ova.md").lower()
        for token in ("avoid glossy modern anime rendering", "tourism-poster",
                      "chibi", "digital gradients", "plastic", "lens flare"):
            self.assertIn(token, mature)

    def test_profile_does_not_override_source_preservation(self):
        entry = read("SKILL.md").lower()
        precedence = entry.split("## decision precedence", 1)[1]
        self.assertIn("selected cel style profile", precedence)
        self.assertLess(precedence.index("p0"), precedence.index("selected cel style profile"))
        for profile in PROFILES:
            with self.subTest(profile=profile):
                text = read(f"profiles/{profile}.md").lower()
                for token in ("p0", "identity", "light direction", "master-lock"):
                    self.assertIn(token, text)

    def test_scene_mode_and_profile_are_independent(self):
        scene = read("references/scene-modes.md").lower()
        for token in ("cel style profile", "independent", "does not select or replace"):
            self.assertIn(token, scene)
        registry = read("references/cel-era-profiles.md").lower()
        self.assertIn("cel_style_profile: auto", registry)
        self.assertIn("explicit", registry)
        self.assertIn("recommendations do not change", registry)

    def test_v01_scene_modes_and_atmospheres_remain_registered(self):
        modes = set(re.findall(r"modes/([a-z-]+)\.md", read("references/scene-modes.md")))
        atmospheres = set(re.findall(r"atmospheres/([a-z-]+)\.md", read("references/atmosphere-selection.md")))
        self.assertTrue(set(MODES).issubset(modes))
        self.assertTrue(set(ATMOSPHERES).issubset(atmospheres))
        self.assertEqual(len(MODES), 14)
        self.assertEqual(len(ATMOSPHERES), 6)

    def test_prompt_assembly_has_profile_in_order(self):
        prompt = read("references/prompt-construction.md")
        sections = re.findall(r"^### [1-6]\. (.+)$", prompt, re.M)
        self.assertEqual(sections, [
            "Source Description", "Preservation Contract", "Shared Cel Grammar",
            "Selected Cel Style Profile", "Selected Scene Mode + Atmosphere",
            "Composition / Background / Negative Constraints",
        ])

    def test_shared_grammar_is_era_neutral(self):
        grammar = read("references/cel-style-grammar.md").lower()
        self.assertIn("era-neutral", grammar)
        self.assertIn("selected cel style profile", grammar)
        self.assertIn("2–3", grammar)
        for obsolete in ("late-20th-century", "subtle analog-era grain", "saturation restraint"):
            self.assertNotIn(obsolete, grammar)

    def test_profile_controls_are_bounded(self):
        registry = read("references/cel-era-profiles.md").lower()
        for token in ("profile_intensity", "palette_character", "surface_texture",
                      "identity colors", "does not change preservation priority",
                      "cannot replace", "profile-specific baseline", "low", "medium", "high"):
            self.assertIn(token, registry)

    def test_style_authenticity_gate_is_independent(self):
        gate = read("references/quality-gates.md").lower()
        self.assertIn("style authenticity gate", gate)
        self.assertIn("fidelity verdict", gate)
        self.assertIn("style verdict", gate)
        for token in ("line hierarchy", "2–3", "selected profile", "analog", "poster", "background"):
            self.assertIn(token, gate)

    def test_profile_comparison_uses_independent_frames(self):
        prompt = read("references/prompt-construction.md").lower()
        for token in ("same source", "same model", "same input ratio", "same preservation",
                      "one independent frame per profile", "previous variant", "master-lock"):
            self.assertIn(token, prompt)

    def test_noir_does_not_invent_night(self):
        noir = read("profiles/urban-noir-cel.md").lower()
        self.assertIn("daytime stays daytime", noir)
        self.assertIn("no invented night", noir)
        self.assertIn("rain", noir)
        self.assertIn("neon", noir)

    def test_industrial_profile_keeps_real_vehicle(self):
        industrial = read("profiles/industrial-mecha-cel.md").lower()
        for token in ("wheel geometry", "front fork", "handlebar", "engine block",
                      "frame structure", "headlight", "suspension", "mechanical perspective",
                      "robots", "pbr"):
            self.assertIn(token, industrial)

    def test_modern_profile_has_distinct_finish(self):
        modern = read("profiles/clean-modern-cel.md").lower()
        for token in ("precise", "brighter", "minimal", "texture", "mature", "outer", "inner"):
            self.assertIn(token, modern)

    def test_v02_image_scenarios_are_truthful(self):
        scenarios = read("tests/scenarios.md")
        for case in ("P01", "P02", "P03", "P04", "P05", "P06"):
            self.assertRegex(scenarios, rf"(?m)^\| {case} \|.*NOT RUN")
        for token in ("same source", "same model", "same input ratio", "same preservation"):
            self.assertIn(token, scenarios.lower())

    def test_readme_documents_v02_profile_usage(self):
        readme = read("README.md")
        for token in (*PROFILES, "cel_style_profile: auto", "feat/photo-cel-studio-v0.2",
                      "Adding a profile", "profile_intensity", "surface_texture"):
            self.assertIn(token, readme)

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

    def test_readme_explains_unmerged_branch_install(self):
        text = read("README.md")
        self.assertIn("git clone -b design/photo-cel-studio-v0.1", text)
        self.assertIn("main", text)

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
