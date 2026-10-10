# Photo Cel Studio — Evaluation Scenarios

**Status:** Original fixture matrix NOT RUN unless its row says otherwise. Current fixed-method evidence below is separate from the historical matrix. Never claim images exist until generated and reviewed. Source files remain private.

## Fixed v0.2 method — actual evidence and routing cases

Baseline observed in use: outputs retained overly precise digital lines, busy road texture, bright sky/background and insufficiently economical cel values; pixel reduction alone did not fix drawing. An independent current-skill retrieval pass across five described subjects found no required fixed pixel size or actual export procedure. These gaps motivate the fixed contract; retrieval does not prove image quality.

| Case | Actual processing / expected behavior | Evidence status |
| --- | --- | --- |
| R01 | Motorcycle sunny street: gray-blue road/building masses, simplified rider/machine cel values, original sunny geometry, one portrait 360×540 PNG + native | GENERATED + VISUALLY INSPECTED; dimensions verified; user accepts direction; Fidelity PARTIAL / Style PARTIAL |
| R02 | City night crossing: gray-blue painted setting, flat adult crowd, real station/train/light positions, dry road; one landscape 540×360 PNG + native | GENERATED + VISUALLY INSPECTED; dimensions verified; user accepts direction; Fidelity PARTIAL / Style PARTIAL |
| R03 | Warm cafe / red scarf, mature default: warm lamps/identity red remain; flat figure/quiet background; original-ratio long edge 540 | Routing/brief-only check; IMAGE NOT RUN |
| R04 | Explicit clean-modern macro flower: precise clear source hues, no aged grain, native baseline; no forced cool food/petal colors | Routing/brief-only check; IMAGE NOT RUN |
| R05 | Mature/industrial/modern motorcycle comparison: original attached for every call, same backend/source/mode/light, common 540 delivery for all + natives | Routing/brief-only check; CONTROLLED IMAGE COMPARISON NOT RUN |

R01/R02 are iterative private edits, not controlled repetitions, calibrated likeness tests or cross-profile experiments. Do not relabel the original P01–P06 rows as passed. All-mode artistic acceptance is NOT RUN. Check actual native and export, separate documentary drift from drawing/paint/finish, and never infer historical cel authenticity from pixel dimensions alone.

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
| Cel Style Profile + resolved intensity/palette/surface | |
| Prompt or brief (private/local) | |
| Without-skill baseline result | NOT RUN |
| With-skill result | NOT RUN |
| Subject identity / event retention, 0–2 | |
| Cel authenticity / anatomy / composition, 0–2 | |
| Atmosphere grounding / series coherence, 0–2 | |
| Hard failures & corrections | |
| Fidelity verdict / Style verdict | NOT RUN / NOT RUN |
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

## v0.2 — Profile comparison matrix (2026-10-10)

These are new acceptance cases, not new generation results. No unambiguously identified source originals for this matrix were supplied with the v0.2 coding request or committed in this repository. This session has a reference-image editing capability, but the required test source images are not established. **All six image tests are NOT RUN**; no stand-in picture, text reconstruction or collage can establish PASS.

| Case | Source | Scene Mode | Cel Style Profile | Image result |
| --- | --- | --- | --- | --- |
| P01 | Motorcycle street photo: yellow top, black helmet, orange/white truck | vehicle-mechanical | mature-ova | NOT RUN |
| P02 | The identical motorcycle original as P01 | vehicle-mechanical | industrial-mecha-cel | NOT RUN |
| P03 | The identical motorcycle original as P01 | vehicle-mechanical | clean-modern-cel | NOT RUN |
| P04 | Bench elder original (S02) | quiet-dramatic | mature-ova | NOT RUN |
| P05 | User's pet photo | pet-character | warm-daily-ova | NOT RUN |
| P06 | User's city street photo | urban-cinematic | urban-noir-cel | NOT RUN |

### Fixed comparison conditions

P01, P02 and P03 must use the **same source**, **same model** and reference-image editing backend/version, **same input ratio**, **same preservation** contract, camera/crop, scene mode, atmosphere selection and non-style controls. Fix seed if supported and record when it is not. Reattach the same original for every call, not a previous generated variant. Record actual ratio/model/settings before editing; they are currently NOT RUN / unset, not invented values. If backend/model changes, rerun the three as one comparable set. Only profile and declared profile-derived rendering controls vary.

