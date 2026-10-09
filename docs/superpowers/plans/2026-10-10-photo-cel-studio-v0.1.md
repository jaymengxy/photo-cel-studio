# Photo Cel Studio v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create an installable Codex-first Agent Skill that preserves a photograph's essential event while rendering it as a mature hand-drawn cel-animation frame using 14 primary scene modes and 6 independently composable atmosphere profiles.

**Architecture:** Keep root `SKILL.md` as the short decision/workflow entrypoint; load detailed source analysis, preservation, cel grammar, prompt construction and QA from `references/`. Use `references/scene-modes.md` as a human/agent-readable mode registry, 14 standalone `modes/*.md` definitions plus `templates/mode-template.md`; atmosphere is a separate optional layer with registry `references/atmosphere-selection.md`, six `atmospheres/*.md` profiles, and `templates/atmosphere-template.md`. No image-generation backend or external runtime dependency is bundled in v0.1.

**Tech Stack:** Agent Skills Markdown + YAML frontmatter, plain YAML presets, Python 3 standard-library structural regression tests, host-provided image editing/generation capability.

**Spec:** `docs/superpowers/specs/2026-10-10-photo-cel-studio-design.md`

## Global Constraints

- The target visual DNA is mature 1980s–1990s Japanese-style hand-drawn cel animation, not a particular series/studio's copied assets.
- Use bold, readable outline hierarchy, broad flat-color regions, hard-edged shadow plates, believable people/animals, designed environments.
- Preserve P0 identities, subject counts, poses, gestures, essential props, and real-world relationship before aesthetic changes.
- Defaults: `style_strength=balanced`, `identity_lock=high`, `background_policy=simplify`, `composition_policy=source-guided`, `scene_mode=auto`, `aspect_ratio=original`, `typography=none`, `output=single-frame`, `revision_mode=new-concept`, `atmosphere_profiles=auto`.
- The 14 primary modes are: `urban-cinematic`, `quiet-dramatic`, `dynamic-action`, `youth-energetic`, `sci-fi-industrial`, `everyday-still-life`, `landscape-cinematic`, `pet-character`, `vehicle-mechanical`, `architecture-graphic`, `portrait-character`, `food-lifestyle`, `macro-nature`, `interior-atmosphere`.
- The six atmospheres are: `neon-night`, `golden-hour`, `rainy`, `snowy`, `misty`, `backlit`. Automatically select 0–2 physically compatible profiles only if observed in the photo; allow explicitly requested creative transformations with preserved hard anchors.
- New scene modes can be added through `modes/<id>.md` + registry + regression case, without editing root `SKILL.md`; atmosphere profiles can be added independently via `atmospheres/<id>.md` + registry + regression case. Unknown modes fall back to neutral source-derived cel direction; unknown or unsupported atmosphere cues produce no profile rather than invented conditions.
- Source photographs and generated test images stay local/conversation-only unless the user expressly requests repository publication.
- Default output is an animation still with original aspect ratio and no labels/logos/typography.
- Model-agnostic prompts cannot guarantee pixel-perfect facial identity or edits; flag fidelity drift explicitly.
- Do not add a public software license without a separate user decision.

## Review Focus

