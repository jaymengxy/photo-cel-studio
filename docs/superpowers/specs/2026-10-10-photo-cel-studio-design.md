# Photo Cel Studio — Design Spec v0.1

**Status:** DESIGN APPROVED — 14 scene modes + 6 atmosphere profiles; implementation plan still under review  
**Target:** Codex-compatible, model-agnostic Agent Skill  
**Repository:** jaymengxy/photo-cel-studio  
**Date:** 2026-10-10

## 1. Intent and success criteria

Photo Cel Studio transforms user-supplied **real photographs** into authored **hand-drawn cel-animation-looking images** inspired by the general visual language of 1980s–1990s mature Japanese animation. The primary output should be an image that looks like **a frame from an animated production**, not an anime selfie filter, generic digital illustration, or unchanged photo with a painted overlay.

Use cases: street/documentary photography, portraits and groups, natural landscapes, pets and wildlife, vehicles, architecture, food, macro close-ups, interiors, everyday objects, atmospheric weather/night scenes, and cohesive photo series.

The defining balance is:
- Preserve people, animals, key objects, actions, relationships, and documentary narrative.
- Translate contours, color masses, shadows, depth cues, and environments into intentionally designed cel-animation grammar.
- Let source content select a suitable **scene mode** and compatible **atmosphere profile(s)** without making every photo follow the same template.
- Support single-frame transformation, coherent series, and exact-scope revisions to approved outputs.

**Success:** viewers immediately recognize the photograph's essential event and see convincing, mature, production-like cel animation: well-designed shapes, clear black outlines, flat colors, coherent stepped shadows, and an intentional anime background.

## 2. Scope / non-goals

### In v0.1
- Analyze one photograph and produce a concise source map and preservation contract.
- Choose one primary scene mode from a 14-mode registry and 0–2 compatible atmosphere profiles from a separate six-profile library; allow explicit user overrides.
- Build a structured edit brief and call an available image-edit/generation tool.
- Inspect the result and revise on substantial deviations if tool capabilities allow.
- Support a series consistency contract across several related images.
- Support approved-master lock for narrowly scoped follow-up edits.
- Offer test prompts and manual evaluation rubric for reproducible skill testing.

### Not in v0.1
- Training or distributing a custom image-generation model.
- Pixel-exact preservation guarantees (not technically assured by prompt alone).
- RAW development, LUT rendering, or deterministic non-generative retouching pipeline.
- Creating comic panels, typography, watermarks, credits, or logos by default.
- Inventing futuristic technology or original events without user consent.
- Reproducing exact copyrighted scenes, character designs, or studio assets.

## 3. Core art direction: cel visual DNA

The primary art direction is not a single franchise's signature. Extract broad traits from mature hand-drawn Japanese cel-era animation:

1. **Line:** readable outer silhouettes; decisive ink-black/dark outlines; purposeful variable line weight (thicker external contours, thinner interior construction lines), without uniformly outlining every texture.
2. **Color:** broad, clearly bounded flat-color regions; cohesive source-derived palette with optional high-contrast art direction; avoid continuous gradient rendering and photorealistic texture mapped onto figures.
3. **Shadow:** hard-edged, intentionally designed shadow shapes, typically base + shadow + selective highlight. Let lighting motivate the planes; soft transitions only where justified in background atmosphere, not indiscriminately everywhere.
4. **Characters:** recognizable individual appearance, pose, gesture, age, anatomy, clothing structure, and expressive acting; mature believable proportions rather than chibi, plastic 3D, or generic beautified anime faces.
5. **Background:** drawn/stylized animation environment with intentional simplification, line perspective and color mass hierarchy; do not just blur or swap the original background.
6. **Camera:** retain the observed moment and photographic perspective unless the user requests bolder recomposition; composition should read like a film still.
7. **Surface:** subtle analog/cel-era imperfection optional; avoid overwhelming film grain, exaggerated halftone overlays, shiny 3D specularity, and excessive neon.

