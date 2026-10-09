# Scene Modes — Primary Selection Registry

Choose **exactly one primary scene mode** by the most important *art-direction challenge* in the image, not simple keyword matching. A source can include person + vehicle + night + rain: one primary is a mode and weather belongs to separate atmosphere profiles.

Read `references/source-analysis.md` and preservation anchors first. The core cel visual DNA overrides all mode-specific aesthetics. Load only the **one chosen** mode file **on demand**.

| Mode ID | File | Common source cues | First exclusion check |
| --- | --- | --- | --- |
| `urban-cinematic` | [modes/urban-cinematic.md](../modes/urban-cinematic.md) | street furniture, crosswalks, vendors, benches, context-rich pedestrians, layered city depths | No default futuristic city |
| `quiet-dramatic` | [modes/quiet-dramatic.md](../modes/quiet-dramatic.md) | one hero, reflective posture, broad negative space, calm eye line or downcast gaze | No dramatic new emotion |
| `dynamic-action` | [modes/dynamic-action.md](../modes/dynamic-action.md) | body lean, reaching arms, motion blur, direction of travel, strong existing diagonal | Do not add fighting |
| `youth-energetic` | [modes/youth-energetic.md](../modes/youth-energetic.md) | playful hands, expressive faces, colorful clothes, laughter, small-scale interpersonal energy | No chibi |
| `sci-fi-industrial` | [modes/sci-fi-industrial.md](../modes/sci-fi-industrial.md) | pipes, vents, metal stairways, towers, industrial grilles, hard mechanical geometry | No unrequested cyborgs |
| `everyday-still-life` | [modes/everyday-still-life.md](../modes/everyday-still-life.md) | isolated items, container rims, reflective surfaces, small animal/fish presence, object grouping | No extra fish |
| `landscape-cinematic` | [modes/landscape-cinematic.md](../modes/landscape-cinematic.md) | distinctive ridge lines, horizon, layered hills, sky masses, vegetation rhythms, water edge | No invented pagodas |
| `pet-character` | [modes/pet-character.md](../modes/pet-character.md) | one or more recognizable pets, breed-specific face, distinctive coat markings, ears, eyes, pose | No automatic anthropomorphism |
| `vehicle-mechanical` | [modes/vehicle-mechanical.md](../modes/vehicle-mechanical.md) | wheel spacing, body panels, chassis, windows, lights, identifiable mechanical interfaces | No car model substitution |
| `architecture-graphic` | [modes/architecture-graphic.md](../modes/architecture-graphic.md) | repeating windows, railings, stair geometry, verticals, perspectives, façade rhythm | No extra windows |
| `portrait-character` | [modes/portrait-character.md](../modes/portrait-character.md) | face occupies significant area, distinctive hair, glasses, wrinkles, expression, hands and clothing | No face swapping |
| `food-lifestyle` | [modes/food-lifestyle.md](../modes/food-lifestyle.md) | edible shapes, plate/cup silhouette, ingredient colors, sauce patterns, table arrangement | No fake menu text |
| `macro-nature` | [modes/macro-nature.md](../modes/macro-nature.md) | petals, leaves, wing veins, insect limbs, natural symmetry, selective shallow focus | No imaginary species |
| `interior-atmosphere` | [modes/interior-atmosphere.md](../modes/interior-atmosphere.md) | windows, furniture alignment, doorways, floor/wall planes, shelves, ceiling light | No invented windows |

## Routing examples and tie-breaks

- **landscape** mountains / shore → `landscape-cinematic`; **architecture** street façade / stair → `architecture-graphic`; **interior** living room → `interior-atmosphere`.
- **cat**, dog or animal portrait → `pet-character`; **pet vs still-life:** choose `pet-character` if a recognizable pet or animal relationship is the hero; choose `everyday-still-life` for fish in a bucket/objects with important container geometry and many small forms.
- **car**, motorcycle, bicycle or train → `vehicle-mechanical`, even in the city; add `neon-night` or `rainy` separately only if observed.
- **portrait** face dominates → `portrait-character`; static interaction or reflective solitude → `quiet-dramatic`; **action vs youth:** `dynamic-action` if precise gesture/timing determines success, `youth-energetic` if the emotional play and authentic acting dominate.
- **food** plate / coffee / café close-up → `food-lifestyle`; **flower** or insect → `macro-nature`.
- Dense everyday street events without a specialist dominant hero → `urban-cinematic`.
- Machinery infrastructure → `sci-fi-industrial` for strong hard-surface design; even this mode does not automatically convert reality into a science-fiction world.

## Neutral fallback and extensibility

If no mode matches the actual photo type, use a **neutral fallback**: source-driven cel visual grammar, restrained flat shading, truthful anchor preservation; never force a possibly wrong preset.

Adding new coverage means making a new `modes/<id>.md` file from `templates/mode-template.md`, registering one new row above, and adding tests/fixtures to `tests/scenarios.md`, **without editing** root `SKILL.md`. Existing modes remain valid.

When two modes overlap, pick the one with greater source-specific fidelity requirements. Do not stack two scene modes. If the user selects an explicit mode, obey it unless that would break P0 anchors; explain the conflict rather than silently replacing the subject.

## Series consistency

Keep shared contours, number of shadow steps and background finish consistent; different scenes may select distinct modes and source palettes. Atmosphere is a separate optional stage, not a scene category.
