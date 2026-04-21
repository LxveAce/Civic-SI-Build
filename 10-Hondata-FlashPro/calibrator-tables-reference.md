# FlashPro Calibrator Tables — My Reference

> Every tuning table in FlashProManager, what it controls, typical values, and safe-range guidance for my K20Z3 at 170k miles. This is the file I open when a tuner says "bump cell 4500-LOAD8 by 0.5 degrees" and I need to know which menu to look in.

**Verification note:** I pulled this together from my accumulated research + Hondata documentation + community knowledge. Before trusting specific numerical ranges on a dyno session, I'm cross-checking with my tuner and against the current Hondata help docs (FlashProManager → Help menu → Help Contents, or [hondata.com/flashpro-civic-si-2006-2011-us](https://hondata.com/flashpro-civic-si-2006-2011-us)). Items I flagged with **[VERIFY]** below are things I'll double-check before I apply them.

---

## How FlashProManager Is Organized

FlashProManager is a single Windows app with a handful of top-level views:

| View | What It Shows | When I Use It |
|------|---------------|---------------|
| **Calibrator** | Every tunable table + setting in the current calibration | Anytime I want to see or change what the car is calibrated to do |
| **Parameter Monitor** | Live data stream from the ECU via OBD2 | Troubleshooting, verifying behavior after a change, gauge-style dashboard |
| **Datalogger** | Start/stop recording, review past logs | Gathering data for tuning, A/B comparisons, diagnosis |
| **FlashPro Status** | Unit status, firmware, calibration currently loaded, VIN pairing | Sanity check before/after a flash |
| **Help** | Built-in reference for every calibrator parameter | First place to look when a table name isn't obvious |

The Calibrator is organized by function. What follows is my cheat sheet for what lives where and what each one actually controls.

---

## 1. Fuel Tables

### Low Cam Fuel Table (Pre-VTEC)

Controls the air-fuel ratio target when the engine is running on the low-lift cam profile (below VTEC engagement). Axes are RPM vs engine load (g/rev or MAP depending on calibration).

**What I tune here:**
- AFR targets at cruise (closed-loop — usually stays at 14.7 stoich regardless)
- AFR targets at mid-throttle (should trend slightly richer, 13.8-14.2)
- AFR targets at WOT below VTEC (12.5-13.0 typical for pump gas)

**Safe range for my NA 170k K20Z3 on pump 93:**
| Condition | AFR Target |
|-----------|-----------|
| Idle / closed-loop | 14.6-14.8 (let ECU do its thing) |
| Cruise | 14.5-14.9 (closed-loop zone) |
| Part-throttle | 13.5-14.2 |
| Low-cam WOT | 12.5-13.0 (Sport) / 12.8-13.2 (Daily) |

**Never lean past 12.0 AFR at WOT on pump gas. Never.**

### High Cam Fuel Table (VTEC Engaged)

Same axes, but for the high-lift cam profile. This is the table that actually matters for WOT power — once VTEC engages, this is where the engine lives at high RPM.

**Safe range for my NA 170k K20Z3 on pump 93:**
| Condition | AFR Target |
|-----------|-----------|
| High-cam light load (rare — usually you only hit high cam at WOT) | 13.0-13.5 |
| High-cam WOT | **11.8-12.2 (Sport)** / **12.0-12.4 (Daily)** |

Honda's stock high-cam WOT AFR is intentionally rich (~11.5 in places) for emissions and reliability. A well-tuned Hondata calibration will lean this up slightly for more power while staying in the reliability envelope.

### Flex Fuel Fuel Tables (E85 Endpoint)

When flex fuel is enabled, FlashPro stores a **second set of fuel tables** for the E85 endpoint. The ECU interpolates between gasoline and E85 tables based on the sensor's ethanol reading.

**Safe range for E85 WOT on my engine:**
| Condition | Lambda | AFR (E85 stoich = 9.765) |
|-----------|--------|--------------------------|
| Low-cam WOT | 0.82-0.85 | 8.00-8.30 |
| **High-cam WOT (Sport)** | **0.78-0.80** | **7.62-7.81** |
| High-cam WOT (Daily) | 0.80-0.82 | 7.81-8.00 |

