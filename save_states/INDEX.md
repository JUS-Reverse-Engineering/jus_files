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

## Not kept, and why

- `verified_training_0/1/2` — regenerate with `cd scripts/emu && python3 boot_verified.py --runs 3`, about two minutes for all three. Training battles reached by the pixel-verified route with items and gimmicks switched OFF.
- `deck2_base` — a battle using deck 2, reachable through the same verified route.
- `fight_cfg`, `training_v3` — inherited from an earlier session, contents undocumented, and superseded by `pos_base` for damage work. Not worth carrying something nobody can describe.
- `luffy_battle` — Goku vs Luffy in a timed point match. CPU Luffy moves and attacks, so positions aren't reproducible between runs — useless for measurement, and the exact moment can't be recreated.
