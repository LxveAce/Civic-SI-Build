# Performance Tune 1 — Full Profile

> **Living document.** This is the dedicated profile for `performance tune.fpcal` — the Sport calibration I flashed and drove on 2026-04-20. Every parameter transcribed from the 48 tab screenshots taken in FPM on 2026-04-20. Updated every time the tune is modified.

**Status as of 2026-04-20:** FLASHED, DRIVEN, **KNOCK DETECTED** — see [Knock Diagnosis](#knock-diagnosis--why-the-knock-sensors-triggered) below. Do not drive hard on this tune again until corrections are made.

---

## Header

| Field | Value |
|-------|-------|
| **Filename** | `performance tune.fpcal` |
| **Location** | `C:\Users\extra\OneDrive\Documents\FlashPro Calibrations\performance tune.fpcal` |
| **HTML export** | `performance tune 1.html` (same folder) |
| **Source** | Received from LxveAce / personal copy (pre-existing file prior to repo build) |
| **Hardware targeted (inferred)** | FBO — header + exhaust + intake + tune. **Car does NOT currently match this.** |
| **Car's actual hardware (2026-04-20)** | K&N Typhoon intake + Exedy Stage 1 clutch + lightweight flywheel + Acuity short shifter + DWS06 tires + **front slotted rotors + pads installed today**. **Stock headers, stock exhaust, stock injectors, stock fuel pump, 170k miles.** |
| **Date file saved** | 2026-04-18 19:53:05 |
| **File size** | 22,842 bytes (411 larger than stock's 22,431) |
| **Flashed to ECU?** | **YES — flashed and driven on 2026-04-20** |
| **Purpose** | Sport calibration — performance mode |

---

## Safety Pre-Check

| Check | Status | Notes |
|-------|--------|-------|
| Matched to current hardware | **❌ NO** | Tune is FBO-targeted. Car has only intake. Header + exhaust absent = less airflow than tune expects = richer than tune expects at low RPM, but lean spots at high RPM because fuel map was built for freer-flowing exhaust |
| Stock backup saved | ✅ | `Factory Flash - Stock Tune.fpcal` dated 2026-04-19 |
| Knock count at WOT = 0 | **❌ FAILED** | Knock sensors triggered on 2026-04-20 drive |
| Pump gas WOT AFR ≥ 12.0 | ⚠️ AT-RISK | WOT lambda tables show cells at 12.54-13.34 AFR. Above Hondata 12.50 ceiling = ECU may not enter WOT mode fully. See [Fuel Analysis](#fuel--wot-lambda-adjustment-tables) |
| Injector duty ≤ 85% | ❓ UNKNOWN | No datalog captured yet. **Must measure.** |
| Rev limiter ≤ 8400 | ✅ | Main 8400 / Recovery 8200 |
| VTEC engagement ≥ 4500 | ✅ | 4200-5500 RPM engage window (engage edge 4200 is below 4500, but upper bound matches FBO convention) |
| ECT sustained ≤ 210°F | ❓ UNKNOWN | No datalog. Measure. |

---

## Full Parameter Extract

### Header / identity
Cal window tree structure confirmed:
- **Fuel** (WOT lambda low, WOT lambda high, Cranking fuel, Cylinder trim, IAT comp, ECT comp, Active fuel tuning low, Active fuel tuning high, Active Tuning)
- **Ignition** (Ignition low, Ignition high, Cylinder trim, IAT comp, ECT comp)
- **VTEC** (engagement table)
- **VTC** (Cam angle low, Cam angle high, Cam angle index low, Cam angle index high)
- **Closed Loop** (Lambda)
- **Knock Control** (Knock ignition limit low, Knock ignition limit high, Knock sensitivity low, Knock sensitivity high, Knock retard low, Knock retard high)
- **Rev Limits**
- **Sensors** (AFM)
- **Boost Control** (disabled — NA)
- **Idle**
- **Throttle** (TPlate Normal)
- **Misc**
- **Traction Control**
- **Ethanol** (Ethanol ignition compensation)

### Rev Limits (screenshot 165507)

| Parameter | Value | Safety |
|-----------|-------|--------|
| Rev limiter (main) | **8400 rpm** | ✅ At my hard ceiling |
| Rev limiter recover | 8200 rpm | ✅ 200 RPM hysteresis |
| Launch RPM (adjustable) | 5000 rpm | — |
| Launch disengage speed | 3 mph | — |
| Speed limiter | 180 mph | ✅ Effectively removed |
| Boost cut enabled | **No** | ✅ Correct for NA |
| Boost cut pressure | 168 kPa (stored but disabled) | — |
| Full throttle shift | Disabled | ✅ Correct — stock internals |
| Anti-lag min RPM | 15000 | ✅ Disabled (above rev limit) |
| Launch additional fuel | 0 | — |
| Launch ign retard | 0° | — |

### VTEC Window

| Parameter | Value |
|-----------|-------|
| Engage RPM | **4200** |
| Disengage RPM | **5500** (actually "min hold RPM" — below this at part throttle, VTEC drops out) |
| Engage min ECT | 140°F |
| Engage min speed | 6 mph |
| Disengage min speed | 3 mph |

**⚠️ Note:** 4200 engage is below my reliability rule of ≥ 4500. This is aggressive-low for FBO hardware. On my current stock-header car it will engage where the cam is making LESS airflow than the tune expects.

### VTC — Cam Angle Tables

| Table | Peak value | At RPM |
|-------|------------|--------|
| Cam angle low | ~40° | 4300-4400 |
| Cam angle high | **~48-49°** | 5500-5750 |
| Cam angle index low | — | stock-like phasing |
| Cam angle index high | — | stock-like phasing |

Comments: Aggressive cam advance (high 40s crank degrees) at peak VTEC RPM — consistent with a tuner trying to extract top-end power on a full FBO car.

### Fuel — WOT Lambda Adjustment Tables

**This is the most concerning table set in the entire tune.**

Both WOT lambda adjustment LOW and HIGH cam tables contain cells with values **12.54 to 13.34 AFR**.

**Why this is a problem (the Hondata 12.50 AFR ceiling):**

- Hondata's WOT fuel mode entry requires the commanded AFR to be richer than 12.50:1.
- Cells leaner than 12.50 cause the ECU to stay partially in closed-loop (targeting ~14.7 stoich) instead of entering open-loop WOT enrichment.
- **Result:** at those WOT cells, the car runs **leaner than 14.7** for brief moments, which is extremely knock-prone at high load.

**Specific worst cells observed (approximate from screenshots — to be re-transcribed from HTML export):**
- Low-cam high-RPM high-load cells: 12.80-13.10 range
- High-cam high-RPM high-load cells: 12.54-12.95 range

**Target after correction:** every WOT cell ≤ **12.20 AFR** (lambda 0.83) per my reliability rule. Factor of safety on a 170k motor demands richer than Hondata's floor, not at it.

### Fuel — Support tables

| Table | Observation |
|-------|-------------|
| Cranking fuel | Standard multi-cell ECT-indexed — not examined for deviations |
| Cylinder trim (fuel) | Baseline zeros — no per-cylinder trim adjustment |
| IAT compensation (fuel) | Standard — richer when intake air is hot |
| ECT compensation (fuel) | Standard — richer when cold |
| Active fuel tuning low/high | **Enabled** — these are the autotune delta tables; they accumulate corrections from wideband feedback |
| Active Tuning | Enabled |

### Ignition — Main Tables

| Table | Peak WOT values |
|-------|-----------------|
| Ignition low (0°, 10° cam) | Peaks in low 20s° — conservative at low cam |
| Ignition high (at 30°, 40° cam) | **30-33° at 5000-6000 RPM, high load cells** |

**⚠️ 30-33° WOT timing:**
- Community consensus for NA K20Z3 pump 93: **24-26° WOT** is safe; 28° is borderline; 30°+ needs E85 or flawless fuel.
- On pump 91 (Indiana winter gas) this is **overtly dangerous**.
- Combined with the leaner-than-12.50 AFR spots = guaranteed knock under load.

### Ignition — Support tables

- Cylinder trim: stock distribution
- IAT compensation: standard pull when IAT rises
- ECT compensation: standard

### Knock Control

| Table | Observation |
|-------|-------------|
| Knock ignition limit low | Up to 45° at -26° cam angle (ceiling; actual demand never approaches this) |
| Knock ignition limit high | Up to 45-47° at -26° cam angle, drops sharply at high-cam/high-load cells (as expected) |
| Knock sensitivity low | Aggressive thresholds — 22-90% threshold curve across RPM |
| Knock sensitivity high | Aggressive thresholds — 22-95% |
| Knock retard low | **Up to 25°** pull at -26° cam angle |
| Knock retard high | **Up to 20°** pull at -26° cam angle |

**Assessment:** Knock detection and response are aggressive and correctly configured. When knock happens, the ECU WILL pull timing hard. The problem isn't knock detection — it's that the base timing + AFR combination **causes knock in the first place**. Pulling timing via knock retard is a safety net, not a substitute for a safe base map.

### Idle

| ECT | Normal idle (rpm) | After-start idle (rpm) |
|-----|-------------------|------------------------|
| -13°F | 1500 | 1800 |
| 5°F | 1500 | 1800 |
| 32°F | 1500 | 1800 |
| 86°F | 1500 | 1800 |
| 113°F | 1500 | 1500 |
| 149°F | 1050 | 1050 |
| 176°F | 750 | 1000 |
| 194°F | 750 | 1000 |

**Note:** Cold idle at 1800 RPM after-start is high but within spec. Warm idle at 750 RPM is normal for stock K20Z3.

### Throttle

| Parameter | Value |
|-----------|-------|
| 1st gear throttle dampening | ✅ Enabled (smooths clutch engagement) |
| Overrun throttle opening (rev hang reduction) | ✅ Enabled (quicker RPM drop on shifts) |
| Tip-in fuel ECT comp | -22°F: +50%, 32°F: +50%, 176°F: +50% |
| Overrun injector cutoff | Configured with MAP + RPM thresholds |

### Traction Control

Table present — not examined in detail. Likely stock-like / disabled.

### Ethanol

Ethanol ignition compensation table present but flex fuel hardware NOT installed on car, so this table is effectively inert until a flex fuel sensor is wired.

---

## Knock Diagnosis — Why the Knock Sensors Triggered

### Symptom
On 2026-04-20 drive after flashing this tune, knock count > 0 in ECU reading. Exact count/RPM/cell needs a datalog to pinpoint.

### Preliminary root cause (before datalog review)

**Two compounding factors:**

1. **WOT AFR target is leaner than Hondata's 12.50 open-loop entry threshold** — ECU stays partially in closed-loop during WOT, so brief moments of AFR lean spike above 12.50 (even toward stoich) occur. On a 93-octane tune in Indiana's 91-octane summer gas, this alone is enough to knock.

2. **WOT ignition timing 30-33° at high-load / 5000-6000 RPM is aggressive for pump gas, and UNMATCHED for my current hardware.** The tune was built for an engine breathing through a Skunk2 Alpha header + HFC + cat-back. Mine still has stock headers + full stock exhaust = more back-pressure = more residual exhaust gas = **hotter combustion = more knock** at the same timing/AFR.

### Contributing factor — hardware mismatch

The car is running the Sport calibration as if it had FBO hardware, but it only has:
- ✅ K&N Typhoon intake
- ❌ Stock header (restrictive)
- ❌ Stock cat-back (restrictive)
- ❌ Stock injectors (fine for NA — not an issue here)

The tune assumes ~220-235 WHP airflow. The car is probably making ~180-190 WHP worth of airflow. The timing is calibrated for the freer-flowing state, and when the engine is making less airflow but the tune is adding more timing than needed, knock happens.

### Fix direction (to be confirmed after datalog review)

| Priority | Action | How |
|----------|--------|-----|
| 1 | **Richen every WOT cell leaner than 12.20 AFR to 12.0-12.2** | WOT lambda adjustment low + high tables — find every cell ≥ 12.30 and pull it to 12.10 |
| 2 | **Pull 3-5° of timing from high-load cells in Ignition high** | 30° → 25-26°. Specifically the cells at 5000-6500 RPM, high load, for all cam-angle slices |
| 3 | **Raise VTEC engagement to ≥ 4500** | 4200 → 4500 to give cam airflow room to match tune expectation |
| 4 | **Re-flash and re-drive with datalog running** | Verify knock count = 0 across multiple pulls |
| 5 | **Long-term: build a Daily calibration** | This tune is the Sport map. I need a sister Daily map that's conservative (≤ 24° WOT timing, ≥ 12.0 AFR, VTEC 4800, rev 7800). Two calibrations on the FlashPro — primary Daily, secondary Sport. |

---

## Datalog Capture Protocol

**For when I take the car out to datalog (no internet needed in the moment — this section travels offline with the repo):**

### Before starting
1. **Engine fully warmed** — ECT ≥ 180°F. No pulls before thermostat fully open.
2. **FlashPro connected via USB cable** (keep cable loose, don't strain port)
3. **FPM open with Datalog → Record armed** (red record icon)
4. **Confirm sensors streaming in FPM** — RPM, MAP, IAT, ECT, AFR, knock count all moving
5. **Fuel in tank:** ¾+ ideally (keeps pump cool, consistent pressure)
6. **Safe, legal, empty road** — 3rd gear WOT pulls to 7000 RPM require 40-70 mph window

### What to log — specific pulls I need

**Pull Set A — 3rd gear WOT sweeps (primary data)**
- **Gear:** 3rd
- **Start RPM:** 3000 (clutch fully out, rolling)
- **End RPM:** 7000-7500 (cut 500 RPM before rev limiter — don't hit the fuel cut on data runs)
- **Throttle:** 100% hammered from start to end, no lift
- **Count:** 3 pulls minimum (so I can see if knock is repeatable or random)
- **Cool between pulls:** 30-60 seconds cruise at low load after each pull so IAT settles back near ambient and ECT doesn't climb

**Pull Set B — 4th gear WOT sweeps (load validation)**
- **Gear:** 4th
- **Start RPM:** 3000
- **End RPM:** 6500-7000
- **Throttle:** 100%
- **Count:** 2 pulls
- **Why:** 4th loads the engine harder than 3rd at the same RPM — MAP readings are higher, so any fuel/timing issue is more visible

**Pull Set C — Part throttle cruise (drivability + knock at light load)**
- **Gear:** 5th or 6th
- **RPM:** 2000-3500
- **Throttle:** 25-50%, steady cruise for 30-60 seconds
- **Why:** most real-world driving is here. If there's knock in cruise, it will show up in this log.

**Pull Set D — Idle + tip-in**
- **Stopped at idle** for 60 seconds after warm-up (proves idle stability)
- **Light tip-ins** from idle to 3000 RPM in neutral, a few times (tests throttle tip-in fuel and trims)

### What to note in a separate text file (I'll create `pull-notes-YYYY-MM-DD.txt` alongside each log)

For each pull, I record:
- **Ambient temp** (outside thermometer / phone weather)
- **Fuel octane** (91 / 93)
- **Fuel brand + station** (different stations have different ethanol content and additive quality)
- **Odometer reading**
- **Wind direction** (for any 1/4-mile timing comparisons later)
- **Road surface** (flat, uphill, downhill — loads differently)
- **Any audible ping** I heard during the pull (even if ECU didn't catch it)

### After the drive
1. **Do NOT shut off FPM before saving the log** — `Datalog → Save As`, name it `performance-tune-1_YYYY-MM-DD_pull-N.fpdl`
2. **Also export to CSV** — `File → Save As → CSV` (or use the Export function depending on FPM version). CSV is the format I send to Claude for analysis.
3. **Save logs to:** `C:\Users\extra\OneDrive\Documents\FlashPro Calibrations\Datalogs\` (create folder if missing)
4. **Back at the desk:** paste CSV contents + pull notes to Claude for analysis.

### Sensors that MUST be in the log

FPM's default datalog preset captures most of these, but verify in `Tools → Datalog Parameters` before the drive:

| Sensor | Why |
|--------|-----|
| **RPM** | x-axis of every analysis |
| **MAP (kPa or bar)** | Load axis — shows when WOT enters open-loop |
| **TPS (%)** | Confirms actual throttle position — proves I was WOT |
| **VSS (mph)** | Speed — proves gear position |
| **Gear (calculated)** | Confirms gear during pull |
| **IAT (°F)** | Intake air temp — knock driver |
| **ECT (°F)** | Coolant temp — knock driver if too high |
| **AFR (commanded)** | Target the ECU is asking for |
| **AFR (measured)** | Actual lambda (from factory O2 or wideband if installed) |
| **Short-term fuel trim** | How much the ECU is correcting fuel |
| **Long-term fuel trim** | Baseline offset |
| **Cam angle (VTC actual)** | Proves cam is reaching its target |
| **Cam angle (VTC target)** | What the tune asked for |
| **VTEC solenoid state** | On/Off — proves cam changeover |
| **Ignition timing** | Actual degrees delivered to plugs |
| **Knock count** | **THE CRITICAL ONE** — any > 0 at WOT is a flag |
| **Knock retard** | Degrees the ECU pulled in response to knock |
| **Injector duty cycle** | Must stay ≤ 85% — proves injector sizing is enough |
| **Fuel pressure (if sensor available)** | — stock car may not have this |
| **Battery voltage** | Low voltage = injectors can't open as fast = lean spikes |
| **Barometric pressure** | Altitude compensation check |

### Offline analysis fallback

Since I won't have internet during the drive and for some time after: **the entire diagnostic playbook is written in `07-Hondata-FlashPro/datalog-analysis-guide.md`** in this repo. It walks through what to look for in a log, in what order. I can self-triage the data before sending to Claude.

When I do get back online, I paste:
1. The CSV log (as text)
2. The pull-notes file
3. The weather + octane + any audible notes

And Claude produces specific cell-level tune corrections.

---

## Comparison — This Tune vs Safety Ceilings

| Parameter | This Tune (Performance Tune 1) | My Reliability Ceiling | Pass/Fail |
|-----------|-------------------------------|------------------------|-----------|
| WOT AFR minimum | ~12.54 (leanest cell) | ≥ 12.0 | ❌ FAIL |
| WOT timing maximum | 30-33° | ≤ 26° (pump) | ❌ FAIL |
| VTEC engage | 4200 RPM | ≥ 4500 | ❌ FAIL (barely) |
| Rev limiter | 8400 | ≤ 8400 | ✅ PASS |
| Boost cut | Disabled | N/A (NA car) | ✅ PASS |
| Full throttle shift | Disabled | Disabled | ✅ PASS |
| Speed limiter | 180 mph | removed | ✅ PASS |
| Launch RPM | 5000 | sensible | ✅ PASS |
| Idle (hot) | 750 rpm | 700-800 | ✅ PASS |
| Anti-lag | Disabled | Disabled | ✅ PASS |
| Knock retard response | Aggressive (up to 25° pull) | aggressive | ✅ PASS |

**Overall:** 3 FAIL / 8 PASS. The failures are exactly where my reliability rule demands margins — AFR and timing on a 170k motor.

---

## Revision Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-04-20 | Tune flashed as Sport map and driven | First real-world test |
| 2026-04-20 | Knock count detected | Root cause analysis initiated |
| 2026-04-20 | Full parameter transcription captured from 48 FPM screenshots | Build baseline record before any changes |
| 2026-04-20 | Profile document created | Dedicated home for this specific tune |

---

## Next Actions

### Immediate (next drive is a datalog, not a spirited drive)
1. Datalog the pull set above so we know exactly which cells triggered knock
2. Do NOT WOT-drive aggressively until corrections flashed

### Short-term (within next week)
1. Paste datalog CSV + notes to Claude for cell-level analysis
2. Apply recommended corrections in FPM: richen lean cells, pull timing, raise VTEC
3. Re-flash, re-datalog, verify knock count = 0

### Medium-term (before Phase 2 mods)
1. Build a conservative **Daily** calibration as primary (25° WOT max, 12.0 AFR floor, VTEC 4800, 7800 rev)
2. Corrected version of this tune becomes the **Sport** secondary calibration
3. Both calibrations load to FlashPro unit → button-combo switching in-car

### Long-term (after FBO hardware install)
1. Re-dyno on Skunk2 Alpha + HFC + cat-back to properly calibrate airflow curves
2. Revisit every WOT cell — the airflow model will have changed
3. Consider E85/flex fuel calibration as third cal

---

*Document created 2026-04-20 — LxveAce + Claude*
*Updated every time this tune's parameters change, every time a datalog reveals something new, every time a flash is performed*
