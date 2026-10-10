# mature-ova

## Profile ID
`mature-ova` — v0.2 default; not subject-dependent.

## When to use
Unspecified style for any real photo, or an explicit request for mature traditional cel-era drawing. Particularly effective for street photography, people, vehicles and quiet daily events. Do not require a dark or retro-looking source.

## Visual intent
A believable mature hand-drawn 1980s–1990s OVA / theatrical-animation frame. Build the era character through ink hierarchy, color organization, sculpted paint planes and background craft before adding medium texture. Extract general drawing principles, not a particular property's characters or shots.

The fixed v0.2 default is **medium / restrained / subtle-analog**, flat foreground cels over opaque painted backgrounds, delivered at long edge 540 with native retained. Read [references/mature-cel-render.md](../references/mature-cel-render.md) for the executable prompt blocks, mode scope and export procedure whenever this profile is selected. User controls and master-lock still take priority. Explicit `profile_intensity: high` can emphasize hand-pressure changes more strongly without changing source geometry or identity; neither vehicles nor a mature-era label selects it automatically.

## Linework
- Give body/vehicle silhouettes weight; use finer lines for facial structure, garment folds, fasteners and distant architecture.
- Make thick-to-thin pressure changes observable at delivery size; taper internal marks and use modest organic/occasionally angular bends instead of uniform vector curves. Keep confident closed contours, without shaky sketching.
- Draw closed, intentionally shaped forms. Do not blacken every photographic edge, trace asphalt grain or impose absolutely uniform vector strokes.

## Color palette
- Organize secondary roads, sky, walls and supported shadows into large connected restrained source-derived paint masses, with source-supported warm light planes and local accents. Use gray-blue/cool dark grouping where compatible with the source or an explicit `palette_character: cool-restrained` override; do not make every setting cool by default. This is value/paint design, not an all-over blue filter; warm interiors, food, skin and identity hues keep their source color roles.
- Keep identity colors recognizable: a yellow shirt and orange truck can stay prominent against quieter blue-gray road and building planes. Do not blanket-desaturate skin, coat markings or vehicle paint.
- Preserve daylight and original exposure relationships. Avoid a sparkling bright blue sky plus candy-green foliage treatment that makes an ordinary street a tourism-poster.

## Shadow grammar
Use **2–3 principal paint values: Base / Shadow / optional Highlight**. Design crisp hard-edged form shadows under jaw, sleeves, helmet, body panels and chassis to describe volume. Trace each plane back to the actual light direction and contact geometry; flat color must still model a solid body. Highlights are sparse flat shapes, not airbrushed gloss. No newly invented cast shadows to manufacture drama.

Foreground cloth/skin starts with one opaque base and **one connected shadow**, with only a few purposeful fold/structural marks. Optional third highlights are sparse. Simplify clothing patterns without erasing their identity.

## Background painting
Redraw the observed setting as a traditionally painted animation background: grouped wall/asphalt/foliage masses, slightly tactile paint boundaries and less ink in distant planes. Preserve street perspective, building openings, palms, signals and region-specific infrastructure when present. Simplify secondary grain while retaining the spatial scaffold; never swap in an idealized picturesque town.

Use opaque gouache/poster-color wall, sign and sky passages; group distant windows into painted rows, quiet the road into broad fields and reduce distant ruling/ink. Show age/discoloration where source-supported; changing facade design/material/era needs user authorization. A clear sky stays clear. Avoid repeating stucco/asphalt microtexture across the frame.

## Character and object treatment
Keep real age, build, expression and incidental acting; model cheeks, shoulders and clothing with economical structural lines. Give vehicles credible wheel ellipses, weight-bearing connections and panel volumes. Differentiate cloth, skin, rubber and metal by line/paint-plane organization rather than digital surface shine.

Metal uses coherent dark structural masses and selective pale flat strokes: e.g. a silver tank has one base, one shadow and one small highlight, rather than a reflection map or many glint dots. Simplification retains load-bearing connections and actual component geometry.

## Material / analog finish
After the ink and plates read correctly, allow faint cel-paint unevenness, modest color-layer variation and fine film-like grain. Keep grain below small face and machine detail; never obscure text uncertainty or repair bad drawing by adding noise. `surface_texture: none` removes the simulated medium layer while retaining the drawn era grammar.

Moderate optical edge rolloff and the separate 540-pixel export give restrained old-transfer density. Neither larger grain nor downsampling proves cel authenticity; do not use heavy blur, block pixels, scanlines or fake scratches.

## Compatible Scene Modes
All registered modes. Strong pairings: urban-cinematic, quiet-dramatic, vehicle-mechanical, portrait-character, architecture-graphic. Selecting a vehicle mode still keeps this default profile.

## Atmosphere compatibility
All six Atmosphere Profiles if source-supported. Preserve observed neon accents locally, golden light only where shown, existing snow/rain/mist geometry and source backlight. No automatic night conversion; source light takes precedence over muted palette preferences.

## Preservation guardrails
P0/P1 identity, count, pose, camera, key objects and relationships outrank every era treatment. Keep original identity hues and **light direction**. Approved **master-lock** preserves the accepted profile, palette and finish outside the requested edit; intensity never permits unrelated changes.

## Negative constraints
- Avoid glossy modern anime rendering.
- Avoid generic colorful anime poster aesthetics and overly cheerful tourism-poster brightness.
- Avoid childish/chibi proportions or uniform youthful faces.
- Avoid excessively smooth digital gradients and plastic-looking characters and vehicles.
- Avoid unnecessary lens flare, glow and decorative effects.
- Avoid texture overlays on unchanged photography, heavy fake scratches and franchise-specific copied assets.

## Quality checks
Visible heavier silhouette/lighter structure hierarchy with controlled hand-ink variation; 2–3 flat paint values visibly model volume; identity accents stand out without brightening every background plane. Background looks painted and geographically credible. Analog finish is subtle and subordinate. Compared with clean-modern, secondary colors and line regularity are more restrained; compared with industrial, ink is less technical. Passing fidelity alone does not establish mature-cel authenticity.