Five likely failures implied by the spec (each appears in an owning task's tests and in human image acceptance scenarios):
1. **Crowd photos with overlapping heads/hands** → retain plausible number and individuality; Task 4 test `test_preservation_policy_handles_overlapping_groups`.
2. **Animals and fish in a bucket** → do not invent extra fish or genericize anatomy; Task 3 test `test_everyday_still_life_covers_animals`.
3. **Readable brand/text on T-shirts** → no made-up text or new labels, while preserving visually meaningful clothing; Task 4 test `test_prompt_policy_avoids_invented_text`.
4. **Unexpected photo category (e.g., underwater or aerial)** → accept an unregistered category with source-driven fallback; Task 3 test `test_registry_has_neutral_fallback`.
5. **Follow-up edit of an approved master** → edit only the requested element, disclose unavoidable generative drift; Task 5 test `test_master_lock_contract`.

Atmosphere-specific risk scenarios are covered in Task 4: dry daytime image must not turn rainy or neon; `neon-night + rainy` must remain source-grounded, while conflicting nighttime/sunset illumination must not be silently mixed.

---

## File responsibilities

| Path | Responsibility |
| --- | --- |
| `SKILL.md` | installable trigger and nine-step workflow; loads only needed references/mode |
| `references/source-analysis.md` | Source Map, P0/P1/P2, event geometry and risks |
| `references/preservation-rules.md` | preservation priorities, conflict resolution and master lock |
| `references/cel-style-grammar.md` | mature cel visual DNA: line/color/shadow/characters/environment |
| `references/scene-modes.md` | mode-routing registry, priority rules, neutral fallback |
| `references/atmosphere-selection.md` | evidence-based atmosphere selection, compatibility rules and zero-profile fallback |
| `atmospheres/<id>.md` | six optional atmosphere-specific light/weather drawing directives |
| `templates/atmosphere-template.md` | reusable schema for new atmosphere definitions |
| `modes/<id>.md` | one independent scene direction per documented mode |
| `templates/mode-template.md` | required fields and extension checklist for future modes |
| `references/prompt-construction.md` | six-section finished-image editing brief |
| `references/quality-gates.md` | separate factual preservation and cel-style review, retry protocol |
| `presets/default.yaml` | explicit default values; docs and tests reference same contract |
| `tests/test_skill_contract.py` | Python stdlib structural tests: integrity and required contracts |
| `tests/scenarios.md` | behavior / image evaluation matrix and baseline test record template |
| `README.md` | purpose, install, quickstart, constraints, expansion guide |
| `agents/openai.yaml` | optional presentation metadata and default prompt |

### Task 1: Baseline scenarios and contract tests (RED)

**Files:**
- Create: `tests/test_skill_contract.py`
- Create: `tests/scenarios.md`

**Interfaces:**
- Consumes: approved v0.1 design spec.
- Produces: `python3 -m unittest discover -s tests -p 'test_*.py' -v` as the structural check; `tests/scenarios.md` as manual prompt/output acceptance cases.

- [ ] **Step 1: Define the pre-Skill baseline** in `tests/scenarios.md`: use the five supplied photo scenarios (green bucket with fish, bench elder, playful children, crowd, anglers) with an invariant request: “convert to a cel-era animation still; keep the real people, animals, action and important props.” Do not commit private images. Record RED observations as `NOT RUN` until image generation actually occurs.
- [ ] **Step 2: Write tests that FAIL without the skill** in `tests/test_skill_contract.py` using `unittest` + `pathlib`. Provide these test method names/assertions:
  - `test_entrypoint_has_valid_frontmatter`: `SKILL.md` exists and frontmatter declares `name: photo-cel-studio` and a photo-to-cel trigger description.
  - `test_default_preset_matches_spec`: ten default values listed in Global Constraints exist exactly in `presets/default.yaml`.
  - `test_required_reference_files_exist`: seven exact reference files exist, including `atmosphere-selection.md`; `SKILL.md` points to the relevant registries/references.
  - `test_initial_modes_are_registered`: all 14 exact initial mode IDs are registered, each points to an existing standalone path, and a 15th mode can be added without modifying `SKILL.md`.
  - `test_mode_extension_schema`: all 14 `modes/*.md` and template contain exact headings `When to use`, `Source cues`, `Composition strategy`, `Linework`, `Palette`, `Shadow grammar`, `Background policy`, `Preservation guardrails`, `Negative constraints`, `Quality checks`.
  - `test_registry_has_neutral_fallback`: registry states what to do when none of the 14 modes match and notes that future modes require no core change.
  - `test_everyday_still_life_covers_animals`: `modes/everyday-still-life.md` describes fish and animal/object recognition.
  - `test_photo_category_routing_samples`: sample category cues map to correct named modes for landscape, cat, car, building, portrait, food, flower/insect and indoor room, with tie-break guidance for pet vs. still-life and action vs. youth.
  - `test_preservation_policy_handles_overlapping_groups`: preservation doc addresses crowded overlapping people and count drift.
  - `test_prompt_policy_avoids_invented_text`: prompt doc forbids made-up lettering/brands.
  - `test_master_lock_contract`: preservation doc states that approved compositions retain unchanged regions and that exact pixel lock is not guaranteed.
  - `test_six_atmospheres_are_registered`: every named atmosphere points to an existing profile file; no profile is also a primary scene mode.
  - `test_atmosphere_extension_schema`: all six profiles and the template expose consistent trigger/evidence, lighting and palette rules, compatibility/negative constraints, and quality checks.
  - `test_atmosphere_observation_only_auto`: source evidence is required for automatic atmospheric overlays; source without evidence gets zero profiles.
  - `test_atmosphere_compatibility`: compatible neon-night + rainy and golden-hour + backlit examples, conflicting neon-night + golden-hour case with resolution precedence.
  - `test_atmosphere_registry_is_extensible`: new atmosphere addition requires only profile + registry + regression fixture.
- [ ] **Step 3: Run RED test**: `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expected FAIL on missing Skill/preset/reference/mode/atmosphere files (not syntax/import errors).
- [ ] **Step 4: Commit tests only**: `test: establish photo-cel-studio skill acceptance contracts`.

### Task 2: Cel core and entrypoint

**Files:**
- Create: `SKILL.md`
- Create: `references/source-analysis.md`
- Create: `references/cel-style-grammar.md`
- Create: `presets/default.yaml`

**Interfaces:**
- Consumes: Task 1 contract tests.
- Produces: concise `SKILL.md` that dispatches to selected references/mode; machine-readable optional defaults.

- [ ] **Step 1: Implement frontmatter** `name: photo-cel-studio`, description phrased as a trigger for converting supplied photos into mature cel-animation stills, not as a workflow summary.
- [ ] **Step 2: Implement core workflow**: inspect → source map → preserve P0/P1/P2 → select 1 scene mode or neutral fallback and 0–2 source-grounded atmosphere profiles → resolve user overrides → six-block edit prompt → actual reference-image editing tool → review → targeted retry → report fidelity caveats. Load only the selected mode/profile docs, never all 20.
- [ ] **Step 3: Add source analysis and drawing grammar**, with hard-edged shadow planes, flat regions, line-weight hierarchy and designed background; enumerate camera angle, subject count and action cues in Source Map.
- [ ] **Step 4: Write exact ten defaults** to `presets/default.yaml`; no extra mandatory configuration.
- [ ] **Step 5: Run** `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expected Task 2-specific tests PASS, remaining reference/mode tests FAIL until next task.
- [ ] **Step 6: Commit** `feat: add photo-cel core and source analysis`.

### Task 3: Scene-mode registry, 14 modes and extension template

**Files:**
- Create: `references/scene-modes.md`
- Create: `modes/urban-cinematic.md`, `modes/quiet-dramatic.md`, `modes/dynamic-action.md`, `modes/youth-energetic.md`, `modes/sci-fi-industrial.md`, `modes/everyday-still-life.md`
- Create: `modes/landscape-cinematic.md`, `modes/pet-character.md`, `modes/vehicle-mechanical.md`, `modes/architecture-graphic.md`, `modes/portrait-character.md`, `modes/food-lifestyle.md`, `modes/macro-nature.md`, `modes/interior-atmosphere.md`
- Create: `templates/mode-template.md`

**Interfaces:**
- Consumes: Task 2's Source Map, shared cel drawing grammar and `scene_mode`.
- Produces: `mode_id → modes/<id>.md → visual rules + exclusions`, source-cue auto routing, explicit override, neutral fallback.

- [ ] **Step 1: Author the first six mode docs** with the ten exact headings required in Task 1 tests; avoid repeated text and emphasize differences in scene/action/subject protection.
- [ ] **Step 2: Add eight new specialized mode docs** (landscape, pet, vehicle, architecture, portrait, food, macro-nature, interior) using the same schema, source-specific preservation and failure checks.
- [ ] **Step 3: Write `references/scene-modes.md`** with 14 registered paths and disambiguation rules: specific subject/geometry vs broad urban, motion vs youth, pet vs small-object still-life; use exactly one primary mode.
- [ ] **Step 4: Write `templates/mode-template.md`** and document future mode registration (new file, registry row, test case) without editing `SKILL.md`. Document neutral fallback for unknown photographs.
- [ ] **Step 5: Run** `python3 -m unittest discover -s tests -p 'test_*.py' -v`. Expected: scene-mode registration/schema/category/fallback tests PASS; missing atmosphere and later references may still FAIL.
- [ ] **Step 6: Commit** `feat: add 14 cel scene modes and extensible registry`.

### Task 4: Atmosphere registry and six composable profiles

**Files:**
- Create: `references/atmosphere-selection.md`
- Create: `atmospheres/neon-night.md`, `atmospheres/golden-hour.md`, `atmospheres/rainy.md`, `atmospheres/snowy.md`, `atmospheres/misty.md`, `atmospheres/backlit.md`
- Create: `templates/atmosphere-template.md`

**Interfaces:**
- Consumes: observed light/weather tags from Source Map, `atmosphere_profiles=auto|none|[ids]`, user explicit transformation request, selected primary mode.
- Produces: ordered 0–2 compatible atmosphere modifiers with a grounded evidence statement, or none.

- [ ] **Step 1: Define six atmosphere contracts**: evidence required for auto-use, cel-rendered lighting/material cues, background/source preservation, forbidden invented weather and signage, interaction with primary mode.
- [ ] **Step 2: Write `references/atmosphere-selection.md`** registry with named paths, default 0–2 profiles, source-evidence checks, user-requested transformation rule, and compatibility/priority: `neon-night+rainy` acceptable if shown; `golden-hour+backlit` acceptable if shown; `neon-night+golden-hour` not silently mixed; no profile when absent.
- [ ] **Step 3: Write `templates/atmosphere-template.md`** with consistent headings/fields: When to use, Source evidence, Lighting strategy, Palette, Rendering grammar, Compatibility, Preservation guardrails, Negative constraints, Quality checks. Future atmosphere additions require only a profile, registry row and scenario.
- [ ] **Step 4: Run** `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expect atmosphere registry, schema, evidence, compatibility and extension tests PASS; remaining preservation/QA reference tests may FAIL.
- [ ] **Step 5: Commit** `feat: add six evidence-grounded cel atmosphere profiles`.

### Task 5: Fidelity rules, prompt assembly and quality gate

**Files:**
- Create: `references/preservation-rules.md`
- Create: `references/prompt-construction.md`
- Create: `references/quality-gates.md`
- Modify: `tests/scenarios.md`

**Interfaces:**
- Consumes: Source Map P0/P1/P2, mode file, defaults, user overrides.
- Produces: six-section edit brief and pass/fail protocol; an approved-master narrow-edit policy.

- [ ] **Step 1: Write preservation rules** for subject/animal count, gesture, props, crowd overlap, identity and camera relationship; master-lock priority overrides scene-mode recomposition; state tool limits plainly.
- [ ] **Step 2: Write prompt assembler guide** with exact six sections: source, must-preserve, cel DNA, one primary mode plus optional atmosphere(s), background/composition, exclusions. Require actual source image attachment. Ban invented logos/text, unrequested futuristic objects, and generic youthful anime homogenization.
- [ ] **Step 3: Define QA rubric** (0–2 each for subject, event, cel fidelity, composition, anatomy, optional series and source-grounded atmosphere). Spell out hard fail and the default one targeted retry; no pretending failed generated images satisfy constraints.
- [ ] **Step 4: Extend `tests/scenarios.md`** with negative cases: dense crowd, many fish, legible shirt print, unexpected scene category, one-element approved-master edit; 14-mode category coverage; 6 atmosphere coverage; dry daytime no forced night/rain; compatible neon/rain and golden/backlit; explicitly requested weather conversion; record expected behavior before testing.
- [ ] **Step 5: Run full structural suite** `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expected ALL PASS. Fix missing contract behavior, not tests, unless a test misstates the approved spec.
- [ ] **Step 6: Commit** `feat: add preservation and generation quality controls`.

### Task 6: Packaging, install documentation and first image evaluation

**Files:**
- Modify: `README.md`
- Create: `agents/openai.yaml`
- Modify: `tests/scenarios.md`

**Interfaces:**
- Consumes: complete root skill, 14 mode files, six atmosphere profiles, both registries.
- Produces: installation and usage guide for Codex, versioned manual image test report.

- [ ] **Step 1: Document install** from the GitHub repository to a Codex-recognized skills folder, restart/refresh, invoke by name, and example prompts for one mode, combined mode+atmosphere, 14-mode auto selection, series consistency and master-lock correction. Explain external image-edit tool requirement.
- [ ] **Step 2: Add optional `agents/openai.yaml`** with display name, short description and default user prompt; do not assume it works in every agent harness.
- [ ] **Step 3: Run** `python3 -m unittest discover -s tests -p 'test_*.py' -v` and inspect text references/links; expected PASS.
- [ ] **Step 4: Run first comparative image test** on at least bench elder and playing children, ideally all five supplied photos: pre-Skill baseline where feasible, then Skill-directed output with the same model/image inputs; record mode, atmosphere choice (including none), prompt metadata, subject/event preservation, cel quality and model drift. Document scenario-only coverage for the new categories without fabricating image-generation results. Manual image runs remain `NOT RUN` until actually executed. These image tests are manual and must be marked `NOT RUN` if no compatible runtime/reference files are accessible.
- [ ] **Step 5: Review and commit** `docs: explain photo-cel usage and record first evaluation`, push to design branch and update Draft PR. Keep all private photos and generated artifacts out of Git history.

## Completion criteria

- `SKILL.md` and all referenced modules exist, with a valid install/usage path.
- `python3 -m unittest discover -s tests -p 'test_*.py' -v` passes in the implementation checkout.
- A new `modes/<id>.md` or `atmospheres/<id>.md` entry can be added with just its registry entry and test case, without editing `SKILL.md`.
- 14 primary modes and six optional atmosphere profiles are validated by the structural suite.
- Automatic atmosphere routing does not hallucinate weather, time of day or neon lighting; incompatible profiles have an explicit tie-break.
- The first two source-photo evaluations are reported as real results, **not** claimed done if tools are unavailable.
- Main stays unchanged until the user reviews/merges the PR; no release tag or unrequested photo uploads.

## Execution handoff

**Status:** proposed plan; do not begin implementation until owner reviews plan and chooses execution mode.

Recommendation: Native / inline implementation because this is a documentation-focused Skill with two registries, 20 independently defined modules and one narrow structural test suite; an end-to-end review after task 5 is sufficient for the initial version.