**Priority:** source identity & user constraints > storytelling relationship > cel visual grammar > mode art direction > incidental aesthetics. Conflicts must be explained or resolved in favor of higher priority.

## 4. Source Map and preservation contract

Build a compact internal Source Map before prompt construction:

- Scene kind: portrait / urban / interaction / action / crowd / animal-object / architecture.
- Hero(s): who/what and how many; defining recognition features.
- Gesture & relationships: hand-object interactions, action direction, proximity, eye lines, grouping.
- Critical anchors (P0): must preserve; identity, count of people/animals, distinct posture, distinctive clothes, essential props or gestures.
- Important anchors (P1): preserve unless they undermine the chosen composition; location cues, secondary props and background spatial logic.
- Incidental details (P2): may simplify; clutter, noise, fine texture, nonessential pedestrians.
- Photograph's emotional register and focal hierarchy.
- Existing geometry, camera angle, crop, negative space, notable palette and light direction.
- Special risks: partial limbs, overlapping people, crowded scenes, printed clothing text, reflective surfaces, species-specific anatomy.

**Default**: P0 stays recognizable; P1 is preserved where feasible; P2 may be simplified but not replaced with fiction that changes the event.

**Do not imply original-photo identity can always be reproduced exactly.** Use an actual image reference/edit operation when available rather than text-only reconstruction.

## 5. Scene modes — fourteen primary directions

Choose **exactly one primary scene mode** for an image. All modes share the same cel visual DNA. The original six are retained to preserve previously approved behavior, and eight new high-frequency photo categories are added.

| Mode | Source-specific cues / when to use | Art direction | Preservation / negative constraint |
| --- | --- | --- | --- |
| `urban-cinematic` | street, parks, public spaces, observed everyday life | designed streetscape, strong eye path, mature cinematic cel frame | do not inject sci-fi architecture or rewrite the location |
| `quiet-dramatic` | lone person, waiting, stillness, introspective gesture | selective negative space, large light/shadow masses, subtle character acting | protect expression, posture, and human-object interaction |
| `dynamic-action` | running, play, movement, sports or dance decisive moment | readable action silhouette, directionality, key-frame staging | preserve the actual action; no invented speed lines by default |
| `youth-energetic` | candid children and lighthearted social interaction | lively but believable expressive acting, bright restrained accents | preserve real age, dignity, count and interaction |
| `sci-fi-industrial` | machinery and infrastructure with industrial geometry, *or* user-requested conceptual futurism | mechanical/architectural perspective, crisp shadow plates | do not manufacture science-fiction tech from an ordinary photograph without request |
| `everyday-still-life` | small everyday objects and simple intimate still lifes, including fish in container | elegant silhouette, efficient flat-color masses, restrained background | retain number and anatomy of animals when present; prefer specialist modes where applicable |
| `landscape-cinematic` | mountains, sea, lakes, forest, sky, geological vistas | layered cel-era painted background, readable horizon, grouped clouds/foliage | retain distinctive terrain, skyline, landmarks and geographic character |
| `pet-character` | cats, dogs, domestic animals, pet portraits and interactions | cel-drawn believable anatomy, expressive but authentic faces, sparse fur detail | preserve species/breed cues, markings, size, eye/ear features; no default anthropomorphism |
| `vehicle-mechanical` | cars, motorcycles, bicycles, trains and transport close-ups | crisp mechanical silhouette, credible perspective, hard-edge paint reflections | preserve model-identifying geometry, components, wheels, viewpoint; no unwanted redesign |
| `architecture-graphic` | exteriors, stairs, corridors, stations, bridges, details | clean structural lines, perspective, planar light and geometric masses | no extra windows/stairs, warped load-bearing shapes or invented architecture |
| `portrait-character` | posed/candid single or multiple face-focused portraits and selfies | believable mature character design, facial acting, silhouette and clothing | avoid same-face anime beautification; keep age, expression, distinct identity |
| `food-lifestyle` | prepared meals, cafés, tableware, drinks, tabletop dining scenes | attractive but restrained hard-edge highlights, flat hue zones and food silhouette | preserve dish ingredients, vessel shapes, object layout; no imaginary garnish or labels |
| `macro-nature` | flowers, plants, insects, textures and biological close-ups | botanical shape rhythm, purposeful contour economy, focal-plane contrast | retain petal/leaf arrangement and biologically meaningful anatomy |
| `interior-atmosphere` | rooms, homes, indoor cafés, stations and designed spaces | simplified architectural volume, layered depth, graphic indoor lighting | preserve room layout, openings, furniture arrangement and consistent perspective |

