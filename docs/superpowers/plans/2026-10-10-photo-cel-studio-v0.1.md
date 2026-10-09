# Photo Cel Studio v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create an installable Codex-first Agent Skill that preserves a photograph's essential event and renders it as a mature hand-drawn cel-animation frame, with replaceable scene-mode modules.

**Architecture:** Keep root `SKILL.md` as the short decision/workflow entrypoint; load detailed source analysis, preservation, cel grammar, prompt construction and QA from `references/`. Use `references/scene-modes.md` as a human/agent-readable mode registry, six standalone `modes/*.md` definitions and `templates/mode-template.md` for future expansion. No image-generation backend or external runtime dependency is bundled in v0.1.

**Tech Stack:** Agent Skills Markdown + YAML frontmatter, plain YAML presets, Python 3 standard-library structural regression tests, host-provided image editing/generation capability.

**Spec:** `docs/superpowers/specs/2026-10-10-photo-cel-studio-design.md`

## Global Constraints

- The target visual DNA is mature 1980s–1990s Japanese-style hand-drawn cel animation, not a particular series/studio's copied assets.
- Use bold, readable outline hierarchy, broad flat-color regions, hard-edged shadow plates, believable people/animals, designed environments.
- Preserve P0 identities, subject counts, poses, gestures, essential props, and real-world relationship before aesthetic changes.
- Defaults: `style_strength=balanced`, `identity_lock=high`, `background_policy=simplify`, `composition_policy=source-guided`, `scene_mode=auto`, `aspect_ratio=original`, `typography=none`, `output=single-frame`.
- The initial registry contains: `urban-cinematic`, `quiet-dramatic`, `dynamic-action`, `youth-energetic`, `sci-fi-industrial`, `everyday-still-life`.
- Future modes can be added through `modes/<id>.md` and a registry entry, without editing `SKILL.md`. Unknown categories fall back to neutral source-derived cel direction, not an arbitrary mode.
- Source photographs and generated test images stay local/conversation-only unless the user expressly requests repository publication.
- Default output is an animation still with original aspect ratio and no labels/logos/typography.
- Model-agnostic prompts cannot guarantee pixel-perfect facial identity or edits; flag fidelity drift explicitly.
- Do not add a public software license without a separate user decision.

## Review Focus

