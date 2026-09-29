# FRIEZA kit

**Series:** DRAGON BALL

## Battle panels

The panels below are the character’s battle koma of size 4 or larger listed in Genroh’s guide. Alternate panels at the same size are listed separately.

### 6-koma — Power
- Panel shape: `[][] / [][] / [][]`
- J-Soul: 160
- Special A: 100% Full Power (Power)
- Special B: Death Ball (Power)

## Passive effects

- Gain more SP energy when KOing opponents.
- Gain more SP energy when taking damage from your opponents.

## Ultimate action

Hold Select to slowly regain SP energy.

## Boosts

- Dio (JJBA)
- Orochimaru (Naruto)
- Sasuke (Naruto)

## Character guide

[GameFAQs character guide 47666-frieza](https://gamefaqs.gamespot.com/ds/933199-jump-ultimate-stars/faqs/47666) is available in the local source collection for move details and combos.

## Source

[Genroh, Jump Ultimate Stars FAQ/Walkthrough](https://gamefaqs.gamespot.com/ds/932999-jump-ultimate-stars/faqs/45856), C5. Koma (Character) List. The kit fields above are transcribed from this guide’s character entry.

## Full movesets from GameFAQs research extracts

The following attack and combo details were extracted into `docs/research/gamefaqs-movesets/`. They are transcriptions or interpretations of player-written FAQs, not verified game measurements.

### Frieza — FAQ 47666

**Source:** `47666-frieza.txt`; author: tech_man54.

#### Basic attacks and actions

- **B:** Frieza spins around and smacks with his tail. Connects with a lot of his other attacks, especially Up B into aerial Y. Recovery is very quick.
  - Damage: 8 damage to Power/Laughter, 12 damage to Knowledge.

- **side B:** Frieza moves forward and hits the enemy with his tail. Nice range, connects well with Side Y. Minimal recovery.
  - Damage: 8 damage to Power/Laughter, 12 damage to Knowledge.

- **up B:** Frieza dashes into the air and smacks the enemy up a bit. Connects with Aerial Y. Frieza must be near the enemy to hit. Vulnerable while falling back, resolvable with a quick fall.
  - Damage: 8 damage to Power/Laughter, 12 damage to Knowledge; Properties: launcher.

- **down B:** This move delays a bit. Frieza moves his hand up and causes the opponent's character to change (if they have another character). Recovery leaves you open to attack.
  - Damage: 10 damage to Power/Laughter, 15 damage to Knowledge; Properties: forced switch.

- **Y:** Frieza hits the opponent with his tail then flips back, launching the opponent in the air. Good for starting combos and juggling. Nice recovery.
  - Damage: 10 damage to Power/Laughter, 15 max damage to Knowledge; Properties: launcher.

- **side Y:** Frieza points his finger forward and shoots purple beams. Pressing Y again shoots more. Good for starting combos. Does less damage at long range.
  - Damage: 20 MAX damage to Power/Laughter, 30 MAX damage to Knowledge; Properties: projectile, mash-extend.

- **up Y:** Frieza lifts 6 rocks from the ground and mentally throws them forward. Maximum of 3 hits to one person. Recovery leaves you open.
  - Damage: 24 MAX damage to Power/Laughter, 36 MAX damage to Knowledge; Hits: 3; Properties: projectile, multi-hit.

- **air Y:** Frieza hovers, makes a purple sphere, and shoots it down. Particularly good for ringing out since it traps the opponent until it hits the ground. Opponent should quick fall to avoid getting hit on the way down.
  - Damage: 18 damage to Power/Laughter, 27 damage to Knowledge; Properties: projectile.

- **down Y:** Frieza raises his hand and shoots the opponent forward. This move delays but guard breaks. The opponent must be a bit away from Frieza's hand for it to connect. Recovery is slow.
  - Damage: 20 damage to Power/Laughter, 30 damage to Knowledge; Properties: guard break.

- **select — Ultimate Action:** Frieza hovers slightly in the air and a purple aura surrounds him, restoring SP quickly (about 4 SP per second).

#### Battle koma specials (4+ panels)

- **6-koma:**
  - X — Special Attack A: Frieza shines purple after a 1 second delay, then shoots forward quickly. If he touches the opponent he continues blasting away in quick succession. The last hit guard breaks. (Damage: 56 damage to Power/Laughter, 84 damage to Knowledge; Hits: 8; Properties: guard break)
  - up X — Special Attack B: Frieza raises his finger with a 2.5 second delay charging up a hit, then shoots a purple orb forward that explodes on touching the enemy. Has immense knockback. (Damage: 38 damage to Power/Laughter, 57 damage to Knowledge)

#### Combos

- B, Y, and Up X. 66 max damage to Power/Laughter, 74 max damage to Knowledge. Must be performed very quickly or the Up X won't connect.
- B, Side B, and X. 87 max damage to Power/Laughter, 108 max damage to Knowledge. Fast, easy, basic combo; usable with support koma's for added damage.
- B, Side B, Side Y. 36 max damage to Power/Laughter, 54 max damage to Knowledge. Non-special combo, two tail hits and an ongoing attack.
- Side B, Y, Up B (wait a little), Y. 36 damage to Power/Laughter, 66 damage to Knowledge. Must wait a little or the enemy will be too high for the final Y to hit.
- B, Side B, Side Y, Huh Huh Brothers (3), X. Called 'Ultimate Might'; start with B and Side B, hit Side Y, count to 4, start Huh Huh Brothers, then press X.
- B, Side B, Y, Seiya 3, Up X. 88 max damage to Power/Laughter, 132 max damage to Knowledge. Use Seiya at the same time as Y, then quickly position under the opponent and use Up X.
- B, Hibari 3 ----> Aerial Y ('Frieza's noob combo'). Hit once with B, immediately unleash Hibari to drag them to the edge and throw them, then use Aerial Y for a Ring-Out. Guide states damage is 'DEATH' if done correctly.

#### Guide notes and unresolved details

- The guide states 'Since Frieza has only one koma, none of the damage values are changed (laughter to power or, ore vice-versa)' -- this appears to describe the game's nature damage-modifier rule (Power/Laughter share one value, Knowledge another) rather than stating Frieza's own nature. The guide never explicitly names Frieza's nature, so natures_available is left empty and koma.nature is null.
- Frieza is described as having only a single 6-koma shape, no help koma and no support koma of his own ('He has no support koma, or any other unlockable stuff'). Sections F6 and F7 ('Useful Help Koma', 'Useful Support Koma') list OTHER characters' koma to pair with Frieza in a deck, not Frieza's own koma -- these were not extracted as koma entries since they belong to other characters, not Frieza.
- F10 'Good Battle Komas' similarly lists other characters (Dio 6-koma, Vegeta 4-koma) as good deck partners for Frieza, not Frieza's own koma.
- The B-string / mash-extend behavior is only described for Side Y ('You can shoot more if you press the Y button'); no separate 'B string' move is described in the guide.
- chr_b_note table shows chr_b 41 with HP column 261 and koma-size column 6, consistent with the guide's single 6-koma claim.
- Damage for the 'noob combo' (B, Hibari 3, Aerial Y) is given only as 'DEATH' with no numeric value; copied as-is rather than invented.
