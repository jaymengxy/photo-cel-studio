# Image-Edit Prompt Contract

Use the actual **reference image** with an available image-editing/generation tool. Do not rebuild a real user photo from text alone when the photo file is available. Construct an image description as a *finished animation frame*, not a request to add a filter.

## Six sections, in this exact order

### 1. Source Description

One or two precise sentences naming the visible hero, actual action, visible number of people/animals when countable, major prop relationships and camera/crop. Do not infer identity, biography, location or backstory.

### 2. Preservation Contract

Explicit P0/P1 constraints, original perspective, age/build/face/coat/model traits, exact object interactions, visually distinguishable people in crowds. Note ambiguous/occluded counts rather than guessing.

### 3. Shared Cel Grammar

Hand-drawn cel frame; thicker exterior and thinner internal structural linework; broad **flat color plates**; generally 2–3 values (base + shadow + optional highlight) with hard-edged form shadows modeling volume under original light. Credible proportions, connected anatomy/mechanics and designed background forms. No global cartoon filter or painterly smearing. Era, secondary saturation and analog texture belong to the selected profile, not this neutral block.

### 4. Selected Cel Style Profile

State exactly one resolved registry ID (never `auto` in the final brief), profile intensity, palette character and surface treatment. Read its file and turn its rules into instructions for the observed subjects: outer/inner contour weights and regularity, base/shadow/highlight shapes, quieter or clearer secondary hue groups, background paint edges, and the amount/location of medium variation. Preserve the source's identity colors and actual illumination.

For mature-ova, read `references/mature-cel-render.md` and adapt its blocks: visibly pressure-varied silhouettes, sparse interior ink, opaque foreground base plus one connected shadow, few folds/reflection strokes, connected restrained source-derived background masses and opaque gouache settings (gray-blue/cool only when source-compatible or explicitly selected). A motorcycle keeps yellow shirt/orange truck identity accents, connected machine geometry and actual daylight; a night street keeps real localized sign colors and dry road. Old-building wear requires source evidence or authorization. Background paint edges, not added uniform surface noise, supply drawing craft. Do not merely repeat “1980s anime / OVA / cinematic / cel-shading.” Clean-modern instead specifies steadier precise ink, clearer/brighter source color groups and minimal/no simulated grain; industrial emphasizes connected forks, wheel ellipses and angular load-bearing metal planes. These are drawing changes, not content changes.

Resolve omitted controls from the registry's profile-specific baseline. User overrides adjust emphasis without defeating selected-profile identity, P0/P1 anchors or approved-master lock. Grain is a final subordinate layer, not the cel transformation itself.

### 5. Selected Scene Mode + Atmosphere

Exactly **one primary** mode from the registry and its distinctive composition/line/background treatment. Add **zero to two** source-grounded atmosphere directives when justified; state evidence and physically consistent lighting. A deliberate user-requested weather/time change is labeled creative and must retain the agreed source core.

### 6. Composition / Background / Negative Constraints

Keep source-guided camera angle and crop by default; simplification removes expendable details without replacing the observed event. Original aspect ratio default. Reserve no typography unless user requests it. A **single source** must yield one standalone edited still, **no collage** or multi-panel layout. For multiple sources, render one image for each source unless a montage is explicitly requested. Series mode uses one common contour/shadow/paint treatment with individual source palettes.

Resolve `delivery_long_edge` from explicit size, accepted master-lock size, then the selected-profile baseline. For mature-ova it is 540, with native retained and a separate verified PNG; 2:3 becomes 360×540, 3:2 becomes 540×360, other ratios retain their own proportions. No cropping or upscaling. Compose economical shapes for that density but do not assume the generator honors dimensions: export/inspect the real delivery file afterward. Other profiles use native unless overridden.

