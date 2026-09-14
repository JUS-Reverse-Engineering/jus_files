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
| `pc-yusuke-npc-nami-dark-tournament` | MOMO deck; saved with Yusuke `32` active but **a reload resets the active koma to deck slot 0 (Momotaro `67`)** — measured 2026-09-12 (`jus-ehcp`); Yusuke (184) vs Nami `15` (136). Owner: Yusuke's X is a **giant high-priority projectile that eats other projectiles**. P1 x 645.4, victim x 576.0. |
| `pc-taikoubou-npc-jotaro-dark-tournament` | **Owner-built 2026-09-03 (second batch, savestate major 14; menu-saved in the fork by the owner, then re-saved through the bridge on 2026-09-03 so the sidecars are real; run 5).** **Taikoubou `68` active** (summoner type; second port character, `jus-4ocm`) vs CPU **Jotaro `28`**. **The only state whose deck has L/R switch hotkeys assigned** in the deck builder (owner: L/R only switch when the hotkey sticker is on a battle koma) — the switch positive control for `jus-e2w4`. Roster verified in run 4 (`jus-e2w4`): deck = Taikoubou `68` 144 / Momotaro `67` 176 / Yusuke `32` 184; L → Yusuke, R → Momotaro. Opponent deck in all eleven: Jotaro `28` 160, Sanji `14` 136, Kenshin `36` 152, Lenalee `46` 128; victim x 576.0. |
| `pc-kakashi-npc-jotaro-dark-tournament` | Same batch. **Loads UNPAUSED (verified 2026-09-12, `jus-atns.4.1`): do not press START before a GDB attach; one START opens the pause menu and freezes the battle tasks.** **Kakashi `23` active** vs Jotaro `28`. Deck: Kakashi 144 / Muhyo `59` 128 / Mashirito `57` 144 / Kurama `33` 144. First port character (`jus-kakashi-moveset-map-33lu`). Roster verified (run 4). |
| `pc-kakashi-npc-jotaro-fightcpu` | **Fight-CPU bridge slot (2026-09-13, `jus-atns.4.5`/`.4.8`), promoted from `pc-kakashi-npc-jotaro-dark-tournament` via the in-match COM設定 menu (`START, DOWN, A, START` → 戦う).** Saved right after the menu sequence closes (Kakashi `obj+0x18` = 0, idle, verified by screenshot at save time) -- **not** 30 idle frames later, which the same ticket found already mid-hit (`kakashi-select-2026-09-13/RESULTS.md`, "Preflight (item 1)"). **Loads UNPAUSED, same as the parent state.** Verified deterministic: reloading and running the same input plan twice gave byte-identical `fc_start`/`fc_end`. Same addresses as the parent (Kakashi obj `0x02228E80`, Jotaro read live off the fighter table). Built for the SELECT residual measurements (`jus-atns.4.8`); the original bridge-slot names from that session were `kakashi-select-fight-tmp` (mid-fight, superseded) and `kakashi-select-fight-ok` (this state, renamed on archival to the `pc-*` convention). |
| `pc-muhyo-npc-jotaro-dark-tournament` | Same batch. **Muhyo `59` active** (summoner) vs Jotaro `28`. Fwd+Y / up+Y pop state (`jus-knockback-pop-spot-check-m4uy`). Roster verified (run 4). |
| `pc-sasuke-npc-jotaro-dark-tournament` | Same batch. **Sasuke `21` active, 7-koma (HP 184; up+X is the five-hit status special)** vs Jotaro `28`. Deck: Sasuke 184 / Yoh White Swan `26` 192 / Eve `37` 128 / Kakashi `23` 16. Up+Y pop (`m4uy`), 8-koma X launcher (`jus-launcher-move-spot-check-hiyh`). Roster verified (run 4). |
| `pc-eve-npc-jotaro-dark-tournament` | Same batch. **Eve `37` active** (LIGHT) vs Jotaro `28`. 4-koma X launcher (`hiyh`). Roster verified (run 4). |
| `pc-yohswan-npc-jotaro-dark-tournament` | Same batch. **Yoh (White Swan) `26` active** vs Jotaro `28`. 6-koma X = launcher + blind (`hiyh`). Roster verified (run 4). |
| `pc-yugi-npc-jotaro-dark-tournament` | Same batch. **Yugi `35` active** (summoner) vs Jotaro `28`. Deck: Goku `0` 160 / Yugi 136 / Naruto `20` 144 / Rukia `41` 128. Roster verified (run 4). |
| `pc-mashirito-npc-jotaro-dark-tournament` | Same batch. **Mashirito `57` active** (item-creator) vs Jotaro `28`. Roster verified (run 4). |
| `pc-rukia-npc-jotaro-dark-tournament` | Same batch. **Rukia `41` active** (LIGHT) vs Jotaro `28`. Roster verified (run 4). |
| `pc-kurama-npc-jotaro-dark-tournament` | Same batch. **Kurama `33` active** vs Jotaro `28`. Roster verified (run 4). |
| `pc-yusuke-npc-jotaro-dark-tournament` | Same batch, **same Taikoubou deck (hotkeys set)**. saved with Yusuke `32` active, but **a reload resets the active koma to slot 0 (Taikoubou `68`)** — `jus-ehcp` 2026-09-12; vs Jotaro `28`. Second Yusuke state (the MOMO-deck one is `pc-yusuke-npc-nami-dark-tournament`). Roster verified (run 4). |
| `pc-raoh-npc-luffy-j-arena` | **Script-built 2026-09-03** (`refresh_savestates.py`, deck 4 RAO: Raoh `62` 192 leader/active, Nami `15`, Franky `17`) vs CPU **Luffy `12` 152** (Naruto `20` benched). **Default J Arena stage, not Dark Tournament** (the script cannot pick a stage): **J Arena moves the element array: slots 0–5 are fixed stage markers, the fighters are slots 6/7 (`0x0220C1E8` / `0x0220C228`), 192 px apart** — the 256 / 767 pair read from slots 0/1 is the marker spread, not the fighters (run 7). Training, auto-recover OFF verified. P1 fighter pointer here is `0x02228A00`, not `0x02228E80`. For Raoh up+Y (`jus-knockback-pop-spot-check-m4uy`). |
| `pc-momotaro-npc-yusuke-projectiles-about-to-collide` | **Owner-built 2026-09-10, pause-menu save from the owner's own melonDS, copied from Desktop; dummy sidecar (true framecount unknown, README dummy-sidecar path).** Momotaro fwd+Y projectile and Yusuke fwd+Y projectile **about to collide**, paused right before they meet. Owner testimony: **Momotaro's wins every time.** The deterministic projectile-conflict state for `jus-hitbox-priority-clash-1evz` / `jus-projectile-conflict-capture-prep-hnap`. Roster not yet verified at first load — do it (HP records, chr_b) before measuring. |
| `pc-hitsugaya-airy-npc-ichigo-fy` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Hitsugaya air Y ice chunk in the air; Ichigo uncharged fwd Y about to contact it. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-ichigo-fy-vegeta` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Ichigo uncharged fwd Y in flight, no projectile collision (single-projectile control). For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-ichigo-charged-fy-vegeta` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Ichigo charged fwd Y in flight, no collision; charging raises damage, speed, size, knockback. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-vegeta-x-ichigo-x` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: P1 Vegeta (right) X beam; Ichigo (left) X projectile. The projectile passes through the beam and does no damage/knockback on reaching Vegeta. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-yugi-fb-npc-vegeta-fy` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Yugi fwd B dice thrown down-right vs Vegeta fwd Y. The dice are "high priority", persist for their whole animation, go through beams. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-yugi-fb-npc-vegeta-x` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Yugi dice on the left, Vegeta X beam from the right. The beam hits the dice, the dice keep moving; the beam hits Yugi; the dice keep "contacting" the beam. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-eve-x-npc-vegeta-x` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Eve X feathers aimed left; Vegeta X beam right. The beam eats the feathers then hits Eve. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-taikoubou-upx-npc-kakashi-x` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Taikoubou (right) up X tornado; Kakashi (left) X beam. The beam stops on the tornado wherever it is as it travels left. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-mashirito-y-npx-yusuke-fy` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Mashirito Y chest (explodes on contact) vs Yusuke fwd Y. The chest and its explosion seem to be classified differently. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-mashirito-fy-momotaro-x` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Mashirito fwd Y walking poop (traveling left) hit by Momotaro X. The poop persists, is never canceled, and explodes at the end of its travel. For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-mashirito-fy-npc-momotaro-b` | **Owner-built 2026-09-10, pause-menu save, dummy sidecar.** Owner testimony: Momotaro B melee hitting the walking poop. Melee attacks also have priority-like outcomes (one side loses and takes damage, or hitboxes cancel and nobody is hurt). For `jus-2s9k`. Roster/addresses unverified at first load. |
| `pc-ichigo-airy-charged` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Ichigo air Y charged projectile — air Y fires the same projectile as fwd Y, at a different angle. For `jus-puc7`. Roster/addresses unverified at first load; the shot may not be spawned at the save point, as with `pc-ichigo-charged-fy-vegeta`. |
| `pc-ichigo-airy-uncharged` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Ichigo air Y uncharged projectile — air Y fires the same projectile as fwd Y, at a different angle. For `jus-puc7`. Roster/addresses unverified at first load; the shot may not be spawned at the save point, as with `pc-ichigo-charged-fy-vegeta`. |
| `pc-ichigo-upy-charged` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Ichigo up Y charged projectile — up Y fires the same projectile as fwd Y, at a different angle. For `jus-puc7`. Roster/addresses unverified at first load; the shot may not be spawned at the save point, as with `pc-ichigo-charged-fy-vegeta`. |
| `pc-ichigo-upy-uncharged` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Ichigo up Y uncharged projectile — up Y fires the same projectile as fwd Y, at a different angle. For `jus-puc7`. Roster/addresses unverified at first load; the shot may not be spawned at the save point, as with `pc-ichigo-charged-fy-vegeta`. |
| `pc-yugi-fb-npc-momotaro-fy` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Yugi dice vs Momotaro fwd Y. They pass through each other. Both projectiles still exist, no collision effect in the UI, and fwd Y passed right through Yugi without damaging. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-yugi-fb-npc-yusuke-x` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Yusuke X passes through Yugi dice and the collision effect IS shown; then Yugi (owner) takes damage when Yusuke X hits. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-naruto-fy-npc-yusuke-x` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Yusuke X eats all 3 of Naruto's fwd Y shuriken; they vanish with the collision effect and Naruto takes damage. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-yugi-y-npc-yusuke-x` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Yugi Y summons a swordsman who swings downward and sends a wave projectile. Owner is not sure: Yusuke X either passed through it or they cancelled out, then X hit Yugi. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-taikoubou-upx-npc-yusuke-x` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Yusuke X hits Taikoubou's tornado and vanishes. Owner thinks the tornado acts the same way a beam does but is not sure. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-kurama-x-npc-yusuke-x` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Kurama's X has super high priority and eats Yusuke X. Owner is not sure Kurama X is technically a projectile. This state also has Taikoubou's tornado out, but Yusuke X hits Kurama X first since it is wider. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-sasuke-x-npc-yusuke-x` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Sasuke X is not a projectile: Sasuke moves fast with a ball of lightning in hand. It has high priority. Collision effect shown, Yusuke X vanishes, Sasuke (owner) takes no damage. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-naruto-fy-npc-yusuke-fy` | **Owner-built 2026-09-11, pause-menu save, dummy sidecar.** Owner testimony: Naruto fwd Y throws three shuriken, flying left in this save. They contact Yusuke's fwd Y projectile; it vanishes with the collision effect along with ONE of the shuriken; the other two shuriken persist. For `jus-pebk`. Roster/addresses unverified at first load. |
| `pc-naruto-fy-npc-yusuke-x-preroll` | **Derived 2026-09-11, real sidecar (session `fable-preroll-2026-09-11`).** Parent `pc-naruto-fy-npc-yusuke-x`, unpaused and advanced with no input, re-paused, census-verified (shuriken rec53/54/55 alive, no Yusuke X record yet), then saved. Built to fix the tail blind spot in `jus-xyqc`: the parent state pauses before Yusuke X spawns, so `projectile_replay.py`'s baseline-only watch never saw it. **Correction (jus-xyqc, 2026-09-11):** the advance was reported as 20 frames; the shuriken `objshot_elements[].lifetime` delta says 14; `framecount_at_save` (113789) agrees with neither. True frame offset from the parent is unknown. Also: this state's own element watch (`rec53_elem`) is frozen at the parent's terminal x-value for the whole capture and its positive control FAILED -- treat its element data (not its `+0x40` flags) as invalid; see `pc-naruto-fy-npc-yusuke-x-preroll/RESULTS.md`. For `jus-xyqc`. |
| `pc-yusuke-fy-npc-unverified-preroll` | **Owner-built 2026-09-12, pause-menu save, dummy sidecar.** Owner testimony: Yusuke is the PLAYER (P1), paused right before his fwd Y goes out. Purpose: the slot-field test (does Yusuke's projectile record read slot 1 when he is P1; `jus-qqiy` gap) — closed by `jus-rp0y`: fires with `RIGHT+Y`, record reads `0x1001`/`0x63C811` (slot 1), not falsified. Opponent (P2) read live 2026-09-12: `--verify-roster` reads `chr_b` 32 (Yusuke) on both HP-slot bases; only one HP bar/name ever renders on screen, so that reading is not independently confirmed visually. **Correction (`jus-rp0y`):** a second, independent signal was sought from this state's own census (any record whose node entry falls in P2's own authored col-file array) and none exists — P2 never fired a projectile in this run, and P2's own fighter-body node entry is the shared engine builtin (id 0), not a reference into any character's col file. The `chr_b=32` read therefore stands uncorroborated; P2's identity is unverified, hence the name (`docs/research/feel-captures/slot-p1-2026-09-12/RESULTS.md`, "P2 identity byte-check"). |

### Charge-transfer empowerment states (22, owner-built 2026-09-11)

Owner pause-menu saves for `jus-charge-transfer-empowerment-pb64`, supplied in
`/Users/djdjo/Desktop/savestates/charge-state-research`. One state per
(observer, charge source) pair; slot names are the owner's, kept verbatim.
All are savestate major 14 (same fork as the 2026-09-10 projectile batch).
**Roster, form (Ichigo 4/5/6 vs 7/8), and charge-source identity are NOT yet
verified in any of these -- resolve them at first load before measuring.**

**The pause status is also mixed and unrecorded** (owner, 2026-09-11): some
states are saved paused, others are not. Determine it per state at first load.
A paused state does not advance on a plain free run and needs a START /
no-input / START plan; an unpaused state may already be moving when the load
settles. Do not reuse one run plan across the batch.

Owner testimony: a charge sets an *empowered* state that transfers across a
character switch. The per-character charge inputs and the full transfer matrix
are recorded in `docs/research/moveset-notes/OWNER-NOTES.md` section
"Charge / empowerment (2026-09-11)" and on the bead.

| slot | observer | charge source |
|---|---|---|
| `yusuke-uncharged` | Yusuke | none (negative control) |
| `yusuke-fully-charged` | Yusuke | own full charge |
| `yusuke-after-franky-chargelvl1` | Yusuke | Franky charge lvl 1 |
| `yusuke-after-franky-chargelvl2` | Yusuke | Franky charge lvl 2 |
| `ichigo-after-yusuke-fully-charged` | Ichigo | Yusuke full charge |
| `ichigo-after-yusuke-tapped-charge` | Ichigo | Yusuke tap charge |
| `ichigo-after-fuusuke-charge` | Ichigo | Fuusuke charge |
| `franky-selfcharge-lvl1` | Franky | own charge once |
| `franky-selfcharge-lvl2` | Franky | own charge twice |
| `franky-after-yusuke-fully-charged` | Franky | Yusuke full charge |
| `franky-after-yusuke-tapped-charge` | Franky | Yusuke tap charge |
| `franky-after-fuusuke-charge` | Franky | Fuusuke charge |
| `fuusuke-after-yusuke-fullcharge` | Fuusuke | Yusuke full charge |
| `fuusuke-after-yusuke-tapcharge` | Fuusuke | Yusuke tap charge ("strange" augmentation) |
| `fuusuke-after-ichigo-charge` | Fuusuke | Ichigo charge ("strange" augmentation) |
| `fuusuke-after-g2luffy-charge` | Fuusuke | G2 Luffy charge |
| `fuusuke-after-raoh-charge` | Fuusuke | Raoh charge |
| `fuusuke-after-franky-chargelvl2` | Fuusuke | Franky charge lvl 2 |
| `raoh-after-g2luffy-charge` | Raoh | G2 Luffy charge |
| `raoh-after-fuusuke-charge` | Raoh | Fuusuke charge |
| `g2-luffy-after-charge` | G2 Luffy | own charge |
| `g2-luffy-nocharge` | G2 Luffy | none (negative control) |

## Not kept, and why

- `verified_training_0/1/2` — regenerate with `cd scripts/emu && python3 boot_verified.py --runs 3`, about two minutes for all three. Training battles reached by the pixel-verified route with items and gimmicks switched OFF.
- `deck2_base` — a battle using deck 2, reachable through the same verified route.
- `fight_cfg`, `training_v3` — inherited from an earlier session, contents undocumented, and superseded by `pos_base` for damage work. Not worth carrying something nobody can describe.
- `luffy_battle` — Goku vs Luffy in a timed point match. CPU Luffy moves and attacks, so positions aren't reproducible between runs — useless for measurement, and the exact moment can't be recreated.