**Routing caveat:** Some of the original six modes describe *dramatic treatment* rather than a distinct subject category. That is intentional backward compatibility. Select whichever mode best explains the **dominant creative task**, rather than matching a photo's tags literally. For example, a child in motion can be `dynamic-action` or `youth-energetic`, but not two primary modes; a cat on a bench normally prefers the more specific `pet-character` to `everyday-still-life`.

## 5a. Extensible mode contract

- `references/scene-modes.md` is the scene registry; each row maps `mode_id → modes/<id>.md → cues → exclusions → example`.
- Every mode file follows a reusable schema: `mode_id`, `when_to_use`, `source_cues`, `composition_strategy`, `linework`, `palette`, `shadow_grammar`, `background_policy`, `preservation_guardrails`, `negative_constraints`, `quality_checks`.
- New modes require one standalone `modes/<id>.md`, one registry row and relevant regression scenarios; **no changes to root `SKILL.md` or the prompt construction contract**.
- When no mode fits, choose a neutral photo-specific cel direction rather than a mismatched mode and note the unmatched photo category for potential later extension.
- Future candidates are `group-narrative`, `wildlife-character`, `night-sky`, underwater, aerial and other truly distinct material/drawing problems. Sports/couple/wedding photography can initially use existing action/portrait/quiet modes.
- Series coherency is conveyed by shared cel linework/shadow/material decisions, not identical compositions or scene modes.

## 5b. Six composable atmosphere profiles

An atmosphere profile modifies lighting, color and environmental treatment **without becoming a second scene mode**. These belong in `atmospheres/<id>.md`; registry/routing guidance is in `references/atmosphere-selection.md`.

| Atmosphere ID | Source evidence | Rendering grammar | Guardrail |
| --- | --- | --- | --- |
| `neon-night` | existing artificial lights, signs, dark urban scene | distinct dark blue/violet cel-shadow planes, saturated local lights, controlled colored reflections | preserve actual light-source locations, no random signs or cyberpunk city |
| `golden-hour` | visible warm low sun, long shadows | amber highlight masses, cool complementary shadow planes, clear backlit edges | do not move sun or invent sunset in daytime image |
| `rainy` | visible rain, wet pavement, droplets and reflections | graphic wet reflection patches, rain marks only if present, restrained cool lighting | no fabricated rain or soaked clothes |
| `snowy` | snow/ice, visible winter conditions | distinct paper-light snow masses, layered blue-gray shadows | no fictional snowfall or loss of snow-relevant geometry |
| `misty` | visible fog, haze or low-contrast atmospheric depth | graded **distance layers**, simplified background contours; flat cel foreground remains clear | do not uniformly blur the whole cel image |
| `backlit` | strong visible rear/side light with silhouette | graphic rim-light masses, controlled near-black shapes and selective inner detail | retain face/subject legibility and original direction of light |

**Composition/compatibility rules:**
- Automatically choose **zero to two** atmosphere profiles only when justified by visible source evidence; no default profile is equally valid.
- User can explicitly request a weather/time change; it is then a conscious **environment redesign**, not observation-preserving auto-routing. Flag if it changes documentary facts substantially.
- Examples of compatible combinations: `vehicle-mechanical + neon-night + rainy`, `portrait-character + golden-hour + backlit`, `landscape-cinematic + misty`.
- Avoid contradictory profiles such as `neon-night + golden-hour` as a single physical lighting condition. If profiles conflict, choose the source-grounded or explicitly requested dominant one; do not silently blend inconsistent lighting.
- Atmosphere must never override P0/P1 preservation, cel-style grammar, or an explicitly approved master composition.

