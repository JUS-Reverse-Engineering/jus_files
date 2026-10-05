# Gon Freecss categorized art

<!-- current-art-summary:start -->
Character package: 121 assets, 121 visible strips/panels and 0 transparent native tracks. 425 referenced canonical native cell PNGs. [Attack map](ATTACKS.md) contains 50 action groups.

Native diagnostics in the current manifest: 78 nodes without cell tracks, 0 unresolved-node records and 0 unsupported-texture records. These diagnostics describe decoding; gameplay selection and composition remain separate review items.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `hh_b_01`, `hh_b_01_4`, `hh_b_01_5`, `hh_b_01_6`, `hh_s_01`, `hh_s_01_2`, `hh_s_01_3`.

Categories: `attacks_heavy` (16), `attacks_light` (6), `attacks_special` (44), `generics` (15), `hitstun` (15), `misc` (4), `panels` (6), `supports` (12), `taunt` (3). Total: 121 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 26 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 1 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Source Pull In boxes are composition instructions and retained references, not fighter frames.
- 3k fishing-rod and 4k/5k aura compositions require transforms; native cells preserve full geometry.
