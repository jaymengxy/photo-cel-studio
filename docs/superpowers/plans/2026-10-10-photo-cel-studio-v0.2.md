# Photo Cel Studio v0.2 Implementation Plan

> **Current request override:** Use medium / restrained / subtle-analog defaults; high/cool remains an explicit option. The execution records below are historical. The owner's latest “一起合并吧” authorizes committing/pushing the combined changes and merging v0.2 into main; see [the current alignment plan](2026-10-10-photo-cel-studio-v0.2-request-alignment.md). No tag, Release, installed-skill sync or media upload is included.

> **For the original execution:** Use superpowers:executing-plans for native implementation; superpowers:test-driven-development governs the contract cycle. Use an independent reviewer at completion. The owner explicitly requested direct implementation and remote push.

**Goal:** Add five executable cel drawing profiles with mature-ova as the default while retaining the v0.1 documentary core.

**Architecture:** Keep the entry short and shared grammar neutral. New profile registry and files own era/color/finish decisions; existing mode and atmosphere registries retain subject and light/weather responsibilities. No image backend or runtime dependency is added.

**Tech Stack:** Markdown, YAML, Python 3 stdlib unittest.

**Spec:** `docs/superpowers/specs/2026-10-10-photo-cel-studio-v0.2-design.md`

## Global Constraints

- Exactly one Cel Style Profile, one primary Scene Mode, 0–2 compatible Atmosphere Profiles per frame.
- Default `mature-ova`; auto style routing only on explicit `cel_style_profile: auto`.
- Preserve all ten v0.1 defaults, 14 scene modes, six atmospheres, source preservation and master-lock.
- Original defaults: medium / restrained / subtle-analog. The historical fixed-method refinement used high / cool-restrained / subtle-analog. The current request restores medium / restrained / subtle-analog while retaining separate delivery controls.
- Do not publish source/generated images or claim unrun visual tests passed.
- Work in the clean local checkout on `feat/photo-cel-studio-v0.2`; commit and push only this branch, without main merge, tag or Release.

## Review Focus

1. Motorcycle with unspecified style must keep mature-ova; recommendation cannot select industrial automatically.
2. Noir applied to a dry daylight street must retain daytime, original shadows and dry surfaces.
3. Clean-modern must stay visibly modern despite global restrained/subtle-analog defaults.
4. A multi-profile comparison must use the same source and tool settings, with one separate frame per profile.
5. Explicit style/intensity changes during master-lock must not regenerate unrelated regions.

## Task 1: Contract tests and RED evidence

**Files:** Modify `tests/test_skill_contract.py`; record results below.
**Interfaces:** Consumes existing 23-test suite and v0.2 spec; produces expanded structural acceptance suite.

- [x] Run unchanged baseline: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v`; 23 PASS.
- [x] Extend expected default keys with the four mandated values; preserve all existing test methods and assertions.
- [x] Add the eleven requested `test_*profile*`/layer/regression tests plus prompt-order, compatibility, controls, neutral-grammar, comparison and independent-style-gate checks. Parse registered paths and validate all registered files rather than forbidding future additions.
- [x] Run full suite and capture RED. Failures name missing profile files/defaults/selection contracts, with no syntax/import errors; existing unaffected tests still pass.

## Task 2: Profile system and workflow integration

**Files:** Create `references/cel-era-profiles.md`, `profiles/{mature-ova,clean-modern-cel,urban-noir-cel,industrial-mecha-cel,warm-daily-ova}.md`, `templates/profile-template.md`; modify `SKILL.md`, `presets/default.yaml`, `references/{cel-style-grammar,prompt-construction,quality-gates,scene-modes,preservation-rules,source-analysis,atmosphere-selection}.md`, `modes/vehicle-mechanical.md`.
**Interfaces:** Consumes Task 1 tests; produces registry-based exactly-one profile selection and six-section edit briefs. IDs and headings follow the schema in tests/template.

- [x] Implement registry precedence, explicit/default/auto routing, neutral fallback and on-demand loading, per-row applicability/priority/mode/atmosphere/conflict guidance and extension steps.
- [x] Write five profiles and template with complete executable contour/palette/shadow/background/material instructions and preserved-source boundaries. Give each profile observable contrast to the others.
- [x] Add four defaults and document profile-aware control resolution; remove era/analog mandates from shared grammar.
- [x] Integrate profile into selection, prompt assembly, layer precedence, series and master-lock handling; retain original single-frame/source-light contracts.
- [x] Strengthen motorcycle component geometry and daytime background treatment under the selected style; industrial is recommendation-only under the default.
- [x] Run v0.2 contracts and full suite with Task 3 documentation; 44/44 PASS on first integrated run.

## Task 3: Documentation, validation, review and delivery

**Files:** Modify `README.md`, `agents/openai.yaml`, `tests/scenarios.md`; update execution record below.
**Interfaces:** Consumes profile registry and prompt contract; produces usage/extension instructions, truthful image matrix and verified Git delivery.

- [x] Document three-layer architecture, five profiles/default, single-photo override/auto, independent comparison, control semantics and profile extension. Retain historical v0.1 install command and add current v0.2 branch instructions.
- [x] Add P01–P06 with invariant motorcycle input/model/ratio/fidelity controls, per-case NOT RUN status and needed references/tool details. Retain existing v0.1 FAIL evidence.
- [x] Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py' -v`; all PASS. Run `git diff --check`; clean. Validate local Markdown links and skill frontmatter.
- [x] Request independent reviewer against spec, tests and all changed/new files, including five Review Focus scenarios; no important defects found.
- [ ] Commit only explicit source/document/test files; push with upstream to origin. Verify remote SHA equals local HEAD and working tree is clean; report branch/base/final SHA, files, test counts, image NOT RUN, review and limits.

