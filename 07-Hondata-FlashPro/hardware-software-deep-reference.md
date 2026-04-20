# FlashPro Hardware + FlashProManager Software — Deep Reference

> Everything I know about the original Hondata FlashPro unit and FlashProManager (FPM) software, consolidated. This complements the basic [overview.md](overview.md) with the engineering-level detail I'll actually need during install, setup, and tuning.

**Verification note:** The live forums and Hondata docs aren't accessible from this research session, so items flagged **[VERIFY]** are claims from my accumulated K-series/FlashPro knowledge (through Jan 2026) that I want to confirm against Hondata's current support KB or the quick-start card in my box before I bet anything important on them. Everything else is high-confidence.

---

## 1. Hardware — What I Own vs What's Current

### FlashPro Original (mine)

| Field | Value |
|-------|-------|
| PC connection | USB Mini-B |
| ECU connection | Built-in male OBD-II connector on the opposite end of the housing |
| Bluetooth | None |
| Wi-Fi | None |
| Analog inputs | **2** external inputs, each 0-5V DC single-ended |
| Calibration storage | One active calibration at a time (the one currently flashed to the ECU) |
| Datalog storage | Internal flash for a limited-length log, plus unlimited via FPM streaming to PC |
| LEDs | 2-3 status LEDs on top of unit (**[VERIFY]** exact count — Hondata quick-start card has definitive diagram) |
| Side button | Used for datalog start/stop on some revisions (**[VERIFY]** my specific unit's behavior from the box doc) |
| Internal chipset | FTDI USB-to-serial bridge — shows up in Windows Device Manager as "USB Serial Port (COMx)" |

### FlashPro 2 (current retail, NOT mine)

| Difference | Impact for Me |
|-----------|---------------|
| Adds Bluetooth | Enables Hondata Mobile iOS/Android app — **my unit doesn't have this** |
| Different USB connector (**[VERIFY]** USB-C vs Micro-B) | Cable incompatibility if I borrow a FlashPro 2 unit |
| More analog inputs (I believe 4) | For my build, 2 is sufficient (wideband + flex fuel sensor) |
| Newer ECU support (Type R FL5, 11th gen Si) | Not relevant to my K20Z3 |

**Bottom line:** for the FG2 K20Z3, the original FlashPro is **fully supported** and gives me everything I need. FlashPro 2 doesn't add any function I'd use on my car.

### ECU Compatibility — PRB Variants

The K20Z3 in the 06-11 Civic SI ships with PRB-family ECUs. Hondata's FlashPro supports **any PRB ECU for a 06-11 Civic SI** (coupe FG2 or sedan FA5). Sub-revisions (PRB-A00, -A10, -A58, etc.) all work — Hondata doesn't discriminate by sub-variant for the Civic SI application.

**What does NOT work:**
- Non-SI Civic ECUs (SDA for automatic, RNA for base)
- ECUs from JDM FD2 (Japanese-market Civic Type R — different ECU family)
- Any ECU not originally an 06-11 Civic SI PRB

### LEDs and Status Indicators

My best understanding of what the LEDs mean (**[VERIFY with box quick-start]**):

| LED | State | Meaning |
|-----|-------|---------|
| Power/USB | Solid | USB is connected, unit is enumerated on the PC |
| Power/USB | Off | Not connected or driver issue |
| OBD/ECU link | Solid | K-line/ISO communication established with the ECU |
| OBD/ECU link | Blinking | Flash or datalog operation in progress |
| Activity | Blinking | Writing internal datalog |
| Activity | Solid | Actively flashing ECU calibration |

### Recovery from Failed Flash

If a flash gets interrupted (car shuts off, USB unplugged, etc.), the ECU is NOT bricked. FlashProManager detects an incomplete flash on the next connection and offers to resume. **Recovery is software-driven**, not via physical button combinations on the unit.

**The one thing that CAN permanently damage the pairing:** trying to flash with a battery below ~11V. Always flash with engine running or with a battery charger attached maintaining voltage.

### Driver Issues (the #1 Support Issue)

Windows 10/11 sometimes replaces the FTDI VCP driver with a generic Microsoft serial driver after Windows Update. Symptoms:
- FPM fails to see the FlashPro unit
- Unit shows in Device Manager but under different category
- Flash attempts timeout

**Fix:** reinstall the FTDI VCP driver from [ftdichip.com/drivers/vcp-drivers/](https://ftdichip.com/drivers/vcp-drivers/). This is the top item in any FlashPro troubleshooting guide.

---

## 2. FlashProManager (FPM) — Software Deep Dive

### Top-Level Views

| View | Function | Keyboard / Menu |
|------|----------|-----------------|
| **Calibrator** | Edit tunable tables and settings | File → Open Calibration, then Edit menu |
| **Parameter Monitor** | Live gauges from ECU over K-line | View → Parameter Monitor |
| **Datalogger** | Start/stop recording, browse past logs | View → Datalogger |
| **FlashPro Status** | Unit info, firmware version, current paired ECU | View → FlashPro Status |
| **Flash Calibration** | Upload a calibration to the ECU | Tools → Flash Calibration (or equivalent) |
| **Read from ECU** | Download the currently-flashed calibration from ECU | Tools → Read from ECU |

### The Calibrator — Organization

Detailed breakdown in [calibrator-tables-reference.md](calibrator-tables-reference.md). Top-level groups I recall:

- Fuel (main fuel, low-cam vs high-cam, cranking, warmup, after-start, flex fuel tables)
- Ignition (main timing, low-cam vs high-cam, cranking, per-gear trims where available)
- VTEC (engagement RPM, throttle threshold, hysteresis, oil pressure gating)
- Cam Angle / VTC (target phase, low-cam vs high-cam, min ECT)
- Idle (base RPM, A/C idle-up, electrical-load idle-up, IACV calibration)
- Rev Limits (main fuel cut, per-gear, valet)
- Speed Limiter
- Launch Control / Flat-Foot / Two-Step
- Shift Cut / No-Lift-Shift
- Torque Management
- Fans (low-speed / high-speed ON/OFF temps, A/C override)
- A/C (WOT cut, high-RPM cut)
- O2 / Fuel Trims (closed-loop target, trim authority limits, rear O2 enable)
- EVAP (purge valve duty, gating conditions)
- Cranking / Startup
- Analog Inputs / Gauges (wideband voltage→AFR curve, flex fuel freq→% curve, scaling for optional oil pressure / boost / etc.)
- DTC / CEL options (rear O2 defeat, IMRC defeat for Ultra Street, EVAP DTCs)
- Misc / Options

### Parameter Monitor — Live PIDs

The K-line runs at ~10-20 Hz for a typical parameter set. Parameters I recall being available (non-exhaustive, **[VERIFY against current FPM]**):

**Core engine:** RPM, VSS, TPS %, APP % (accelerator pedal), MAP, MAF, IAT, ECT, Calculated Load, Ignition Advance (commanded), Ignition Advance (actual, post-knock-retard), Knock Count, Knock Retard amount, STFT, LTFT, Commanded AFR, Primary O2 narrowband voltage, Rear O2 narrowband voltage, Injector Duty %, Injector Pulse Width (ms), Battery Voltage.

**VTEC/VTC:** VTEC solenoid state (on/off), VTC target (deg), VTC actual (deg).

**Control signals:** IACV duty %, Purge Valve duty %, A/C request, Fan request (low/high), Commanded Throttle, Actual Throttle, Clutch switch, Brake switch, Neutral switch, Closed-loop flag, Open-loop flag, Gear (calculated).

**User analog inputs:** Analog 1 (raw voltage + configurable scaled value — e.g., wideband AFR), Analog 2 (same — e.g., flex fuel %).

### Datalogger Details

- **File format:** `.fpdl` — **binary, proprietary, not publicly documented.** Cannot be parsed by external tools directly.
- **Sample rate:** ~20 Hz typical per parameter (**[VERIFY in FPM settings]**).
- **File size:** 10-minute mixed-drive log with ~30 parameters typically produces ~500KB-2MB.
- **Export to CSV:** **File → Export → CSV** (or Datalog menu → Export — exact location varies by FPM version). Produces a human-readable CSV with a header row of parameter names + units and one row per sample.
- **What's logged by default:** Core engine parameters (RPM, TPS, ECT, IAT, MAP, STFT/LTFT, Knock Count, Knock Retard, Commanded/Actual Timing, VSS).
- **What I must manually enable:** Analog inputs (wideband, flex fuel), VTC actual/target, injector duty, per-cell fuel trim, detailed cam phase.

**Before my first dyno session, I open Datalog → Parameters and check every box I might want data on.** Logging more doesn't cost anything; missing data is expensive.

### Analog Inputs — How They Work

My original FlashPro has 2 analog inputs, each 0-5V DC single-ended referenced to FlashPro ground. Typical use:

**Analog 1 → AEM X-Series Wideband (30-0300)**
- Wire the AEM's "Analog Output 1" wire to FlashPro's analog 1 input
- Common scaling: 0V = 10.0 AFR, 5V = 20.0 AFR (AEM X-Series gasoline default)
- Configure in FPM: Analog Inputs → Analog 1 → Wideband O2 preset (AEM 30-0300)

**Analog 2 → Flex Fuel Sensor**
- The GM/Continental 13577429 sensor outputs a **frequency** signal (50 Hz = 0% ethanol, 150 Hz = 100%), NOT a voltage.
- **[VERIFY — load-bearing for my flex fuel build]:** whether the original FlashPro's analog 2 can directly read frequency, or if it requires:
  - Wiring to the rear O2 signal input pin at the ECU (bypassing the analog input entirely), OR
  - An external frequency-to-voltage converter before feeding analog 2
- FlashPro 2 reads frequency natively. I'm less sure about the original unit. **This is the single most important thing to verify before I commit to flex fuel wiring.**

**Cross-reference:** Both [12-Flex-Fuel-and-Fuel-System/overview.md](../12-Flex-Fuel-and-Fuel-System/overview.md) and [17-Wideband-AFR/overview.md](../17-Wideband-AFR/overview.md) already flag this wiring question. My tuner's answer (or Hondata's flex-fuel setup KB article) is what I trust.

### Calibration Files (`.fpc`)

- **Binary proprietary format.** Cannot be edited outside FPM.
- **Storage:** I can save as many `.fpc` files as I want on my PC. FPM opens one at a time for editing.
- **Unit-side storage:** The FlashPro holds only the **currently-flashed** calibration. To switch tunes (daily ↔ sport), I open FPM and flash the other `.fpc`.
- **Read from ECU:** Tools → Read from ECU downloads whatever is currently flashed to the ECU into a new `.fpc` file. This is how I'd back up my stock calibration before flashing anything else.
- **Diff two calibrations:** FPM has a "compare" feature (**[VERIFY name]**) that shows which cells differ between two `.fpc` files. Essential for understanding what a tuner changed.

### Multi-Calibration Switching (Daily ↔ Sport)

**The original FlashPro cannot switch calibrations without a PC flash.** This is a meaningful limitation for my two-map goal.

Options:
1. **Laptop in car + flash on-demand:** inconvenient but works. Each flash is ~20-45 seconds (**[VERIFY — I initially said 5-6 min but that's more likely the full calibration READ time, not the WRITE]**).
2. **LattePanda in car + permanent FPM install:** what I'm actually building toward. One-tap calibration switching via a Python script that calls FPM's flash operation.
3. **FlashPro 2 upgrade:** supports on-unit calibration switching natively via the mobile app. Would cost ~$700 to upgrade from original. Not worth it for me.

### Flash Time Reality Check

**[VERIFY actual times by stopwatch on my first flash]**:
- Calibration write (flash to ECU): ~20-45 seconds
- Calibration read (download from ECU): ~2-5 minutes (slower)
- Firmware update (FPM → FlashPro unit itself): ~1-3 minutes

The "5-6 minutes" I saw in forum posts is likely a worst-case or older-FPM-version read operation. Real-world flash is fast.

### Export Capabilities

- Calibration → CSV: No direct export of every table to CSV. FPM has a printable/exportable **calibration report** (HTML or PDF, depending on version — **[VERIFY]**) that lists all table values. Useful for sharing with a tuner who doesn't have FPM handy.
- Datalog → CSV: Yes. **File → Export → CSV** (or equivalent).
- Calibration compare → CSV: Possible via the compare feature if it exists.

---

## 3. What's NOT Possible (Important for Setting Expectations)

These things I cannot do with the original FlashPro, and no amount of clever wiring or software will change that:

1. **No public API.** Hondata does not publish an SDK, REST endpoint, or documented IPC interface. Third-party tools cannot read `.fpdl` or write `.fpc` files in a supported way.
2. **No Bluetooth.** Mobile app support is FlashPro 2 only.
3. **No on-unit calibration switching.** Always requires FPM + a flash.
4. **No .fpdl parsing outside FPM.** CSV export is the only way to get data into Python / Excel / another tool.
5. **No command-line flash operations (that I'm aware of).** **[VERIFY]** whether FPM has a documented CLI — last I checked, it didn't.
6. **No odometer adjustment.** K-Pro (a different Hondata product for older Hondas) has more ECU manipulation capability than FlashPro. FlashPro is calibration-focused only.

---

## 4. Ownership Housekeeping

### ECU Re-Registration

If I ever sell the car or swap ECUs, Hondata charges a fee to re-pair my FlashPro to a new ECU. **Commonly cited as $200** (**[VERIFY current price at hondata.com/support]**). One-time per transfer.

### Counterfeits

Counterfeit FlashPro units have been sold on eBay and Facebook Marketplace. Signs of a fake:
- Price significantly below new retail
- Seller won't provide serial number before purchase
- Missing Hondata hologram sticker
- FPM won't enumerate the unit despite driver install

**I bought mine from a legit retailer. Anyone buying used: verify serial with Hondata support before paying.**

### Firmware Updates

FPM auto-updates FlashPro firmware when a new version is available. I do firmware updates with:
- Laptop plugged into stable power (not battery-only)
- FlashPro plugged into USB (not into OBD2)
- No interruption (don't unplug during update)

A failed firmware update is recoverable — FPM detects it on next connection and retries.

---

## 5. Integration Paths for My Build

### Phase 1 Workflow (Laptop-Based)

1. Windows laptop on passenger seat during drives
2. FlashPro plugged into OBD2 + laptop USB
3. FPM running with datalogger armed
4. 7" external screen on dash showing live parameter monitor gauges (via FPM's display-only mode)
5. Post-drive: CSV export for analysis, compare calibrations, plan changes

### Phase 2 Workflow (LattePanda 3 Delta In-Car)

Covered in detail at [Permanent-LattePanda-Install/full-guide.md](Permanent-LattePanda-Install/full-guide.md). High-level:

1. LattePanda permanently mounted with auto-boot on ACC
2. FPM auto-launches on Windows login
3. FlashPro permanently wired via USB Mini-B inside the cabin (no connector exposed)
4. 7" touchscreen on dash = FPM display
5. Arduino GPIO on the LattePanda drives the QTP exhaust valve relay
6. **[ASPIRATIONAL]** Python script watches the datalog folder, auto-exports `.fpdl` → `.csv`, uploads to cloud for Claude to analyze remotely (**[VERIFY if FPM has a CLI or if this requires UI automation — see agent research notes above]**)

### Phase 3 Workflow (Future — Claude Integration)

Covered in [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md). I paste exported CSV datalogs to Claude for analysis, get specific table-cell recommendations back, apply them in FPM manually, flash, verify.

---

## 6. What I'd Do Differently In Hindsight

If I were buying a FlashPro today from scratch:
- **For a daily-driven street car that never leaves the country:** the original FlashPro does everything I need. Stick with it.
- **For track days where I want mobile datalogging:** FlashPro 2 for the Bluetooth → mobile app.
- **For anyone doing only quick tuning without a PC ever in the car:** FlashPro 2.

But my build is primarily a PC-based workflow (the whole LattePanda plan), so the original FlashPro was honestly the right buy.

---

## 7. Action Items Before My First Flash

Everything I need to verify / do before I press Flash for the first time:

- [ ] Confirm FlashPro enumerates in FPM (driver installed correctly)
- [ ] Confirm FlashPro firmware is current (FPM will prompt)
- [ ] **Read stock calibration from ECU** → save as `STOCK_ORIGINAL_20260419.fpc` (the factory reset file)
- [ ] Register the FlashPro with Hondata (ties unit serial to my ECU serial)
- [ ] Pick starting calibration — Hondata community base map for "stock + intake" ([VERIFY correct base map name])
- [ ] Verify battery voltage above 12.5V before flashing (ideally engine running)
- [ ] After flash: verify no CELs, idle reads sane, no knock in first 10 minutes of driving
- [ ] Set up datalog parameters to include everything relevant, not just defaults
- [ ] **Verify analog input wiring works** (wideband reads sensibly at idle) before trusting any datalog

---

## See Also

- [overview.md](overview.md) — hardware overview + setup-path summary
- [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md) — Daily/Sport map rules, reliability-first ceilings
- [calibrator-tables-reference.md](calibrator-tables-reference.md) — every tunable table with safe ranges
- [datalog-analysis-guide.md](datalog-analysis-guide.md) — how to read the logs I'll record
- [advanced-features.md](advanced-features.md) — launch, flat-foot, per-gear, shift lights, torque management
- [troubleshooting-and-faq.md](troubleshooting-and-faq.md) — CEL codes, common issues, Windows driver fixes
- [tuner-directory.md](tuner-directory.md) — shops I'm considering for the three dyno sessions
- [Temporary-Setup/getting-started.md](Temporary-Setup/getting-started.md) — laptop-based first-flash walkthrough
- [Permanent-LattePanda-Install/full-guide.md](Permanent-LattePanda-Install/full-guide.md) — in-car PC build

---

*Last updated: 2026-04-19*
