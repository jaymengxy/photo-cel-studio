---
name: photo-cel-studio
description: Use when transforming user-supplied photographs into distinctive hand-drawn cel-animation stills, including street photos, portraits, animals, cars, landscapes, architecture, food, macro, interiors, and coherent photo series.
---

# Photo Cel Studio

Turn a real photographed moment into a believable mature hand-drawn cel animation frame. **Reality of the event first; cel drawing language second; scene-specific art direction third.** Reinterpret broad 1980s–1990s Japanese cel-era drawing traits without reproducing a particular animation property.

## When to use

Use this Skill for photo-to-cel conversion, series-matched stills, source-grounded lighting treatments, and revisions to accepted cel results. Do not use it for purely photographic retouching, exact restoration, 3D anime avatars, or animation/video generation.

## Workflow

1. **Inspect the actual image**, not just the user's caption. Read `references/source-analysis.md`; construct a Source Map with subject count, primary action, camera view, P0/P1/P2 preservation anchors, original light, and risk points. If content is obscured, note uncertainty; never infer hidden facts.
2. **Lock the documentary core.** Read `references/preservation-rules.md`. Protect P0 identity, silhouettes, relative positions, actual activity and essential object relationships. The user can override creative details but should not unknowingly lose documentary anchors.
3. **Apply the shared cel DNA.** Read `references/cel-style-grammar.md`. Clean decisive ink contours, expressive line weight, broad flat-color plates, 1–2 hard-edge shadow masses, believable anatomy, designed backgrounds. Never substitute a global cartoon filter.
4. **Choose exactly one primary scene mode** from `references/scene-modes.md`. Read **only its selected `modes/<id>.md`**, on demand. Unknown subject categories use a neutral source-derived cel treatment; do not force a mismatched mode.
5. **Choose 0–2 atmosphere profiles** using `references/atmosphere-selection.md`. Read only applicable `atmospheres/<id>.md`, on demand. Auto-selection requires visible weather/light evidence; no evidence means none. If a user explicitly asks for different weather/time, label that as a creative setting change. Reject incoherent lighting combinations.
6. **Resolve controls**, using `presets/default.yaml` unless the user supplies overrides: balanced style, high identity lock, simplified backgrounds, source-guided composition, original aspect, no typography, one still frame. A stronger drawing style is not permission to replace people, poses or events.
7. **Compose an image-edit brief** with `references/prompt-construction.md`: actual source photograph + must-preserve contract + cel DNA + one primary mode and optional atmospheres + camera/background plan + negative constraints. Pass the original as a **reference image** to an available image-edit or image-generation tool. If unavailable, provide the brief and **do not claim** an image was generated.
8. **Review the result** using `references/quality-gates.md`: compare against the original for count, faces, poses, meaningful props, cel contours, flat paints, shadows, anatomy, weather and unrequested text. Make at most one targeted correction by default when the tool supports it, and identify unresolved fidelity drift.
9. **Deliver** the visual and short explanation of the selected primary mode and optional atmospheres. For multiple photos, lock one shared line/shadow/material grammar while respecting different content. For a previously approved image, apply **master-lock**: change only the specified feature.

## Decision precedence

Explicit user constraints and approved-master lock > P0 preserved documentary content > shared cel grammar > primary mode > atmosphere modifiers > decorative preferences.

Do not invent people, faces, brands, props, signs, metadata, or weather without an explicit creative request. Do not upload source photography to a public repository; do not promise pixel-perfect generative identity preservation. See `references/quality-gates.md` for honest failure reporting.
