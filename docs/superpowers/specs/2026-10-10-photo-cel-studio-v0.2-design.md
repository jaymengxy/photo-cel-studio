# Photo Cel Studio v0.2 — Mature Cel-Era Style Profiles

**Current authority (2026-10-10 request reconciliation):** the supplied Mature Cel-Era Style Profiles task requires medium / restrained / subtle-analog defaults. The owner's subsequent “一起合并吧” authorizes committing/pushing the combined local changes and merging v0.2 into main; no tag, Release, installed-skill sync or media upload is included. The fixed-method high/cool baseline below is historical and now explicit-only; its drawing and export capabilities remain. See the current [alignment plan](../plans/2026-10-10-photo-cel-studio-v0.2-request-alignment.md).

**Historical authority:** owner's earlier v0.2 instruction to implement, commit and push. No additional design approval is needed. This extends the approved v0.1 design; it does not replace its preservation, modes, atmospheres or master-lock contracts.

## Intent

The reported motorcycle conversion preserved the event but looked too bright, uniform and digitally polished. Add a selectable drawing language that changes contour hierarchy, palette, form shadows, painted backgrounds and surface finish through concrete instructions. Success requires independent fidelity and style assessments; structural tests cannot establish artistic success.

## Architecture and selection

Photography → Preservation → Cel Style Profile → Scene Mode → Atmosphere → Render → Quality Gate.

- Exactly one Cel Style Profile per rendered frame; exactly one primary Scene Mode (existing neutral fallback for unmatched subjects); zero to two compatible, evidence-grounded Atmosphere Profiles.
- Unspecified style resolves to `mature-ova`, including vehicles and pets. Explicit registered style takes precedence. Only `cel_style_profile: auto` authorizes content-based style routing; recommendations do not change the selected profile.
- `references/cel-era-profiles.md` owns style registration, priorities, mode pairings, atmosphere compatibility and extension. Load only `profiles/<selected-id>.md`. Modes still own subject geometry and treatment; atmospheres still own observed light/weather.
- Shared cel grammar is era-neutral: drawn contours, flat plates, 2–3 principal values, hard form shadows and credible proportions/perspective. Selected style refines this grammar; mode refines subject-specific details without resetting style.
- Explicit constraints and approved-master lock > P0/P1 preservation > shared cel grammar > selected style > scene mode > atmosphere > decorative controls. No style or intensity setting changes count, event, camera, identity hues, light direction or weather.

## Five style profiles

| ID | Observable intent |
| --- | --- |
| `mature-ova` | Weighted silhouettes, lighter irregular construction lines, restrained secondary colors, modeled hard shadows, hand-painted backgrounds, subtle cel/film finish. Default. |
| `clean-modern-cel` | Precise even stroke control with outer/inner hierarchy, clearer brighter source colors, crisp plane separation and little surface texture. Believable adult proportions. |
| `urban-noir-cel` | Cooler/deeper secondary planes, stronger source-motivated contrast, heavier silhouette and selective dark merges. Daytime stays daytime. |
| `industrial-mecha-cel` | Load-bearing outlines, exact mechanical construction, angular metal planes and limited graphic reflections. Real machines stay real machines. |
| `warm-daily-ova` | Warm restrained domestic colors, tactile painted settings, natural expressions and stable stepped shadows. Actual source lighting and ages stay intact. |

Every profile follows `templates/profile-template.md`, including ID, use, intent, line/color/shadow/background, subject/material, modes, atmosphere compatibility, preservation, negatives and observable QA. Adding a profile requires only its file, registry row and test/scenario coverage, with no core-workflow edits.

## Controls and prompt

Retain the ten v0.1 defaults. Original v0.2 controls were mature-ova / medium / restrained / subtle-analog; the historical fixed-method refinement below used high/cool controls. The current task restores medium/restrained as the default, retaining high/cool as explicit options. Resolve profile-specific baseline first so choosing clean-modern actually produces a modern comparison despite global defaults. Explicit controls cannot defeat defining profile traits or preservation.

Use six prompt sections: Source Description; Preservation Contract; Shared Cel Grammar; Selected Cel Style Profile; Selected Scene Mode + Atmosphere; Composition / Background / Negative Constraints. Translate adjectives into executable contours, paint planes, hue roles and bounded texture. Use the actual reference image, never reconstruct it from caption alone.

Same-photo multi-profile comparison is an explicit request for multiple independent frames, one selected profile per call. Keep source, backend/model, input ratio, preservation and non-style settings fixed. Never feed a previous variant as the source. A comparison does not unlock an approved master; a deliberate new concept must be requested.

## Validation and delivery

### Fixed-method refinement within v0.2

Historical mature baseline: high / cool-restrained / subtle-analog; current baseline: medium / restrained / subtle-analog. Foregrounds use opaque base plus one connected shadow, few folds/metal highlights and visibly pressure-varied ink. Backgrounds use restrained gray-blue/cool dark masses and opaque painted building/sign/sky/road passages. Source light, warm accents, identity colors and weather stay intact; facade redesign/aging needs source evidence or explicit authorization. All 14 modes inherit selected-profile craft, with direct city/vehicle/built-setting rules and source-specific treatment for other subjects. No new profile/mode/atmosphere.

`references/mature-cel-render.md` owns prompt blocks, mode scope and export. Add delivery_long_edge profile-default, retain_native true, delivery_format png. Mature resolves to original-ratio long edge 540 with no upscale/crop; other profiles resolve native unless overridden. Master-lock keeps accepted size; comparisons use one common size. Save native, actually export, verify dimensions and inspect delivery. The macOS PNG helper tests real portrait/landscape/square/native/small/override exports, not art-quality claims. Existing P01–P06 states remain, with separate current-method evidence. This refinement updates local v0.2 source and installed skill; historical push authority in the original design is not renewed by this section.

- Baseline: 23 existing Python stdlib contract tests; keep all old assertions, extending only the default-key schema for four mandated additions.
- Fail-first tests cover default, registry/files/schema/extension, exactly-one/on-demand selection, preservation precedence, layer independence, vehicle recommendation and unchanged v0.1 registration; additional contracts cover prompt order, profile differentiation, controls, comparison and independent style gates.
- P01/P02/P03 compare the same motorcycle source in mature, industrial and modern styles. P04 bench elder, P05 pet, P06 urban street. All remain NOT RUN until actual reference edits and visual review occur; no invented substitute fixtures.
- Independent review checks user-visible routing and prompt behavior as well as changed files. Fix important defects before committing/pushing. Report structural and visual evidence separately.
- Branch `feat/photo-cel-studio-v0.2` starts at latest unmerged v0.1 `848f0b0ca57423e29538cbb0c6c55f148c86a4f1`. The owner's latest confirmation authorizes combined-change publication and main integration after validation. Do not tag, release, synchronize the installed skill, or publish private media.
