# Ignition Refresh — Spark Plugs + Coils + VTC Actuator

## Status: Planned — Do BEFORE any dyno tune

## Why This Gets Its Own Folder Now

I originally lumped spark plugs into Phase 0 maintenance, but after digging deeper into 8thcivic.com and k20a.org threads for 170k-mile K20Z3s, it became obvious that ignition is a whole system that deserves its own treatment — especially before I flash anything with Hondata. Three things go together here:

1. **Spark plugs** — almost certainly cooked at 170k
2. **Ignition coils** — coil-on-plug (COP) units that get tired and start dropping cylinders under load, especially on E85 where more fuel needs more spark energy
3. **VTC actuator** — the #1 K20Z3 gripe on the forums (that cold-start rattle everyone hears)

Doing these together, before a dyno session, eliminates the single biggest source of "tune won't dial in / mystery misfires / ragged idle" headaches that get blamed on the tuner.

---

## 1. Spark Plugs

### Stock Spec

| Field | Value |
|-------|-------|
| OEM plug | NGK ILZKR7B-11S |
| Type | Iridium, laser-welded, pre-gapped |
| Gap | 0.043" (1.1mm) — pre-gapped from factory, do NOT re-gap |
| Heat range | 7 (NGK scale) |
| Change interval (Honda) | 100,000 mi |
| Change interval (community) | 60,000-80,000 mi on a driven SI |

At 170k, if these are originals they're cooked. Even if they were replaced once around 85k, they're on borrowed time. Symptoms I'd be looking for: slightly rough idle, MPG drop, misfire codes, hesitation off VTEC.

### What I'm Going With

**For pump gas (now through full bolt-on tune):** NGK ILZKR7B-11S OEM replacement. 4 plugs, ~$40.

**For E85 / flex fuel tune (later):** NGK ILFR7H (or ILKAR7L11) — **one heat range colder**. E85 burns cooler than gas but produces more combustion volume; a colder plug resists pre-ignition under the higher effective octane timing I'll be running. Community consensus on k20a.org for E85 K-series builds.

**Do NOT re-gap iridium plugs.** The fine iridium electrode is fragile. If the plug isn't at spec gap out of the box, it's defective — send it back.

### Buy Links

| Plug | P/N | Use | Price | Link |
|------|-----|-----|-------|------|
| NGK ILZKR7B-11S | 4912 | Pump gas tune | ~$10/ea | Any auto parts store / Amazon |
| NGK ILFR7H | 6102 | E85 flex fuel tune | ~$12/ea | Amazon / RockAuto |

I'll verify current pricing before buying.

---

## 2. Ignition Coils (Coil-on-Plug)

### A Note First

The K20Z3 is **coil-on-plug (COP)** — there are no spark plug wires. One coil sits directly on each plug. People confuse this on forums constantly. No wires. Don't let anyone sell me wires.

### Stock Spec

| Field | Value |
|-------|-------|
| OEM coil | Denso / Honda |
| Part number | 30520-RWC-A01 |
| Qty | 4 (one per cylinder) |
| Community-reported lifespan | 100-150k on a driven SI |

### Why OEM, Not "Performance" Coils

I looked at the Accel, MSD, and Granatelli "hi-output" coils. Verdict: marketing. The K20Z3 OEM coil is already adequate for 300+ WHP on pump gas. The aftermarket "upgrade" coils add zero real spark energy at normal combustion pressures — they just cost 3x more and sometimes ship with worse build quality than OEM Honda units.

**The actual problem at 170k is that my stock coils are tired**, not that stock coils are underpowered. Fresh OEM Honda coils (30520-RWC-A01) solve the problem completely.

### Symptoms of Tired Coils on a K20Z3

- Random misfire codes (P0301-P0304) especially at high RPM / high load
- "Stutter" under WOT above 6000 RPM
- Rough cold-start idle that smooths out after 30 seconds
- Slight MPG drop

