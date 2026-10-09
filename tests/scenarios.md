# Photo Cel Studio — Evaluation Scenarios

**Status:** NOT RUN. This matrix defines RED (without skill) and GREEN (with skill) comparisons; never claim outputs exist until generated and reviewed. Source files remain private.

## Five street-photo fixtures

| Case | Original photo / visual anchor | Candidate scene mode | Critical failure |
| --- | --- | --- | --- |
| S01 | Green bucket, koi and other fish | everyday-still-life | wrong number/color/species, added fish |
| S02 | Older person seated with backpack, thermos, hat and bench | quiet-dramatic | changed face, gesture, props or camera |
| S03 | Two children playing | dynamic-action or youth-energetic | altered age/number/interaction or hands |
| S04 | Crowd of older onlookers | urban-cinematic | duplicated heads or genericized faces |
| S05 | Two anglers and nearby crowd | urban-cinematic | rods, figures or railing changed |

## Mode-and-atmosphere coverage

| Test | Observed photo | Expected primary mode | Atmosphere and risk |
| --- | --- | --- | --- |
| C01 | Car on rainy neon street | vehicle-mechanical | neon-night + rainy; grounded reflection |
| C02 | Mountain at sunrise | landscape-cinematic | golden-hour only if visible |
| C03 | Indoor gray cat | pet-character | none by default, retain breed |
| C04 | Architectural stairwell | architecture-graphic | none; respect geometric perspective |
| C05 | Backlit portrait | portrait-character | backlit, preserve expression |
| C06 | Food and tableware | food-lifestyle | none; no invented dish |
| C07 | Flower and insect close-up | macro-nature | none; correct biology |
| C08 | Warm interior | interior-atmosphere | golden-hour only when observed |
| C09 | Sunny dry daytime street | urban-cinematic | **zero profiles**; no rain or neon |
| C10 | Snow-covered courtyard | architecture-graphic | snowy if source shows snow |
| C11 | Misty forest | landscape-cinematic | misty; foreground remains drawn |
| C12 | Low-contrast quiet figure | quiet-dramatic | none when no atmosphere evidence |
| C13 | Future unknown underwater macro | neutral fallback | no invented weather |

## Negative / pressure tests

- Overlapping crowds: protect individuals and plausible subject count; never multiply limbs or faces.
- Fish: maintain count where identifiable, relative size and anatomical plausibility; when count cannot be resolved, note uncertainty instead of inventing a number.
- Printed T-shirt: respect real markings when readable, and do not hallucinate corrected brand names.
- Conflicting atmospheres: neon-night + golden-hour auto selection must not mix contradictory times; explicit transformation takes precedence over auto.
- Approved master: change only one requested prop/color; do not silently redesign other areas, report pixel-level model drift.
- Missing generation tool: return a reusable editing brief with honest statement; **do not claim** an image was produced.

## Run sheet template

| Field | Value |
| --- | --- |
| Case + source file (local only) | |
| Model + tool | |
| Skill revision / SHA | |
| Selection (mode + atmospheres) | |
| Prompt or brief (private/local) | |
| Without-skill baseline result | NOT RUN |
| With-skill result | NOT RUN |
| Subject identity / event retention, 0–2 | |
| Cel authenticity / anatomy / composition, 0–2 | |
| Atmosphere grounding / series coherence, 0–2 | |
| Hard failures & corrections | |
| Verdict | NOT RUN |

Check **RED→GREEN** for structural skill behavior. Visual quality is a separate manual assessment: agents must not turn an unrun case into a PASS.


## Actual generation attempts — 2026-10-10

**Test type:** exploratory ChatGPT image-edit tool call using the five user-attached street photos present in this conversation. **This was not a Codex runtime loading the installed Skill**; therefore it validates prompt-direction risks, not end-to-end Skill execution. No source images or generated result files were committed to GitHub.

| Attempt | Requested / intended output | Observed output | Quality observation | Verdict |
| --- | --- | --- | --- | --- |
| V01 | S02 older-person bench photo as one standalone `quiet-dramatic` cel still | Tool returned a five-photo cel-styled comic/contact sheet instead | Strong graphic outlines and flat color separation; **wrong output cardinality**, original photo panel scaled down, extra foliage-cast shadows/stronger sunlight not in source | **FAIL** as independent single-image fidelity test |
| V02 | Retry S02 with explicit one-photo/no-collage instructions | Tool again returned a five-photo montage | Persistent output-cardinality failure, original source images combined; hard-edged added tree-shadow shape changed illumination | **FAIL** as independent single-image fidelity test |

**Follow-up changes:** added explicit `single source → one standalone frame / no collage` hard output contracts to `SKILL.md`, `references/prompt-construction.md`, and `references/quality-gates.md`. Added `no invented shadows` lighting checks. New unit tests `test_single_input_stays_one_frame_not_collage` and `test_lighting_not_reinvented_for_style` first failed (RED), then passed on CI after the rule changes. **These are instruction compliance checks, not proof an image model will obey.**

**Unresolved/manual acceptance:** independent S02 and S03 reference-guided outputs, original vs generated face/pose/object QA, comparative baseline under the same Codex image-editing backend, master-lock targeted region edit, and all other category images remain **NOT RUN / NOT PASSED**. Once a suitable Codex image-generation connector is configured, test single-photo reference selection independently; reject any multi-panel output under default `single-frame` mode.
