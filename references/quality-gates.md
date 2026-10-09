# Quality Gates — Photo Fidelity and Cel Authenticity

Run these after any generated image. Instructions and a confident prompt are not evidence of quality: compare original and result visually.

## Stage A — Non-negotiable preservation

1. **Identity/count:** Same discernible people/animals, distinct facial traits, pet markings, vehicle geometry. Unknown counts stay uncertain. For crowd photos compare placement and personal differences.
2. **Event/props:** Same action, head/hand-to-object interaction, fishing lines, clothing, important bag/hat, furniture or other essential props.
3. **Geometry/anatomy:** Hands, limbs, fingers, animal legs/tails/fins, perspective, stairs, wheels and perspective structures credible.
4. **No inventions:** New logos/text, weather, neon signs, people, pets, fabricated metadata or timeline changes fail unless user requested.

A critical violation is **HARD FAIL**, even if the image is visually impressive. Do not report faithful conversion.

## Single-image and source-light hard checks

- A **single source** photo must produce one isolated output frame: **no collage**, no contact-sheet layout, no comic panels, no unexpected reference photos in the same picture. A series defaults to one separate output per original.
- For an explicitly requested multi-profile comparison, inspect one independent frame per profile as a separate artifact against the same source. Multiple requested standalone outputs are valid; a combined panel image is not single-frame acceptance.
- Keep the original lighting direction and real shadow geometry. Reject **invented shadows** or newly added tree silhouettes cast over an originally plain wall unless the user specifically asked to change the light or environmental setting. A model making the image prettier is not authorization to change weather/time.

## Stage B — Style Authenticity Gate

Evaluate against the **selected profile**, not one universal retro treatment. For mature-ova ask whether the result reads as mature traditional cel drawing rather than polished modern digital illustration. For clean-modern expect its clearer ink/color and minimal surface; its modern finish is intentional. Inspect line hierarchy, paint planes, volume, palette, background and medium independently of factual fidelity.

1. Outer/inner line-weight hierarchy visible, not generic black edge filter or vector tracing.
2. **2–3** principal flat paint values (Base / Shadow / optional Highlight) and hard form shadows that model the subject, rather than smooth gradient/photo texture or arbitrary flat patches.
3. Drawn background staging, scene-specific perspective and visible source narrative.
4. Source-grounded palette and lighting, original aspect/crop unless overridden.
5. Mature believable character design, not generic anime beautification, chibi or realistic 3D.
6. For series, consistent stroke weight, shadow steps, surface and background treatment across images.
7. Atmosphere passes **source evidence**, physical compatibility and no invention checks.
8. Palette fits the selected profile while keeping identity colors: mature-ova restrains large sky/road/building planes; clean-modern has clearer secondary hues; noir cools/deepens supported groups; industrial separates material planes; warm-daily warms secondary domestic groups within real source light.
9. Reject overly bright/saturated tourism-poster appearance for mature/noir/industrial or an undifferentiated colorful anime poster. Modern contrast must still be cel-drawn, never glossy 3D.
10. **Analog** finish follows the resolved surface control and stays subordinate to ink/paint: subtle by default; explicitly requested moderate texture may be visible but must not obscure recognition or drawing. Noise over untouched photography or grain used to conceal uniform digital rendering fails; no simulated medium texture is required for clean-modern.
11. Profile has recognizable line/color/shadow/background/finish traits. In same-source comparisons, inspect actual observable differences; profile names alone are insufficient. If no comparison has been rendered, mark cross-profile distinction NOT RUN instead of inventing comparative evidence.

For each applicable style criterion, score 0 = fail, 1 = partial, 2 = satisfactory, with a short observed reason. Any 0 means Style FAIL; any 1 with no 0 means Style PARTIAL; all applicable criteria at 2 means Style PASS. Non-applicable series/comparison/atmosphere items are N/A, not automatic points. Criterion 7 failing source evidence or criterion 2 inventing lighting also triggers the preservation hard gate.

## Evaluation rubric

Score **0 = fail**, **1 = partial**, **2 = satisfactory** for:
- subject recognition/individuality;
- event and prop retention;
- cel visual authenticity;
- composition/scene-mode suitability;
- anatomy/perspective;
- optional series consistency;
- applicable atmosphere grounding.

Any P0 hard failure is an immediate fail regardless of total score. A visually poor anime-style result with flat colors but changed subject is not acceptable.

## Independent verdicts

Record a **fidelity verdict** and a **style verdict** separately. Fidelity PASS requires no hard source/output/light violations and satisfactory identity/event/geometry checks; uncertain details are explicitly recorded, never guessed. Any critical drift means Fidelity FAIL; lesser unresolved drift means PARTIAL. Style PASS requires the selected profile's observable craft to pass Stage B. Faithful content with generic digital-anime rendering is Fidelity PASS / Style FAIL or PARTIAL, not a successful conversion.

| Fidelity verdict | Style verdict | Overall report |
| --- | --- | --- |
| PASS | PASS | PASS for the inspected output, with stated model limits |
| PASS | PARTIAL / FAIL | Incomplete style conversion; name the actual drawing/color/finish defect |
| PARTIAL / FAIL | Any | Unresolved documentary drift; do not claim faithful conversion |
| NOT RUN | NOT RUN | No rendered/inspected output; instructions or structural PASS are insufficient |

Keep fidelity/line/palette/shadow/background/finish observations distinct in the run sheet. Style enthusiasm cannot compensate for wrong faces, missing motorcycle parts, invented shadows or collage output.

## Corrective workflow

- Name the *actual observed defect* and its P0/P1/style category; e.g., “extra fish”, “new backpack color”, “missing thermos”, “same-face in crowd”, “rain inserted into dry daylight”, or “smooth 3D shadows”.
- If there is an edit-capable tool, attempt **one targeted correction** by default; prefer a locked base and small region rather than regenerating everything.
- Re-compare after correction. If still wrong, tell the user what drift remains instead of claiming success.
- Test cases are **NOT RUN** until the image was actually created, and never claim quantitative image-quality pass from prose checks alone.

## Model/tool limitations

Prompt contracts are probabilistic controls. Preserve the output's successful visual grammar, but recognize that exact face/hand/individual item stability can be limited by image models. Explicit masking, outpainting or pixel processing may be needed when the user requires hard local edit guarantees.

Private images and outputs stay in their authorized scope. Do not publish to GitHub or other public hosts without explicit user instruction.