Five likely failures implied by the spec (each appears in an owning task's tests and in human image acceptance scenarios):
1. **Crowd photos with overlapping heads/hands** → retain plausible number and individuality; Task 4 test `test_preservation_policy_handles_overlapping_groups`.
2. **Animals and fish in a bucket** → do not invent extra fish or genericize anatomy; Task 3 test `test_everyday_still_life_covers_animals`.
3. **Readable brand/text on T-shirts** → no made-up text or new labels, while preserving visually meaningful clothing; Task 4 test `test_prompt_policy_avoids_invented_text`.
4. **Unexpected photo category (night street / macro / landscape)** → accept an unregistered category with source-driven fallback; Task 3 test `test_registry_has_neutral_fallback`.
5. **Follow-up edit of an approved master** → edit only the requested element, disclose unavoidable generative drift; Task 4 test `test_master_lock_contract`.

---

## File responsibilities

| Path | Responsibility |
| --- | --- |
| `SKILL.md` | installable trigger and nine-step workflow; loads only needed references/mode |
| `references/source-analysis.md` | Source Map, P0/P1/P2, event geometry and risks |
| `references/preservation-rules.md` | preservation priorities, conflict resolution and master lock |
| `references/cel-style-grammar.md` | mature cel visual DNA: line/color/shadow/characters/environment |
| `references/scene-modes.md` | mode-routing registry, priority rules, neutral fallback |
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
  - `test_default_preset_matches_spec`: eight default values listed in Global Constraints exist exactly in `presets/default.yaml`.
  - `test_required_reference_files_exist`: seven exact reference files exist; `SKILL.md` points to them.
  - `test_six_modes_are_registered`: exactly six named v0.1 mode paths are present in `references/scene-modes.md`; each target file exists.
  - `test_mode_extension_schema`: each `modes/*.md` and template contains exact headings `When to use`, `Source cues`, `Composition strategy`, `Linework`, `Palette`, `Shadow grammar`, `Background policy`, `Preservation guardrails`, `Negative constraints`, `Quality checks`.
  - `test_registry_has_neutral_fallback`: registry states what to do when none of the six modes match and notes that future modes require no core change.
  - `test_everyday_still_life_covers_animals`: `modes/everyday-still-life.md` describes fish and animal/object recognition.
  - `test_preservation_policy_handles_overlapping_groups`: preservation doc addresses crowded overlapping people and count drift.
  - `test_prompt_policy_avoids_invented_text`: prompt doc forbids made-up lettering/brands.
  - `test_master_lock_contract`: preservation doc states that approved compositions retain unchanged regions and that exact pixel lock is not guaranteed.
- [ ] **Step 3: Run RED test**: `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expected FAIL on missing Skill/preset/reference/mode files (not syntax/import errors).
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
- [ ] **Step 2: Implement core workflow**: inspect → source map → preserve P0/P1/P2 → select 1 mode or neutral fallback → resolve user overrides → build six-block edit prompt → use actual reference-image editing tool → review → single targeted retry → report fidelity caveats.
- [ ] **Step 3: Add source analysis and drawing grammar**, with hard-edged shadow planes, flat regions, line-weight hierarchy and designed background; enumerate camera angle, subject count and action cues in Source Map.
- [ ] **Step 4: Write exact eight defaults** to `presets/default.yaml`; no extra mandatory configuration.
- [ ] **Step 5: Run** `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expected Task 2-specific tests PASS, remaining reference/mode tests FAIL until next task.
- [ ] **Step 6: Commit** `feat: add photo-cel core and source analysis`.

### Task 3: Mode registry, six modes and extension template

**Files:**
- Create: `references/scene-modes.md`
- Create: `modes/urban-cinematic.md`, `modes/quiet-dramatic.md`, `modes/dynamic-action.md`, `modes/youth-energetic.md`, `modes/sci-fi-industrial.md`, `modes/everyday-still-life.md`
- Create: `templates/mode-template.md`

**Interfaces:**
- Consumes: Task 2's source map, cel visual DNA and selected `scene_mode`.
- Produces: a registry mapping `mode_id → file path → source cues`; a reusable field/heading contract for new modes.

- [ ] **Step 1: Author six focused mode docs** with the ten headings specified in Task 1 tests. Give each distinct trigger cues, compositional treatment, palette/light behavior and prohibited drift. Do not copy the look of a named anime IP.
- [ ] **Step 2: Implement routing catalogue** in `references/scene-modes.md`: exactly one primary mode; explicit choice overrides auto; default mappings from the spec; human/agent-readable file paths.
- [ ] **Step 3: Make the neutral fallback explicit**: source-derived cel grammar when no mode applies. New modes require only new mode file + catalogue row + scenario, not edit to `SKILL.md`.
- [ ] **Step 4: Add `templates/mode-template.md`** with required fields, example trigger/negative case and mini acceptance checklist.
- [ ] **Step 5: Run** `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expected six-mode/schema/fallback/fish tests PASS, other missing content failures remain expected.
- [ ] **Step 6: Commit** `feat: add extensible cel scene-mode library`.

### Task 4: Fidelity rules, prompt assembly and quality gate

**Files:**
- Create: `references/preservation-rules.md`
- Create: `references/prompt-construction.md`
- Create: `references/quality-gates.md`
- Modify: `tests/scenarios.md`

**Interfaces:**
- Consumes: Source Map P0/P1/P2, mode file, defaults, user overrides.
- Produces: six-section edit brief and pass/fail protocol; an approved-master narrow-edit policy.

- [ ] **Step 1: Write preservation rules** for subject/animal count, gesture, props, crowd overlap, identity and camera relationship; master-lock priority overrides scene-mode recomposition; state tool limits plainly.
- [ ] **Step 2: Write prompt assembler guide** with exact six sections: source, must-preserve, cel DNA, chosen mode, background/composition, exclusions. Require actual source image attachment. Ban invented logos/text, unrequested futuristic objects, and generic youthful anime homogenization.
- [ ] **Step 3: Define QA rubric** (0–2 each for subject, event, cel fidelity, composition, anatomy, optional series). Spell out hard fail and the default one targeted retry; no pretending failed generated images satisfy constraints.
- [ ] **Step 4: Extend `tests/scenarios.md`** with negative cases: dense crowd, many fish, legible shirt print, unexpected scene category, one-element approved-master edit; record expected behavior before testing.
- [ ] **Step 5: Run full structural suite** `python3 -m unittest discover -s tests -p 'test_*.py' -v`; expected ALL PASS. Fix missing contract behavior, not tests, unless a test misstates the approved spec.
- [ ] **Step 6: Commit** `feat: add preservation and generation quality controls`.

### Task 5: Packaging, install documentation and first image evaluation

**Files:**
- Modify: `README.md`
- Create: `agents/openai.yaml`
- Modify: `tests/scenarios.md`

**Interfaces:**
- Consumes: complete root skill and six mode docs.
- Produces: installation and usage guide for Codex, versioned manual image test report.

- [ ] **Step 1: Document install** from the GitHub repository to a Codex-recognized skills folder, restart/refresh, invoke by name, and example prompts for single image, series consistency, and master-lock correction. Explain external image-edit tool requirement.
- [ ] **Step 2: Add optional `agents/openai.yaml`** with display name, short description and default user prompt; do not assume it works in every agent harness.
- [ ] **Step 3: Run** `python3 -m unittest discover -s tests -p 'test_*.py' -v` and inspect text references/links; expected PASS.
- [ ] **Step 4: Run first comparative image test** on at least bench elder and playing children, ideally all five supplied photos: one pre-Skill baseline where feasible, then Skill-directed output with the same model/image inputs; record actual mode, prompt metadata, subject/event quality, cel appearance and known model drift. These image tests are manual and must be marked `NOT RUN` if no compatible runtime/reference files are accessible.
- [ ] **Step 5: Review and commit** `docs: explain photo-cel usage and record first evaluation`, push to design branch and update Draft PR. Keep all private photos and generated artifacts out of Git history.

## Completion criteria

- `SKILL.md` and all referenced modules exist, with a valid install/usage path.
- `python3 -m unittest discover -s tests -p 'test_*.py' -v` passes in the implementation checkout.
- A new `modes/<id>.md` entry can be added without editing `SKILL.md`.
- The first two source-photo evaluations are reported as real results, **not** claimed done if tools are unavailable.
- Main stays unchanged until the user reviews/merges the PR; no release tag or unrequested photo uploads.

## Execution handoff

**Status:** proposed plan; do not begin implementation until owner reviews plan and chooses execution mode.

Recommendation: Native / inline implementation because this is a small interdependent documentation-focused Skill with one narrow structural test suite; an end-to-end review after task 5 is sufficient for the initial version.