Output one independent still per profile. A separately requested display contact sheet cannot count as single-image acceptance; inspect the underlying independent artifacts. Keep sources, full prompts, model outputs and local file paths outside public Git history.

### What to inspect

- **P01 mature vs v0.1:** weighted exterior/lighter structural ink with restrained hand variation; modeled Base / Shadow / Highlight; quieter sky/road/architecture around the original yellow/orange identity accents; credible painted city and faint medium texture. The v0.1 motorcycle result is reported by the owner but not locally available in this coding session; improvement versus it is NOT RUN until both outputs can be inspected under documented comparable conditions.
- **P02 industrial vs P01:** correct wheel ellipses/contact, front fork, handlebar/grips, engine block, frame, headlight, suspension and shared mechanical perspective; more explicit load-bearing ink/angular metal planes without added parts, robots or PBR shine.
- **P03 modern vs P01:** steadier contours, clearer/brighter source palette, cleaner paint edges and minimal/no simulated grain; keep mature anatomy and hard cel shadows, no cheap cartoon filter.
- **Across P01–P03:** rider pose/count, helmet/clothes, motorcycle and truck/car/building/palm/signal/road-marking relations remain recognizable. Report fidelity drift separately from line/color/shadow/background/finish differences.
- **P04:** same elder age/face, hands-to-backpack action and bench/thermos/cup/hat relationship; no new foliage shadows or collage.
- **P05:** original pet species/breed, coat, eyes/ears/paws, pose and expression; restrained warmth, no kawaii or invented light.
- **P06:** noir color/contrast without converting a dry daylight street into night, rain or neon; retain street geography and people.

Each run records separate Fidelity and Style verdicts with observed evidence. Fidelity PASS is insufficient for overall PASS. Cross-profile distinctiveness remains NOT RUN until comparable outputs exist.

### Routing / control pressure cases

| Input/request | Expected behavior | Evidence type |
| --- | --- | --- |
| Motorcycle + unspecified style + scene_mode auto | mature-ova + vehicle-mechanical; industrial only a recommendation | Agent brief + image review |
| Same motorcycle + cel_style_profile auto | One registry-resolved industrial style; same preservation | Agent brief + image review |
| Bright motorcycle + explicit clean-modern | Cleaner/brighter color groups, baseline surface none; no default analog contamination | Agent brief + image review |
| Dry daylight city + explicit noir | Daytime, dry surfaces and observed light stay intact | Agent brief + image review |
| Pet + unspecified style | mature-ova, not automatic warm-daily | Agent brief + image review |
| High intensity + yellow shirt/orange truck | Stronger drawing hierarchy, identity hues preserved | Agent brief + image review |
| Unknown profile ID / two stacked styles | Clarify one profile or request separate comparison; no silent replacement | Agent brief |
| Unknown scene category + explicit style | Neutral subject fallback keeps the selected profile | Agent brief |
| Approved master + only change headlight + new style preference | Keep accepted unrelated regions/style; clarify incompatible full redraw | Agent brief + local-edit review |

### Requirements to run the image matrix

Provide or identify the exact private motorcycle original for P01–P03, bench elder original for P04, pet photo for P05 and city-street photo for P06, plus the v0.1 motorcycle output for historical comparison. Use a reference-image editing tool with controllable model/version and ratio; inspect each returned image against its original. No repository upload is needed. Generation and visual QA have not been performed by the v0.2 structural suite.

## Current v0.2 request reconciliation — 2026-10-10

This execution reuses the existing feature branch and restores omitted mature controls to **medium / restrained / subtle-analog**. High/cool remains available through explicit overrides; existing native-retained export behavior remains. No images were generated for this reconciliation, and no private originals or generated frames were uploaded.

A read-only independent consumer check of the pre-change skill resolved mature-ova + vehicle-mechanical, zero provisional atmospheres, but high/cool-restrained controls. The exact original was unavailable, so the draft explicitly treated the motorcycle description as a caption, not observed image evidence. Structural RED: 52 tests, four expected default-consistency failures, no errors. These checks address routing/configuration, not artwork.

P01–P06 remain **NOT RUN** for this execution: no exact motorcycle, bench, pet or city originals were supplied or identified in the repository. The historical R01/R02 partial results and V01/V02 failures above are preserved and were not rerun. To run image acceptance, identify the private original for each case and the v0.1 motorcycle result, then use the same reference-image model/version, ratio, fidelity constraints and common export size for P01–P03. Image-edit capability is available; source availability is the missing prerequisite. A generated substitute cannot satisfy this matrix.
