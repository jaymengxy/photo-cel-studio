# Source Map — Read Before Art Direction

Analyse the supplied **reference image** itself, not filenames or earlier guesses. Never claim to know the person, exact place, date, brand or event unless grounded in visible evidence or user context.

## Internal Source Map contract

```yaml
source_map:
  type: "portrait | street | action | crowd | pet | vehicle | architecture | landscape | food | macro | interior | still-life | other"
  hero: "primary recognizable subject"
  count: "exact only when visibly countable; otherwise uncertain"
  camera: "orientation, framing, perspective, horizon, relative subject scale"
  actual_action: "visible gesture/movement/object interaction"
  relationship: "who/what is next to or interacting with what"
  P0: ["identity-defining appearance", "actual body pose", "essential objects or event"]
  P1: ["secondary but meaningful objects", "place-defining geometry", "lighting direction"]
  P2: ["non-essential clutter", "incidental textures"]
  color_evidence: ["dominant hue and key identity accent"]
  atmosphere_evidence: ["only directly observed time/weather/light cues"]
  drawing_opportunities: ["readable silhouette", "graphic shadow", "negative space"]
  risks: ["overlapping limbs", "small text", "fine mechanics", "species anatomy"]
```

## Anchor priority

- **P0 / must survive:** primary people/animals/objects, subject count when visible, distinct facial traits/coat markings, action, pose, clothing identity cues, relationship to essential props. Do not transform a candid action into a different scene.
- **P1 / ordinarily survive:** camera angle, important location/geographic architecture, lighting direction, interaction geometry and distinguishing incidental props. Simplify only when it does not rewrite the observed story.
- **P2 / expendable:** busy low-value texture, distracting clutter, redundant detail. Reduce detail by drawing smarter shapes, not by hallucinating a different place.
- Do not convert a hard-to-read detail into a confident invented fact. Say “partially obscured” and preserve the perceptual impression.
- For a photograph of multiple individuals, record spatial order and distinguishing clothing; don't replace everyone with one generic animation face.

## Quick scene reading

1. What would an observer recognize after one second?
2. What action makes this moment meaningful?
3. Which camera perspective, spatial overlap or object relation proves it is the same moment?
4. Which 2–5 areas deserve drawn detail, and where can the background breathe?
5. Which light/weather cues are genuinely visible?
6. Which failure would make the transformed picture factually wrong?

Then route through the scene-mode registry and atmosphere registry independently. No artwork is produced at this stage.
