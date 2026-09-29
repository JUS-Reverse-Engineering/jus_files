# Character-mapping save states: notes

Owner rulings, 2026-09-24.

## What each state is

- `<NAME>/<koma>.mln` is that character with their `<koma>`-size panel active. For example, `KAKASHI HATAKE/4.mln` is Kakashi with his 4-koma active.
- Every state here is correct, so trust the path. The character and the active panel come from it, and there's no need to check them in RAM.
- The opponent doesn't matter.
- Every state is ready to capture as soon as it loads: training mode, the CPU standing idle, and enough SP to fire X. No setup step is needed.
- HP regen is ON in every state. HP climbs back between hits, so:
  - read damage per hit, on the frame it lands (the damage store, or that frame's HP drop). Never take start HP minus end HP;
  - anything that depends on low HP (the launcher HP band below full, low-health passives such as Yusuke's SP gain) can't be measured while regen is on.
- **Turning regen off:** START (open the menu), down, down, A, START (close the menu). Do this right after loading, before any capture. Then check it took: after the first hit, HP must not climb back.
- **Stage:** most states were made in the deckbuilder training mode, on a stage with more platforms than we'd like. A platform can catch a jump, a knockback or a shot. A trial where a platform touches a fighter or a shot is flagged and not used. If a panel's specials can't be captured cleanly there, that panel goes on a list for the owner to remake on a flat stage.
- Imported copies (gzipped, in `jus_files/save_states`) stay local and untracked. Don't commit them to the jus_files repo; this folder is the backup.
- The states are raw `.mln` files. To use one with the capture tooling, import it through the bridge so it gets a real sidecar (`.meta.json`).

## Alternate panels

- There are no states for alternate koma, and none are needed.
- An alternate panel uses the same specials as the regular panel of that size.
- Only the nature for normal and heavy attacks can differ. For example, Kakashi's laughter 6-koma.

## What to capture from each state

- **A normal panel state** (`<koma>.mln`): capture that panel's **X and up X only**. It doesn't need the full moveset.
- **A form-change state** (the filename contains `-FORMCHANGE`, for example `7-FORMCHANGE.mln`; Yoh's is `6-FORMCHANGED.mln`): capture the **whole moveset**, because the character changes form.
- A character's base moveset (normals, heavies and the rest) comes from one ordinary state.

Form-change states as of 2026-09-24: Naruto 7 and 8, Luffy 7 and 8, Ichigo 7 and 8, Seiya 8, Dr. Mashirito 8, Nami 6 and Yoh 6.

## Natures

- Power does 1.5× damage to knowledge.
- Knowledge does 1.5× damage to laughter.
- Laughter does 1.5× damage to power.
- Normal and heavy attacks use the panel's nature.
- The defender also takes damage as its panel's nature. For example, Kakashi's laughter 6-koma takes damage as laughter, so knowledge attacks do 1.5× to him there.
- Specials carry their own nature. It's usually the same as the panel's, but not always:
  - Sakura's 6-koma X is laughter, even though she is power.
  - On Kakashi's laughter 6-koma, his specials still do knowledge damage.

## kit.md files

Each character folder has a `kit.md` with:
- the Genroh guide's panel list: shape, J-Soul, and both specials with their nature and charge or steering notes;
- GameFAQs moveset extracts.

These are guide transcriptions, not game measurements. Use them to know which specials to expect and to check captures against. Never use them as the source of a kit number.

## Clashes

- Don't make a save state for each pair of characters. That's hard to reproduce and doesn't scale.
- Instead, read each shot's clash flags from single-character captures, and run them through one general rule in the game.
- The pair states in `../projectile-research/` are for checking that rule.

## Handling

- These states and all JUS assets are not for release. Keep them local, and never ship, export or publish them.
