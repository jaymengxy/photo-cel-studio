# Cel Style Profiles — Drawing-Language Registry

Cel Style Profile owns era, contour treatment, color hierarchy, shadow organization, background paint and medium finish. Scene Mode owns the subject's geometry and acting; Atmosphere owns source-observed light/weather. These are independent dimensions. Select **exactly one Cel Style Profile** per frame and load only its file on demand.

## Selection and priority

1. Apply explicit user style requests before default or auto routing. Resolve a named registered ID or an unambiguous visual description to one profile. If two incompatible styles are requested for one frame, clarify the desired single style or offer separate comparison frames; do not stack profiles. Unknown IDs need clarification, not silent substitution.
2. An **unspecified** style selects **`mature-ova`**, **including vehicles**, machinery, pets, bright daylight and interiors. This is the default priority across all Scene Modes. `scene_mode: auto` is independent and does not authorize auto style selection.
3. Only an explicit **`cel_style_profile: auto`** permits content-based style selection. Use the candidate conditions and ascending Auto priority below; the first applicable condition wins. A portrait with a car in the distance is not mechanically dominant. If no specialized condition fits, use `mature-ova`. Report the resolved ID and evidence.
4. Pair the selected style with one Scene Mode, then zero to two compatible Atmosphere Profiles from `references/atmosphere-selection.md`. **Recommendations do not change** the selected profile: suggesting an industrial comparison for a motorcycle keeps mature-ova until explicitly chosen or auto authorized.
5. User constraints and approved-master lock > P0/P1 preservation > shared cel grammar > selected Cel Style Profile > Scene Mode > Atmosphere > decoration. A mode's palette/stroke advice is subject-specific emphasis inside the selected style, not a competing era preset. Preserve identity colors and source illumination across all styles.

