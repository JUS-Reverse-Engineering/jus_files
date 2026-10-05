# Heihachi Edajima categorized art

<!-- current-art-summary:start -->
Character package: 103 categorized assets, including 0 transparent native tracks. 379 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 45 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 0. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 116; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `oj_b_01`, `oj_b_01_8`, `oj_s_01`, `oj_s_01_2`.

Categories: `attacks_heavy` (16), `attacks_light` (7), `attacks_special` (18), `generics` (17), `hitstun` (15), `misc` (2), `panels` (2), `supports` (8), `taunt` (2). Total: 87 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 31 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 35 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Source lower-left lightning/tornado material is reference-only pending per-component source/native correspondence.
- 8k giant fist ground effects require keyed transforms. No 3k support archive exists.