## Execution record

- Setup: origin fetched; local v0.1 equals remote (0 ahead / 0 behind), main does not include v0.1; clean worktree. New branch created at `848f0b0ca57423e29538cbb0c6c55f148c86a4f1`.
- Baseline: 23/23 PASS locally before any product changes.
- Process ruling: owner requested full direct implementation; use the supplied spec as approved requirements and implement natively without additional plan approval pauses. Separate fresh reviewer is still required. Structural tests are requested documentation contracts, not image/model behavior proof.
- Task 1 RED: 44-test suite produced 21 expected contract failures, no errors (20 missing new contracts plus the old default-schema test correctly rejecting the absent four v0.2 values). The added v0.1-registration regression already passed because those capabilities exist.
- Task 2/3 GREEN: all 44 integrated contract tests passed; all eleven explicitly requested test names are covered.
- CI finding and correction: existing push trigger omitted feature branches. Added `test_ci_covers_v02_development_branch`, observed RED for the v0.2 branch, then included `feat/**` alongside main/design. Full suite: 45/45 PASS (23 existing + 22 new).
- Verification: AST comparison confirms all 23 old test methods/assertions unchanged and all ten old default values retained. Thirteen non-vehicle modes plus all six atmospheres are byte-identical to baseline; 35 local Markdown links resolve; frontmatter name/description validated with stdlib checks; `git diff --check` clean. No project dependencies added.
- Images: P01–P06 NOT RUN; required motorcycle/bench/pet/city originals and v0.1 motorcycle output are not supplied/unambiguously identified. Reference-edit capability exists in this session, but no alternative sources were invented. Existing v0.1 collage FAIL records retained.
- Independent review: fresh reviewer inspected the supplied requirements, diff/new files and CI change, reran 45/45 tests and clean whitespace checks, and found no blocking/important defects. Five forward-routing cases passed at the brief/instruction level: default motorcycle stays mature-ova; dry-daylight noir preserves conditions; modern baseline is clear-bright/none; comparisons are independent original-reference frames; master-lock preserves unrelated regions/style. These are not image-generation results.
- Review's minor evidence note: plan progress and final delivery had not yet been recorded during review; completed task checks and this record now reflect actual verification. The remaining Git delivery checkbox is intentionally pending in this pre-commit snapshot; final commit, remote SHA match and clean worktree are reported in the delivery message after execution.
- Final clarification: quality-gate cardinality explicitly evaluates each requested comparison artifact separately, and analog finish is checked against the resolved surface control (subtle default or bounded explicit moderate), without changing preservation or drawing criteria.

## Delivery manifest

### Fixed-method refinement execution record (2026-10-10)

- [x] Inspect actual iterative motorcycle/city frames and user-approved treatment; record visual PARTIAL limitations independently of acceptance of direction.
- [x] Read-only baseline across five subject/style requests confirms no fixed export size/procedure in original v0.2; unchanged 45-test suite PASS.
- [x] Add fail-first contract/export tests; 49-test suite RED with five expected missing method/helper/default failures.
- [x] Implement shared mature prompt blocks, mode-impact table, high/cool-restrained baseline, original-ratio 540 delivery/native retention, profile/master/comparison boundaries and export helper.
- [x] Independent reviewer checks changed contracts and five retrieval scenarios; finds non-PNG conversion gap. Add JPEG-native test, observe expected RED, fix supported-format conversion without native overwrite.
- [x] Full suite 50/50 PASS; independent focused re-review finds no remaining material issue. Quick validator PASS with isolated temporary PyYAML; 37 local Markdown links resolve. Real private motorcycle/city exports verify 360×540 / 540×360; no new images generated for skill tests.
- [x] Synchronize 19 source/document/helper/test files into local development and installed v0.2 copies; checksums match, installed full suite 50/50 PASS, installed quick validator PASS, development git diff --check clean. Original changed files backed up outside the skill. Local-only update; no new public image upload, Git push, merge or release authorized by this refinement record.

New resources: `references/mature-cel-render.md`, `scripts/export_frame.py`, `tests/test_export_frame.py`. Modified entry/default/profile/registry/prompt/QA plus urban/vehicle/architecture/industrial mode guidance; all 14 modes inherit only the selected mature profile. Existing five profiles, fourteen mode IDs and six atmosphere IDs retained. Other profile files and neutral shared grammar are unchanged. Low pixel count is not visual acceptance; formal controlled profile/image matrix remains NOT RUN where recorded.

Modified:

- `.github/workflows/validate-skill.yml`
- `README.md`, `SKILL.md`, `agents/openai.yaml`, `presets/default.yaml`
- `modes/vehicle-mechanical.md`
- `references/atmosphere-selection.md`, `references/cel-style-grammar.md`, `references/preservation-rules.md`, `references/prompt-construction.md`, `references/quality-gates.md`, `references/scene-modes.md`, `references/source-analysis.md`
- `tests/scenarios.md`, `tests/test_skill_contract.py`

New:

- `references/cel-era-profiles.md`
- `profiles/mature-ova.md`, `profiles/clean-modern-cel.md`, `profiles/urban-noir-cel.md`, `profiles/industrial-mecha-cel.md`, `profiles/warm-daily-ova.md`
- `templates/profile-template.md`
- `docs/superpowers/specs/2026-10-10-photo-cel-studio-v0.2-design.md`
- `docs/superpowers/plans/2026-10-10-photo-cel-studio-v0.2.md`

Profiles implemented: mature-ova (default), clean-modern-cel, urban-noir-cel, industrial-mecha-cel, warm-daily-ova. Remaining product limitation: these are model-agnostic prompt contracts; actual style authenticity and simultaneous identity/event preservation need reference-image generation and visual review, and are not certified by the structural suite.