Richer lambda on E85 is safer because E85 cools the charge more aggressively, and the extra fuel volume buffers against lean spikes during transients.

### Cranking Fuel

Short table that governs how much fuel gets injected during engine cranking.

**When I touch this:**
- After switching to E85 for the first time — E85 needs significantly richer cranking fuel, especially in cold weather
- If cold starts get rough after hardware changes

**Don't touch unless:** I have a cold-start problem I'm diagnosing. Stock cranking fuel is well-dialed for gasoline.

### After-Start Enrichment

Rich-mixture period immediately after starting, tapers off over seconds. Helps smooth cold idle.

### Warm-Up Enrichment

Extra fuel based on coolant temp during warmup. Tapers to 0 once ECT hits target.

**[VERIFY]** The exact axes (ECT thresholds and duration) vary by calibration version — I'll confirm with tuner.

---

## 2. Ignition Tables

### Low Cam Ignition Table

Timing advance (degrees BTDC) at each RPM × load cell during low-cam operation.

**Safe conservative peak values on my pump 93 build:**
| RPM | Load | Peak Timing (pump 93) |
|-----|------|----------------------|
| 2000-3000 | Light (cruise) | 30-35 deg |
| 2000-3000 | WOT | 20-25 deg |
| 4000-5000 | WOT (low cam) | 22-28 deg |
| 5500-6000 | Just before VTEC | 24-28 deg |

### High Cam Ignition Table

Same, for VTEC-engaged operation. This is where most of the power-vs-knock fight happens.

**Safe conservative peak values on pump 93:**
| RPM | Load | Peak Timing (Sport) |
|-----|------|--------------------|
| 5500-6000 | WOT | 26-29 deg |
| 6000-7000 | WOT | 28-32 deg |
| 7000-8000 | WOT | 26-30 deg (backing off near redline is normal) |

**Rule I won't break:** If knock count in the datalog is > 0 at any cell for sustained operation, I pull timing at that cell. No "maybe it's sensor noise" excuses. Every knock event matters on a 170k-mile engine.

### Flex Fuel Ignition Tables (E85 Endpoint)

E85 tolerates more timing. Typical gains on a well-tuned NA K20Z3:
- Low cam: +1 to +3 degrees across the band
- High cam: +2 to +5 degrees, concentrated in the 5000-7000 RPM range where knock margin on pump gas is tightest

**[VERIFY]** I'll let my tuner dial these. Arm-chair advancing timing on E85 "because it can take more" is the single most common way people hurt NA K-series engines.

### Knock Retard

Not directly a table I tune, but a setting that controls how aggressively the ECU pulls timing when it detects knock. Stock is conservative. I leave this alone — the whole point is that knock correction is my safety net.

---

## 3. VTEC Settings

### VTEC Engagement RPM (Low to High Cam)

Single RPM value where the ECU activates the VTEC solenoid to switch from low-lift to high-lift cam profile.

**Stock:** ~5800 RPM
**Safe range for tuning:** 4500-6000 RPM
**My plan:**
- **Daily map:** 5400-5600 RPM (close to stock — smoother VTEC transition, preserves fuel economy)
- **Sport map:** 4800-5200 RPM post-full-bolt-on (earlier VTEC = more area under the curve in hard driving)

**Hard floor I won't go below: 4500 RPM.** Below this, the cam profile doesn't make sense for the airflow — you get a weird lumpy off-VTEC power band and nothing gained.

### VTEC Engagement Throttle

