# SON GOHAN kit

**Series:** DRAGON BALL

## Battle panels

The panels below are the character’s battle koma of size 4 or larger listed in Genroh’s guide. Alternate panels at the same size are listed separately.

### 4-koma — Power
- Panel shape: `[] / [] / [] / []`
- J-Soul: 136
- Special A: Kamehame Ha (Power)
- Special B: Masenko (Power)

### 5-koma — Power
- Panel shape: `[][][] /   [][]`
- J-Soul: 152
- Special A: Father & Son Kamehame Ha (Power)
- Special B: Burst of Anger (Power) — (Gains Attack-Boost effect)

## Passive effects

- When KOed and return, Goku's max Health and SP gauge increases.

## Ultimate action

Hold Select to slowly regain SP energy.

## Boosts

- Kuririn
- Goku
- Robin (One Piece)

## Character guide

[GameFAQs character guide 46542-gohan](https://gamefaqs.gamespot.com/ds/933199-jump-ultimate-stars/faqs/46542) is available in the local source collection for move details and combos.

## Source

[Genroh, Jump Ultimate Stars FAQ/Walkthrough](https://gamefaqs.gamespot.com/ds/932999-jump-ultimate-stars/faqs/45856), C5. Koma (Character) List. The kit fields above are transcribed from this guide’s character entry.

## Full movesets from GameFAQs research extracts

The following attack and combo details were extracted into `docs/research/gamefaqs-movesets/`. They are transcriptions or interpretations of player-written FAQs, not verified game measurements.

### Gohan — FAQ 46542

**Source:** `46542-gohan.txt`; author: BlueAlchem1st; version 1.1.

#### Basic attacks and actions

- **B — Chop:** Standard B attack, a chop.
  - Damage: Power/Laughter 8, Knowledge 12.

- **side B — Sliding Kick:** Forward + B, a sliding kick.
  - Damage: Power/Laughter 8, Knowledge 12.

- **up B — Upward Chop:** Up + B, a chop aimed upward.
  - Damage: Power/Laughter 8, Knowledge 12.

- **down B — Push aside with Ki:** Down + B pushes the opponent aside with Ki and changes Gohan's battle character (forced switch).
  - Damage: Power/Laughter 8, Knowledge 12; Properties: forced switch.

- **air B — Kick (Spike attack):** A+B, a kick used as a spike attack. The guide also describes an aerial B as slightly risky: if it misses you are left open, but hitting an opponent near a ledge with it sends them off the stage for edge guarding.
  - Damage: Power/Laughter 8, Knowledge 12.

- **Y — 5 Rapid Punches:** Standard Y attack, five rapid punches.
  - Damage: Power/Laughter 17, Knowledge 25; Hits: 5; Properties: multi-hit.

- **side Y — 4 Rapid Ki Blasts:** Forward + Y fires rapid Ki blasts; keep pressing Y to continuously fire blasts up to 16 times, with a slight pause when the attack ends. It hits characters holding on a ledge and can interfere with recovery, though there is a delay after 16 beams.
  - Damage: 4 (if all hit) Power/Laughter, 6 (if all hit) Knowledge; Properties: mash-extend, multi-hit.

- **up Y — Ki blast upward at 45-degree angle:** Up + Y fires a Ki blast upward at a 45-degree angle.
  - Damage: Power/Laughter 15, Knowledge 22; Properties: projectile.

- **down Y — Forward Charge:** Down + Y is a forward charge that guard breaks.
  - Damage: Power/Laughter 16, Knowledge 24; Properties: guard break.

- **air Y — Ki blast downward at 45-degree angle:** A+Y fires a Ki blast downward at a 45-degree angle. This is Gohan's main aerial attack; the second blast can be fired almost immediately after the first, even if the first missed or was blocked.
  - Damage: Power/Laughter 16, Knowledge 24; Properties: projectile.

- **select — Ultimate Action - Regain SP:** Hold Select to regain SP. This is the Battle Koma 4 Ultimate Action.

#### Battle koma specials (4+ panels)

- **4-koma — power:** HP 136.
  - Passive: When KO'd, Max SP and Max HP and SP increase
  - X — Special A - Kamehameha Wave: Kamehameha wave that lasts 1/2 a second. (Damage: Power/Laughter 36, Knowledge 54)
  - X — Special B - Masenko: Fire a Masenko upward at a 45-degree angle. (Damage: Power/Laughter 28, Knowledge 42)

- **5-koma — power:** HP 152.
  - X — Special A - Father & Son Kamehameha: Fire a Strong Kamehameha wave that pushes your opponent back. Also hits characters hanging on ledges. (Damage: Power/Laughter 42, Knowledge 62; Properties: projectile)
  - X — Special B - Burst of Anger: Increase amount of damage done by 25%, lasts for 5 seconds. Note: Does NOT affect Gohan's Forward +Y. (Properties: status:damage-up)

#### Combos

- B, Up + B, Up + Y -- a simple hit followed by one that sends the opponent up and finish with an upward Ki blast
- Forward +B, Y -- Kick sends the opponent forward and finish with rapid punch. Does not work with all characters since Forward + B sends some characters farther away than others, which causes Y to miss. Works well on the edges since Y stuns an opponent and may cause a ring out. Forward + B can be repeated (about 2, sometimes 3 times depending on the character) to lengthen the combo before Y
- Up + B, Forward + B, Y -- send the opponent up, hit them with forward + B before they hit the ground and finish with Y
- The Chain Combo: Forward + B, Y, Up + Y, repeat -- has the potential to keep the opponent airborne for a while; author reports managing 3 repetitions in a row before the opponent was sent too far to continue

#### Guide notes and unresolved details

- chr_b ambiguity: Battle Koma 4 is labeled '(SSJ1)' and Battle Koma 5 is labeled '(SSJ2)' in the guide, which line up in name with chr_b=4 'Gohan (SSJ)' and chr_b=5 'Gohan (SSJ2)' in chr_b-Complete-Mapping.md, but the mapping table's HP values (258 for both) do not match this guide's per-koma HP (136 for koma 4, 152 for koma 5), so the two cannot be confidently equated to a single chr_b id for this whole file. Left chr_b null.
- The guide's 'A + B' and 'A + Y' inputs for the aerial Kick (Spike attack) and aerial Ki blast are not spelled out as 'air B'/'air Y' by the guide itself; mapped them to 'air B'/'air Y' per schema input vocabulary, but the guide's own notation is 'A + B' / 'A + Y'.
- Help Koma's koma size (number of panels) is never stated by the guide for Gohan's own help koma; left size null. The '4Koma Only!!' and '5Koma Only!!' headers in Ally Boosts refer to Krillin's and Piccolo's own help koma sizes, not Gohan's.
- Support Koma 2 and 3's koma size fields were inferred from their section headers ('Support Koma 2', 'Support Koma 3'), which the guide uses as both the koma's display name and, apparently, its size.
- Guide gives a single 'Standard Attacks' table (B/Y strings) without stating whether these differ between Battle Koma 4 and Battle Koma 5 (SSJ1 vs SSJ2 forms); treated them as top-level moves shared across the character rather than duplicating per koma, since the guide does not say they change.
- Special B - Burst of Anger has no listed damage/hit count (it's a self-buff), consistent with the guide not stating one; left damage/hits null.
- Guide credits 'Genroh' for an unspecified prior guide it relied on; not otherwise relevant to moveset data.