## 5c. Automatic selection and prompt assembly

1. Parse the photo into **subject/object**, **observed action**, **environment**, **lighting/weather** and preservation anchors. Distinguish *what appears* from *what could be creatively added*.
2. Apply explicit user mode/profile choices first (unless they conflict with hard preservation).
3. Choose a single primary mode by dominant creative difficulty: subject-specific faithful depiction generally outranks broad `urban-cinematic`; a decisive motion/narrative may outrank static subject classification. Surface material ambiguity via a concise choice only if materially necessary.
4. Auto-select compatible grounded atmosphere profile(s) or none. Do not create rain, snow, neon, fog or sunset that was not present.
5. Build a single brief: P0/P1 anchors + shared cel grammar + one mode + zero-to-two atmosphere modifiers + composition/crop + exclusions.
6. Run independent checks: core-photo retention, primary-mode suitability, atmosphere realism, drawing consistency, no invented labels, and series cohesion where relevant.


## 6. User-controllable parameters

Keep natural language as the main interface; formal fields are internal and optional.

| Field | Default | Allowed values |
| --- | --- | --- |
| `style_strength` | `balanced` | `subtle`, `balanced`, `strong` |
| `identity_lock` | `high` | `high`, `balanced`, `stylized` |
| `background_policy` | `simplify` | `preserve`, `simplify`, `redesign` |
| `composition_policy` | `source-guided` | `locked`, `source-guided`, `recompose` |
| `scene_mode` | `auto` | `auto` or one registered primary mode |
| `atmosphere_profiles` | `auto` | `auto`, `none`, or ordered list of profile IDs (normally 0–2) |
| `aspect_ratio` | `original` | `original` or explicit ratio |
| `typography` | `none` | `none`, `user-specified` |
| `output` | `single-frame` | `single-frame`, `series` |
| `revision_mode` | `new-concept` | `new-concept`, `master-lock` |

`strong` increases stylization, **not license to alter the factual action or replace identity**. `redesign` can remodel unimportant environment only; drastic story changes need user approval.

## 7. Default processing workflow

1. **Inspect** reference photograph(s) and any user style references.
2. **Map** Source Map, P0/P1/P2 anchors, emotional register, constraints and pitfalls.
3. **Select** exactly one primary scene mode and zero-to-two compatible atmosphere profiles (or neutral fallback) and summarize the visual proposition in one sentence. No atmosphere is the valid default when the source provides no matching evidence.
4. **Resolve** user overrides, preservation level, original aspect ratio and background policy; avoid inventing unspecified typography.
5. **Build** an image-edit brief from (a) source fidelity, (b) cel visual DNA, (c) one primary mode and grounded atmosphere modifiers, (d) background & composition, (e) exclusions, (f) evaluation checklist.
6. **Generate** with original reference file and edit-capable tool, not text-only if image source is available. If no image-edit tool is available, explicitly say so and output a reusable brief rather than claiming image production.
7. **Review** source/result side-by-side: identity/subject count, action/pose, relevant props, cel drawing features, perspective, background, text and artifacts.
8. **Correct** major failures in at most one targeted retry by default; ask for direction if multiple plausible artistic outcomes remain.
9. **Deliver** transformed image; briefly name mode/creative choice and any fidelity limitation. Do not assert unchanged identity if generation drift is visible.

For `master-lock`, preserve all accepted aspects and change only the user's requested item. Specify a narrow target edit. Tool/model limitations mean pixel-perfect freeze is aspirational; if it drifts, flag rather than concealing it.

## 8. Generation brief template

Use six compact semantic blocks, adapted to the actual photograph:

1. **Original photo:** visible event, subjects, pose, key objects, camera viewpoint.
2. **Preserve:** explicit P0 identity/count/pose/relationships, critical P1 props and spatial cues.
3. **Cel DNA:** decisive line weight, ink outlines, flat regions, hard-edged shadow plates, mature cel-era character/background grammar.
4. **Scene mode & atmosphere:** exactly one primary strategy, plus zero-to-two compatible grounded lighting/weather profiles; explain explicit source-to-weather changes.
5. **Composition:** photo-guided or locked crop; what background clutter may be redrawn/suppressed.
6. **Guardrails:** no generic anime beautification, no childlike proportions, no text/logos unless requested, no extra anatomy or swapped props, no unrelated sci-fi or hallucinated scenery.

Prompt must describe the **finished edited image** and refer clearly to original reference imagery. Avoid stacking raw IP titles or contradictory buzzwords. Extract generalizable traits from reference works instead.

## 9. Series coherence

For multi-photo sets, lock:
- outline weight family and shape clarity;
- color quantization/shadow strategy;
- character proportion policy;
- background rendering philosophy;
- target finishing texture;
- output aspect/canvas strategy if requested.

Allow each photo's palette, light, viewpoint, action and scene mode to respond to its source. Consistency should come from a shared **visual grammar**, not identical color presets or staging.

## 10. Quality gates

Every output gets both factual and visual review. A baseline 0–2 scale for each:
- **Subject retention:** identity, number and key appearance remain identifiable.
- **Event retention:** action, hand-object relationship and meaningful props remain correct.
- **Cel authenticity:** outlines + flat paints + hard-edged stepped shadows are truly depicted, not just a painterly overlay.
- **Composition:** source relationship survives; intended primary scene mode reads clearly.
- **Atmosphere:** lighting and weather follow source evidence unless the user explicitly requested conversion; combinations are physically coherent.
- **Integrity:** anatomy, faces, hands, physical perspective and unintended text are acceptable.
- **Series coherence:** if relevant, image belongs in the same cel-animation universe.

Hard failures: wrong number of people/fish, major identity drift, changed core action, malformed anatomy, unrelated inserted objects, unrequested text/branding, or output that stays photorealistic. Reject or transparently flag these.

## 11. Initial + expansion test matrix

Reuse the five user-provided street photos as **local-only** test fixtures; never upload/commit private reference photos without express request.

| Photo | Expected auto mode | Main potential failure |
| --- | --- | --- |
| Fish in green bucket | `everyday-still-life` | invents fish, changes count/colors/anatomy |
| Older man and backpack on bench | `quiet-dramatic` | changes face/gesture/thermos/hat |
| Two children playing | `dynamic-action` or `youth-energetic` | changes interaction or age, deforms hands |
| Group of older men | `urban-cinematic` | duplicates heads, invents faces, loses individuality |
| Two anglers with onlookers | `urban-cinematic` | removes fishing rods / changes crowd and spatial relations |

Extension acceptance scenarios (photo references remain local and uncommitted):

| Input class | Primary mode | Atmosphere choice | Key failure to reject |
| --- | --- | --- | --- |
| Wet neon street with parked vehicle | `vehicle-mechanical` | `neon-night`, `rainy` | car geometry drift / invented signs |
| Mountains at dawn | `landscape-cinematic` | `golden-hour` only if lighting shows it | replaced mountain silhouette |
| British Shorthair cat indoors | `pet-character` | `none` unless clearly backlit etc. | changed breed, fur, eyes or body |
| Bicycle or train close-up | `vehicle-mechanical` | observed only | changed components or perspective |
| Stairwell/façade close-up | `architecture-graphic` | observed only | invented or warped structural elements |
| Face-focused portrait | `portrait-character` | `backlit` if supported | younger anime-template face |
| Food and a café table | `food-lifestyle` | observed only | added ingredients or fictional packaging |
| Flower and insect macro | `macro-nature` | observed only | incorrect petal or wing anatomy |
| Living room or interior café | `interior-atmosphere` | `golden-hour` if supported | changed furniture/room perspective |
| Daytime sunny street, no rain | `urban-cinematic` | `none` | invented neon/rain/snow |
| Snow-covered courtyard | `architecture-graphic` | `snowy` | lost snow distribution or invented storm |
| Fog-covered forest | `landscape-cinematic` | `misty` | whole image uniformly blurred |
| Portrait in clear rear sunlight | `portrait-character` | `backlit` | changed light direction or lost face |

