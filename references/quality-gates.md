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
- Keep the original lighting direction and real shadow geometry. Reject **invented shadows** or newly added tree silhouettes cast over an originally plain wall unless the user specifically asked to change the light or environmental setting. A model making the image prettier is not authorization to change weather/time.

## Stage B — Designed cel frame

1. Outer/inner line-weight hierarchy visible, not generic black edge filter or vector tracing.
2. Broad flat-color blocks and one/two hard-edge shadow plates rather than smooth gradient/photo texture.
3. Drawn background staging, scene-specific perspective and visible source narrative.
4. Source-grounded palette and lighting, original aspect/crop unless overridden.
5. Mature believable character design, not generic anime beautification, chibi or realistic 3D.
6. For series, consistent stroke weight, shadow steps, surface and background treatment across images.
7. Atmosphere passes **source evidence**, physical compatibility and no invention checks.

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

## Corrective workflow

- Name the *actual observed defect* and its P0/P1/style category; e.g., “extra fish”, “new backpack color”, “missing thermos”, “same-face in crowd”, “rain inserted into dry daylight”, or “smooth 3D shadows”.
- If there is an edit-capable tool, attempt **one targeted correction** by default; prefer a locked base and small region rather than regenerating everything.
- Re-compare after correction. If still wrong, tell the user what drift remains instead of claiming success.
- Test cases are **NOT RUN** until the image was actually created, and never claim quantitative image-quality pass from prose checks alone.

## Model/tool limitations

Prompt contracts are probabilistic controls. Preserve the output's successful visual grammar, but recognize that exact face/hand/individual item stability can be limited by image models. Explicit masking, outpainting or pixel processing may be needed when the user requires hard local edit guarantees.

Private images and outputs stay in their authorized scope. Do not publish to GitHub or other public hosts without explicit user instruction.
