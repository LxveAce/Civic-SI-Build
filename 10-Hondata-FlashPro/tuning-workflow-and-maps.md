# Tuning Workflow, Daily/Sport Maps, and the Reliability-First Rule

## The One Rule That Overrides Everything

> **Engine life and reliability come before power. Every time. No exceptions.**

I'd rather leave 10 WHP on the table than bend a valve or spin a bearing on a 170k-mile K20Z3. This rule applies to every calibration decision, every parts choice that feeds into tuning, and every "should I bump this one more degree?" moment on a dyno. Safety first, power second.

If a number on a dyno sheet costs me the engine, that number doesn't count.

---

## Every Tune = Two Maps

Whenever I do a tune (base map flash, post-exhaust retune, post-intake-manifold retune, flex fuel), the output is **two calibrations, not one:**

### Daily Map

- **Valve:** Cutout closed (quiet)
- **Timing:** Conservative — 2-3 deg under max safe
- **AFR at WOT:** 12.0-12.2 on pump gas, lambda 0.80 on E85
- **VTEC crossover:** Stock-adjacent (~5400-5800 RPM)
- **Rev limiter:** Stock (8200 RPM fuel cut)
- **Launch control:** Off
- **Idle:** Smooth, OEM-feeling
- **Cold start:** Polished, no rough minute-one
- **Goal:** Drives like a new SI from the dealer. Quiet. Predictable. Nothing on the edge.

### Sport Map

- **Valve:** Cutout open (loud)
- **Timing:** Max safe — always verified with knock datalog at 0 counts AND wideband AFR at target
- **AFR at WOT:** 11.8-12.0 on pump gas, lambda 0.78-0.80 on E85 (slightly richer = cooler, safer)
- **VTEC crossover:** Lowered to 4800-5200 RPM (only after the exhaust flows enough to justify it)
- **Rev limiter:** +100 to +200 RPM over stock (8300-8400), not more
- **Launch control:** Optional, conservative (4500 RPM, no 2-step aggression)
- **Idle:** Tolerable. Slight lope allowed from lower VTEC crossover, nothing more.
- **Goal:** Squeezes the engine for everything it's got, WITHIN THE RELIABILITY ENVELOPE. Not "let's see what happens." Not "maybe push it one more click." Verified safe, every parameter.

**What "Sport = max" actually means:**

Sport is NOT "remove safety margins." It IS "stop leaving free power on the table." Free power lives in:
- Timing advance that the engine can take without knock, proven by datalog
- Fuel enrichment that's cooler and safer than what a stock conservative tune runs
- VTEC crossover dropped to where the exhaust/intake combo actually supports it
- Fan tables dialed tight so heat soak doesn't force defensive retune

Every one of these is a gain measured against a conservative baseline, not against the engine's destruction point.

---

## The Three Tune Sessions Plan

| Session | After Installing | Both Maps Tune | Budget |
|---------|-----------------|----------------|--------|
| **Tune #1** | Exhaust (cutout + headers + HFC) | Daily + Sport on pump gas, no intake mfld yet | $300-500 |
| **Tune #2** | Intake manifold + bored TB | Daily + Sport on pump gas — FULL BOLT-ON pump final | $300-500 |
| **Tune #3** | Flex fuel system (sensor + injectors + pump) | Daily + Sport with gas↔E85 real-time interpolation | $400-600 |

**Never combine sessions.** Each tune session isolates one set of hardware changes so I can attribute gains (or regressions) cleanly. Combining intake + flex fuel + exhaust retune in one dyno day = four hours of the tuner guessing which mod caused what.

**Cross-reference:** Each session maps to a datalog milestone in [docs/baseline-logs.md](../../docs/baseline-logs.md). Pre-session logs + post-session logs + dyno graph = complete paper trail.

---

## Pre-Session Checklist (Runs Before Every Dyno Day)

### Hardware Health

Any NO answer below = reschedule. Tuning a sick engine is throwing money away.

