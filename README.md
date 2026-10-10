# photo-cel-studio

English | [简体中文](README.zh-CN.md)

**Photograph → Preservation → Cel Style Profile → Scene Mode → Atmosphere → Redraw → Independent Quality Gates → Verified Export.** The v0.2 default, `mature-ova`, uses pronounced hand-drawn line-weight variation, flat character colors with economical folds, restrained source-derived background colors and broad form-shadow masses, and painted architecture, signs, and skies. The source photograph determines spatial relationships and lighting; identity colors and localized warm light remain intact. Default delivery is an original-aspect **PNG with a 540-pixel long edge**, with the native-resolution generated file retained separately.

This project is a **visual creation Skill** for Codex and other Agent Skills environments. It provides art direction and editing instructions rather than an image-processing algorithm, filter, LUT, or standalone generation model. Producing images requires an **available reference-image editing or generation tool**.

## Installation (Codex)

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

Or use SSH if you have configured a GitHub SSH key:

```bash
git clone git@github.com:jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

Restart or refresh your Codex session so `SKILL.md` is discovered. The same directory can be installed under `~/.agents/skills/` in Agent Skills environments that support that location. `main` includes v0.2 and is the default installation source.

**Installing the Skill does not install an image-generation tool.** Your environment needs an editor or generator that accepts reference images. With **no image editing capability**, the Skill can provide an editing brief but cannot claim that it generated an image.

### Optional v0.2 development branch

```bash
git clone -b feat/photo-cel-studio-v0.2 git@github.com:jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

In an existing Skill clone, use `git fetch origin && git switch feat/photo-cel-studio-v0.2`, then restart or refresh the session. The development checkout at `~/Code/photo-cel-studio` and the installed Skill are separate copies; editing the development repository does not automatically update the installed copy.

### Historical v0.1 Draft PR branch

