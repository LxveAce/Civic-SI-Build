# Datalog Analysis Guide — Reading FlashPro Logs Like a Tuner

> How I interpret a datalog after a drive. What to look for first, what patterns mean, what's a red flag vs normal noise. This is the file I open after every session so I'm not wasting tuner time on obvious stuff.

**Reliability-first reminder:** every analysis here assumes the engine is more valuable than any number on a dyno sheet. If something looks wrong, I pull over, investigate, and fix before driving hard again.

---

## What I Log — Standard Parameter Set

These are the parameters I configure FlashProManager to log on every session. Sample rate: highest available (usually ~20 Hz / 50ms intervals).

### Engine Basics
- RPM
- Engine Load (g/rev)
- MAP (kPa)
- TPS (%)
- VSS (vehicle speed)
- Gear (derived from VSS × RPM ratio)

### Fuel
- Short-Term Fuel Trim (STFT, %)
- Long-Term Fuel Trim (LTFT, %)
- Lambda (from stock narrowband O2)
- **Wideband AFR (via analog input, from AEM X-Series)**
- Injector duty cycle (%)
- Injector pulse width (ms)
- Target AFR (what the calibration is asking for)

### Ignition
- Ignition advance (actual, degrees)
- Ignition advance correction (negative = knock retard)
- **Knock count (the watchdog)**
- Knock volts (if logged at fast rate — high-frequency knock sensor data)

### Cam / VTEC
- VTC target (degrees advance commanded)
- VTC actual (degrees advance achieved)
- VTC error (target − actual)
- VTEC solenoid state (on/off, boolean)

### Thermal
- ECT (coolant temperature, °F)
- IAT (intake air temperature, °F)
- Oil temp (if wired — optional analog input)

### Electrical
- Battery voltage
- MIL (Malfunction Indicator Light) status

### Flex Fuel (when installed)
- Ethanol content (%)
- Fuel temperature (°F)

---

## The Analysis Order — What to Check First

When I open a datalog, I go through it in a specific order. Each step either passes (move on) or flags something that needs investigation.

### 1. Knock Count (Safety First — Non-Negotiable)

**First thing I look at. Every time.**

Filter the log for any row where knock count > 0. Then look at what the engine was doing at that moment.

| Pattern | Interpretation | Action |
|---------|---------------|--------|
| 0 knock events across entire log | Healthy, proceed to next check | — |
| Isolated spike during rough road / pothole | Chassis noise false positive | Document + ignore, but flag if it persists |
| Recurring events in specific RPM × load cell | **Real knock** | Pull timing at that cell, investigate fuel quality / sensor health |
| Cluster during WOT pull at high RPM | Aggressive timing | Pull 1-2 deg at affected cells, retest |
| Event during shift | Transient lean, usually torque-management-related | Tune shift cut smoothing, not timing |

**Hard rule:** I never ship a tune with known recurring knock. Period.

### 2. Fuel Trims (STFT and LTFT)

Short-Term Fuel Trim: what the ECU is actively adding/subtracting RIGHT NOW to hit target AFR.
Long-Term Fuel Trim: long-running average bias (what the ECU has learned it needs to add/subtract consistently).

**Healthy ranges at cruise (closed-loop):**
| STFT | LTFT | Meaning |
|------|------|---------|
| ±3% | ±3% | Tune is dialed in for cruise |
| ±5% | ±5% | Minor issue — dirty MAF, slight vacuum leak, injectors slightly off |
| ±10% | ±10% | **Real problem** — vacuum leak, failing sensor, wrong injector data |
| 0 (pegged) | ±15%+ | Closed-loop running out of authority — ECU can't correct, something is significantly wrong |

**Pattern analysis:**

| Pattern | Likely Cause |
|---------|-------------|
| LTFT consistently -5 to -10% (running rich) | MAF reading high, fuel pressure too high, injector dead time wrong |
| LTFT consistently +5 to +10% (running lean) | Vacuum leak, dirty MAF, injector clog, weak fuel pump |
| LTFT shifts from +5 to -5 between logs | Could be ambient temp / altitude — normal within limits |
| LTFT drifts over a single log from 0 to +10% | Fuel pump pressure drop under heat, failing sensor |

### 3. AFR at WOT (Wideband Ground Truth)