- [ ] Spark plugs fresh (< 5,000 mi on current set)
- [ ] Ignition coils healthy (no misfire codes in 500 mi)
- [ ] VTC actuator replaced or confirmed silent at cold start (see [06-Ignition-Refresh/](../06-Ignition-Refresh/))
- [ ] Valve adjustment in spec (within last 60k mi)
- [ ] Timing chain inspected (measured via FlashPro cam phase datalog, < 2-3 deg retardation)
- [ ] Coolant system fresh (see [09-Cooling-System/](../09-Cooling-System/))
- [ ] Oil fresh, correct viscosity (5W-30 for my 170k motor)
- [ ] Fuel filter clean (replaced post-E85 introduction if applicable)
- [ ] Battery healthy (13.8+V at idle with alternator charging)
- [ ] Wideband O2 sensor installed and reading sensibly at idle (see [11-Wideband-AFR/](../11-Wideband-AFR/))

### Software / Calibration

- [ ] **Stock calibration saved as backup** (the factory reset button)
- [ ] Previous dyno's final calibration saved to a known filename (for rollback)
- [ ] FlashProManager on current version
- [ ] All FlashPro firmware updates applied (test flash at home before dyno day)
- [ ] My log set from the last baseline session is reviewed — no ignored knock events, no drifting trims

### Session Plan

- [ ] Tuner knows both calibrations are needed (daily + sport)
- [ ] Tuner has the datalog files from previous session
- [ ] Tank is HALF FULL of the target fuel (not empty, not full — stable fuel pressure matters)
- [ ] If running E85: verified station I filled at, and flex fuel sensor is reporting sensible %

---

## The Safety Ceilings I Won't Cross

These are bright lines. Below any of them, no tune ships.

| Parameter | Safe Ceiling | Reliability Margin |
|-----------|-------------|-------------------|
| **Knock count at WOT** | 0 (strictly zero) | Ever. If I see any count, timing gets pulled immediately. |
| **Pump gas WOT AFR** | Never leaner than 12.0 | Cool-running richness is free reliability. |
| **E85 WOT lambda** | Never leaner than 0.82 | E85 forgives rich, punishes lean. |
| **Peak cylinder temp proxy (IAT + ignition advance)** | Stay well under OEM map's hot cells | Datalog ECT + IAT + timing. Retreat at 220F ECT. |
| **Injector duty cycle** | Never above 85% sustained | If I hit 85%, upsize injectors — never compensate with raised fuel pressure. |
| **Rev limiter** | +200 RPM over stock, max | The factory 8200 is already conservative by design. Moving it further is pure risk. |
| **VTEC engagement RPM** | Never below 4500 | Below this, the cam profile doesn't make sense for the airflow. |
| **Fuel pressure at WOT** | Within 2 PSI of base spec | Pressure drop = lean spike. Hard fail condition. |
| **Coolant temp sustained** | Target ≤ 200F at cruise, ≤ 210F at WOT | Above this, fan tables need work, not tune changes. |

**If any of these get crossed mid-session, the session stops.** Fix the cause, come back another day.

---

## How Each Mod Affects The Tune

| Mod | Affects Fuel? | Affects Timing? | Affects VTEC? | Retune Required? |
|-----|---------------|-----------------|---------------|------------------|
| K&N intake (installed) | Yes — more air → leaner baseline | Slight — can advance a hair | Slight — crossover could drop | Base map only, no dyno |
| Clutch + flywheel (installed) | No | No | No | None — pure mechanical |
| Shifter + bushings (installed) | No | No | No | None |
| Engine mounts | No | No | No | None (maybe idle AFR hair off until ECU adapts — stock tune self-corrects) |
| Brakes | No | No | No | None |
| Strut bar | No | No | No | None |
| **Headers + HFC** | **YES — major** | **YES — significant** | **YES — crossover drop opportunity** | **Dyno required** |
| **Valved exhaust cutout** | Yes — AFR shifts valve open vs closed | Minor | No | Dyno — tune both valve states |
| **Intake manifold + bored TB** | **YES — major** | **YES — significant** | **YES — crossover drop opportunity** | **Dyno required** |
| **Pulleys + damper** | No | No | No | None (mechanical — slight ECU idle relearn) |
| **Flex fuel system** | **YES — total recalibration** | **YES — interpolated** | Optional | **Dyno required, long session** |
| Clutch hydraulics | No | No | No | None |
| Suspension / brakes | No | No | No | None |
| LattePanda install | No | No | No | None — just monitoring |

