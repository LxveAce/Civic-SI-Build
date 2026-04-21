# FlashPro Advanced Features — Launch, Flat-Foot, Per-Gear, Torque Management

> The features that make FlashPro more than "just a fuel-and-timing reflash." What each does, when I'd use it, and the reliability-first settings for my 170k-mile K20Z3.

**Verification note:** Exact FPM menu names, parameter availability, and default values for the PRB calibration (06-11 Civic SI) change slightly between FPM software versions. Items flagged **[VERIFY]** I'll confirm against my current FPM version or with my tuner before enabling.

---

## 1. Launch Control (2-Step)

### What It Does

Holds engine RPM at a user-set value while the car is stationary with clutch in. Releases immediately on clutch pedal release. Activation is gated on clutch switch, VSS (speed), and sometimes brake.

### Typical Settings

| Parameter | Value (my plan) |
|-----------|-----------------|
| Activation: Clutch switch | Required (pressed) |
| Activation: VSS below | 5 mph |
| Activation: Min TPS | 90%+ (only engaged at WOT) |
| Activation: Min ECT | 150°F (no cold-engine launches) |
| Launch RPM — Daily map | Disabled entirely |
| Launch RPM — Sport map | **4500 RPM** (conservative — protects clutch/axles at 170k) |

### Why 4500 RPM, Not 5500

The K20Z3 makes meaningful torque below VTEC, so I don't need to pre-load VTEC to get off the line. Launching at 5500+ RPM with my stock engine mounts (before Hybrid Racing 70A mounts are in) and 170k-mile axles = grenading something on the drivetrain.

- Stock clutch (new Exedy Stage 1): rated ~280 WHP, so shock-loading at 5500 RPM is pushing it
- 170k-mile axles: inner CV joints are a known wear point; sudden high-torque engagement accelerates failure
- Stock or fresh engine mounts: high-RPM launches with soft mounts transfer more torque to the drivetrain than to the wheels

After my Phase 5 suspension work and axle refresh (if I ever do them), I could bump launch to 5000-5200. Not before.

### How the RPM Is Held

The ECU uses one of two mechanisms:
- **Ignition cut:** ECU skips spark events to limit RPM. Preferred for street use — softer, quieter.
- **Fuel cut:** ECU skips fuel injection. Harsher, louder, potentially lean transients.

**My setting:** Ignition cut. Fuel cut is what race cars use for the flamethrower effect; daily-drivable isn't worth the lean risk.

### Ignition Retard During Launch

Some calibrations retard timing while launch control is active to reduce power to the wheels (so RPM stays at target without all the exhaust drama). **Stock retard: around -5 to -10 degrees during launch.** Leave alone.

### When I Won't Use Launch Control

- Before engine mounts are upgraded
- Before clutch hydraulics are upgraded
- On public roads (outside tracked spaces, per the reliability-first rule)
- In the rain
- With a cold engine (below 150°F ECT)

---

## 2. Flat-Foot Shifting (No-Lift-Shift)

### What It Does

Allows the driver to keep the throttle pinned during the upshift. The ECU detects the clutch depression and briefly cuts ignition (or fuel, or both) to prevent over-rev while the transmission is between gears. Throttle stays 100%, shift is cleaner.

### The Trade-Off

**Pros:**
- Slightly faster upshifts (0.05-0.1 sec)
- No throttle lift = no intake vacuum spike = cleaner AFR during shift
- Flashier, more "race-y" feel

**Cons:**
- Shock-loads the drivetrain harder than a normal lift-shift
- Accelerates clutch wear
- At high RPM, the shock can damage transmission synchros on a 170k-mile gearbox
- Shift cut isn't free — every cut is a fuel/spark interruption the engine doesn't love

### My Decision

**Disabled on both maps.** My 170k-mile transmission doesn't need the abuse, and 0.1 seconds is meaningless on the street. Might revisit after a full clutch + trans refresh. Until then, traditional clutch-in/throttle-lift/shift/clutch-out is fine.

### If I Ever Enable It