**No invented text**, fictional brands, guessed logos, signs, watermarks, serial codes, fake credits or **no invented dates**; **no logos** unless explicitly requested and provided. Keep real clothing markings when faithfully reproducible, otherwise do not turn blurred text into fabricated claims. No added props, limbs, faces, neon, rain, snow, sci-fi machines or altered action by default. There must be **no invented shadows**, foliage silhouettes, sunlight or light-source positions merely to make a daytime photograph more dramatic. Avoid cute chibi, generic idol-face changes, 3D/PBR anime shader, blurry digital paint or hand-drawn outlines layered over untouched photo textures.

Include the selected profile's specific negatives and the selected mode's geometry/anatomy failures. Background edges/detail must follow the selected profile while preserving the source location. Finish with separate fidelity and style checks; neither vague style names nor faithful counts alone establish artistic success.

## Example brief (specificity over keywords)

**Original:** An older person sits at left of a public bench, looking down while adjusting a backpack. A thermos and cup are at the bench, with a hat beneath; camera is medium-wide with a quiet light wall.

**Preserve:** One older adult, glasses and distinctive beard/hair/face, original hand-to-backpack action, bench and cup/thermos/hat relationship, wide horizontal framing. Keep the wall negative space.

**Shared Cel:** Decisive outer/inner ink hierarchy, broad flat fills and 2–3 hard paint values following source light; believable face/hand anatomy and drawn bench/wall geometry.

**Profile:** `mature-ova`, medium intensity, restrained secondary palette, subtle-analog surface. Give shoulder/bench silhouettes heavier visibly tapered ink and facial/backpack folds sparse pressure-varied lines. Keep clothing identity hues and source-supported warm wall colors, grouping supported secondary shadow planes quietly. Shape cheek/neck and clothing into opaque base plus one connected shadow, with a painted wall field and faint subordinate medium variation. Native retained; separate original-ratio long-edge-540 PNG verified before display.

**Mode:** `quiet-dramatic`. No atmosphere profile because no conspicuous observed night/neon/rain/snow/mist/backlight. Let large calm color fields carry the stillness without changing the event.

**Composition / Background / Negatives:** Keep original viewpoint and subject position; redraw bench/wall as simplified accurate painted backgrounds and gently simplify scattered clutter. One standalone still, no collage. No extra people, altered age, invented writing, new spotlight, new props, distorted hands, invented shadows, glossy modern gradients or faux-3D effects.

## Variation and revision

For an explicit same-photo multi-profile comparison, render **one independent frame per profile**. Use the **same source**, **same model** and tool/backend version, **same input ratio**, **same preservation** contract, same Scene Mode/Atmospheres, camera, non-style controls and seed if supported. Vary only the chosen profile and its declared style-derived controls. Reattach the original on every call; never use a **previous variant** as the next source. Record model/settings and any unavailable reproducibility controls. If the backend changes, mark the run non-comparable and repeat the set consistently rather than silently claiming style causation.

Pixel density is a non-style comparison control: use one common explicit delivery size for the entire set. Without an explicit size, a set containing mature-ova uses long edge 540 for **every variant**; a set without it uses native for every variant. Keep all natives. Do not compare a reduced mature frame against a full-resolution modern frame and attribute the density difference solely to drawing style.

P01/P02/P03 use mature-ova, industrial-mecha-cel and clean-modern-cel respectively on the identical motorcycle source. Identity, mechanical fidelity and style difference must be checked separately. Multiple explicitly requested variants are separate artifacts; no collage/contact sheet unless separately requested. A single default conversion still yields one frame.

For other explicitly requested concept variants, vary only authorized composition/light/palette dimensions; do not invent events or cast shadows under a fidelity-preserving request. For a cohesive multi-photo series, lock one style and control family, write one shared rendering paragraph and per-photo P0/mode specifics.

For an approved **master-lock**, cite the accepted image and exact target, keeping its existing profile and all unrelated regions unchanged. A profile switch/intensity override does not authorize full regeneration during an “only change X” request. Full-style comparisons require an explicitly requested new concept from the original. If the tool cannot constrain edit regions, state the risk of collateral change. Never imply deterministic identity restoration.
