# melonDS savestates

Battle states for the agent harness — start an experiment from a known position instead of navigating there every time. These used to live only in `/tmp/jus_emu/states/`, which disappears on reboot.

**Only the expensive ones are tracked.** A savestate is a derived artifact, and this repo would rather rebuild derived things than store them. The ones here either cost real manual effort no script can recreate, or gate an interactive session where a slow rebuild would waste the owner's time. Anything a script regenerates in a couple of minutes is left out on purpose — see "Not kept" below.

**Stored gzipped.** Each raw `.mln` is 18.4 MB and compresses to about 1.9 MB.

```bash
mkdir -p /tmp/jus_emu/states
for f in jus_files/save_states/*.mln.gz; do
  gunzip -c "$f" > "/tmp/jus_emu/states/$(basename "$f" .gz)"
done
cp jus_files/save_states/*.meta.json /tmp/jus_emu/states/
# then, with the emulator running:
cd scripts/emu && python3 jusemu.py state load pos_base
```

The `.meta.json` files carry the framecount and session id from when each state was saved.

## Two things to know before trusting any of these

**Addresses are session-local, but a savestate restores RAM exactly.** Every address that was valid when a state was saved stays valid each time you reload *that* state. Confirmed: `luffy_training` reloaded in a fresh emulator process and Luffy's ability bitset still read `0x02005200` at `0x02244308`. What does *not* carry over is addresses between *different* states or different battles. Re-derive with `find_battle_structs.py` whenever you switch states.

**Loading these repeatedly can hang melonDS.** It happened twice in one session, both times right after "Resetting JIT block cache". The process stays alive and keeps drawing its last frame, so it looks healthy — only the bridge framecount gives it away. Check with `scripts/emu/emu_health.py`.

## The states

