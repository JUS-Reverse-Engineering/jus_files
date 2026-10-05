# Sasuke categorized art

<!-- current-art-summary:start -->
Character package: 133 categorized assets, including 0 transparent native tracks. 462 canonical native cell PNGs. [Attack map](ATTACKS.md) contains 47 action groups.

Authored alternate-facing assets: 0. Source-controlled loose-pose references: 3. Move groups retain body, summon, projectile, effect and conditional-phase associations in `art.json`. Shared art records every action use. Alternate-facing assets preserve actual authored pixels and record runtime display mirroring separately.

Unresolved native node records: 138; unsupported texture records: 0. Source references and poses with unknown sequence positions remain explicit; art-track key times do not establish gameplay trigger times.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `na_b_02`, `na_b_02_7`, `na_b_02_8`, `na_s_02`, `na_s_02_2`.

Categories: `attacks_heavy` (13), `attacks_light` (8), `attacks_special` (31), `generics` (17), `hitstun` (15), `misc` (3), `panels` (4), `supports` (8), `taunt` (1). Total: 100 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 77 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 52 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- 7k/8k lightning/fire compound strips and source UNUSED SPRITES have no certified playback/composition.