```bash
git clone -b design/photo-cel-studio-v0.1 git@github.com:jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

Use this only to inspect the historical v0.1 implementation. In an existing clone, run `git fetch origin && git switch design/photo-cel-studio-v0.1`. Return to the current version with `git switch main && git pull --ff-only`. Reference-image editing capability is required for either version to produce images.

## Usage

Upload your own photograph in a session that can read the Skill:

```text
Use $photo-cel-studio to turn this photo into a traditional Japanese cel-animation
still. Preserve the original people or animals, action, key objects, and composition.
```

For a coherent series:

```text
Use $photo-cel-studio on these five street photos. Keep linework, flat colors,
and shadows consistent across the series while selecting a suitable Scene Mode
for each photograph.
```

For a specific subject and observed atmosphere:

```text
Use $photo-cel-studio with vehicle-mechanical as the primary Scene Mode.
Apply neon-night + rainy only if the source actually shows neon lighting
and wet surfaces.
```

For a narrow revision to an accepted result:

```text
Treat this approved image as master-lock. Correct only the fish tail;
keep the people, composition, colors, lighting, and all other elements unchanged.
```

## Core Design

**Shared drawing grammar:** hierarchical contours, source-derived flat color plates, 2–3 principal paint values, hard-edged shadows that model volume, credible human/animal/mechanical structure, and deliberately drawn animation backgrounds. This shared layer is era-neutral; the selected Profile supplies line character, palette, period treatment, and medium finish. Defaults preserve the camera and original aspect ratio, use moderate overall stylization, and add no typography.

### Three independent style layers

| Layer | Selection per frame | Responsibility / Registry |
| --- | --- | --- |
| Cel Style Profile | Exactly 1 | Era, linework, color, shadow organization, background painting, and medium finish; [Profile Registry](references/cel-era-profiles.md) |
| Scene Mode | Exactly 1 primary mode; neutral fallback for unmatched subjects | Subject anatomy, mechanics, architecture, action, and composition; [Mode Registry](references/scene-modes.md) |
| Atmosphere Profiles | 0–2 compatible modifiers | Light and weather visibly present in the source; [Atmosphere Registry](references/atmosphere-selection.md) |

### Five Cel Style Profiles

| ID | Observable drawing differences |
| --- | --- |
| `mature-ova` (default) | Pronounced hand-drawn contour hierarchy, character base color plus one coherent shadow mass, sparse folds/reflections, restrained source-derived color groups and traditionally painted settings; 540-pixel-long-edge PNG plus native file |
| `clean-modern-cel` | More precise, regular contours, clearer/brighter source color groups, clean flat-color boundaries, no simulated grain by default; credible mature proportions |
| `urban-noir-cel` | Cooler secondary colors, stronger source-supported value contrast, heavier silhouettes and selective dark merges; daytime remains daytime |
| `industrial-mecha-cel` | Clearer mechanical connections, wheel/fork/engine perspective, weight-bearing volumes and metal planes; real vehicles remain real vehicles |
| `warm-daily-ova` | Warm restrained everyday colors, natural expressions, tapered ink and stable hard-edged values, lived-in painted surroundings; no default infantilization |

**Default versus automatic selection:** an unspecified style always resolves to `mature-ova`, including cars, motorcycles, and pets. `scene_mode: auto` chooses only the subject treatment. Only an explicit `cel_style_profile: auto` authorizes content-based style routing through the Profile Registry. Vehicle Mode may recommend an industrial comparison but does not replace the default. Explicit style choices take precedence over automatic routing.

### v0.2 single-photo conversion and style comparisons

Default single-photo conversion:

```text
Use $photo-cel-studio on this motorcycle street photo. Preserve the yellow top,
black helmet, motorcycle structure, and the original rider/truck relationship.
Use the default mature-ova treatment. Keep daylight; add no rain, neon, or new shadows.
```

Explicit modern treatment:

```text
Use $photo-cel-studio with cel_style_profile: clean-modern-cel and primary Scene Mode
vehicle-mechanical. Preserve the original vehicle, people, and street structure.
```

Authorize style routing only when you want it:

```text
Use $photo-cel-studio with cel_style_profile: auto and scene_mode: auto.
State the resolved style and primary mode, then follow the source lighting.
```

Compare styles using the same original:

```text
Use $photo-cel-studio to convert the same motorcycle original separately into
mature-ova, industrial-mecha-cel, and clean-modern-cel. Keep the model/editing backend,
input ratio, preservation contract, Scene Mode, Atmosphere, and composition fixed.
Produce one independent image per style, with no collage. Compare linework,
mechanical structure, cel shadows, palette, background, and medium finish;
report fidelity and style quality separately.
```

Reattach the same original for each edit; do not use a previous variant as the next input. A comparison explicitly requests multiple standalone outputs; a default conversion still produces one frame. Changes to model version or input settings must be controlled before attributing differences to a Profile. An “only change X” Master Lock request continues to freeze the other accepted regions and their style.

### v0.2 controls

The ten v0.1 fields remain available. Additional style and delivery controls are:

| Field | Default | Effect and boundary |
| --- | --- | --- |
| `cel_style_profile` | `mature-ova` | One registered ID or explicit `auto` |
| `profile_intensity` | `medium` | Keeps readable hand-drawn contours and flat shading; intensity never reduces preservation priority |
| `palette_character` | `restrained` | Restrains source-derived background and shadow groups while preserving clothing, coat, skin, vehicle paint, and original warm light |
| `surface_texture` | `subtle-analog` | `none` / `subtle-analog` / `moderate-analog`; texture cannot substitute for contours, flat plates, or shadow drawing |
| `delivery_long_edge` | `profile-default` → `540` for mature-ova | Explicit positive integer or `native` takes precedence; other Profiles default to native delivery; preserve aspect ratio without upscaling or cropping |
| `retain_native` | `true` | Save native and delivery files separately; export must not overwrite the native file |
| `delivery_format` | `png` | Actually export and verify dimensions; prompt dimensions alone do not establish delivery size |

The mature default is `medium / restrained / subtle-analog`. Set `profile_intensity: high` and/or `palette_character: cool-restrained` explicitly for stronger/cooler treatment; subject routing never enables these overrides. Identity colors, source light and Master Lock remain protected.

When another Profile is explicitly selected, omitted controls use that Profile's baseline. For example, clean-modern uses `clear-bright` and `none` for surface texture; noir uses `cool-restrained`; warm-daily uses `warm-restrained`. Preset defaults are not explicit user overrides. See the [Profile Registry](references/cel-era-profiles.md) for allowed values and conflict handling.

### Fixed mature-cel rendering and delivery

The reusable brief, mode adaptations, and export procedure are in the [Mature Cel Rendering and Export Guide](references/mature-cel-render.md). Under the default mature-ova Profile, all 14 modes inherit this drawing/delivery method. Urban and vehicle scenes use it most directly; architecture, industrial, landscape, and interior scenes primarily adapt environmental painting. People, action, pets, objects, food, and macro subjects use economical ink and flat paint without turning skin, food, fur, or warmly lit rooms uniformly blue. Changes to architectural style, materials, or period still require user authorization.

A 2:3 frame becomes 360×540; 3:2 becomes 540×360; square becomes 540×540. Other ratios remain unchanged, and native files smaller than 540 pixels are not enlarged. Retain the native file, export, verify width/height, then display the delivery image. On macOS, export a generated image as PNG with:

```bash
python3 scripts/export_frame.py /absolute/native.png /absolute/delivery.png --max-edge 540
```

Other explicitly selected Profiles retain their own style and native-delivery baselines. Multi-profile comparisons use a common delivery size to avoid pixel-density differences confounding the comparison. Master Lock preserves the accepted dimensions and unrelated regions. Lower resolution cannot replace flat-color, linework, or background redrawing, and neither texture overlays nor a blue filter supply the intended drawing language.

### 14 primary Scene Modes — choose one

| Mode | Main use |
| --- | --- |
| `urban-cinematic` | Street photography and urban daily life |
| `quiet-dramatic` | Quiet figures and reflective moments |
| `dynamic-action` | Movement, running, jumping, and sport |
| `youth-energetic` | Children's interaction and lively scenes |
| `sci-fi-industrial` | Industrial structures and explicitly authorized futuristic design |
| `everyday-still-life` | Everyday objects, small still lifes, and fish in containers |
| `landscape-cinematic` | Mountains, coastlines, lakes, and natural landscapes |
| `pet-character` | Pet close-ups and interactions |
| `vehicle-mechanical` | Vehicles and transport machinery |
| `architecture-graphic` | Buildings, stairs, bridges, and structural details |
| `portrait-character` | Portraits and individual character |
| `food-lifestyle` | Food, coffee, and table scenes |
| `macro-nature` | Flowers, insects, and macro nature |
| `interior-atmosphere` | Homes and indoor spaces |

**Six optional Atmosphere Profiles, automatically 0–2:** `neon-night`, `golden-hour`, `rainy`, `snowy`, `misty`, and `backlit`.

**Automatic selection requires evidence:** no rain, neon, or sunset is invented when absent from the source. Users can explicitly request changed weather or period, but that is deliberate reinterpretation rather than a documentary-equivalent conversion.

## Adding a profile

1. Copy the [Profile template](templates/profile-template.md) to `profiles/<new-id>.md`. Fill in executable line, palette, shadow, background, character/object, medium, compatibility, preservation, negative-constraint, and observable quality rules.
2. Add a registry entry and control baseline in `references/cel-era-profiles.md`, defining applicability, auto priority, mode recommendations, atmosphere compatibility, and conflict handling.
3. Add contract coverage and positive/negative image scenarios, then run the tests. The five existing Profiles are minimum coverage; schema checks follow the registry to validate new files.
4. No core `SKILL.md` or prompt-workflow edits are needed. The agent loads only the selected Profile on demand.

## Adding a mode

1. Copy `templates/mode-template.md` to `modes/<new-mode>.md`, replacing placeholders with subject-specific contour, color, shadow, preservation, and exclusion rules.
2. Add a registration entry and routing tie-breaks in `references/scene-modes.md`.
3. Add positive and negative scenarios in `tests/scenarios.md`, then run structural tests.
4. Register new modes without modifying root `SKILL.md`; it loads the matching file through the registry.

Add Atmosphere Profiles similarly using `templates/atmosphere-template.md`, `atmospheres/<id>.md`, and `references/atmosphere-selection.md`. Every automatic atmosphere trigger needs visible source evidence.

## Development and Testing

Run the structural and export checks using Python 3's standard library:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The detailed scenarios and evaluation sheet are in [tests/scenarios.md](tests/scenarios.md). Historical **NOT RUN** results for the original P01–P06 matrix and v0.1 collage **FAIL** records remain intact. Later motorcycle-daylight and city-night outputs were generated and visually inspected; the user accepted the direction, with fidelity/style items still **PARTIAL**. Those experiments inform the fixed rendering method; they are not a controlled five-style comparison or image acceptance for all modes. Source photos and outputs remain private and are not uploaded to the public repository.

Quality gates report **Fidelity** and **Style Authenticity** separately. Faithful content rendered as generic modern digital illustration does not establish a successful mature-ova conversion. Structural tests validate instruction contracts, not model compliance or the artistic success of all five Profiles.

## Limitations

- The Skill supplies decisions and prompt structure: **no image output** without a connected image-edit model.
- Prompts cannot guarantee pixel-exact identity, frozen local pixels, accurate blurred text, occluded subject counts, or biological counts.
- Prompting alone cannot guarantee both the intended drawing style and content fidelity; backend capability, reference-image interfaces, and visual review affect results.
- Outputs require visual inspection. Passing structural tests does not establish image-quality acceptance.
- New people, weather, brands, fictional locations, and invented text require explicit creative authorization.
- The visual references are general traits of mature 1980s–1990s cel animation, not reproductions of specific characters, frames, or official assets.
- Original photographs and generated results are not automatically published to this repository.

## Design and Plans

- [v0.1 design specification](docs/superpowers/specs/2026-10-10-photo-cel-studio-design.md)
- [v0.1 implementation plan](docs/superpowers/plans/2026-10-10-photo-cel-studio-v0.1.md)
- [v0.2 design specification](docs/superpowers/specs/2026-10-10-photo-cel-studio-v0.2-design.md)
- [v0.2 implementation plan and verification record](docs/superpowers/plans/2026-10-10-photo-cel-studio-v0.2.md)