Some calibrations gate VTEC on throttle position too (so light-throttle cruise at 5500 RPM doesn't wake up the high cam). I leave this at stock unless specifically addressing a drivability issue.

### VTEC Disengagement RPM / Hysteresis

The RPM at which VTEC drops back to low cam. Typically 300-500 RPM below engagement to prevent flutter.

---

## 4. VTC (Cam Phase) Tables

Variable Timing Control phases the intake cam by 0-50 degrees (crank degrees). This is continuously variable based on RPM × load.

### VTC Target Table

What phase the ECU asks for at each RPM × load cell. Honda's stock cam phase map is already highly optimized — there's not much room for gains here on an NA build.

**When to touch this:**
- After intake manifold swap (Skunk2 Ultra Street changes breathing dynamics — tuner may recommend 2-5 degrees of advance at specific cells)
- After headers — similar small adjustments possible

**When to NOT touch this:**
- On day 1 with stock hardware — Honda engineered this; I don't know better yet

### VTC Minimum / Maximum

Limits on how far the ECU is allowed to phase the cam. **I don't change these.** Going past Honda's engineering limits risks valve-to-piston clearance issues.

---

## 5. Idle Settings

### Target Idle RPM

**Stock:** 740-780 warm
**Tunable:** 650-1000 RPM
**My plan:** leave stock for Daily. Sport map may bump to 800-850 if engine mounts are causing idle roughness at lower RPM.

### IACV (Idle Air Control Valve) Settings

Controls how the ECU manages airflow at idle. After intake manifold swap, this sometimes needs recalibration — Skunk2 Ultra Street has different idle airflow characteristics than stock RRC.

### Idle Spark Advance

Typically stock or slightly bumped for idle stability after aftermarket mods.

---

## 6. Rev Limits

### Fuel Cut RPM (Hard Limiter)

**Stock:** 8200 RPM
**Tunable:** up to ~8800 RPM on stock internals (don't)
**My plan:**
- **Daily:** 8200 RPM (stock)
- **Sport:** 8300-8400 RPM (100-200 RPM over stock max)

**Hard ceiling I won't cross: 8400 RPM on stock internals at 170k miles.** Community consensus is that K20Z3 bottom ends survive 8500+ in built/fresh engines, but mine is neither built nor fresh. Reliability-first.

### Per-Gear Rev Limits

FlashPro lets me set different fuel-cut RPMs per gear. Useful for:
- Lower limit in 1st gear (prevents over-rev on a 1-2 upshift)
- Higher limit in 5-6 (not really needed on NA K20Z3)

**[VERIFY]** Per-gear rev limit is commonly in the "advanced" or "misc" section — exact menu location varies by FPM version.

---

## 7. Launch Control

### Launch Control RPM

RPM target when driver is at WOT with car stationary. Clutch-engagement-sensitive.

**My plan (Sport map only):**
- 4500 RPM launch limit
- No 2-step aggression — just a rev limiter at 4500 when stationary
- Disable in Daily map

**Not recommended for me until:** engine mounts are in, clutch hydraulics are upgraded. Launching a worn clutch at 4500 RPM = new clutch next week.

### Flat Foot Shift (No-Lift-Shift)

Allows the driver to keep WOT through the upshift — ECU cuts spark briefly during clutch depression to prevent over-rev. Nice feature but hard on the drivetrain.

**My plan: disabled.** My 170k-mile transmission doesn't need the abuse, and the time saved on a shift is negligible for street driving.

---

## 8. Torque Management

### Torque Management Disable

Honda's stock ECU pulls timing during 1-2 and 2-3 upshifts to smooth the shift. Community consensus is this feels like a dead spot and is worth disabling for a sporty feel.

**My plan:** disable in Sport map. Leave stock in Daily for smoother commuting.

### Ignition Retard per Gear

Some calibrations allow per-gear timing maps. Not commonly used on NA builds — more of a turbo tuning feature.

---

## 9. Fan and Cooling Tables

### Primary Fan ON Temperature

**Stock:** ~205F
**My plan:** 195F on Daily, 190F on Sport. With the Koyorad radiator ([09-Cooling-System/](../09-Cooling-System/)) and 5W-30 synthetic, tighter fan control keeps ECT stable under sustained load.

### Primary Fan OFF Temperature

Typically 5-10F below ON temp to prevent hunting.

### Secondary Fan (A/C) Triggers

Controls the second fan for A/C operation. Leave stock unless diagnosing A/C-related overheating.

**Cross-reference:** the cooling system refresh feeds directly into these tables. New radiator + tuner-dialed fan maps = peace of mind on a hot dyno day.

---

## 10. Sensor / Input Settings

### O2 Sensor Settings

- **Primary (upstream) O2:** tune uses it for closed-loop fuel correction
- **Secondary (downstream) O2:** normally monitors cat efficiency; often **repurposed for flex fuel signal input on FG2** ([VERIFY the exact pin with tuner](../19-Flex-Fuel-and-Fuel-System/))

### MAP Sensor Calibration

If I add a larger MAP sensor (unusual on NA), it's recalibrated here. Stock MAP is fine for my build.

### Wideband O2 (Analog Input)

FlashPro has configurable analog inputs that can read a 0-5V wideband O2 signal. This is where the **AEM X-Series 30-0300** ([11-Wideband-AFR/](../11-Wideband-AFR/)) gets wired. Configuration:
- Set analog input type: "Wideband O2 (AEM 30-0300)" (or Innovate, PLX, etc. — tool has presets)
- Calibration: verify idle reads ~14.7 AFR when the engine is warm

### Ethanol Content Sensor Input

Second analog input (or repurposed rear O2 signal) for the flex fuel sensor. **[VERIFY exact pin for FG2]** — forum consensus points to the rear O2 signal wire, but I want Hondata's official wiring doc or my tuner's sign-off before I splice.

---

## 11. DTCs / CELs (Diagnostic Trouble Codes)

### Rear O2 CEL Defeat

If I run a test pipe or delete the cat downstream of the OEM position, the rear O2 throws P0420 (catalyst efficiency). FlashPro can suppress this code.

**I don't need this** — I'm running the Berk HFC which keeps cat efficiency within spec.

### EVAP / Canister CEL Defeat

If the EVAP system is removed (race-only), FlashPro suppresses the related codes. **I don't need this.**

### Intake Manifold Runner Control CEL

Stock RBC/RRC intake manifolds have a runner control flap (IMRC). Skunk2 Ultra Street deletes this. The calibrator has a setting to disable the CEL that would otherwise throw after the IM swap.

### Injector Calibration (Slopes / Offsets / Dead Times)

When I swap to Bosch EV14 550cc injectors, I enter their characterization data here:
- Injector flow rate (cc/min at base fuel pressure)
- Dead time at various battery voltages
- Slope correction factors

**[VERIFY]** Most injector manufacturers publish Hondata-ready characterization sheets. I'll ask Bosch or check DeatschWerks/ID documentation for whichever injector I end up with.

---

## 12. What I Leave Alone (Mostly)

Settings I don't touch as a novice — they're either stock-calibrated well, or only matter for forced induction / built engines:

- Knock sensor settings (stock threshold is what I want catching real knock)
- Barometric pressure compensation
- Intake air temp compensation (stock is good)
- Coolant temp fuel/timing compensation
- Startup crank timing
- Closed-loop gain / PID tuning
- Misfire detection thresholds

My tuner may touch some of these during a session. I don't DIY any of them.

---

## Priority of Changes — What to Tune in What Order

When a session starts, this is the order of operations:

1. **Base tables match hardware** (correct injector size, MAP, VTC range)
2. **Closed-loop fuel trims clean up** (cruise AFR hits 14.7 consistently, LTFT ±3%)
3. **Low-cam WOT AFR on target** (verify with wideband)
4. **High-cam WOT AFR on target** (most important — this is peak power territory)
5. **Ignition timing — low cam, WOT** (verify via dyno pulls, knock = 0)
6. **Ignition timing — high cam, WOT** (same)
7. **VTEC crossover adjustment** (based on torque curve from dyno)
8. **VTC cam phase tweaks** (small gains, last to touch)
9. **Idle / drivability polish**
10. **Flex fuel E85 tables** (entire process repeats for E85 endpoint)

---

## See Also

- [overview.md](overview.md) — FlashPro hardware + setup paths
- [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md) — Daily/Sport map rules, safety ceilings
- [datalog-analysis-guide.md](datalog-analysis-guide.md) — how to read the logs that feed these tables
- [advanced-features.md](advanced-features.md) — launch, flat-foot, per-gear, shift lights
- [../19-Flex-Fuel-and-Fuel-System/](../19-Flex-Fuel-and-Fuel-System/) — flex fuel hardware that feeds the E85 tables
- [../11-Wideband-AFR/](../11-Wideband-AFR/) — wideband that validates every AFR change

---

*Last updated: 2026-04-19*