| Parameter | Conservative setting |
|-----------|---------------------|
| Activation | Clutch pressed + TPS > 80% |
| RPM threshold | > 5000 RPM (don't cut at low RPM) |
| Cut duration | 100-200 ms max |
| Cut type | Ignition cut (not fuel cut) |
| Gear range | 1→2, 2→3, 3→4 only (above 4th, normal shifts are fine) |

---

## 3. Per-Gear Rev Limits

### What It Does

FlashPro lets me set different fuel-cut RPMs per gear. Useful for protecting the drivetrain from over-rev scenarios.

### What I'd Set

| Gear | Rev Limit (Sport map) | Why |
|------|----------------------|-----|
| 1st | 8200 RPM | Prevent massive over-rev on a missed 1→2 shift |
| 2nd | 8400 RPM | Same, slightly more headroom |
| 3rd | 8400 RPM | Comfortable peak-power range |
| 4th | 8400 RPM | Same |
| 5th | 8400 RPM | Same |
| 6th | 8200 RPM | Highway cruise gear — no reason to push past stock |

**Daily map:** all gears at stock 8200 RPM.

### The Hard Ceiling

I won't go above 8400 RPM on any gear on stock internals at 170k miles. Full stop. **[VERIFY]** the exact per-gear parameter location in FPM — it may be under "Rev Limits" or "Advanced" depending on FPM version.

---

## 4. Torque Management Disable

### What Honda's Stock Tune Does

During upshifts (especially 1→2 and 2→3), Honda's stock calibration pulls ignition timing by 5-15 degrees for 100-200 ms to "cushion" the shift. The result: a slight hesitation in the pull, often perceived as a dead spot around VTEC engagement during aggressive shifts.

### What Disabling Does

Flattens the torque-reduction tables so timing stays commanded throughout the shift. The pull feels uninterrupted.

### Community Consensus

Most Hondata tuners on K20 builds flatten these tables as part of a Sport tune. It's a well-understood modification with no reliability cost as long as:
- The clutch is healthy
- Rev limits are respected
- The shift isn't so violent it exceeds transmission torque capacity

### My Plan

- **Daily map:** leave stock. Smoother commuting.
- **Sport map:** tuner flattens the torque management tables during Tune #1. Cleaner VTEC pulls through shifts.

**I don't flatten these myself.** They interact with ignition timing authority in subtle ways, and a dyno-verified flattening is safer than armchair editing.

---

## 5. Shift Light / Shift Indicator

### The Reality

**The 8th gen Civic SI does NOT have a factory shift light on the gauge cluster.** The tachometer needle is the "shift indicator" — you watch the VTEC crossover and redline yourself.

### What FPM Offers

FPM has a **software shift-light display** in the parameter monitor gauge view. A configurable RPM threshold triggers a visual alert (color change, flash, etc.) on the laptop/LattePanda screen.

**[VERIFY]** whether the original FlashPro has a **hardware digital output pin** that could drive an external LED shift light. I don't recall one. FlashPro 2 has more I/O. If I want a physical shift LED, I'd need an Arduino on the LattePanda reading RPM from the FPM datalog stream and driving the LED.

### My Plan

- **Software shift light in FPM gauge view:** set to 7800 RPM (200 RPM before my 8200 rev limit, gives me a visual cue to upshift).
- **Physical LED:** possible future project via Arduino, not a priority.

---

## 6. Rev Hang / Throttle Response

### What Rev Hang Is

When I lift off the throttle, the stock calibration holds the throttle plate slightly open (for emissions purposes — cleaner combustion during deceleration) before fully closing. Result: engine revs "hang" at the lift-off point for 0.3-0.8 seconds before decaying, making rev-matching on downshifts awkward.

### The Fix

FPM has a setting to reduce or eliminate rev hang by closing the throttle plate more aggressively on lift-off. **[VERIFY exact parameter name]** — commonly called something like "Lift-off throttle plate control" or "Deceleration throttle position."

### My Plan

**Daily map:** minor reduction in rev hang (better driveability, still clean emissions).
**Sport map:** aggressive reduction. Sharper throttle response, easier rev-matching.

Dyno tuner handles this during Session #1 or #2.

---

## 7. Gear Detection Calibration

### What It Does

The ECU calculates which gear you're in based on VSS ÷ RPM ratio. Per-gear features (rev limits, flat-foot, etc.) depend on this working correctly.

### When It Needs Recalibration

- After changing tire size (e.g., going from 215/45R17 to 235/40R17 shifts ratios by ~2-3%)
- After changing final drive (axle ratio swap — not planned for my build)
- If the ECU misidentifies a gear (FPM parameter monitor shows wrong gear under load)

### How to Calibrate

FPM has a **gear-learning mode** where I drive in each gear at steady RPM and the ECU records the ratio. Alternative: manually enter known VSS/RPM values per gear in the calibration table.

### My Plan

I'll let the ECU auto-learn after the first flash. Check gear detection in the parameter monitor during a test drive (drive in each gear, verify FPM displays the correct gear number). Recalibrate if I ever change tire sizes.

---

## 8. Speed Limiter Removal

### What Stock Does

The 8th gen SI has an electronic top-speed limiter (**[VERIFY]** approx 110-125 mph). Engages via fuel cut when VSS exceeds the threshold.

### FPM Setting

"Remove Speed Limiter" checkbox or adjusting the limiter to 180+ mph (effectively removed). Common setting for any performance tune.

### My Plan

**Both maps:** speed limiter off. I don't plan to drive at those speeds on public roads, but I don't want a fuel cut surprising me on a track day or open-road event.

---

## 9. A/C Cut at WOT

### What It Does

On WOT with A/C on, the ECU disengages the A/C compressor clutch. Recovers 3-8 HP that would otherwise be absorbed by compressor drag.

### Stock Behavior

Already enabled on the stock calibration — Honda does this by default. **Leave alone.**

**[VERIFY]** whether the stock threshold is adjustable (some calibrations let me change the TPS% that triggers A/C cut).

---

## 10. Cooling Fan Tables

### What It Does

Controls when the primary and secondary (A/C) cooling fans turn on and off based on ECT.

### Stock Settings

- Primary fan ON: ~205°F
- Primary fan OFF: ~195°F
- Secondary fan: triggers with A/C or with high ECT

### My Plan (with Koyorad radiator + Phase 0 coolant)

- **Daily map:** Fan ON 195°F, Fan OFF 185°F
- **Sport map:** Fan ON 190°F, Fan OFF 180°F

Tighter fan control keeps ECT stable during sustained load (canyon runs, dyno pulls). The Koyorad has extra heat rejection capacity; running the fan earlier uses that capacity proactively. See [09-Cooling-System/](../09-Cooling-System/).

---

## 11. CEL Defeat Flags

### Rear O2 Sensor CEL (P0420 Cat Efficiency)

**When I'd need this:** If I ran a catless test pipe (not in my plan — I have the Berk HFC).

**My plan:** Not needed.

### IMRC (Intake Manifold Runner Control) CEL

**When I'd need this:** After installing the Skunk2 Ultra Street intake manifold, which deletes the stock IMRC flap. Without this defeat flag, I get a persistent P2004/P2005 code.

**My plan:** Tuner enables this flag during Tune #2 (post-intake manifold install). See [14-Intake-Manifold/](../14-Intake-Manifold/).

### EVAP System CELs

**When I'd need this:** Only if I physically removed the EVAP canister (race-only). Not in my plan.

**My plan:** Not needed.

---

## 12. Closed-Loop Authority Limits

### What They Are

The ECU's short-term and long-term fuel trims operate within a limited authority range — they can add/subtract fuel up to ±25% from the calibration's target, but clamp beyond that.

### When They Matter

If my injectors, MAF, or fuel pressure is significantly off, trims can peg at the limit. FPM has tunable limits:
- **STFT limit:** typically ±25%
- **LTFT limit:** typically ±20%

**I don't touch these unless diagnosing a specific trim-pegging issue.** Widening the limits masks the underlying problem.

---

## 13. Features I Won't Touch

These exist but are either well-calibrated stock or too specialized for my build:

- **Boost control tables** (N/A on NA)
- **Wastegate duty** (N/A on NA)
- **Intercooler sprayer** (N/A on NA)
- **Map switching via clutch-pedal tap** (FlashPro 2 feature, not available on original unit)
- **TPS calibration** (only adjusted after a throttle body replacement or cleaning)
- **CAM sensor learning** (auto-learned by ECU; don't manually adjust)
- **Immobilizer settings** (never touch — I'll brick the car)

---

## 14. Summary — My Advanced Feature Matrix

| Feature | Daily Map | Sport Map |
|---------|-----------|-----------|
| Launch control | Disabled | 4500 RPM (post-mount upgrade) |
| Flat-foot shift | Disabled | Disabled (reliability call) |
| Per-gear rev limit | Stock 8200 | 8400 in 2-5, 8200 in 1 and 6 |
| Torque management | Stock | Flattened (tuner) |
| Shift light | FPM gauge at 7800 | FPM gauge at 7800 |
| Rev hang reduction | Mild | Aggressive |
| Speed limiter | Removed | Removed |
| A/C WOT cut | Stock (enabled) | Stock (enabled) |
| Fan ON temp | 195°F | 190°F |
| Rear O2 defeat | No (have HFC) | No (have HFC) |
| IMRC defeat | Yes (after IM swap) | Yes (after IM swap) |

---

## See Also

- [overview.md](overview.md) — FlashPro hardware overview
- [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md) — reliability-first rules these features operate under
- [calibrator-tables-reference.md](calibrator-tables-reference.md) — tables these features interact with
- [datalog-analysis-guide.md](datalog-analysis-guide.md) — verifying behavior after enabling features
- [troubleshooting-and-faq.md](troubleshooting-and-faq.md) — issues related to these features

---

*Last updated: 2026-04-19*
