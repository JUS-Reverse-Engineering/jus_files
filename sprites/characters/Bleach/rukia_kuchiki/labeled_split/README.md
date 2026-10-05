# Rukia Kuchiki categorized art

<!-- current-art-summary:start -->
Character package: 129 categorized assets, including 0 transparent native tracks. 396 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 50 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 185; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `bl_b_03`, `bl_b_03_4`, `bl_b_03_5`, `bl_b_03_6`, `bl_s_03`, `bl_s_03_2`, `bl_s_03_3`.

Categories: `attacks_heavy` (19), `attacks_light` (5), `attacks_special` (34), `generics` (15), `hitstun` (15), `misc` (2), `panels` (5), `supports` (14), `taunt` (2). Total: 111 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 34 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 44 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Source 5k Flip the effects to fit / Example at y2490 remains composition guidance; no universal facing rule is inferred.
