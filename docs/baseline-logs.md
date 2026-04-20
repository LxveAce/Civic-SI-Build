# Baseline Datalogs — A/B Tracking for Every Mod

> The point: before and after every tune change or hardware mod, I run the same standardized set of datalogs. Apples-to-apples. This way I can see what each change actually did instead of guessing from the seat of my pants.

**Rule:** Log BEFORE I change anything. No exceptions. Once a mod is on, I can't go back in time.

---

## Why I'm Doing This

I'm about to spend a lot of money on a lot of different mods that all affect each other. Without baseline datalogs at each phase:

- I can't tell which mod actually moved the needle
- I can't catch a mistuned calibration early
- I have no way to argue with a dyno tuner if results come back lower than expected
- If something goes wrong later (a sensor goes bad, a misfire starts), I have no "healthy" reference

FlashPro's datalogger captures everything I need. It's free. The only cost is ~15 minutes per log session. No excuse to skip this.

---

## Standard Log Set — Every Time

Four logs, run in sequence, same day, same route:

### Log 1 — Cold Start / Idle Quality
- **Duration:** 3-5 min from key-on
- **Conditions:** Engine COLD (sat overnight)
- **Procedure:**
  1. Key to ON, FlashPro connected, logger running
  2. Start engine, let idle for 2 minutes without touching pedals
  3. Blip throttle 3x to 3000 RPM, return to idle
  4. Rev to 5000 RPM and hold 5 seconds
- **Looking for:** Cold start fuel trim, VTC actuator behavior (phase lock time), coolant temp rise rate, idle stability, misfire counts

### Log 2 — Cruise / Steady State
- **Duration:** 10-15 min
- **Conditions:** Engine fully warmed (coolant 185F+, IAT stable)
- **Procedure:**
  1. 35 mph, 4th gear, level ground, 3 minutes
  2. 55 mph, 5th gear, level ground, 3 minutes
  3. 70 mph, 6th gear, level ground, 3 minutes
  4. Light throttle transitions between speeds
- **Looking for:** Closed-loop fuel trims (STFT / LTFT), knock counts at cruise, timing behavior, MPG reference

### Log 3 — Part-Throttle Pulls
- **Duration:** 5-10 min
- **Conditions:** Fully warm
- **Procedure:**
  1. 3rd gear, 2000 to 5000 RPM, 50% throttle pull x 3
  2. 3rd gear, 2000 to 5000 RPM, 75% throttle pull x 3
  3. Let cool ~30 seconds between pulls
- **Looking for:** Partial-load fuel tables, timing ramp, VTEC engagement behavior (below crossover)

### Log 4 — WOT Pulls
- **Duration:** 5-10 min
- **Conditions:** Fully warm, clear road, safe conditions
- **Procedure:**
  1. 3rd gear, 2500 RPM to redline, 100% throttle x 3
  2. 4th gear, 2500 RPM to redline, 100% throttle x 2 (if space allows)
  3. Let cool fully between pulls
- **Looking for:** WOT AFR hitting target, knock counts (MUST be 0), peak timing, peak RPM, injector duty cycle

**Total time:** ~45 minutes per log session. I do this quarterly in stock form, and before/after every tune or hardware change.

---

## What Parameters I Log

FlashPro lets me configure which parameters are captured. My standard log profile:

| Category | Parameters | Why |
|----------|-----------|-----|
| Engine basics | RPM, Load (g/rev), TPS, MAP, VSS, gear | Context for every other reading |
| Fuel | STFT, LTFT, AFR (narrowband + **wideband** via analog input), injector duty cycle, injector pulse width | Tune health |
| Timing | Ignition advance (actual), timing correction, knock count | SAFETY — knock count is the #1 watchdog |
| Cam / VTEC | VTC target, VTC actual, VTEC solenoid state, VTC error | Actuator health |
| Thermal | ECT (coolant), IAT (intake air), oil temp (if wired) | Heat soak detection |
| Electrical | Battery voltage, MIL status | System health |
| Flex fuel | Ethanol content %, fuel temp | Once flex fuel sensor is wired |
| Wideband | External AFR signal (via analog input) | Tuning ground truth |

---

## Baseline Milestones I'll Capture

Each milestone gets a full 4-log set + date-stamped filename. I'll keep logs in `docs/logs/` (I'll create the folder once I have my first session).