Test stages:
- **RED / baseline:** same request *without* skill; capture failures in fidelity/cel style.
- **GREEN:** apply v0.1 and run same reference set with same model/settings where possible.
- **Series:** render selected images together as one coherent mode system.
- **Lock:** take one approved output and request a single-detail edit; compare unintended drift.
- **Regression:** preserve prompts, model, mode, skill revision and qualitative scores.

## 12. Proposed repository layout

```text
photo-cel-studio/
├── README.md
├── SKILL.md
├── references/
│   ├── source-analysis.md
│   ├── preservation-rules.md
│   ├── cel-style-grammar.md
│   ├── scene-modes.md            # primary mode registry
│   ├── atmosphere-selection.md   # profile registry, source evidence + conflicts
│   ├── prompt-construction.md
│   └── quality-gates.md
├── modes/                        # fourteen primary modes
│   ├── urban-cinematic.md
│   ├── quiet-dramatic.md
│   ├── dynamic-action.md
│   ├── youth-energetic.md
│   ├── sci-fi-industrial.md
│   ├── everyday-still-life.md
│   ├── landscape-cinematic.md
│   ├── pet-character.md
│   ├── vehicle-mechanical.md
│   ├── architecture-graphic.md
│   ├── portrait-character.md
│   ├── food-lifestyle.md
│   ├── macro-nature.md
│   └── interior-atmosphere.md
├── atmospheres/                  # six optional profiles
│   ├── neon-night.md
│   ├── golden-hour.md
│   ├── rainy.md
│   ├── snowy.md
│   ├── misty.md
│   └── backlit.md
├── templates/
│   ├── mode-template.md
│   └── atmosphere-template.md
├── presets/
│   └── default.yaml
├── agents/
│   └── openai.yaml
├── tests/
│   ├── test_skill_contract.py
│   └── scenarios.md           # no user photographs checked in
└── docs/
    └── superpowers/
        ├── specs/
        └── plans/
```

`SKILL.md` remains a short decision/workflow entrypoint. Detailed style grammar, registries and evaluation rules live in `references/` and are loaded on demand. No executable image-processing engine is included in v0.1; image generation requires an available host image editing tool.


## 13. Boundaries, licenses and distribution

- Write original instructions inspired by studied **principles**, not copies of restricted external Skill content or protected sample artwork.
- Do not depend on titles or exact rendering of specific anime/film IPs; translate references into generic visual features.
- Don't add user-uploaded photography, biometric descriptions beyond visible task needs, or unapproved test images to a public GitHub repository.
- Confirm desired public-license choice before adding one (no license added in this design draft).
- Distinguish declarative Skill compliance from actual image-generation capability, and do not promise deterministic identity fidelity.

## 14. Decision points for owner review

1. **Core priority:** keep photo's action and subject recognizable even when artistic redesign is strong — proposed default: YES.
2. **Default output:** still frame, original aspect ratio, no lettering — proposed default: YES.
3. **Default background:** simplify rather than replace real-world setting — proposed default: YES.
4. **V0.1 scope:** 14 primary scene modes plus 6 evidence-grounded atmosphere profiles, each independently extensible — **APPROVED**.
5. **Target runtime:** optimize first for Codex Agent Skill; keep portable layout to other Agent Skills readers — proposed default: YES.

**Next gate:** owner has approved the original core defaults and this expanded scope. Update and review the implementation plan before authoring Skill files; run the baseline-vs-skill image tests during implementation.
