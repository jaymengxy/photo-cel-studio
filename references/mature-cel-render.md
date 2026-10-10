# Mature Cel — Fixed v0.2 Render and Delivery

Read when `mature-ova` is selected. This is the accepted default drawing/output method, not a sixth style profile. Resolve medium intensity, restrained secondary palette and subtle-analog surface unless explicitly overridden. Medium still requires legible hand-ink hierarchy, hard volume-building paint planes and painted backgrounds. `profile_intensity: high` and `palette_character: cool-restrained` are explicit options for stronger/cooler treatment, never content-triggered defaults. Other selected profiles retain their own baselines. Apply source-specific anchors before the following prompt blocks.

## Reusable prompt blocks

**Drawing:** Redraw the whole observed scene as an authored late-1980s/early-1990s mature cel frame. The photo supplies people, event, geometry, camera and light relationships. Foreground silhouettes have strong thick-to-thin hand-pressure variation, naturally shaped curves and occasional angular bends; sparse tapered interior marks. Confident closed forms, credible adult individuality/anatomy/mechanics. Do not trace every photographic edge or retain uniform vector/CAD contours.

**Foreground paint:** Skin and each garment use one opaque matte base plus **one connected shadow**, with a few structural folds at elbow/waist/knee/contact. An optional third flat highlight is small. No soft gradients or fragmented decorative shading. Preserve real age/build, individual faces, hair, markings, glasses, gestures and prop contacts; simplify patterned clothing into selective grouped marks while retaining its identity. Never beautify a crowd into the same young face.

**Background and values:** Compose roads, walls, sky and supported shadow sides as large connected restrained source-derived paint planes. Gray-blue/slate/cool dark groups suit compatible source hues or an explicit cool-restrained palette; warm and neutral sources keep their own secondary color family. Preserve source-lit warm planes and identity accents. Repaint buildings, signs, sky, foliage and road in opaque gouache/poster color: broad organically varied paint passages, grouped window rows, hand-painted edges, less precise distant ruling and less background ink. Road texture is quiet broad paint, not repeating asphalt/stucco grain. Old-building wear is source-supported or explicitly authorized, not a default physical aging effect. Existing sky/cloud shapes stay source-bound; a clear sky stays clear. This is drawn mass organization, not a desaturation/blue-filter overlay.

**Mechanical paint, when present:** Use coherent load-bearing dark masses, selective seams/negative spaces and sparse pale flat highlights. A silver tank/panel has one base, one broad shadow and one pale patch. Chrome has a few purposeful flat strokes, no PBR maps/glint dots. Wheel ellipses, forks, axles, frame, suspension, grips and engine connections stay recognizable and physically correct; selective spokes must not change the wheel.

**Light and medium:** Daylight stays daylight, night stays night. Preserve actual light positions/direction and cast/contact shadow geometry. Cool dark grouping does not authorize new tree shadows, night conversion, rain, clouds or neon. At night, keep observed signs/signals as localized restrained luminous accents and predominantly dry roads dry. Warm cafe lamps, sunsets, skin, food, pet markings, clothing and vehicle paint retain their source roles. Foreground cels separate from softer opaque painted background; mild optical edge rolloff and faint subordinate film/cel variation follow the drawing. No grain blanket, heavy blur, fake scratches/scanlines or 8-bit mosaic.

**Delivery-aware drawing:** Compose for a long edge of 540 pixels at the original ratio: economical shapes must read at that density. Generate a normal native frame first; actual pixel reduction is a separate verified export. One standalone frame per source, no collage.

Use these blocks in section 4 of `references/prompt-construction.md`, adapted to visible content. Do not copy motorcycles, Shibuya signs or specific film assets into unrelated scenes. A user-supplied style reference supplies craft, not permission to import its content/time/weather.

## Mode impact

All 14 modes inherit this profile's drawing/paint/export treatment **only when mature-ova is selected**. Modes still own geometry, action and subject preservation.

| Modes | Application and boundary |
| --- | --- |
| urban-cinematic, vehicle-mechanical | Direct: flat people/vehicles, sparse reflections/ink, large cool road/building masses, painted city/sign/sky. Keep documentary crowd and mechanical relationships. |
| architecture-graphic, sci-fi-industrial | Direct built-setting application: grouped architectural/industrial paint and structural ink economy. Retain openings/connections/landmarks; facade/material redesign is not automatic. |
| landscape-cinematic | Painted sky/terrain/foliage depth, large source-derived shadow groups; cool grouping requires compatible source hues or an explicit cool-restrained palette. Keep actual terrain, clouds, vegetation type and daylight. |
| interior-atmosphere | Painted room depth and simpler object planes; preserve actual lamp colors and warm interior illumination instead of forcing a gray-blue room. |
| portrait-character, quiet-dramatic, dynamic-action, youth-energetic | Flat skin/clothing, few purposeful folds, strong hand-ink hierarchy and quieter background; preserve real ages, expressions and exact acting. |
| pet-character, everyday-still-life, food-lifestyle, macro-nature | Economical ink/paint and simpler background only; animal markings, food freshness, petals/species colors and object materials are identity anchors, not cool-palette targets. |

Explicit other profiles keep their defining line/palette/finish and native delivery baseline. Existing 6 atmosphere profiles continue to require source evidence; this update introduces no new mode/atmosphere or auto-routing.

## Fixed delivery procedure

1. Resolve `delivery_long_edge`: explicit positive integer or `native` wins; otherwise mature-ova → **540**, other profiles → native. Preserve an approved master-lock's accepted delivery size unless changed. Multi-profile comparisons resolve one common export size before rendering (see prompt contract).
2. Save the generated native frame separately. Export a **PNG** at original aspect, longest edge at most the resolved size, **no crop/stretch/upscale**. Thus native 2:3 → 360×540, 3:2 → 540×360, square → 540×540; smaller natives stay smaller. Other ratios follow their source, not a forced 3:2/2:3.
3. For generated raster frames on macOS, run the bundled helper through Python:

```bash
python3 scripts/export_frame.py /absolute/native.png /absolute/delivery.png --max-edge 540
```

Use `--max-edge 0` for native-sized PNG delivery. The helper retains the input, rejects overwriting it/existing delivery files, uses macOS `sips` for reduction or conversion of supported non-PNG natives (e.g. JPEG/TIFF), checks actual PNG dimensions and reports JSON metadata. Unsupported formats need an available equivalent converter; do not rename a JPEG/WebP extension to PNG or claim conversion. On another platform use an available equivalent export tool and verify dimensions; if unavailable, retain the native and report that the requested export was not made.

4. Inspect the actual exported frame and display that delivery file, not the full-size generator preview. Keep native accessible when useful. Record prompt, selected profile/mode/atmosphere, resolved size and separate fidelity/style observations. Never say a 1024×1536 native is 360×540 because the prompt requested it.

An approved **master-lock** narrows the requested edit; transferring this style does not unlock unrelated subjects, region geometry, light or color decisions. Low resolution is the export choice, not evidence of authentic cel drawing or faithful identity.
