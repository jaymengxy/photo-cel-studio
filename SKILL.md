---
name: photo-cel-studio
description: Use when transforming user-supplied photographs into distinctive hand-drawn cel-animation stills, including street photos, portraits, animals, cars, landscapes, architecture, food, macro, interiors, and coherent photo series.
---

# Photo Cel Studio

Turn a real photographed moment into a believable hand-drawn cel animation frame. **Preserved event → Cel Style Profile → Scene Mode → Atmosphere → Render → Quality Gate.** Default to mature traditional cel-era drawing (`mature-ova`); extract general visual craft rather than a particular property's characters or shots.

## When to use

Use this Skill for photo-to-cel conversion, series-matched stills, source-grounded lighting treatments, and revisions to accepted cel results. Do not use it for purely photographic retouching, exact restoration, 3D anime avatars, or animation/video generation.

## Workflow

1. **Inspect the actual image**, not just the user's caption. Read `references/source-analysis.md`; construct a Source Map with subject count, primary action, camera view, P0/P1/P2 preservation anchors, original light, and risk points. If content is obscured, note uncertainty; never infer hidden facts.
2. **Lock the documentary core.** Read `references/preservation-rules.md`. Protect P0 identity, silhouettes, relative positions, actual activity and essential object relationships. The user can override creative details but should not unknowingly lose documentary anchors.
3. **Choose exactly one Cel Style Profile.** Read `references/cel-era-profiles.md` and **only the selected `profiles/<id>.md`**, on demand. An unspecified style always resolves to `mature-ova`, even for vehicles. Honor explicit style choices; only explicit `cel_style_profile: auto` permits content-based style routing. Recommendations never replace the selected style.
4. **Apply shared cel grammar and choose exactly one primary scene mode.** Read `references/cel-style-grammar.md` and `references/scene-modes.md`; load only the selected `modes/<id>.md`, on demand. Shared grammar supplies contours, flat plates, hard form shadows and credible structure; Profile supplies era/line/color/finish; Scene Mode supplies subject-specific rules. Unknown categories retain the neutral source-derived fallback, with the selected style intact.
5. **Choose 0–2 atmosphere profiles** using `references/atmosphere-selection.md`. Read only applicable `atmospheres/<id>.md`, on demand. Auto-selection requires visible weather/light evidence; no evidence means none. If a user explicitly asks for different weather/time, label that as a creative setting change. Reject incoherent lighting combinations.
6. **Resolve controls** with `presets/default.yaml` and the registry's profile-specific baselines: balanced style, high identity lock, simplified backgrounds, source-guided composition, original aspect, no typography, one still frame. Profile intensity, palette and surface controls refine drawing without reducing preservation priority or replacing identity colors. Texture never substitutes for drawing.
7. **Compose an image-edit brief** with `references/prompt-construction.md`: Source Description + Preservation Contract + Shared Cel Grammar + Selected Cel Style Profile + Selected Scene Mode/Atmosphere + Composition/Background/Negative Constraints. Expand the profile into executable visual instructions. Pass the original as a **reference image** to an available image-edit or image-generation tool. If unavailable, provide the brief and **do not claim** an image was generated.
8. **Review fidelity and style independently** using `references/quality-gates.md`: count, identity, event, geometry and source light first; then selected-profile linework, 2–3 paint values, background, palette and finish. Fidelity PASS alone cannot establish success. Make at most one targeted correction by default when supported; report both verdicts and unresolved drift.
9. **Deliver** the visual with selected style, primary mode and optional atmospheres. For a series, lock one profile and shared drawing controls while respecting source differences. For explicit same-photo multi-profile comparisons, follow the independent-frame protocol in `references/prompt-construction.md`. For an approved image, apply **master-lock**: change only the specified feature; a new style request does not unlock unrelated regions.

## Single-image output contract

For a **single source** photo request, produce one independent animation frame at the requested/original ratio: **no collage**, no multi-panel grid, no contact sheet, no before/after composite, no adding other reference photos into the rendered scene. For a set of photos, generate **one output per input** by default, each as its own artifact; optionally show a *separate* contact sheet only when explicitly requested.

An explicit multi-profile comparison requests one separate frame per profile from the same original, never a default collage or blended-style frame.

Keep the original light direction and actual cast-shadow shapes unless the user explicitly requests a changed lighting scene; **no invented shadows** solely to appear cinematic.

## Decision precedence

Explicit user constraints and approved-master lock > P0/P1 preserved documentary content > shared cel grammar > selected Cel Style Profile > primary Scene Mode > Atmosphere modifiers > decorative preferences.

Do not invent people, faces, brands, props, signs, metadata, or weather without an explicit creative request. Do not upload source photography to a public repository; do not promise pixel-perfect generative identity preservation. See `references/quality-gates.md` for honest failure reporting.