| Profile ID | File | Suitable scenes / auto candidate condition | Visual target | Auto priority | Scene Mode pairing | Atmosphere compatibility | Conflict handling |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mature-ova` | [profiles/mature-ova.md](../profiles/mature-ova.md) | All real photography; default regardless of subject; auto fallback | Weighted hand-ink silhouettes, subdued secondary planes, sculpted cel shadows, painted setting, subtle analog finish | 5; default always | All 14 modes; vehicle, quiet, urban are strong examples | All six with visible evidence; retain daylight and local light colors | Identity accents outrank desaturation; grain cannot substitute for drawing |
| `clean-modern-cel` | [profiles/clean-modern-cel.md](../profiles/clean-modern-cel.md) | Clear bright source with sparse uncluttered shapes, after more specific candidates are excluded | Precise clean contours, clearer/brighter source palette, sharply separated fills, minimal texture | 4 | All modes; portrait, youth, macro, food especially | All six; rain/neon stay local rather than all-over gloss | Keep outer/inner hierarchy and mature proportions; global analog default must not obscure clean finish |
| `urban-noir-cel` | [profiles/urban-noir-cel.md](../profiles/urban-noir-cel.md) | Urban source with already cool/deep value groups and strong existing shadow contrast | Cooler secondary planes, heavier outlines, selective dark merges, restrained urban narrative | 3 | Urban, quiet, portrait, architecture, interior; also other modes | All six; warmer observed illumination stays warm; no night/rain/neon conversion | Preserve daytime exposure logic and identity legibility over darkening |
| `industrial-mecha-cel` | [profiles/industrial-mecha-cel.md](../profiles/industrial-mecha-cel.md) | Mechanical construction dominates the source: vehicle close-up, transport or industrial plant | Accurate structural ink, weighty metal planes, angular hard shadows, limited graphic reflections | 1 | Vehicle, sci-fi-industrial, architecture; other modes retain biological anatomy | All six where observed; reflection geometry remains source-bound | Real machines stay real machines; no robots, added equipment or PBR reflections |
| `warm-daily-ova` | [profiles/warm-daily-ova.md](../profiles/warm-daily-ova.md) | Pet, family or domestic interaction is the hero, with a lived-in daily-life context | Softly tapered ink, warm restrained secondary colors, natural acting, tactile painted rooms | 2 | Pet, portrait, interior, food, quiet, everyday, youth; usable elsewhere | All six; cold snow/night/rain remains credible and original lamps/sun remain located | Warm treatment cannot invent sunset or infantilize subjects |

The pairings are recommendations, not a closed allowlist. All registered modes can use each style when preservation and shared cel grammar remain intact. Auto priority is a tie-break for explicit auto only, never permission to replace the default. All six atmospheres remain conditional on evidence or an explicit creative setting request; a style's name is not that request.

## Controls: resolve after selecting the profile

`presets/default.yaml` retains the ten v0.1 defaults, the four v0.2 style fields and the v0.2 fixed-delivery refinement. Treat omitted controls as **profile-specific baseline** choices below. Preset values are defaults, not explicit user overrides. This prevents a selected clean-modern-cel from inheriting unwanted aged grain, cool grouping or a reduced-size preview. An explicit user control refines the chosen baseline; it does not silently select a different profile.

| Field | Values | Effect and boundary |
| --- | --- | --- |
| `cel_style_profile` | One registry ID or `auto` | Omitted → mature-ova. `auto` resolves to one registry ID before generation. |
| `profile_intensity` | `low`, `medium`, `high` | Low: light contour/color/finish emphasis; medium: fully readable profile traits; high: stronger hierarchy, palette grouping and painted finish within source geometry. **Does not change preservation priority**, anatomy, count, pose, camera, identity or time/weather. |
| `palette_character` | `source-faithful`, `restrained`, `clear-bright`, `cool-restrained`, `warm-restrained` | Changes secondary hue/value organization; never overwrites **identity colors** (coat markings, yellow shirt, orange truck, vehicle paint). Keep observed light color/direction. |
| `surface_texture` | `none`, `subtle-analog`, `moderate-analog` | None: drawn ink/paint remains, no simulated grain. Subtle: faint paint/cel/film variation below facial/mechanical detail. Moderate: visible yet non-obscuring medium texture. Texture **cannot replace** flat cel plates, form shadows or designed linework. |
| `delivery_long_edge` | `profile-default`, `native`, or a positive integer | Omitted/profile-default resolves from the selected profile below; explicit size wins. Actual export after generation, original ratio, no upscale. Master-lock keeps accepted size; comparisons resolve one common size. |
| `retain_native` | `true` default | Save native separately from delivery; export never overwrites it. Discarding native requires an explicit user request. |
| `delivery_format` | `png` default | Separate delivery is PNG; generated native remains intact. A prompt's requested dimensions are not verified output metadata. |

| Selected profile | Intensity baseline | Palette baseline | Surface baseline | Delivery long edge |
| --- | --- | --- | --- | --- |
| mature-ova | high | cool-restrained | subtle-analog | 540 |
| clean-modern-cel | medium | clear-bright | none | native |
| urban-noir-cel | medium | cool-restrained | subtle-analog | native |
| industrial-mecha-cel | medium | restrained | subtle-analog | native |
| warm-daily-ova | medium | warm-restrained | subtle-analog | native |

The fixed mature method is defined in `references/mature-cel-render.md`, loaded through `profiles/mature-ova.md`. It affects all modes using this selected profile; gray-blue is a secondary-background/shadow strategy, not permission to blue-tint warm sources, identity hues or all subjects. Other profiles keep their defining traits and native baseline. Delivery density is not evidence of cel authenticity.

If a control conflicts with the profile's defining treatment, retain preservation and the profile's core line/shadow language, explain the tension and use a compatible bounded interpretation. For example, high saturation means stronger existing accents, not a uniformly candy-colored city; requested analog texture on clean-modern remains faint enough to keep the comparison clean. Switching to a different profile requires an explicit style choice.

In a series, lock selected style and resolved control family unless the user requests per-photo variation. A multi-profile comparison deliberately varies those style-derived baselines; keep non-style settings fixed. Approved-master lock takes priority: a new profile or stronger controls do not authorize a full redraw during an “only change X” edit.

## Extension contract

Copy `templates/profile-template.md` to `profiles/<id>.md`; give it the matching ID, complete executable visual rules and checks. Add a **registry row** with path, applicability, visual target, priority, pairings, atmosphere compatibility and conflict handling; include a baseline-controls row. Add schema/selection regression **tests** and a positive/negative visual scenario. New profiles are discoverable from this registry **without editing** `SKILL.md`, Scene Mode registry or the core prompt workflow. The initial five-profile list in tests is a minimum; schema validation follows every registered file, allowing additional IDs.