The stock narrowband O2 pegs rich outside the stoich range — I can't use it for WOT tuning. The **AEM X-Series wideband** signal coming in on the FlashPro analog input is my real data.

**Comparing logged wideband AFR to calibration target AFR:**

| Delta | Meaning |
|-------|---------|
| Actual = Target ± 0.1 | Tune is locked in |
| Actual > Target + 0.3 (leaner than commanded) | Fuel delivery issue — pump, injectors, pressure |
| Actual < Target − 0.3 (richer than commanded) | Injectors slow to close (dead time wrong), leaky injector, wrong injector constant |
| Actual sawtooths around target | Noisy sensor, wiring issue, or wideband sensor aging |

**Red flag at WOT on pump gas: AFR > 12.5.** That's leaner than any reasonable tune would target. Pull over.

**Red flag at WOT on E85: lambda > 0.85.** Same deal.

### 4. Ignition Advance vs Target

FlashPro logs both "commanded" timing (what the calibration table says) and "actual" timing (after corrections — knock retard, IAT compensation, ECT compensation).

**Healthy:** actual = commanded within ±0.5 deg across most of the log.

**Red flags:**
| Pattern | Meaning |
|---------|---------|
| Actual consistently 2-3 deg below commanded at high RPM WOT | Knock correction active — usually accompanied by knock count > 0 |
| Actual drops sharply during a shift | Torque management active (if not disabled) |
| Actual varies wildly cell-to-cell with no knock | IAT or ECT compensation triggering — check if engine is overheating or intake getting heat-soaked |

### 5. VTC Error (Actuator Health Check)

**VTC error = VTC target − VTC actual**

| Error | Meaning |
|-------|---------|
| ±1 deg sustained | Healthy VTC actuator |
| ±2-3 deg transient during fast transitions | Normal — actuator takes time to hit target |
| ±3+ deg sustained | Failing VTC actuator — **this is the cold-start-rattle actuator problem.** See [15-Ignition-Refresh/](../15-Ignition-Refresh/). |
| Error oscillates at idle | VTC actuator spring is weak — replace before further tuning |
| Error ~0 at idle, grows at high RPM | Oil pressure issue (worn pump, wrong oil viscosity) |

**If I see sustained VTC error > 3 deg anywhere in my log, I stop tuning and replace the actuator (OEM 14310-RBC-003, revised part).** Tuning on a failing VTC is a waste of money because the engine isn't doing what the tune asks.

### 6. Injector Duty Cycle

**Healthy at WOT peak:**
- Stock 310cc injectors at stock power: 50-60% duty
- Stock 310cc injectors on NA full-bolt-on: 75-85% duty (starting to run out of headroom)
- Bosch EV14 550cc on full-bolt-on pump gas: 45-55% duty (comfortable)
- Bosch EV14 550cc on full-bolt-on E85: 60-75% duty (comfortable)

**Red flag: sustained duty cycle > 85%.** Injectors are maxed out. Fuel delivery is about to fall off a cliff and cause a lean spike. Either:
- Upsize injectors immediately, OR
- Verify fuel pressure is within spec, OR
- Reduce target AFR richness until hardware can be upgraded (temporary band-aid)

**Never** try to compensate by raising fuel pressure — that's an E85-world fuel line failure in the making.

### 7. Thermal Behavior

**Healthy ECT:**
- Cruise on highway: 185-195°F
- Cruise in traffic (no A/C): 195-205°F
- WOT pulls: brief rise to 200-210°F, recovers in seconds
- Sustained WOT (dyno pull, canyon run): should not exceed 215°F with fresh Koyorad radiator

**Red flag: ECT > 220°F** — stop driving hard, let it cool, check coolant system.

**Healthy IAT (my K&N Typhoon is hot-side):**
- Cruise at speed: ambient + 15-25°F
- Traffic at idle: ambient + 30-50°F (hot-side intake absorbs heat soak — this is the trade-off I accepted)
- After WOT: drops within 10-20 seconds back to baseline as airflow recovers

**Red flag: sustained IAT > 150°F** — intake has insufficient cooling, heat shield may be inadequate.

### 8. Battery Voltage

Should stay at 13.8-14.4V with the alternator charging. If I see it drop below 13.0V during engine running:
- Alternator failing (common at 170k)
- Loose battery terminal or bad ground
- Overloaded electrical system (rare on NA — becomes relevant with LattePanda installed)

### 9. Flex Fuel Specific (Once Installed)