| slot | what it is |
|---|---|
| `pos_base` | **The damage reference.** Goku (`chr_b[0]`, abilities `[7, 15]`) against the ability-free dummy `chr_b[70]`, 112.0 max HP, ability count 0. Positioned so a B press lands clean: 384 raw net of auto-heal, i.e. 8.0 true. Used for the 32-bit ability sweep. Auto-heal is ON, so read HP per frame, never before/after. |
| `pos_heal_off` | Same setup with auto-heal switched off, so HP falls steadily instead of bouncing back. |
| `luffy_training` | **The resistor.** Goku against Luffy (`chr_b[12]`, 152.0 max HP, abilities `[9, 25, 12, 14]` — `0x09` blunt resistance and `0x0C` slash weakness). Training mode, so Luffy stands still. Used for the converse resistance test. Opponent HP `0x021DF7F0`, Luffy's entity `0x022441E0`, ability bitset `0x02244308` = `0x02005200`. |
| `ds8t_jj_battle_noheal` | **Owner feel-capture battle.** JJ deck (deck 5): Jotaro `28`, Sanji `14`, Kenshin `36`, Lenalee `46`. Training mode, auto-heal OFF, items + gimmicks OFF, roster verified at save time. Rebuilt by `refresh_savestates.py` on 2026-09-01 for `docs/research/feel-captures/PROTOCOL.md` matches. Kept because a cold rebuild costs several minutes of menu driving and the owner restarts matches often. |
| `ds8t_jj_battle_darktournament` | **Scripted feel-experiment battle.** Same JJ deck (deck 5, Jotaro `28` active) vs the Luffy `12` / Naruto `20` CPU deck, training mode, auto-recover OFF (set and RAM-verified by `match_run.autoheal_off`), on the Dark Tournament stage, which the owner picked on 2026-09-01 because the default stage starts the players on a platform with a wall that scripted approaches ran into. Saved by hand from the owner's navigation (`jusemu state save`), so it cannot be rebuilt by `refresh_savestates.py`. Live position block at save time: `0x0220C074`; player slot array `0x021DF1D4`; opponent `0x021DF7F0`. |
| `pc-kenshin-npc-luffy-dark-tournament` | **Owner-built scripted-sweep state (2026-09-01).** JJ deck with **Kenshin `36` active** (152) vs CPU **Luffy `12`, max 152** (standard weight), Naruto `20` benched. Dark Tournament, training, auto-recover OFF, both on flat ground apart from the walls: P1 x 641.8, victim x 576.0. Menu-saved by the owner, then re-saved through the bridge so the sidecar is real. Live position block `0x0220C074`, slot arrays `0x021DF1D4` / `0x021DF7F0` in all seven `pc-*` states. |
| `pc-kenshin-npc-naruto-dark-tournament` | Same, victim **Naruto `20`, max 144** (active). P1 x 740.5, victim x 676.9. The max-HP control for the launch tiers (`jus-launch-hp-tiers-u1jw`): fraction rule predicts edges 108/72/36, flat rule 114/76/38. |
| `pc-kenshin-npc-nami-dark-tournament` | Same, victim **Nami `15`, max 136** (LIGHT). P1 x 658.7, victim x 576.0. |
| `pc-kenshin-npc-franky-dark-tournament` | Same, victim **Franky `17`, max 176** (HEAVY); Raoh `62` (192) and a damaged Nami benched. P1 x 728.0, victim x 649.6. |
| `pc-kenshin-npc-raoh-dark-tournament` | Same, victim **Raoh `62`, max 192** (HEAVY). P1 x 739.8, victim x 681.4. |
| `pc-kenshin-luffy-guard` | **Guard-break sweep state (2026-09-02).** `pc-kenshin-npc-luffy-dark-tournament` with the in-match pause menu's COM設定 set to **ガード** (START, DOWN, A, A, START), then re-saved through the bridge. The CPU guards after the first hit lands and holds guard until 122 frames pass with no blocked hit. Same live addresses as the parent state. Built for `jus-hitstun-types-0nxs` / `jus-guard-gauge-discovery-7mr8`; the menu dance is scripted but a fresh state costs a launch, so it is kept. |
| `pc-kenshin-nami-guard` | Same, from the Nami parent (LIGHT victim). |
| `pc-kenshin-franky-guard` | Same, from the Franky parent (HEAVY victim). |
| `pc-momotaro-npc-nami-dark-tournament` | MOMO deck with **Momotaro `67` active** (184) vs Nami `15` (136). Owner: Momotaro's X is a **beam**. P1 x 645.4, victim x 576.0. |
| `pc-yusuke-npc-nami-dark-tournament` | MOMO deck with **Yusuke `32` active** (184) vs Nami `15` (136). Owner: Yusuke's X is a **giant high-priority projectile that eats other projectiles**. P1 x 645.4, victim x 576.0. |
| `pc-taikoubou-npc-jotaro-dark-tournament` | **Owner-built 2026-09-03 (second batch, savestate major 14; menu-saved in the fork by the owner, then re-saved through the bridge on 2026-09-03 so the sidecars are real; run 5).** **Taikoubou `68` active** (summoner type; second port character, `jus-4ocm`) vs CPU **Jotaro `28`**. **The only state whose deck has L/R switch hotkeys assigned** in the deck builder (owner: L/R only switch when the hotkey sticker is on a battle koma) — the switch positive control for `jus-e2w4`. Roster verified in run 4 (`jus-e2w4`): deck = Taikoubou `68` 144 / Momotaro `67` 176 / Yusuke `32` 184; L → Yusuke, R → Momotaro. Opponent deck in all eleven: Jotaro `28` 160, Sanji `14` 136, Kenshin `36` 152, Lenalee `46` 128; victim x 576.0. |
| `pc-kakashi-npc-jotaro-dark-tournament` | Same batch. **Kakashi `23` active** vs Jotaro `28`. Deck: Kakashi 144 / Muhyo `59` 128 / Mashirito `57` 144 / Kurama `33` 144. First port character (`jus-kakashi-moveset-map-33lu`). Roster verified (run 4). |
| `pc-muhyo-npc-jotaro-dark-tournament` | Same batch. **Muhyo `59` active** (summoner) vs Jotaro `28`. Fwd+Y / up+Y pop state (`jus-knockback-pop-spot-check-m4uy`). Roster verified (run 4). |
| `pc-sasuke-npc-jotaro-dark-tournament` | Same batch. **Sasuke `21` active** vs Jotaro `28`. Deck: Sasuke 184 / Yoh White Swan `26` 192 / Eve `37` 128 / Kakashi `23` 16. Up+Y pop (`m4uy`), 8-koma X launcher (`jus-launcher-move-spot-check-hiyh`). Roster verified (run 4). |
| `pc-eve-npc-jotaro-dark-tournament` | Same batch. **Eve `37` active** (LIGHT) vs Jotaro `28`. 4-koma X launcher (`hiyh`). Roster verified (run 4). |
| `pc-yohswan-npc-jotaro-dark-tournament` | Same batch. **Yoh (White Swan) `26` active** vs Jotaro `28`. 6-koma X = launcher + blind (`hiyh`). Roster verified (run 4). |
| `pc-yugi-npc-jotaro-dark-tournament` | Same batch. **Yugi `35` active** (summoner) vs Jotaro `28`. Deck: Goku `0` 160 / Yugi 136 / Naruto `20` 144 / Rukia `41` 128. Roster verified (run 4). |
| `pc-mashirito-npc-jotaro-dark-tournament` | Same batch. **Mashirito `57` active** (item-creator) vs Jotaro `28`. Roster verified (run 4). |
| `pc-rukia-npc-jotaro-dark-tournament` | Same batch. **Rukia `41` active** (LIGHT) vs Jotaro `28`. Roster verified (run 4). |
| `pc-kurama-npc-jotaro-dark-tournament` | Same batch. **Kurama `33` active** vs Jotaro `28`. Roster verified (run 4). |
| `pc-yusuke-npc-jotaro-dark-tournament` | Same batch, **same Taikoubou deck (hotkeys set)**. **Yusuke `32` active** vs Jotaro `28`. Second Yusuke state (the MOMO-deck one is `pc-yusuke-npc-nami-dark-tournament`). Roster verified (run 4). |
| `pc-raoh-npc-luffy-j-arena` | **Script-built 2026-09-03** (`refresh_savestates.py`, deck 4 RAO: Raoh `62` 192 leader/active, Nami `15`, Franky `17`) vs CPU **Luffy `12` 152** (Naruto `20` benched). **Default J Arena stage, not Dark Tournament** (the script cannot pick a stage): P1 x 256.0, victim x 767.0, 511 px apart, so plans need a long approach. Training, auto-recover OFF verified. P1 fighter pointer here is `0x02228A00`, not `0x02228E80`. For Raoh up+Y (`jus-knockback-pop-spot-check-m4uy`). |

## Not kept, and why

- `verified_training_0/1/2` — regenerate with `cd scripts/emu && python3 boot_verified.py --runs 3`, about two minutes for all three. Training battles reached by the pixel-verified route with items and gimmicks switched OFF.
- `deck2_base` — a battle using deck 2, reachable through the same verified route.
- `fight_cfg`, `training_v3` — inherited from an earlier session, contents undocumented, and superseded by `pos_base` for damage work. Not worth carrying something nobody can describe.
- `luffy_battle` — Goku vs Luffy in a timed point match. CPU Luffy moves and attacks, so positions aren't reproducible between runs — useless for measurement, and the exact moment can't be recreated.
