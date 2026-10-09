# Photo Cel Studio — Design Spec v0.1

**Status:** DRAFT — pending owner review before implementation  
**Target:** Codex-compatible, model-agnostic Agent Skill  
**Repository:** jaymengxy/photo-cel-studio  
**Date:** 2026-10-10

## 1. Intent and success criteria

Photo Cel Studio transforms user-supplied **real photographs** into authored **hand-drawn cel-animation-looking images** inspired by the general visual language of 1980s–1990s mature Japanese animation. The primary output should be an image that looks like **a frame from an animated production**, not an anime selfie filter, generic digital illustration, or unchanged photo with a painted overlay.

Use cases: street/documentary photography, portraits, people interacting, animals/objects, public spaces, architecture, and grouped image series.

The defining balance is:
- Preserve people, animals, key objects, actions, relationships, and documentary narrative.
- Translate contours, color masses, shadows, depth cues, and environments into intentionally designed cel-animation grammar.
- Let source content select a suitable **scene mode** without making every photo follow the same template.
- Support single-frame transformation, coherent series, and exact-scope revisions to approved outputs.

**Success:** viewers immediately recognize the photograph's essential event and see convincing, mature, production-like cel animation: well-designed shapes, clear black outlines, flat colors, coherent stepped shadows, and an intentional anime background.

## 2. Scope / non-goals

### In v0.1
- Analyze one photograph and produce a concise source map and preservation contract.
- Choose one primary scene mode from a documented list; allow explicit user overrides.
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

## 5. Scene modes (select exactly one primary)

| Mode | When to use | Art direction | Specific guardrail |
| --- | --- | --- | --- |
| `urban-cinematic` | street, park, everyday urban documentary | mature anime film still, careful background perspective, restrained palette, graphic shadows | don't arbitrarily transform the scene into sci-fi |
| `quiet-dramatic` | solo subjects, stillness, waiting, reflective moments | sparse detail, controlled negative space, subtle emotional acting, large light/shadow masses | don't change the subject's gesture or expression |
| `dynamic-action` | running, play, movement, decisive moments | action-keyframe energy, directionality, forceful pose silhouettes, tighter value grouping | don't invent new gestures, people, speed lines by default |
| `youth-energetic` | candid children, friendly interactions and play | brighter clear accent colors, expressive but believable acting | maintain age, dignity, and actual interaction |
| `sci-fi-industrial` | existing machines, infrastructure, geometric cityscapes | hard perspective, mechanical/architectural mark making, controlled industrial lighting | sci-fi conversion/invented tech only if user requests |
| `everyday-still-life` | pets, fish, food, small objects, close-up everyday observations | elegant silhouette, simplified object shapes, source-derived flat palette and hard-edged accents | don't add animals/objects or convert real anatomy into generic cartoon icons |

Scene modes are **rendering strategies**, not separate franchises. They share the same visual DNA. In a series, modes may vary, but line/shadow/material behavior should remain recognizably coherent.

## 6. User-controllable parameters

Keep natural language as the main interface; formal fields are internal and optional.

| Field | Default | Allowed values |
| --- | --- | --- |
| `style_strength` | `balanced` | `subtle`, `balanced`, `strong` |
| `identity_lock` | `high` | `high`, `balanced`, `stylized` |
| `background_policy` | `simplify` | `preserve`, `simplify`, `redesign` |
| `composition_policy` | `source-guided` | `locked`, `source-guided`, `recompose` |
| `scene_mode` | `auto` | `auto` or one named mode |
| `aspect_ratio` | `original` | `original` or explicit ratio |
| `typography` | `none` | `none`, `user-specified` |
| `output` | `single-frame` | `single-frame`, `series` |
| `revision_mode` | `new-concept` | `new-concept`, `master-lock` |

`strong` increases stylization, **not license to alter the factual action or replace identity**. `redesign` can remodel unimportant environment only; drastic story changes need user approval.

## 7. Default processing workflow

1. **Inspect** reference photograph(s) and any user style references.
2. **Map** Source Map, P0/P1/P2 anchors, emotional register, constraints and pitfalls.
3. **Select** primary scene mode and summarize the visual proposition in one sentence (what makes this an animation frame, what remains from the photograph).
4. **Resolve** user overrides, preservation level, original aspect ratio and background policy; avoid inventing unspecified typography.
5. **Build** an image-edit brief from (a) source fidelity, (b) cel visual DNA, (c) mode-specific direction, (d) background & composition, (e) exclusions, (f) evaluation checklist.
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
4. **Scene mode:** one primary strategy and its mood, lighting, palette and motion/stillness rules.
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
- **Composition:** source relationship survives; intended scene mode reads clearly.
- **Integrity:** anatomy, faces, hands, physical perspective and unintended text are acceptable.
- **Series coherence:** if relevant, image belongs in the same cel-animation universe.

Hard failures: wrong number of people/fish, major identity drift, changed core action, malformed anatomy, unrelated inserted objects, unrequested text/branding, or output that stays photorealistic. Reject or transparently flag these.

## 11. Initial test matrix

Reuse the five user-provided street photos as **local-only** test fixtures; never upload/commit private reference photos without express request.

| Photo | Expected auto mode | Main potential failure |
| --- | --- | --- |
| Fish in green bucket | `everyday-still-life` | invents fish, changes count/colors/anatomy |
| Older man and backpack on bench | `quiet-dramatic` | changes face/gesture/thermos/hat |
| Two children playing | `dynamic-action` or `youth-energetic` | changes interaction or age, deforms hands |
| Group of older men | `urban-cinematic` | duplicates heads, invents faces, loses individuality |
| Two anglers with onlookers | `urban-cinematic` | removes fishing rods / changes crowd and spatial relations |

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
│   ├── scene-modes.md
│   ├── prompt-construction.md
│   └── quality-gates.md
├── presets/
│   └── default.yaml
├── agents/
│   └── openai.yaml          # optional, if supported by target runtime
├── tests/
│   └── scenarios.md         # no user photographs checked in
└── docs/
    └── superpowers/specs/
```

`SKILL.md` should be a concise trigger/workflow entrypoint; detailed style grammar and QA belong in `references/`, loaded on demand. No executable toolchain or external dependency is required for v0.1 unless a selected runtime needs an image tool bridge.

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
4. **V0.1 scope:** six scene modes described above; no new generation engine — proposed default: YES.
5. **Target runtime:** optimize first for Codex Agent Skill; keep portable layout to other Agent Skills readers — proposed default: YES.

**Next gate:** owner reviews/approves this design. Then prepare an implementation plan and author the actual Skill and reference files, followed by baseline vs skill image tests.