All of these get worse on E85 because E85 needs more spark energy to ignite (higher latent heat of vaporization). If I tune for E85 on tired coils, I'll chase phantom knock that's actually misfire.

### Buy

| Part | P/N | Qty | Approx Price | Notes |
|------|-----|-----|--------------|-------|
| Honda OEM Ignition Coil | 30520-RWC-A01 | 4 | ~$40-50/ea | OEM Denso. Buy from a Honda dealer or majestichonda.com for the real deal — eBay has a lot of fakes. |

---

## 3. VTC Actuator — The Big One

### What It Is

The Variable Timing Control (VTC) actuator is the cam phaser that sits on the front of the intake camshaft. It uses oil pressure to advance/retard intake cam timing through the rev range. This is part of what makes the K20Z3 feel like it has an expanding torque band — the VTC works in combination with VTEC (which is a different system — VTEC switches between low- and high-lift cam lobes, VTC continuously varies intake cam phase).

### The Problem

The original VTC actuator has a **known weak spring** that loses preload over time. When the engine is cold and oil pressure is low (first 1-3 seconds of startup), the actuator rattles against its stops before oil pressure locks it in place. **That cold-start rattle everyone on 8thcivic complains about — that's it.**

Left alone long enough, the actuator can fail catastrophically (lose phase lock under load, jumping cam timing) which bends valves. Not common but it happens.

### Revised Honda Part

Honda revised the part silently. The new actuator has a stronger internal spring and better locking pin geometry.

| Part | P/N (superseded) | P/N (current) | Price |
|------|------------------|---------------|-------|
| VTC Actuator | 14310-RBC-002 (old) | **14310-RBC-003** (revised) | ~$280 OEM |

**Buy the 003 part. Not 002.** Any dealer ordering by VIN will ship the 003; the 002 has been end-of-life'd but aftermarket sellers still list it.

### When To Do It

**Ideal: during timing chain inspection.** The actuator is the first thing you pull when the timing cover comes off. Labor is effectively free if I'm already in there.

**Also ideal: before the full bolt-on tune.** If I tune on a weak VTC actuator, the tuner will chase phantom cam timing issues. Fresh actuator = clean baseline.

**Absolutely required: before E85 tune.** E85 runs more timing advance; if the VTC can't hold phase precisely, I'll get unpredictable tune behavior.

### Symptom Check (How I'll Know Mine Is Bad)

1. **Cold-start rattle** for 1-3 seconds after first morning start, goes away once oil pressure builds. That's the diagnostic.
2. **Worst case:** persistent rattle even warm. Replace immediately, don't drive.
3. **FlashPro datalog:** cam timing actual vs. commanded will show oscillation or lag at idle-to-2500 RPM transitions.

---

## Cost Summary

| Item | Price |
|------|-------|
| NGK ILZKR7B-11S x4 (pump gas) | ~$40 |
| Honda OEM coils 30520-RWC-A01 x4 | ~$160-200 |
| Honda VTC actuator 14310-RBC-003 | ~$280 |
| Later: NGK ILFR7H x4 (E85 swap) | ~$50 |
| **Subtotal (do-it-all-now)** | **~$480-520** |

Labor if someone else does it: add ~$150-300 for the VTC actuator (timing cover off). Plugs + coils are a 30-minute DIY job.

---

## Where This Sits in the Mod Order

**Phase 0.5** — between Phase 0 (fluids/maintenance) and Phase 1 (already-purchased installs). Specifically:

- BEFORE FlashPro first flash → clean baseline for datalogging
- BEFORE any dyno session → no phantom misfire/timing issues
- WITH timing chain inspection → VTC labor is free

---

## See Also

- [docs/mod-order-and-maintenance.md](../docs/mod-order-and-maintenance.md) — where this slots in the master plan
- [07-Hondata-FlashPro/](../07-Hondata-FlashPro/) — the tune this enables

---

*Last updated: 2026-04-18*
