# Preservation and Master Lock

## Principle: redraw appearance, not history

A style transformation changes the *rendering medium*, not the underlying real-world event. Prioritize explicit user instructions and approved edits; protect P0 anchors before applying any visual mode.

| Anchor | Default policy | Example |
| --- | --- | --- |
| P0 core event | preserve | Two children running together; a person adjusting their backpack; two people fishing |
| P0 recognizable subject | preserve where model permits | Face age, body build, pet fur markings, car wheelbase, key gestures |
| P0 count | preserve if visible | Number of individuals, fish or vehicle wheels |
| P1 place/camera context | maintain unless user requests redesign | Bench, sidewalk perspective, mountain skyline, window structure |
| P2 incidental texture | simplify | Stray litter, wall grain, fine fabric texture |

### Real people and crowded/overlapping groups

- Protect distinct individuals: different heads, face shapes, eyewear, hair and clothing. Explicitly forbid same-face replacement or duplicated persons.
- Inspect **overlap** between heads, arms, hands and props. **Count** bodies, faces and visible arms if possible; do not invent hidden anatomy behind occlusion.
- When person count cannot be verified due to partial cropping, do not assert a false count; preserve visible silhouettes and crowd geometry.
- Each **hand** must attach to a believable body and interact with the correct object; keep original limb position, gesture and age cues.
- Maintain dignity and authentic ages for children and older adults. “Anime style” is not permission to rejuvenate everyone.

### Animals, food, vehicles and place

- Preserve species/breed, fish tail/fins, pet eyes/ears/markings, number of paws/legs and original posture; no automatic humanoid traits.
- Preserve dish type and plated ingredients; no unsolicited substitutions or new garnish.
- Preserve vehicle/model identity if discernible, wheel count, perspective, bike frames, train doors and mechanical relationships.
- Preserve architecture/terrain that locates the scene; never randomize window/step counts, hillside outlines or perspective to look “more anime.”
- Printed text in the source is not free license to invent readable new brands. If the editing model cannot copy it accurately, simplify illegible marks instead of supplying false text.

### Conflicts and transformations

- The priority order is user-approved master/source identity > preservation P0 > common cel art direction > mode > atmosphere.
- If a user requests wholesale creative re-staging, disclose that the final image becomes **interpretation**, not a documentary-equivalent frame.
- If the user expressly asks for snow on a sunny street, that is an allowed creative setting change, not observational automatic weather classification.

## Master-lock mode

Activate **master-lock** when the user points to an **approved** output and asks “only change X” or “everything else unchanged.” Lock the accepted camera/crop, pose, arrangement, background, lighting, color system, shared visual grammar and identity. Specify the smallest target region and requested edit; do not treat the original source photo as permission to regenerate unrelated areas.

Localized editing or masking is preferable when available, but prompt controls **cannot guarantee pixel-perfect** unchanged regions. Recheck the rest of the approved image; if significant drift occurs, flag it or decline a false precision claim rather than reporting a perfect edit.

## User-facing failure reporting

Always distinguish: *intended locks* vs *visibly preserved result*. If recognizable identity, essential props, overlapping figures or anatomy drift, do not mark the image as an exact faithful conversion. Offer a narrower corrective pass where supported; never upload private source photos to public repositories by default.