| # | Milestone | What's Changed | Goal |
|---|-----------|----------------|------|
| 0 | **Today — stock ECU, current mods (intake + clutch + shifter + tires)** | None (baseline) | My reference "before" state. Captures K&N intake on stock calibration. |
| 1 | Post-maintenance (Phase 0 done) | Plugs, VTC actuator, coils, fluids, thermostat, radiator | Clean healthy-engine baseline before any tune changes. |
| 2 | Post-FlashPro first flash (base map, no mods) | Community base map for stock + intake | Tune-only delta vs stock ECU. |
| 3 | Post-mounts + brakes + hydraulics + FlashPro | All Phase 1 mods installed | Ready-for-tuning baseline. |
| 4 | Post-exhaust (cutout + headers + HFC) | Phase 2 complete | Exhaust flow improvements. |
| 5 | Post-dyno tune #1 (both daily + sport) | Dual calibrations dialed in | **Verify reliability-first rule.** Knock counts = 0. |
| 6 | Post-intake mfld + bored TB | Phase 3 complete | Full bolt-on hardware. |
| 7 | Post-dyno tune #2 (daily + sport, pump gas) | FBO pump gas maps dialed | Pump gas final. |
| 8 | Post-ATI damper + NST pulleys | Phase 4 | Rotating assembly. |
| 9 | Post-flex fuel install (hardware only) | Phase 6 hardware, running pump | Still on pump, new injectors/pump/sensor. |
| 10 | Post-dyno tune #3 (flex fuel final) | Daily + sport, gas + E85 interpolated | Final state. |

---

## Log File Naming Convention

`YYYY-MM-DD_milestone_NN_log-type.fpdl`

Examples:
- `2026-04-18_milestone-00_baseline_log-1-cold-idle.fpdl`
- `2026-04-18_milestone-00_baseline_log-4-wot-pulls.fpdl`

This way chronological sorting works automatically, and I can tell at a glance what each file represents.

---

## Red Flags I'm Watching For

If ANY of these show up in a log, I pull over immediately and investigate before continuing:

| Symptom in log | What It Means | Action |
|----------------|---------------|--------|
| Knock count > 0 under sustained load | Engine is knocking | Pull timing immediately. Do not drive hard until resolved. |
| Knock correction > -2 deg | ECU is fighting knock | Pull over. Check fuel quality, sensors, timing tables. |
| STFT/LTFT > ±10% | Fuel trim running extreme | Check injectors, fuel pressure, O2 sensor, MAF (if applicable) |
| AFR leaner than 12.0 WOT (pump gas) or lambda > 0.82 (E85) | **DANGEROUS lean condition** | STOP. Pull over. Do not drive until fixed. Increase fuel. |
| VTC error > 3 deg sustained | VTC actuator failing | Replace actuator — engine is not running commanded cam timing. |
| Injector duty cycle > 85% at any RPM | Injectors near limit | Upsize injectors or verify fuel pressure. |
| ECT > 220F sustained | Cooling system inadequate | Stop, let cool. Check coolant level, thermostat, radiator condition. |
| IAT > ambient + 50F at speed | Heat soak — intake cooking | Confirm heat shield function; a normal hot-side intake runs IAT elevated but not extreme. |
| Battery voltage < 13.2V with alternator on | Charging system weak | Check alternator, belt, battery. |

---

## Sharing Logs with Claude / Tuner

**FlashPro exports logs to CSV** via FlashProManager → File → Export Datalog. That's the format I use for analysis.

For the Claude workflow (see `feedback_tuning_priorities.md` in my memory system if you're reading this through me): paste the CSV content directly, or attach the file. I'll analyze specific cells, flag outliers, and propose table edits. I cannot flash the ECU — I can only recommend what to change.

For my tuner: `.fpdl` binary files directly. He loads them in his FlashProManager and sees everything native.

---

## What a "Healthy" Baseline Looks Like on a Stock 8th Gen SI

Rough reference values so I know when something's off:

| Parameter | Healthy Range (stock + K&N intake) |
|-----------|-----------------------------------|
| Idle RPM | 740-780 |
| Idle AFR (warm, closed loop) | 14.5-14.9 |
| Cruise AFR (45 mph, level, 5th gear) | 14.5-14.9 |
| WOT AFR (stock tune) | 11.5-12.2 (Honda is intentionally rich) |
| Knock count at WOT (stock) | 0 (should never see any) |
| ECT at cruise | 185-195F |
| IAT at cruise (65F ambient) | 85-110F (K&N runs hotter than stock airbox) |
| LTFT cruise | ±5% (stock + intake — intake tune will bring closer to 0) |
| Peak ignition advance, WOT | 25-32 deg at 5000-6500 RPM |
| VTEC engagement | 5800 RPM (stock), tunable to 4500-5500 |
| Battery voltage, alternator charging | 13.8-14.4 |

Anything outside these ranges in my current "stock tune + intake" state is a flag to investigate before I flash anything.

---

*Created: 2026-04-18*
