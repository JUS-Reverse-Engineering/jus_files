#!/usr/bin/env python3
"""collision_data_miner.py

Data-only miner for the COLLISION DATA subsystem of Jump Ultimate Stars.

ROUND 2 (full-roster scale): reads every *_collision.json file exported by
P1's batch export (jus_files/exported_combat/), split into:
  - 74 per-character "battle" files (*_b_*_collision.json)   -- PRIMARY scope
  - 206 per-support files (*_s_*_collision.json)              -- secondary scope
  - 1 item_collision.json (shared item hitbox table)          -- context only
plus jpower.json and chr_b.json (unchanged since round 1).

All reads are read-only, absolute paths, stdlib json only. No mutation, no
network, no git, no disassembly. Pure stdlib (json, os, glob, collections,
statistics).

Determinism: every file set is discovered via sorted(glob.glob(...)); every
dict/set is iterated/printed in sorted key order (see counter_str/sorted());
no timestamps, no os.listdir() (unsorted), no reliance on hash-randomized
set iteration order in any printed output. Running this script twice must
produce byte-identical stdout.

Run with:
    /Users/djdjo/Documents/mine/JUSToolkit/.claude/worktrees/battle-engine-atlas/scripts/analysis/.venv/bin/python \
        jus_files/analysis/findings/collision_data_miner.py
(plain python3 works equally well; the venv is only needed by other tracer
scripts in this directory that import capstone.)
"""

import glob
import json
import os
import statistics
import collections

COMBAT_DIR = "/Users/djdjo/Documents/mine/JUSToolkit/jus_files/exported_combat"
JPOWER_PATH = os.path.join(COMBAT_DIR, "jpower.json")
CHR_B_PATH = os.path.join(COMBAT_DIR, "chr_b.json")

# Total characters in the game per the task brief / docs/research mapping docs.
EXPECTED_TOTAL_CHARACTERS = 74

# Round-1 sample's per-file entry counts, for a byte-level sanity re-check
# that the original 4 files are unchanged by the P1 batch re-export.
ROUND1_SAMPLE_COUNTS = {
    "bb_b_01": 24,
    "bl_b_01": 20,
    "db_b_01": 25,
    "ds_b_03": 23,
}


def load_collision_dir(pattern):
    """Discover + load every file matching pattern in COMBAT_DIR, keyed by characterId."""
    paths = sorted(glob.glob(os.path.join(COMBAT_DIR, pattern)))
    data = {}
    for p in paths:
        d = json.load(open(p))
        cid = d.get("characterId", os.path.basename(p))
        data[cid] = d
    return data


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def counter_str(c):
    return dict(sorted(c.items(), key=lambda kv: (str(type(kv[0])), kv[0])))


def pool_entries(data):
    """data: {cid: {"entries": [...], ...}} -> (per_char_entries, pooled_list)."""
    per_char = {}
    pooled = []
    for cid in sorted(data.keys()):
        entries = data[cid]["entries"]
        per_char[cid] = entries
        for e in entries:
            e2 = dict(e)
            e2["_char"] = cid
            pooled.append(e2)
    return per_char, pooled


def ct_to_tier_crosstab(entries):
    ct = collections.defaultdict(collections.Counter)
    for e in entries:
        ct[e["collisionType"]][e["hitTier"]] += 1
    return ct


def per_char_rule_check(per_char, ct_value, tier_value):
    """For each char, count (n_matching_ct, n_matching_ct_and_tier). Returns dict cid->(n_hit, n_total)."""
    out = {}
    for cid in sorted(per_char.keys()):
        n_total = 0
        n_hit = 0
        for e in per_char[cid]:
            if e["isTerminator"]:
                continue
            if e["collisionType"] == ct_value:
                n_total += 1
                if e["hitTier"] == tier_value:
                    n_hit += 1
        if n_total > 0:
            out[cid] = (n_hit, n_total)
    return out


