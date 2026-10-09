# Atmosphere Profiles — Evidence-Based Optional Modifiers

Photo Cel Studio chooses **zero profiles** when the reference photo lacks relevant lighting or weather. In automatic selection, **source evidence** is mandatory and **no invented** rain, sun, neon, haze, snow, lens flares or time change is permitted. Atmosphere profiles modify drawing of observed light; a profile never becomes a primary scene mode.

These are **Atmosphere Profiles**, distinct from the one **Cel Style Profile** in `references/cel-era-profiles.md`. Style controls drawing era/palette/finish; atmosphere describes observed environmental light/weather. Noir never supplies evidence of night, warm-daily never supplies evidence of sunset, and industrial never supplies evidence of neon. Apply atmospheric hues locally within the selected style while preserving actual light colors, geometry and compatibility.

| Profile | File | Positive source evidence |
| --- | --- | --- |
| `neon-night` | [atmospheres/neon-night.md](../atmospheres/neon-night.md) | Dark sky/night exposure, localized red/blue/green light pools, signs, cast colored light. |
| `golden-hour` | [atmospheres/golden-hour.md](../atmospheres/golden-hour.md) | Warm direct illumination, long soft-edged geometric cast shadows, setting or rising sun cues. |
| `rainy` | [atmospheres/rainy.md](../atmospheres/rainy.md) | Existing wet roads/windows/garments and their local reflections, visible wet sheen or droplets. |
| `snowy` | [atmospheres/snowy.md](../atmospheres/snowy.md) | Distinct white snow masses, covered edges, tracked texture, cool shadow depth. |
| `misty` | [atmospheres/misty.md](../atmospheres/misty.md) | Depth layers diminishing in contrast, edges disappearing with distance, defined near-field objects. |
| `backlit` | [atmospheres/backlit.md](../atmospheres/backlit.md) | Subject dark-side form with bright background and edge illumination; physically grounded light direction. |

## Selection algorithm

1. Inspect actual image before applying any tags. Extract source evidence for lamps, sun direction, clouds/water, wet reflections, snow, mist and rim light.
2. If `atmosphere_profiles: none`, use none. If `auto`, choose **zero to two** visibly justified and compatible profiles. If none match, use **zero profiles**.
3. If an **explicit user** request specifies a changed time/weather, do it as a deliberate creative environmental alteration and explain that documentary context changed. This is not automatic classification.
4. Prefer the strongest observed illumination. Where two rules conflict, prioritize user-approved master restrictions, then source geometry, then one dominant profile.
5. The output brief states where each profile is supported by visual evidence, what it changes, and what it must not change.

## Compatibility examples

- `neon-night + rainy` is coherent for an actually wet night street with visible signage/light sources; respect actual reflections.
- `golden-hour + backlit` is coherent only when the low, warm light falls behind the subject.
- `neon-night + golden-hour` must **not** be silently mixed as one physical time-of-day. Choose one supported dominant condition or ask about an explicit conceptual change.
- `snowy + rainy` should not be automatically combined without credible simultaneous evidence of both.
- Some images contain subtle lighting that fits none: choose 0, not `golden-hour` by habit.
- In a series, scene drawing grammar remains consistent even when one frame has neon and another no atmosphere.

## Limits and extensibility

Profiles never override P0 identity, action, key objects or agreed camera layout. Cel linework remains decisive; don't solve night/rain by applying photorealistic glow or full-image blur.

For a seventh profile, create `atmospheres/<id>.md` from `templates/atmosphere-template.md`, add a **registry** row here and a regression scenario to `tests/scenarios.md`, **without editing** core `SKILL.md`. New light/weather cases should still require visible evidence by default.