**Tune-required mods get grouped into dyno sessions.** Tune-unaffected mods get installed whenever — they don't drive the calendar.

---

## What "Sport Map" Looks Like Per Phase

As the hardware progresses, the Sport map gets more aggressive — but always within the reliability ceilings above.

| Phase | Hardware | Sport Map Character |
|-------|----------|--------------------|
| Now (intake only) | K&N, no cat/exhaust mods | Community base map, no sport/daily split yet — just "don't break anything" |
| Post-exhaust | Cutout + headers + HFC | First real Sport map: +1-2 deg timing, AFR 11.9, VTEC at 5200 |
| Post-intake mfld | FBO complete | Refined Sport: +2-3 deg over stock, VTEC at 4900-5000, rev to 8300 |
| Post-flex fuel | Gas + E85 dual | E85 Sport: lambda 0.79, +4-5 deg over stock, VTEC at 4800, rev to 8400 |

None of these exceed the safety ceilings. Each phase has more to work with because the hardware lets the engine breathe better — not because I'm pushing it harder into the red.

---

## Working With Claude On Tune Changes (Eventually)

Right now I can't directly give Claude live ECU access — FlashProManager is Windows-only and hardware-paired. What I can do:

### The CSV Export Workflow

1. Drive with FlashPro datalogging on.
2. Back at my PC, open FlashProManager → File → Export Datalog → CSV.
3. Paste the CSV content into a chat with Claude (or attach the file).
4. Claude analyzes — flags outliers, identifies unsafe cells, proposes specific table edits.
5. I open the corresponding fuel/timing/cam table in FlashProManager.
6. I type the proposed values into specific cells (or reject them if the reasoning is off).
7. Save calibration, flash, verify.
8. Log again, repeat.

### What Claude CAN Do

- Read my CSV datalog and flag knock events, lean AFR, trim drift, over-temp cells
- Compare two sessions (before/after) and quantify what changed
- Propose conservative timing/fuel adjustments with specific cell addresses
- Spot patterns I'd miss (e.g., a specific load cell that's consistently lean-biased)
- Talk me through which cells a given mod should affect most

### What Claude CANNOT Do

- Flash my ECU (no hardware access)
- Read my .fpc or .fpdl binary files directly (I need to export to CSV/text)
- Replace a professional tuner for dyno-verified timing advances
- Know what my engine "sounds like" or respond to physical feedback
- Make safety calls that override the ceilings above — even at my explicit request

### What I Share With Claude Per Session

- Datalog CSV (or excerpt of relevant cells)
- Screenshot of the fuel, timing, VTEC, or cam phase table I'm considering editing
- My current calibration name and any notes from my tuner
- What I'm trying to accomplish (e.g., "smooth out the transition from closed to open loop at 3500 RPM")

---

## The Future: LattePanda as Live Tune Companion

Once the [LattePanda 3 Delta is installed](Permanent-LattePanda-Install/full-guide.md), the workflow gets tighter. The LattePanda runs FlashProManager natively — so it can be logging continuously, and the wideband O2 signal is coming in on an analog input that the same machine reads. A lightweight Python script can:

- Auto-export datalogs after each drive to a dedicated folder
- Compute simple alerts ("today you had 3 knock events above 6500 RPM in cells X, Y, Z — investigate")
- Sync logs to cloud storage so I can paste them to Claude from any device

But this is a Phase 7+ project. The core workflow (drive → export CSV → analyze → edit → flash) works fine on a laptop at home today.

---

## See Also

- [overview.md](overview.md) — the FlashPro hardware + my temporary/permanent setup paths
- [Temporary-Setup/getting-started.md](Temporary-Setup/getting-started.md) — getting online with a laptop first
- [Permanent-LattePanda-Install/full-guide.md](Permanent-LattePanda-Install/full-guide.md) — in-car PC install
- [../docs/baseline-logs.md](../docs/baseline-logs.md) — my datalog protocol
- [../11-Wideband-AFR/](../11-Wideband-AFR/) — the wideband this workflow relies on

---

*Last updated: 2026-04-18*
