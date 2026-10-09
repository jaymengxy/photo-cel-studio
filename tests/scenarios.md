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