**Ethanol content sensor readings:**
- Should be stable (±2%) between shifts in fuel source
- Pump gas fills read E0-E15 (ethanol in regular gas)
- "E85" at the pump actually reads E60-E83 depending on season/station
- Winter blend E85 often reads E51-E65

**Red flag: sensor reads 0% or 100% constantly** — sensor failure or wiring issue. ECU should fall back to a safe "assume E0" map, but I'll verify by checking fueling behavior.

---

## Common Datalog Patterns — What They Mean

### Pattern: "Lean spike at 3500 RPM on a light-cruise pull"

Common 8th gen SI complaint. Usually caused by:
- Incorrect VTC phase at that cell (transitional region)
- Torque management timing pull creating airflow change the fuel didn't anticipate
- Stock lean-cruise calibration designed for emissions

**Fix:** tuner adjusts low-cam fuel table at 3500 RPM × medium load. Not a DIY fix.

### Pattern: "Rough idle after Skunk2 Ultra Street install"

Ultra Street has different plenum volume than stock RBC. IACV calibration is off.

**Fix:** tuner recalibrates IACV tables. Some trial and error.

### Pattern: "Engine stutters at exactly 4800 RPM"

Two common causes:
- VTEC engagement hitch (cam transition timing slightly off)
- Knock retard kicking in repeatedly at that cell

**Fix:** check knock count at 4800 RPM first. If knock-driven, pull timing at that cell. If VTEC-transition-driven, adjust VTEC engagement RPM or hysteresis.

### Pattern: "WOT power falls off flat after 7000 RPM"

On a supposedly FBO car, this is usually:
- Injectors hitting duty cycle ceiling
- Fuel pump pressure dropping under load
- Stock intake restriction (if manifold isn't yet upgraded)
- Stock exhaust restriction (if exhaust isn't yet upgraded)
- Cam phase not optimized for top-end

**Fix:** datalog injector duty and fuel pressure. Hardware gap or tune gap.

### Pattern: "STFT/LTFT clean at cruise but lean at part-throttle acceleration"

Tip-in enrichment (transient fuel) is under-calibrated.

**Fix:** tuner dials in tip-in fuel table.

### Pattern: "Knock count spikes at 6200 RPM on a hot day only"

IAT compensation insufficient — timing not being pulled enough when intake temps climb.

**Fix:** IAT compensation table gets more aggressive at high IAT, OR I improve intake cooling (heat shield, true cold-air duct).

---

## What I Share With Claude / My Tuner

### For Claude (CSV export workflow)

From FlashProManager: **File → Export Datalog → CSV**.

The CSV contains one row per sample (~20 Hz), one column per logged parameter. Typical file: 10-minute drive = ~12,000 rows × ~30 columns = ~500KB plain text. Pasteable into chat in chunks, or attachable directly.

When I paste a log to Claude:
- Include the calibration name I was running
- Include what mods were on the car at time of log
- Specify what question I'm asking ("why did I see knock at WOT in 4th?" not "look at this log")
- Include a datalog range of interest if the log is long (e.g., "rows 8500-9200 is the WOT pull")

### For my tuner

The tuner wants the raw `.fpdl` file — he loads it in his own FlashProManager and sees everything native. I email / upload it. He sends back a new calibration `.fpc` file.

---

## Red-Flag Quick Reference (One-Glance Checklist)

After any drive, I scan for these:

- [ ] Knock count = 0 everywhere (no exceptions)
- [ ] Knock retard correction stays above -1 deg (no active pulling)
- [ ] LTFT within ±5% at cruise
- [ ] Wideband AFR at WOT within 0.2 of target
- [ ] Injector duty < 85% at peak
- [ ] ECT < 215°F sustained
- [ ] VTC error < 2 deg sustained
- [ ] Battery voltage > 13.2V running
- [ ] No MIL codes thrown

Any NO above = investigate before the next hard pull.

---

## See Also

- [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md) — safety ceilings these analyses enforce
- [calibrator-tables-reference.md](calibrator-tables-reference.md) — the tables I'd edit based on these findings
- [../docs/baseline-logs.md](../docs/baseline-logs.md) — the log session protocol (pre/post every mod)
- [troubleshooting-and-faq.md](troubleshooting-and-faq.md) — CEL codes and common issues

---

*Last updated: 2026-04-19*