def main():
    b_data = load_collision_dir("*_b_*_collision.json")
    s_data = load_collision_dir("*_s_*_collision.json")
    all_data = load_collision_dir("*_collision.json")
    item_paths = sorted(
        p
        for p in glob.glob(os.path.join(COMBAT_DIR, "*_collision.json"))
        if "_b_" not in os.path.basename(p) and "_s_" not in os.path.basename(p)
    )

    b_ids = sorted(b_data.keys())
    s_ids = sorted(s_data.keys())

    # ------------------------------------------------------------------
    # 0. COVERAGE
    # ------------------------------------------------------------------
    section("0. COVERAGE (round 2, full-roster export)")
    print("total *_collision.json files found:", len(glob.glob(os.path.join(COMBAT_DIR, "*_collision.json"))))
    print("battle (*_b_*) character files found:", len(b_data), "-> ids:", b_ids)
    print("support (*_s_*) files found:", len(s_data))
    print("item/other collision files found:", len(item_paths), "->", [os.path.basename(p) for p in item_paths])

    coverage_pct = 100.0 * len(b_data) / EXPECTED_TOTAL_CHARACTERS
    print(f"battle-file coverage = {len(b_data)}/{EXPECTED_TOTAL_CHARACTERS} = {coverage_pct:.2f}%")

    chr_b = json.load(open(CHR_B_PATH))
    print("chr_b.json entries count (all battle-character identity rows):", len(chr_b["entries"]))
    jpower = json.load(open(JPOWER_PATH))
    print("jpower.json entries count (all attack-block rows, all characters pooled):", len(jpower["entries"]))

    print("\nround-1 sample sanity check (same 4 files, count field unchanged by P1 re-export):")
    for cid in sorted(ROUND1_SAMPLE_COUNTS):
        now = len(b_data[cid]["entries"]) if cid in b_data else None
        print(f"  {cid}: round1={ROUND1_SAMPLE_COUNTS[cid]} round2={now} match={now == ROUND1_SAMPLE_COUNTS[cid]}")

    for label, data in (("battle", b_data), ("support", s_data)):
        mism = sum(1 for cid, d in data.items() if d["count"] != len(d["entries"]))
        print(f"'count' field vs len(entries) mismatches ({label}, n={len(data)}):", mism)
    item_mism = 0
    for p in item_paths:
        d = json.load(open(p))
        if d["count"] != len(d["entries"]):
            item_mism += 1
    print(f"'count' field vs len(entries) mismatches (item, n={len(item_paths)}):", item_mism)

    all_keysets = set()
    for p in sorted(glob.glob(os.path.join(COMBAT_DIR, "*_collision.json"))):
        d = json.load(open(p))
        for e in d["entries"]:
            all_keysets.add(frozenset(e.keys()))
    print("distinct entry key-sets across ALL 281 collision files:", len(all_keysets), "(1 means fully uniform schema)")

    # ------------------------------------------------------------------
    # Pool battle-file entries (PRIMARY SCOPE)
    # ------------------------------------------------------------------
    per_char, pooled = pool_entries(b_data)
    nonterm = [e for e in pooled if not e["isTerminator"]]
    term = [e for e in pooled if e["isTerminator"]]

    # ------------------------------------------------------------------
    # 1. STRUCTURAL (battle files, full scale)
    # ------------------------------------------------------------------
    section("1. STRUCTURAL: entries per file / terminator sentinel / schema (battle files, n=74)")
    for cid in b_ids:
        print(f"  {cid}: count field={b_data[cid]['count']}  len(entries)={len(per_char[cid])}")
    counts = {cid: len(per_char[cid]) for cid in b_ids}
    print("TOTAL pooled entries (sum across 74 battle files):", len(pooled))
    print(
        "entries-per-file: min={} ({}) max={} ({}) mean={:.4f} median={}".format(
            min(counts.values()),
            min(counts, key=lambda k: (counts[k], k)),
            max(counts.values()),
            max(counts, key=lambda k: (counts[k], k)),
            sum(counts.values()) / len(counts),
            statistics.median(sorted(counts.values())),
        )
    )

    print("\nisTerminator distribution (pooled, battle):", counter_str(collections.Counter(e["isTerminator"] for e in pooled)))
    term_per_file = {cid: sum(1 for e in per_char[cid] if e["isTerminator"]) for cid in b_ids}
    term_count_histogram = collections.Counter(term_per_file.values())
    print("histogram of (terminator-count-per-file -> number of files):", counter_str(term_count_histogram))
    zero_term_files = sorted(cid for cid, n in term_per_file.items() if n == 0)
    print(f"files with 0 isTerminator=True entries: {len(zero_term_files)} / {len(b_ids)} -> {zero_term_files}")
    max_term_n = max(term_per_file.values())
    max_term_files = sorted(cid for cid, n in term_per_file.items() if n == max_term_n)
    print(f"max terminator count observed: {max_term_n} in file(s) {max_term_files} (entries in that file: {[counts[c] for c in max_term_files]})")

    print("\nterminator-row (isTerminator=True) field-value deep dive (battle, n={}):".format(len(term)))
    print("  damageFlags distribution on terminator rows:", counter_str(collections.Counter(e["damageFlags"] for e in term)))
    print("  knockback distribution on terminator rows (top 10 by count):", sorted(collections.Counter(e["knockback"] for e in term).most_common(10)))
    n_df255 = sum(1 for e in term if e["damageFlags"] == 255)
    n_kb255 = sum(1 for e in term if e["knockback"] == 255)
    n_both255 = sum(1 for e in term if e["damageFlags"] == 255 and e["knockback"] == 255)
    n_term_tier0 = sum(1 for e in term if e["hitTier"] == 0)
    print(f"  terminator rows with damageFlags==255: {n_df255}/{len(term)} = {n_df255/len(term):.4f}")
    print(f"  terminator rows with knockback==255: {n_kb255}/{len(term)} = {n_kb255/len(term):.4f}")
    print(f"  terminator rows with BOTH damageFlags==255 AND knockback==255: {n_both255}/{len(term)} = {n_both255/len(term):.4f}")
    print(f"  terminator rows with hitTier==0: {n_term_tier0}/{len(term)} = {n_term_tier0/len(term):.4f}")

    collision_keys = set(pooled[0].keys()) - {"_char"}
    jpower_keys = set(jpower["entries"][0].keys())
    shared_keys = collision_keys & jpower_keys
    print("\ncollision entry schema keys (count={}):".format(len(collision_keys)), sorted(collision_keys))
    print("jpower entry schema keys (count={}):   ".format(len(jpower_keys)), sorted(jpower_keys))
    print("shared key names between collision entries and jpower entries:", sorted(shared_keys), f"(count={len(shared_keys)})")

    print("\nframeStart range (non-terminator, battle):", min(e["frameStart"] for e in nonterm), "..", max(e["frameStart"] for e in nonterm))
    duration_vals = sorted(set(e["durationMult"] for e in nonterm))
    print("durationMult distinct values (non-terminator, battle):", duration_vals)
    duration_nonzero = [e for e in nonterm if e["durationMult"] != 0]
    print(f"durationMult!=0 entries: {len(duration_nonzero)} / {len(nonterm)}")
    print("width range (non-terminator, battle):", min(e["width"] for e in nonterm), "..", max(e["width"] for e in nonterm))
    print("height range (non-terminator, battle):", min(e["height"] for e in nonterm), "..", max(e["height"] for e in nonterm))
    neg_size = [e for e in nonterm if e["width"] < 0 or e["height"] < 0]
    print(f"entries with negative width or height (non-terminator, battle): {len(neg_size)} / {len(nonterm)} = {len(neg_size)/len(nonterm):.4f}")

    reserved_tuples = set((e["reserved0"], e["reserved1"], e["reserved2"], e["reserved3"]) for e in pooled)
    print("\ndistinct (reserved0,reserved1,reserved2,reserved3) tuples across all", len(pooled), "battle entries:", reserved_tuples)

    print("positionFlags distribution (pooled, battle):", counter_str(collections.Counter(e["positionFlags"] for e in pooled)))
    ef_dist = collections.Counter(e["extFlags"] for e in pooled)
    print("extFlags distribution (pooled, battle):", counter_str(ef_dist))
    ef_nonzero = sum(v for k, v in ef_dist.items() if k != 0)
    print(f"extFlags!=0 count: {ef_nonzero} / {len(pooled)} = {ef_nonzero/len(pooled):.4f}")

    # ------------------------------------------------------------------
    # 2. hitTier
    # ------------------------------------------------------------------
    section("2. hitTier distribution & collisionType correlation (battle files, full scale)")
    pooled_tier = collections.Counter(e["hitTier"] for e in nonterm)
    print("POOLED hitTier (non-terminator, battle, n={}):".format(len(nonterm)), counter_str(pooled_tier))
    tiers = [e["hitTier"] for e in nonterm]
    print(f"hitTier non-terminator: min={min(tiers)} max={max(tiers)} distinct_count={len(set(tiers))}")
    print("hitTier (terminator-only) distribution:", counter_str(collections.Counter(e["hitTier"] for e in term)))

    jp_total_damage = [e["totalDamage"] for e in jpower["entries"]]
    jp_damage1 = [e["damage1"] for e in jpower["entries"]]
    print(f"\n[contrast] jpower totalDamage (all {len(jp_total_damage)} attack rows): min={min(jp_total_damage)} max={max(jp_total_damage)} distinct_count={len(set(jp_total_damage))}")
    print(f"[contrast] jpower damage1      (all {len(jp_damage1)} attack rows): min={min(jp_damage1)} max={max(jp_damage1)} distinct_count={len(set(jp_damage1))}")

    print("\ncollisionType -> hitTier crosstab (pooled, non-terminator, battle):")
    ct = ct_to_tier_crosstab(nonterm)
    for k in sorted(ct):
        n = sum(ct[k].values())
        print(f"  collisionType={k} (n={n}): {counter_str(ct[k])}")
    if 5 in ct:
        n5 = sum(ct[5].values())
        n5_tier3 = ct[5].get(3, 0)
        print(f"  -> POOLED collisionType=5 tier-3 fraction: {n5_tier3}/{n5} = {n5_tier3/n5:.4f}")
    if 3 in ct:
        n3 = sum(ct[3].values())
        n3_tier1 = ct[3].get(1, 0)
        print(f"  -> POOLED collisionType=3 tier-1 fraction: {n3_tier1}/{n3} = {n3_tier1/n3:.4f}")

    print("\nPER-CHARACTER collisionType=5 -> hitTier=3 rule check (battle, n=74 chars):")
    ct5_per_char = per_char_rule_check(per_char, 5, 3)
    print(f"  characters with >=1 collisionType=5 entry: {len(ct5_per_char)} / {len(b_ids)}")
    for cid in sorted(ct5_per_char):
        hit, tot = ct5_per_char[cid]
        print(f"    {cid}: {hit}/{tot} = {hit/tot:.4f}")
    full5 = sum(1 for hit, tot in ct5_per_char.values() if hit == tot)
    zero5 = sum(1 for hit, tot in ct5_per_char.values() if hit == 0)
    partial5 = len(ct5_per_char) - full5 - zero5
    print(f"  -> chars at 100% tier3: {full5}; chars at 0% tier3: {zero5}; partial (neither 0% nor 100%): {partial5}; total chars-with-ct5: {len(ct5_per_char)}")

    print("\nPER-CHARACTER collisionType=3 -> hitTier=1 rule check (battle, n=74 chars):")
    ct3_per_char = per_char_rule_check(per_char, 3, 1)
    print(f"  characters with >=1 collisionType=3 entry: {len(ct3_per_char)} / {len(b_ids)}")
    for cid in sorted(ct3_per_char):
        hit, tot = ct3_per_char[cid]
        print(f"    {cid}: {hit}/{tot} = {hit/tot:.4f}")
    majority3 = sum(1 for hit, tot in ct3_per_char.values() if hit > tot / 2)
    print(f"  -> chars where hitTier=1 is a STRICT MAJORITY of their collisionType=3 entries: {majority3} / {len(ct3_per_char)}")

    print("\nsubType -> hitTier crosstab (pooled, non-terminator, battle):")
    st = collections.defaultdict(collections.Counter)
    for e in nonterm:
        st[e["subType"]][e["hitTier"]] += 1
    for k in sorted(st):
        print(f"  subType={k} (n={sum(st[k].values())}): {counter_str(st[k])}")

    # ------------------------------------------------------------------
    # 3. projectileId
    # ------------------------------------------------------------------
    section("3. projectileId distribution (battle files, full scale)")
    pooled_pid = collections.Counter(e["projectileId"] for e in pooled)
    print("POOLED projectileId (battle, n={}):".format(len(pooled)), counter_str(pooled_pid))
    nonzero_pid = [e for e in pooled if e["projectileId"] != 0]
    print(f"nonzero-projectileId entries: {len(nonzero_pid)} / {len(pooled)} = {len(nonzero_pid)/len(pooled):.4f}")
    distinct_nonzero_pid = sorted(set(e["projectileId"] for e in nonzero_pid))
    print("distinct nonzero projectileId values (battle):", distinct_nonzero_pid, f"(count={len(distinct_nonzero_pid)} distinct value(s) across {len(nonzero_pid)} nonzero occurrence(s))")

    chars_with_nonzero_pid = collections.defaultdict(list)
    for e in nonzero_pid:
        chars_with_nonzero_pid[e["_char"]].append(e["projectileId"])
    print(f"\ncharacters with >=1 nonzero-projectileId entry: {len(chars_with_nonzero_pid)} / {len(b_ids)}")
    for cid in sorted(chars_with_nonzero_pid):
        vals = chars_with_nonzero_pid[cid]
        print(f"  {cid}: count={len(vals)} values={sorted(vals)}")

    ct4 = [e for e in nonterm if e["collisionType"] == 4]
    ct4_pid_nonzero = [e for e in ct4 if e["projectileId"] != 0]
    print(f"\ncollisionType==4 entries (non-terminator, battle): {len(ct4)}; of those with projectileId!=0: {len(ct4_pid_nonzero)}")
    non_ct4_pid_nonzero = sorted(
        ((e["_char"], e["collisionType"], e["subType"], e["projectileId"]) for e in nonzero_pid if e["collisionType"] != 4)
    )
    print(f"nonzero-projectileId entries with collisionType != 4: {len(non_ct4_pid_nonzero)}")
    for row in non_ct4_pid_nonzero:
        print("  (char, collisionType, subType, projectileId) =", row)

    pid_nonzero_by_ct = collections.Counter(e["collisionType"] for e in nonzero_pid)
    print(f"\ncollisionType distribution across ALL {len(nonzero_pid)} nonzero-projectileId entries (incl. terminator rows):", counter_str(pid_nonzero_by_ct))
    for k in sorted(pid_nonzero_by_ct):
        v = pid_nonzero_by_ct[k]
        print(f"  collisionType={k}: {v}/{len(nonzero_pid)} = {v/len(nonzero_pid):.4f}")
    ct45_nonzero = sum(v for k, v in pid_nonzero_by_ct.items() if k in (4, 5))
    print(f"  collisionType in {{4,5}} union: {ct45_nonzero}/{len(nonzero_pid)} = {ct45_nonzero/len(nonzero_pid):.4f}")
    term_nonzero_pid = [e for e in nonzero_pid if e["isTerminator"]]
    print(f"nonzero-projectileId entries that are ALSO isTerminator=True rows: {len(term_nonzero_pid)}/{len(nonzero_pid)} = {len(term_nonzero_pid)/len(nonzero_pid):.4f}")
    for e in sorted((e["_char"], e["collisionType"], e["projectileId"]) for e in term_nonzero_pid):
        print("  (char, collisionType, projectileId) [terminator row] =", e)

    # ------------------------------------------------------------------
    # 4. hitProperties
    # ------------------------------------------------------------------
    section("4. hitProperties bit-level analysis & per-character constancy (battle files, full scale)")
    pooled_hp = collections.Counter(e["hitProperties"] for e in pooled)
    print("POOLED hitProperties (battle, n={}):".format(len(pooled)), counter_str(pooled_hp))
    distinct_hp_values = sorted(set(e["hitProperties"] for e in pooled))
    print("distinct hitProperties values observed (battle):", distinct_hp_values)
    bit0 = sum(1 for e in pooled if e["hitProperties"] & 0x1)
    bit1 = sum(1 for e in pooled if e["hitProperties"] & 0x2)
    bit2 = sum(1 for e in pooled if e["hitProperties"] & 0x4)
    bit1_without_bit0 = sum(1 for e in pooled if (e["hitProperties"] & 0x2) and not (e["hitProperties"] & 0x1))
    print(f"bit0 (0x1) set count: {bit0}/{len(pooled)}; bit1 (0x2) set count: {bit1}/{len(pooled)}; bit2 (0x4) set count: {bit2}/{len(pooled)}; bit1-set-without-bit0 count: {bit1_without_bit0}")

    print("\nPER-CHARACTER hitProperties constancy check (battle, n=74 chars):")
    const_chars = []
    varying_chars = []
    for cid in b_ids:
        vals = sorted(set(e["hitProperties"] for e in per_char[cid]))
        if len(vals) == 1:
            const_chars.append(cid)
        else:
            varying_chars.append((cid, vals))
    print(f"  characters with a SINGLE hitProperties value across their whole file: {len(const_chars)} / {len(b_ids)} = {len(const_chars)/len(b_ids):.4f}")
    print(f"  characters with >1 distinct hitProperties value in their own file (VARYING): {len(varying_chars)} / {len(b_ids)} = {len(varying_chars)/len(b_ids):.4f}")
    for cid, vals in varying_chars:
        print(f"    {cid}: distinct values={vals}")

    print("\nhitProperties -> hitTier crosstab (pooled, non-terminator, battle):")
    hp_tier = collections.defaultdict(collections.Counter)
    for e in nonterm:
        hp_tier[e["hitProperties"]][e["hitTier"]] += 1
    for k in sorted(hp_tier):
        print(f"  hitProperties={k} (n={sum(hp_tier[k].values())}): {counter_str(hp_tier[k])}")

    print("\nhitProperties -> collisionType crosstab (pooled, non-terminator, battle):")
    hp_ct = collections.defaultdict(collections.Counter)
    for e in nonterm:
        hp_ct[e["hitProperties"]][e["collisionType"]] += 1
    for k in sorted(hp_ct):
        print(f"  hitProperties={k}: {counter_str(hp_ct[k])}")

    print(f"\nhitProperties distribution on the {len(nonzero_pid)} nonzero-projectileId entries (battle, full scale):")
    hp_on_nonzero_pid = collections.Counter(e["hitProperties"] for e in nonzero_pid)
    print(" ", counter_str(hp_on_nonzero_pid))
    baseline_hp1 = pooled_hp.get(1, 0)
    subset_hp1 = hp_on_nonzero_pid.get(1, 0)
    print(f"  hitProperties==1 baseline rate (all battle entries): {baseline_hp1}/{len(pooled)} = {baseline_hp1/len(pooled):.4f}")
    print(f"  hitProperties==1 rate WITHIN nonzero-projectileId subset: {subset_hp1}/{len(nonzero_pid)} = {subset_hp1/len(nonzero_pid):.4f}")

    # ------------------------------------------------------------------
    # 5. damageFlags
    # ------------------------------------------------------------------
    section("5. damageFlags distribution & bitfield decomposition (battle files, full scale)")
    pooled_df_nonterm = collections.Counter(e["damageFlags"] for e in nonterm)
    print("POOLED damageFlags (non-terminator, battle, n={}):".format(len(nonterm)), counter_str(pooled_df_nonterm))
    n_zero = sum(1 for e in nonterm if e["damageFlags"] == 0)
    print(f"fraction damageFlags==0 (non-terminator, battle): {n_zero}/{len(nonterm)} = {n_zero/len(nonterm):.4f}")

    print("\nPER-CHARACTER damageFlags==0 fraction (battle, n=74 chars, sorted by fraction then char id):")
    per_char_zero_frac = []
    for cid in b_ids:
        nt = [e for e in per_char[cid] if not e["isTerminator"]]
        if not nt:
            continue
        z = sum(1 for e in nt if e["damageFlags"] == 0)
        per_char_zero_frac.append((z / len(nt), cid, z, len(nt)))
    per_char_zero_frac.sort()
    for frac, cid, z, n in per_char_zero_frac:
        print(f"  {cid}: {z}/{n} = {frac:.4f}")
    n_chars_all_zero = sum(1 for frac, cid, z, n in per_char_zero_frac if frac == 1.0)
    n_chars_none_zero = sum(1 for frac, cid, z, n in per_char_zero_frac if frac == 0.0)
    print(f"  -> characters with damageFlags==0 on 100% of entries: {n_chars_all_zero}; on 0% of entries: {n_chars_none_zero}; total chars with entries: {len(per_char_zero_frac)}")

    print("\ndamageFlags(zero vs nonzero) -> hitTier crosstab (non-terminator, battle):")
    df_tier = collections.defaultdict(collections.Counter)
    for e in nonterm:
        key = "zero" if e["damageFlags"] == 0 else "nonzero"
        df_tier[key][e["hitTier"]] += 1
    for k in sorted(df_tier):
        print(f"  damageFlags={k} (n={sum(df_tier[k].values())}): {counter_str(df_tier[k])}")

    mismatches = 0
    for e in pooled:
        low6 = e["damageFlags"] & 0x3F
        special = bool(e["damageFlags"] & 0x40)
        if low6 != e["damageFlagsLow"] or special != e["hasSpecialFlag"]:
            mismatches += 1
    print(f"\nbitfield-decomposition check (damageFlagsLow==damageFlags&0x3F AND hasSpecialFlag==bool(damageFlags&0x40)), battle, n={len(pooled)}: mismatches={mismatches}")
    print("hasSpecialFlag distribution (pooled, battle):", counter_str(collections.Counter(e["hasSpecialFlag"] for e in pooled)))

    # ------------------------------------------------------------------
    # 6. knockback / hitModifier
    # ------------------------------------------------------------------
    section("6. knockback / hitModifier ranges & correlation with hitTier (battle files, full scale)")
    kb_all = [e["knockback"] for e in nonterm]
    print(f"POOLED knockback (non-terminator, battle, n={len(kb_all)}): min={min(kb_all)} max={max(kb_all)} avg={sum(kb_all)/len(kb_all):.4f}")

    hitmod_pooled = collections.Counter(e["hitModifier"] for e in pooled)
    print("hitModifier distribution (pooled incl. terminator, battle, n={}):".format(len(pooled)), counter_str(hitmod_pooled))
    hitmod_nonzero = sorted(
        ((e["_char"], e["hitModifier"], e["collisionType"], e["hitTier"], e["isTerminator"]) for e in pooled if e["hitModifier"] != 0)
    )
    print(f"hitModifier!=0 entries: {len(hitmod_nonzero)} / {len(pooled)}")
    for row in hitmod_nonzero:
        print("  (char, hitModifier, collisionType, hitTier, isTerminator) =", row)

    print("\nknockback by hitTier (non-terminator, battle, pooled across all 74 chars):")
    by_tier = collections.defaultdict(list)
    for e in nonterm:
        by_tier[e["hitTier"]].append(e["knockback"])
    for t in sorted(by_tier):
        v = by_tier[t]
        print(f"  hitTier={t}: n={len(v)} avg={sum(v)/len(v):.4f} min={min(v)} max={max(v)}")
    pooled_tier_avgs = [sum(by_tier[t]) / len(by_tier[t]) for t in sorted(by_tier)]
    is_pooled_monotonic = all(pooled_tier_avgs[i] <= pooled_tier_avgs[i + 1] for i in range(len(pooled_tier_avgs) - 1))
    print(f"  pooled avg-by-tier sequence (tier order {sorted(by_tier)}): {[round(v,4) for v in pooled_tier_avgs]} monotonic_non_decreasing={is_pooled_monotonic}")

    print("\nPER-CHARACTER knockback-by-hitTier monotonicity check (battle, n=74 chars):")
    monotonic_chars = []
    non_monotonic_chars = []
    insufficient_chars = []
    for cid in b_ids:
        nt = [e for e in per_char[cid] if not e["isTerminator"]]
        tiers_present = collections.defaultdict(list)
        for e in nt:
            tiers_present[e["hitTier"]].append(e["knockback"])
        ts = sorted(tiers_present.keys())
        if len(ts) < 2:
            insufficient_chars.append(cid)
            continue
        avgs = [sum(tiers_present[t]) / len(tiers_present[t]) for t in ts]
        if all(avgs[i] <= avgs[i + 1] for i in range(len(avgs) - 1)):
            monotonic_chars.append(cid)
        else:
            non_monotonic_chars.append(cid)
    print(f"  monotonic non-decreasing avg-knockback-by-tier: {len(monotonic_chars)} / {len(b_ids)} -> {sorted(monotonic_chars)}")
    print(f"  non-monotonic: {len(non_monotonic_chars)} / {len(b_ids)}")
    print(f"  insufficient data (<2 distinct hitTier values present): {len(insufficient_chars)} / {len(b_ids)} -> {sorted(insufficient_chars)}")

    hitmod_vals_nonterm = sorted(set(e["hitModifier"] for e in nonterm))
    print("\nhitModifier distinct values (non-terminator, battle, all 74 files):", hitmod_vals_nonterm)

    # ------------------------------------------------------------------
    # 7. SUPPORT FILES (secondary scope)
    # ------------------------------------------------------------------
    section("7. SUPPORT FILES (*_s_*, n=206) -- comparison stats")
    s_per_char, s_pooled = pool_entries(s_data)
    s_nonterm = [e for e in s_pooled if not e["isTerminator"]]
    print(f"support files: {len(s_data)}; pooled entries: {len(s_pooled)}; non-terminator entries: {len(s_nonterm)}")

    s_ct = ct_to_tier_crosstab(s_nonterm)
    print("\ncollisionType -> hitTier crosstab (pooled, non-terminator, SUPPORT):")
    for k in sorted(s_ct):
        n = sum(s_ct[k].values())
        print(f"  collisionType={k} (n={n}): {counter_str(s_ct[k])}")
    if 5 in s_ct:
        n5s = sum(s_ct[5].values())
        n5s_tier3 = s_ct[5].get(3, 0)
        print(f"  -> SUPPORT collisionType=5 tier-3 fraction: {n5s_tier3}/{n5s} = {n5s_tier3/n5s:.4f}  (battle-file equivalent printed in section 2 above)")
    if 3 in s_ct:
        n3s = sum(s_ct[3].values())
        n3s_tier1 = s_ct[3].get(1, 0)
        print(f"  -> SUPPORT collisionType=3 tier-1 fraction: {n3s_tier1}/{n3s} = {n3s_tier1/n3s:.4f}")

    s_pid = collections.Counter(e["projectileId"] for e in s_pooled)
    print("\nPOOLED projectileId (SUPPORT, n={}):".format(len(s_pooled)), counter_str(s_pid))
    s_nonzero_pid = [e for e in s_pooled if e["projectileId"] != 0]
    print(f"SUPPORT nonzero-projectileId entries: {len(s_nonzero_pid)} / {len(s_pooled)} = {len(s_nonzero_pid)/len(s_pooled):.4f}  (battle-file rate printed in section 3 above)")
    s_distinct_nonzero_pid = sorted(set(e["projectileId"] for e in s_nonzero_pid))
    print("SUPPORT distinct nonzero projectileId values:", s_distinct_nonzero_pid, f"(count={len(s_distinct_nonzero_pid)})")

    s_hp = collections.Counter(e["hitProperties"] for e in s_pooled)
    print("\nPOOLED hitProperties (SUPPORT, n={}):".format(len(s_pooled)), counter_str(s_hp))
    s_const = 0
    s_varying = 0
    for cid in s_ids:
        vals = set(e["hitProperties"] for e in s_per_char[cid])
        if len(vals) == 1:
            s_const += 1
        else:
            s_varying += 1
    print(f"SUPPORT per-file hitProperties constancy: constant-within-file={s_const}/{len(s_ids)} = {s_const/len(s_ids):.4f}; varying={s_varying}/{len(s_ids)} = {s_varying/len(s_ids):.4f}")

    s_n_zero_df = sum(1 for e in s_nonterm if e["damageFlags"] == 0)
    print(f"\nSUPPORT damageFlags==0 fraction (non-terminator, n={len(s_nonterm)}): {s_n_zero_df}/{len(s_nonterm)} = {s_n_zero_df/len(s_nonterm):.4f}")

    s_hitmod_vals = sorted(set(e["hitModifier"] for e in s_pooled))
    print("SUPPORT hitModifier distinct values (pooled incl. terminator):", s_hitmod_vals)

    # ------------------------------------------------------------------
    # 8. ITEM FILE (context only)
    # ------------------------------------------------------------------
    section("8. ITEM COLLISION FILE (item_collision.json) -- context only, n=1 file")
    for p in item_paths:
        d = json.load(open(p))
        entries = d["entries"]
        nt = [e for e in entries if not e["isTerminator"]]
        print(f"{os.path.basename(p)}: characterId={d['characterId']!r} count={d['count']} len(entries)={len(entries)}")
        print("  hitTier distribution (non-terminator):", counter_str(collections.Counter(e["hitTier"] for e in nt)))
        print("  projectileId distribution:", counter_str(collections.Counter(e["projectileId"] for e in entries)))
        print("  hitModifier distinct values:", sorted(set(e["hitModifier"] for e in entries)))
        z = sum(1 for e in nt if e["damageFlags"] == 0)
        print(f"  damageFlags==0 fraction (non-terminator): {z}/{len(nt)} = {z/len(nt):.4f}" if nt else "  (no non-terminator entries)")

    # ------------------------------------------------------------------
    # Done
    # ------------------------------------------------------------------
    section("END OF REPORT")
    print("All numbers above are computed directly from the input JSON files listed at the top of this script.")


if __name__ == "__main__":
    main()
