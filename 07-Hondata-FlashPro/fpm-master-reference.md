# FlashProManager 4.6.6.0 — Master Reference

> **Single source of truth for everything Hondata FlashPro + FlashProManager.** This file is built from Hondata's own official help content (pasted section-by-section from the live help site), cross-referenced with community sources and my own FlashPro install evidence. Future Claude instances should load this before any Hondata conversation.

---

## 0. Navigation Index (Mirrors the Hondata Help TOC)

Jumping-off points organized exactly like the FlashPro Help tree:

**Basics**
- [1. What's New — Version Timeline](#1-whats-new--version-timeline)
- [2. FlashPro Features](#2-flashpro-features-hardware--software)
- [3. Hardware Specifications](#3-hardware-specifications)
- [4. System Requirements](#4-system-requirements)
- [6.6 The FlashPro (variants, LEDs, buttons)](#66-the-flashpro-hardware-unit--captured)

**Installation / Setup**
- [6.5 Introduction (overview workflow)](#65-introduction--captured)
- [6.7 Installation Warnings (injectors, plugs, ground)](#67-installation-warnings--captured-critical)
- [6.47 Security / Vehicle Locking](#647-security-flashpro-anti-theft--captured)

**Calibrations**
- [6.9 Calibrations (New Cal Workflow)](#69-calibrations-new-cal-workflow--captured)
- [6.10 Modifications](#610-modifications-reusable-calibration-snippets--captured)
- [6.11 Quick Modifications](#611-quick-modifications-in-window-shortcuts--captured)

**Programming Your ECU**
- [6.13 Opening a Calibration](#613-opening-a-calibration--captured)
- [6.14 Uploading a Calibration — DUAL-CAL](#614-uploading-a-calibration--captured-game-changer)
- [6.15 Downloading a Calibration](#615-downloading-a-calibration--captured)
- [6.16 ECU Recovery Mode](#616-ecu-recovery-mode--captured)
- [6.17 Maintenance Minder Reset](#617-maintenance-minder-service-light-reset--captured)
- [6.18 Live Tuning](#618-live-tuning--captured-major-feature)
- [6.19 Instant Live Tuning](#619-instant-live-tuning--captured)

**Tuning Your Vehicle**
- [6.20 Overall Process (VTC Engines)](#620-tuning-your-vehicle-overall-process-for-vtc-engines--captured)
- [6.21 Fuel Tuning (MAF vs MAP)](#621-fuel-tuning-maf-vs-map-methods--captured)
- [6.22 Mass Flow Fuel](#622-tuning-mass-flow-afm-fuel--captured)
- [6.23 AFM Flow Calibration](#623-tuning-afm-flow-calibration-procedure--captured)
- [6.24 Speed/Density Fuel](#624-tuning-speeddensity-map-fuel--captured)
- [6.25 Part Throttle Fuel Tuning (MAP)](#625-part-throttle-fuel-tuning-map-no-dyno--captured)
- [6.26 Starting Fuel](#626-tuning-starting-cranking-fuel--captured)
- [6.27 Ignition Tables](#627-tuning-ignition-tables--captured)
- [6.28 VTC Tuning](#628-vtc-tuning-variable-timing-control--captured)
- [6.29 VTEC Point Tuning](#629-vtec-point-tuning--captured)
- [6.30 VTEC Crossover Tuning](#630-vtec-crossover-tuning-hondatas-technique--captured)
- [6.31 AFM Removal](#631-afm-removal-map-conversion--captured)
- [6.32 Table Indexes](#632-table-indexes-re-indexing--captured)
- [6.33 Knock Control Tables](#633-knock-control-tables-advanced--captured)
- [6.34 Individual Cylinder Ignition](#634-individual-cylinder-ignition--captured)
- [6.35 Lambda Correction (AF.Corr)](#635-lambda-correction-afcorr-channel--captured-important)
- [6.36 Rev Hang](#636-rev-hang-reduction--captured)
- [6.37 Cruise Control Lambda Display](#637-cruise-control-lambda-display-hidden-feature--captured)
- [6.38 Active Tuning](#638-active-tuning--captured-potentially-game-changing)
- [6.39 Active Fuel Tuning parameters](#639-active-fuel-tuning-parameters--captured-detailed-config)
- [6.40 Active AFM Tuning](#640-active-afm-tuning--captured)
- [6.41 Multi-tune](#641-multi-tune--captured-not-for-my-platform)

**Datalogging**
- [6.42 Overview](#642-datalogging-overview--captured)
- [6.43 Laptop Datalogging](#643-laptop-datalogging--captured)
- [6.44 On-board Datalogging](#644-on-board-datalogging--captured)
- [6.45 Sensor Setup](#645-sensor-setup--captured)
- [6.46 Graphing](#646-graphing--captured)

**Security**
- [6.47 Overview](#647-security-flashpro-anti-theft--captured)
- [6.48 Owner Information](#648-owner-information--registration--captured)
- [6.49 Security Password](#649-security-password--captured)
- [6.50 Reset Password](#650-reset-password--captured)
- [6.51 Purchasing a Used FlashPro](#651-purchasing-a-used-flashpro--captured)

**Hondata Vault**
- [6.52 Overview](#652-hondata-vault--captured)
- [6.53 Searching Vault](#653-searching-vault--captured)

**Reference**
- [6.54 Shortcut Keys](#654-keyboard-shortcuts-complete-list--captured)
- [6.55 Settings](#655-settings-window--captured)
- [6.56 Main Window](#656-main-window--status-bar--captured)
- [6.57 Options](#657-options-menu--captured)
- [6.58 Table Window](#658-table-window--captured-important--primary-tuning-interface)
- [6.59 Changing Table Indexes](#659-changing-table-indexes--captured)
- [6.60 Proportional Tracing](#660-proportional-tracing--captured)
- [6.61 Changed Value Highlight](#661-changed-value-highlight--captured)
- [6.62 Sensor Overlay](#662-sensor-overlay--captured)

**Calibration Window — Parameters**
- [6.63 Overview](#663-calibration-window--captured-the-parameter-editor)
- [6.64 Calibration Parameters (revision, notes, permissions)](#664-calibration-parameters-revision-notes-gear-ratios-permissions--captured)
- [6.65 Fuel Parameters](#665-fuel-parameters-detailed--captured)
- [6.66 Fuel Pump (HPFP DI only)](#666-fuel-pump-parameters-hpfp--direct-injection--captured)
- [6.67 Ignition Parameters](#667-ignition-parameters-detailed--captured)
- [6.68 VTEC Parameters](#668-vtec-parameters-detailed--captured)
- [6.69 VTC Parameters](#669-vtc-parameters-detailed--captured)
- [6.70 Closed Loop Parameters](#670-closed-loop-parameters--captured-critical-for-wideband)
- [6.71 Knock Control Parameters](#671-knock-control-parameters--captured)
- [6.72 Rev Limit Parameters](#672-rev-limit-parameters-detailed--captured)
- [6.73 Launch Control (Adjustable)](#673-launch-control-adjustable--captured)
- [6.74 Hondata Mode](#674-hondata-mode-sporteco-button--not-my-platform)
- [6.75 Sensor Parameters](#675-sensor-parameters--captured)
- [6.76 Idle Parameters](#676-idle-parameters--captured)
- [6.77 Throttle Parameters](#677-throttle-parameters--captured)
- [6.78 Boost Control](#678-boost-control-parameters--not-my-platform)
- [6.79 Turbocharger](#679-turbocharger-parameters--not-my-platform)
- [6.80 Torque Parameters](#680-torque-parameters--likely-not-applicable-to-my-prb)
- [6.81 Misc Parameters](#681-misc-parameters--captured)
- [6.82 Ethanol Parameters — FLEX FUEL](#682-ethanol-parameters--captured--the-critical-flex-fuel-answer)
- [6.83 Methanol Injection](#683-methanol-injection--captured-not-planned--reference-only)
- [6.84 Traction Control](#684-traction-control--limited-on-my-platform)

**Graph / Display Windows**
- [6.85 Graph Window](#685-graph-window--captured-datalog-analysis)
- [6.86 Datalog Comments](#686-datalog-comments--captured)
- [6.87 Advanced Graphs](#687-advanced-graphs-xy-histogram--captured)
- [6.88 Graph Templates](#688-graph-templates--captured)
- [6.89 Sensor / Display Windows](#689-sensor-window--display-window--captured)
- [6.90 Error Codes Window](#690-error-codes-window--captured)
- [6.91 FlashPro Window (Tabs)](#691-flashpro-window-tabs--captured)
- [6.92 EPA/CARB Restrictions](#692-epacarb-restrictions--captured)
- [6.93 OBDII Diagnostics](#693-obdii-diagnostics-window--captured)
- [6.94 Shortcuts Window](#694-shortcuts-window--captured)
- [6.95 Dealer FlashPro](#695-dealer-flashpro-window--not-my-unit)
- [6.96 G Force Window](#696-g-force-window--captured)

**Commands**
- [6.97 Check For Updates / Check Internet](#697-check-for-updates--check-internet-connection--captured)
- [6.98 Update Boot Firmware](#698-update-boot-firmware--captured-rare-fix)
- [6.99 Compare Calibration](#699-compare-calibration--captured-useful-diff-tool)

**Sensors (Datalog Channels)**
- [6.100 Compatibility Matrix for Civic Si '06](#6100-sensors-complete-k20z3-compatibility--captured)
- [6.101 Per-Sensor Definitions](#6101-sensor-definitions-per-sensor--captured)

**Advanced Reference (Sections 7+)**
- [7. ECU Connectors & Pins](#7-ecu-connectors--pins--captured-critical-for-wiring)
- [8. DDE Server (FPM ↔ Excel integration)](#8-dde-server--fpm--excel-integration--captured)
- [9. Plugins and Scripting (Lua)](#9-plugins-and-scripting-lua--captured-new-automation-path)
- [10. Bluetooth](#10-bluetooth--captured)
- [11. Vehicle-Specific Notes: Civic Si 2006-2011 (MY CAR)](#11-vehicle-specific-notes-civic-si-2006-2011-my-car--captured-definitive)
- [12. Updating Calibrations](#12-updating-calibrations--captured)
- [13. Frequently Asked Questions](#13-frequently-asked-questions--captured)
- [14. Error Reporting](#14-error-reporting--captured)
- [15. Verified vs. To-Verify Summary](#15-verified-vs-to-verify-summary)

**Practical Quick-References**
- [PRB Calibration Window Tree (what I actually see in FPM)](#prb-calibration-window-tree-what-i-actually-see-in-fpm)
- [Pin Allocation Decision for My Build](#pin-allocation-decision-for-my-build)

---

## PRB Calibration Window Tree (What I Actually See in FPM)

From screenshot of FPM's Calibration window with my PRB K20Z3 calibration loaded. This is the navigable tree in the software — each ⊞ expands to reveal parameters and tables. Maps 1:1 to sections 6.64-6.84 below.

```
📋 Calibration
├─ 🔥 Fuel
│  ├─ 📈 WOT lambda adjustment low
│  ├─ 📈 WOT lambda adjustment high
│  ├─ 📊 Cranking fuel
│  ├─ 🎯 Cylinder trim
│  ├─ 🌡️ Air temperature compensation
│  ├─ 🌡️ Coolant temperature
│  ├─ 📈 Active fuel tuning low
│  ├─ 📈 Active fuel tuning high
│  └─ ⚙️ Active Tuning (enable/disable + settings)
├─ ⚡ Ignition
│  ├─ 📈 Ignition low
│  ├─ 📈 Ignition high
│  ├─ 🎯 Cylinder trim
│  ├─ 🌡️ Air temperature compensation
│  └─ 🌡️ Coolant temperature
├─ 🔀 VTEC
│  (no sub-tables — parameters only: rpm window, pressure window, conditions)
├─ ⏱️ VTC
│  ├─ 📈 Cam angle low (low-cam VTC targets, 3D by cam angle)
│  ├─ 📈 Cam angle high (high-cam VTC targets)
│  ├─ 🔢 Cam angle index low (RPM/load breakpoints for low-cam table)
│  └─ 🔢 Cam angle index high (RPM/load breakpoints for high-cam table)
├─ λ  Closed Loop
│  └─ 📈 Lambda (target lambda + related)
├─ 🔔 Knock Control
│  ├─ 📈 Knock ignition limit low
│  ├─ 📈 Knock ignition limit high
│  ├─ 📈 Knock sensitivity low
│  ├─ 📈 Knock sensitivity high
│  ├─ 📈 Knock retard low
│  └─ 📈 Knock retard high
├─ 🚫 Rev Limits
│  (parameters only: overall, launch, speed, boost cut, full throttle shift)
├─ 📡 Sensors
│  └─ 🌀 AFM (air flow meter calibration table)
├─ 💨 Boost Control
│  └─ 📈 Boost control duty lookup (not usable on NA)
├─ 🔁 Idle
│  (idle speed tables + parameters)
├─ 🎛️ Throttle
│  └─ 📈 TPlate Normal (target throttle plate table)
├─ ⚙️ Misc
│  (VSA, EPS, cruise control, fan temps, etc.)
├─ 🎾 Traction Control
│  (if Hondata TC module connected — hardware + software)
└─ 🌽 Ethanol
   └─ 📈 Ethanol ignition compensation
   (+ Ethanol percentage table, fuel multiplier, boost limit)
```

**Key observations:**
- Fuel and Ignition are **mirrored** — same sub-structure for both (low, high, cylinder trim, IAT comp, ECT comp). Learning one teaches the other.
- VTC has **4 tables** (cam angle low, cam angle high, and their separate index tables). The index tables are where I do VTEC crossover optimization per Section 6.30.
- Knock Control has **6 tables** (3 parameters × low/high cam). Deep tuner territory.
- **WOT lambda adjustment has two copies** (low/high). Critical since Hondata ceiling of 12.50:1 applies to BOTH.
- **Active fuel tuning low AND high** — ECU-side auto-tuning works on BOTH cam profiles.
- **Ethanol ignition compensation** lives here — my flex fuel interaction point.

---

## Pin Allocation Decision for My Build

Based on official Hondata ECU Connectors topic + Wideband + Ethanol Parameters docs:

**My 2006-2011 Civic Si (PRB ECU) pinout for aftermarket inputs:**

| Pin | Stock Function | Repurposable For | My Plan |
|-----|----------------|-------------------|---------|
| **A23** | ELD (Electrical Load Detector) | Wideband input | **WIDEBAND (AEM X-Series 30-0300)** ← my wideband goes here |
| **A33** | ECT2 (second coolant temp sensor) | Wideband OR Flex fuel input | **FLEX FUEL (Innovate ECF-1 controller output)** ← flex fuel goes here |
| **B2** | EGR output | Boost control output | Unused (NA) — future turbo prep only |
| **B29** | EGRL (EGR lift input) | Wideband input | Unused — redundant for my needs |
| **C27** | SO2 (Rear O2 sensor input) | **NOT RECOMMENDED** for wideband | Keep stock function (with Berk HFC, rear O2 is valid) |

**Why this allocation:**
- **A23 / ELD for wideband:** Hondata explicitly lists as good wideband input. ELD must be disabled in misc params + factory pin removed from ECU connector.
- **A33 / ECT2 for flex fuel:** Ethanol Parameters topic confirms ECT2 is the K-series flex fuel input path. Must disable ECT2 in misc + remove factory pin.
- **C27 / SO2 left stock:** Section 6.8 says SO2 is NOT recommended for wideband (ECU voltage limiting). I have the Berk HFC so rear O2 stays functional and verifies catalyst efficiency.
- **B2 unused on NA:** saves a pin if I ever go turbo.

**Wiring reality:** this means I need to:
1. Remove the ECT2 pin from the ECU connector → solder flex fuel controller signal to that wire (or new wire going to ECT2 pin location)
2. Remove the ELD pin from the ECU connector → solder AEM wideband analog output signal to that wire
3. Disable ELD AND ECT2 in FPM Misc parameters before flashing
4. Configure the wideband input calibration (0V=10 AFR, 5V=20 AFR for AEM X-Series)
5. Configure the ethanol percentage table (Innovate ECF-1: 0.00V=0%, 5.00V=100%)

**Critical:** disable BEFORE flashing, flash with ELD/ECT2 disabled, THEN do the wiring. Otherwise ECU throws DTCs during boot.

**My install:**
- **FlashPro hardware:** FlashProOG (original, not Mini, not FlashPro 2)
- **FlashProManager version:** 4.6.6.0 (installed from `FlashProManagerV4-6-6-Full.exe` in `C:\Users\extra\Downloads\`)
- **FlashProManager exe:** `C:\Program Files (x86)\FlashPro\FlashProManager.exe` (+ 64-bit variant)
- **Help file (local):** `C:\Program Files (x86)\FlashPro\FlashPro.chm`
- **Config file:** `C:\Users\extra\AppData\Local\Hondata\FlashPro\FlashPro.ini`
- **Calibration directory:** `C:\Users\extra\OneDrive\Documents\FlashPro Calibrations\`
- **Internal FlashPro unit version (per ini):** `FlashPro=461004`

---

## 1. What's New — Version Timeline

Source: https://www.hondata.com/help/flashpro/index.html?whatsnewtopic.htm (fetched 2026-04-19)

| Version | Released | Changes |
|---------|----------|---------|
| **4.6.6** | **2026-04-02** | Firmware updated to v278. Added Spoon Sports 2026 N One 5K7-J11. CANFlex support for 2016-2021 Civic. Extended 2022+ Civic to 64A-X110 Mexico variant. |
| 4.6.5 | 2026-02-26 | Firmware v277. Enhanced 2012-2015 Civic Si boost target/duty params. Fixed ethanol boost limit on FK8/FL5/DE5. |
| 4.6.4 | 2026-02-13 | Firmware v276. Expanded US FL5 engine swap compatibility. |
| 4.6.3 | 2026-01-15 | Firmware v275. FK8 support for 5BF-S13 Singapore ECU. |
| 4.6.2 | 2025-11-26 | FL5 compatibility with 66V-Q04 binary. Fixed cranking on 2014 Civic Si Mexico. |
| 4.6.1 | 2025-11-21 | Fixed no-boost on 2020 Civic MT Japan. |
| 4.6.0 | 2025-10-30 | Firmware v274. Broadened 2019+ RDX support. |

**Key observation for my K20Z3 FG2 build:** the 4.6.x series has been entirely focused on newer platforms (FK8, FL5, 2012+ Civic Si, RDX). **The PRB calibration for 06-11 Civic SI has not changed in any 4.6.x release.** This means my calibration files and community base maps from older FPM versions remain valid on 4.6.6.0 — no migration concerns, no lost features.

---

## 2. FlashPro Features (Hardware + Software)

Source: FlashProManager help, "Features" topic (pasted by user)

### Hardware Features
- Programmable ECU interface
- Connects via OBDII diagnostic port
- **No ECU modification necessary** (exception: Bosch ECUs)
- Fast ECU programming time
- **20 hours on board datalogging memory** (unit stores logs independently of PC)
- **Fast datalogging — 4x faster than OBDII protocols** (uses CAN, not K-line)
- Check and clear diagnostic codes (DTCs)

### Software Features (FlashProManager)
- Custom laptop gauges (on-screen display while connected)
- Readiness codes and smog check status
- Cam angle aware table editing
- **🔑 Dual calibration support** — **THIS IS SIGNIFICANT**

### The Dual Calibration Question (Open)

The earlier reference docs I wrote stated that the original FlashPro stores **one** calibration at a time. Hondata's own help says **"Dual calibration support."** This contradicts what I had written. What "dual calibration" means in FPM context needs verification:

- **Possibility A:** The FlashPro unit holds both a primary AND secondary calibration, and the driver switches between them via some input (a physical button tap, a dashboard toggle wired to an input). If true, this enables **Daily ↔ Sport switching without a PC flash** — a game-changer for my build.
- **Possibility B:** "Dual calibration" means FPM on PC can manage two calibrations (which is trivially true — you can save unlimited .fpcal files on disk).
- **Possibility C:** "Dual calibration" means per-ECU slots (primary + secondary ROM slots in the ECU itself that the FlashPro can flash independently).

**[VERIFY]** with a Hondata official docs page specifically about dual calibrations, or via the "Dual Cal" menu in FPM.

If the answer is Possibility A, my entire Daily/Sport workflow changes — no LattePanda required for on-demand switching. If it's C, the LattePanda still matters.

---

## 3. Hardware Specifications

Source: FlashProManager help, "Specifications" topic (pasted by user)

### Physical — FlashProOG (what I have)
| Spec | Value |
|------|-------|
| Weight | 210g / 7.4oz |
| Storage temperature range | -20 to 85 °C / 0 to 185 °F |
| Operational temperature range | 0 to 70 °C / 30 to 160 °F |
| OBDII cable length | 2m / 6' |

### Physical — FlashProMini (smaller variant, not mine)
| Spec | Value |
|------|-------|
| Weight | 85g |
| Storage temperature range | -20 to 85 °C / 0 to 185 °F |
| Operational temperature range | 0 to 70 °C / 30 to 160 °F |

### Electrical (both variants)
| Spec | Value |
|------|-------|
| Supply voltage | 9-16V |
| Current consumption (active) | < 100 mA |
| Current consumption (standby) | < 10 mA |

### Communication Protocols
- **ISO 15765 CAN** — note this is CAN bus, not K-line. Explains the "4x faster than OBDII" claim.

### Practical Implications
- Operational temp ceiling of 70°C / 160°F = careful about engine-bay placement. The cabin is fine. Under the dash is fine. Not in the engine bay.
- 100mA active current draw is trivial for the car's 12V system. Doesn't load the alternator.
- 10mA standby is low enough that leaving it plugged into OBDII indefinitely won't drain the battery in a reasonable timeframe (weeks), but I'll unplug when parking for extended periods.

---

## 4. System Requirements

Source: FlashProManager help, "Requirements" topic (pasted by user)

### FlashPro Requirements
- Laptop or Desktop
- **Windows 10 or 11 (32 or 64 bit)** — official support
- USB Port (1.1 or 2.0 or 3.0)
- **Internet connection** (for registration, updates, some features)

### Power Management (laptop users)
- **Recommended: disable automatic standby** in Power Options. Standby during a flash = potentially bricked calibration.
- **Not recommended: allow hibernation.** Same reason.

### Implication for LattePanda Install
- LattePanda 3 Delta runs Windows 11 x64 natively — **confirmed compatible.**
- USB 3.0 port on the Panda (for the FlashPro unit) — confirmed.
- I need to disable Windows sleep/hibernation in the LattePanda's Power Options. Critical for reliability.

---

## 5. Help Site Structure (as discovered)

Live Hondata help root: https://www.hondata.com/help/flashpro/

Known working topic URLs (confirmed via WebFetch):
- `https://www.hondata.com/help/flashpro/index.html?whatsnewtopic.htm` — What's New / Changelog
- `https://www.hondata.com/help/flashpro/whatsnewtopic.htm` — Same content, direct topic URL
- `https://www.hondata.com/help/flashpro/introduction.htm` — Introduction overview (confirmed via fetch — includes getting started, calibration creation, reflashing, datalogging)

Known NOT working (returned generic Hondata homepage):
- `https://www.hondata.com/help/flashpro/tuningguidetopic.htm`
- `https://www.hondata.com/help/flashpro/calibrationtopic.htm`
- `https://www.hondata.com/help/flashpro/datalogtopic.htm`
- `https://www.hondata.com/help/flashpro/parameterstopic.htm`
- `https://www.hondata.com/help/flashpro/tocindex.htm`
- `https://www.hondata.com/help/flashpro/helpindex.htm`

This means URL pattern is **not predictable by topic name guessing**. Hondata's CHM-to-web export uses specific filenames that don't match the topic titles in obvious ways. The user feeding content directly (copy-paste from the help page) is the most reliable way to build this reference.

---

## 6. Topics Captured So Far

### 6.1 Features — CAPTURED (see Section 2)
### 6.2 Specifications — CAPTURED (see Section 3)
### 6.3 Requirements — CAPTURED (see Section 4)
### 6.4 What's New / Changelog — CAPTURED (see Section 1)
### 6.5 Introduction — CAPTURED

The Introduction topic confirms workflow sequence:
1. Install software, check for updates, connect USB drivers, complete owner info, register with Hondata
2. Locate OBDII port, insert device, ignition ON (engine off), lock to vehicle
3. Open Calibration window, select ECU type, choose starting calibration matched to mods, save
4. Ignition on / engine off, Upload to flash
5. Datalog with F9, save from menu, open graph windows with templates
6. Refer to Tuning Guide for actual tuning

Known Hondata tutorial videos (require internet): FlashPro Introduction, Getting Started, Race Calibration, Datalogging and Air/Fuel ratios.

---

### 6.6 The FlashPro (Hardware Unit) — CAPTURED

**Physical variants:**

| Variant | Connection to car | USB connector | Bluetooth | Colors available |
|---------|-------------------|---------------|-----------|------------------|
| **FlashProOG** (mine) | OBDII via 2m cable | USB Type B | Yes, if after December 2013 | Race (grey), Dealer (black), CARB (blue) |
| FlashProMini | Directly onto OBDII connector | USB Type C | Yes | Race (grey) only |

**Both are functionally identical** — differences are only size, shape, appearance, connectors. Same software, same features, same ECU support.

**Indicator lights (on the unit itself):**

| LED | Behavior | Meaning |
|-----|----------|---------|
| **Power** | On | FlashPro has power (from USB or OBDII diagnostic connector) |
| | Off | Disconnected or in power saving mode |
| **Program** | On / steady flashing | **RE-FLASHING ECU — do NOT unplug or switch off ignition** |
| **Datalog** | Steady flashing | Datalogging from ECU to onboard memory, or indicating USB activity |
| **USB** | On | FlashPro connected and USB drivers installed correctly |
| | Off | USB not connected OR drivers not installed correctly |

**Physical buttons:**

| Button | Function |
|--------|----------|
| **Program** | Initiates ECU re-programming (flash). **Short press primary calibration**. |
| **Datalog** | Starts/stops datalogging from vehicle |

**Dual calibration button combo** (from "Uploading a Calibration" topic):
- **Primary calibration:** press Program for at least 1 second
- **Secondary calibration:** hold Datalog button down, THEN press Program for at least 1 second, release Program before releasing Datalog

This is on the FlashPro unit itself — no PC connection needed to switch.

---

### 6.7 Installation Warnings — CAPTURED (CRITICAL)

**Hondata's warranty will NOT cover damage from:**
- Low-impedance injectors
- Non-resistor spark plugs
- Incorrect engine ground location

**Injector impedance:**
- Honda ECU designed for **high-impedance ("saturated") injectors**
- Low-impedance ("peak and hold") injectors will damage ECU and/or wiring
- Low-Z can be used with a resistor box, but high-Z strongly preferred
- **For my build:** verify Bosch EV14 550cc are high-impedance (they are — standard saturated EV14 platform). ID1050x are also high-impedance. Safe either way but confirm part-specific spec.

**Spark plugs:**
- **Do NOT use non-resistor plugs** — causes electrical interference that can affect ECU
- **My NGK ILZKR7B-11S and ILFR7H are resistor plugs** (the "R" in ILFR indicates resistor type) — compatible

**Engine Ground (G101) — extremely important:**
- Ground from wiring harness to engine at G101 must make good electrical contact with the cylinder head
- If G101 ground is poor, return path for sensors/ignition/VTEC can flow through OBDII → FlashPro → laptop → laptop charger → inverter → vehicle body
- **This can damage ECU and/or FlashPro**
- **Recommended ground location:** stud on cylinder head (best electrical connection)
- **Acceptable alternative:** top bolt holding radiator water output to cylinder head
- **Stock location on intake manifold:** usually works but inferior to cylinder head

**For my 170k K20Z3:** I need to inspect G101 condition during the next engine work. A corroded G101 ground at this mileage is plausible. Cleaning or relocating to the cylinder head stud is cheap insurance.

**Software versions:**
- **Do NOT roll back or backdate FPM versions**
- FlashPro firmware gets updated by newer FPM — older FPM trying to access newer-firmware FlashPro may malfunction

**Reflashed ECUs:**
- If ECU has been reflashed by anyone other than Hondata (uprev, Ktuner, etc.), **do NOT use FlashPro until ECU is reflashed back to stock by the original company**
- Most aftermarket reflashers corrupt ECU flash memory in a way that prevents future reflashing
- **My ECU:** confirmed as stock (Factory Flash backup = original OEM calibration). Safe.

---

### 6.8 Wideband Lambda Interface — CAPTURED (CRITICAL for Phase 6 + 17-Wideband-AFR)

**This contradicts my earlier reference docs that said "Analog Input 1" of the FlashPro unit.** The wideband actually wires into unused **ECU** input pins (not FlashPro analog inputs). The ECU's K-series pinout has several available inputs:

**Available ECU inputs for wideband (with caveats):**

| ECU Input | Viability | Notes |
|-----------|-----------|-------|
| **SO2** (secondary O2 / rear O2) | **NOT RECOMMENDED** | ECU internally limits voltage; accurate wideband reading not possible. Also conflicts with flex fuel sensor if using this pin. |
| **EGRL** (EGR lift) | OK | Requires adding an ECU pin and wire |
| **ECT2** (second water temp sensor) | OK | Second ECT must be disabled; factory pin must be removed from ECU connector |
| **ELD** (electrical load detector) | OK | ELD must be disabled; factory pin must be removed from ECU connector |

**See:** ECU Connectors topic (not yet captured) for pin locations.

**Grounding — critical to avoid ground loops:**
- Wideband meter MUST use same ground as ECU for BOTH power AND analog output
- **For K-series: G101 on the intake manifold is the correct ground point**
- Do NOT ground the ECU or wideband to any other points
- Do NOT share wideband ground wire with any other devices

**Settings in FPM:**
- Wideband input settings under: **Closed loop parameters**
- Select which analog input pin (from the 4 options above)
- Voltage offset can be configured — **but if you need a voltage offset you have a ground problem that should be fixed, not compensated**
- Voltage-to-lambda translation: typically 0V = 10.0 AFR, 5V = 20.0 AFR (linear). If wideband has more than 2 voltage/lambda pairs, it may be non-linear and cannot be used.

**Wideband-specific output specs (from Hondata help):**

| Brand | Output spec |
|-------|-------------|
| **PLX** | 0V = 10:1, 5V = 20:1 (standard) |
| **AEM** (later models) | 0V = 10:1, 5V = 20:1 (earlier AEMs had different outputs — check manual) |
| **Innovate** | Program to "standard" 0V=10:1, 5V=20:1 via their programming software/cable |

**For my AEM X-Series 30-0300:** It's the "later AEM" spec = 0V=10:1, 5V=20:1. No reprogramming needed.

**Implications for [17-Wideband-AFR/overview.md](../17-Wideband-AFR/overview.md):**
- That doc said "FlashPro analog input 1" — **wrong**. Needs updating.
- The ECU pin to use depends on what I'm doing with flex fuel. ECT2 or ELD are the best candidates for my build. EGRL requires adding a pin/wire.
- Both wideband AND flex fuel sensor need ECU input pins. I need to plan which pin each gets.

---

### 6.9 Calibrations (New Cal Workflow) — CAPTURED

**About:**
- A calibration contains all settings and table values that can be changed in the ECU
- Normal extension: `.fpcal` (CONFIRMED — was wrong in earlier docs that said `.fpc`)

**New calibration workflow:**
1. File → New Calibration
2. Verify correct vehicle model and type. If FlashPro plugged in, defaults to correct; otherwise uses last-used vehicle
3. Double-click calibration name to select and close window
4. Calibrations marked:
   - **Stock equivalent** = same as what car shipped with
   - **Tuned** = calibration is tuned for best performance from that part combination
5. For some vehicles, a **New Calibration Wizard** is available — select mod combo + fuel octane → wizard picks best calibration

**For me:** When creating a new calibration for my car, I'd pick one that matches my current installed mods. Starting point likely "stock equivalent + K&N Typhoon intake" since that's my current hardware state.

---

### 6.10 Modifications (Reusable Calibration Snippets) — CAPTURED

**What a Modification is:**
- A **subset** of a calibration — reusable across compatible calibrations
- Example: a custom throttle mapping table that can be imported into any calibration without touching the rest of the cal
- Installed/removed via Modifications window

**How to use:**
- File menu → Modifications, or toolbar button
- Click checkbox or double-click modification to install/remove
- Warning: a mod may change several parameters at once, so installing one may cause another to show as "installed" too. Some mods can appear installed even on a stock cal. This is normal.

**Creating a mod (to share or archive my own):**
- In Modifications window: Export button
- Set Category, Author, Revision, Description, Notes
- Select the specific Parameters (P) and Tables (T) to include
- Export creates the mod file
- Update button: refreshes an existing mod file
- **Storage location:** `C:\Program Files (x86)\FlashPro` (Modifications directory)
- Windows won't allow saving directly there from an app — must save to different dir then copy via Explorer

**Usefulness for my build:**
- If a tuner gives me a "modification file" for (e.g.) flex fuel tables, I can layer it onto my base calibration
- If I make useful changes (e.g., my custom fan tables), I can export them as a mod for future reuse
- Don't need to keep re-doing the same changes across every new base cal

---

### 6.11 Quick Modifications (In-Window Shortcuts) — CAPTURED

- Quick Modifications are mods accessible directly from the Calibration window
- Example: drop-down for different intake AFM calibrations
- When regular mods are added/removed, the Quick Modification drop-down updates to match
- If an underlying table is edited, the drop-down either switches to a different modification or shows blank (if no mod matches)

Practical: a fast way to swap between "stock airbox" / "short ram" / "cold air intake" calibrations without hunting through Modifications window.

---

### 6.12 Programming Your ECU — CAPTURED

**Key stats (correcting my earlier estimate of 20-45 seconds):**
- **Actual flash time: approximately 90 seconds**
- **Do NOT interrupt the flash** — unplugging cable or cancelling upload puts ECU in recovery mode
- Interrupted flash = ECU won't run engine, but CAN still be re-programmed with FlashPro (see 6.15 Recovery Mode)

**For my workflow:** 90 seconds is still fast enough that Daily ↔ Sport switching via re-flash is viable (if I didn't want to use the on-unit dual cal feature). But dual calibration + button switching is faster still.

---

### 6.13 Opening a Calibration — CAPTURED

- Before programming the ECU, open a calibration (New, or from file)
- Calibrations from older FPM versions OR non-calibration files: FPM shows error
- Implication: if a tuner sends me an old `.fpcal`, FPM may refuse to load it until they resend from a current version

---

### 6.14 Uploading a Calibration — CAPTURED (**GAME CHANGER**)

This is the dual calibration mechanism. It's not PC-dependent at runtime.

**Uploading from PC to ECU (standard workflow):**
1. Load calibration in FlashProManager
2. Plug FlashPro into PC via USB
3. Plug FlashPro into OBDII, switch on ignition
4. Select Upload from Online menu

**Uploading from FlashPro to ECU (using stored calibration, NO PC needed):**
1. Plug FlashPro into OBDII, switch on ignition
2. **Primary calibration:** press Program button for at least 1 second
3. **Secondary calibration:** hold Datalog button down, press Program for at least 1 second, release Program before Datalog

**Storing calibrations on the FlashPro unit:**
1. Load calibration in FPM
2. Plug FlashPro into PC via USB
3. Open FlashPro window → Calibrations tab → Upload
4. Choose primary or secondary slot

**Prerequisites:**
- FlashPro must be locked to your vehicle
- FlashPro must be registered with Hondata

### 🔑 THE DAILY/SPORT WORKFLOW I NOW WANT

1. Build a Daily calibration, upload to **primary slot** on FlashPro
2. Build a Sport calibration, upload to **secondary slot** on FlashPro
3. In the car:
   - Want daily quiet? Ignition on, press Program 1 sec, wait ~90 sec, start car.
   - Want sport loud? Ignition on, hold Datalog + press Program 1 sec, wait ~90 sec, start car.
4. **No PC required for the switch.** Previously I assumed I'd need the LattePanda permanently connected. Now: the LattePanda is still valuable for datalogging + exhaust valve control, but **calibration switching works without it**.

This changes the game for Phase 7 planning. The LattePanda becomes more about monitoring + logging + valve relay, less about "flash button replacement."

---

### 6.15 Downloading a Calibration — CAPTURED

- The last uploaded calibration is stored on the FlashPro
- Download via: Online menu → Download
- Once downloaded, the cal can be edited, saved, or re-uploaded

Useful when:
- I don't have the `.fpcal` file locally but want to pull back what's on the unit
- Someone else has flashed the car and I need to know what's running

---

### 6.16 ECU Recovery Mode — CAPTURED

**What triggers it:** interrupted flash (power loss, cable unplug, cancel).

**What it is:** ECU won't run engine, but CAN still be re-programmed.

**How to recognize:** FPM status bar shows exclamation icon.

**Recovery procedure:**
1. Upload a calibration to the ECU (can be the same as before)
2. **Switch ignition OFF then back ON** (important step!)
3. Verify ECU icon changes to indicate normal mode

**Implication:** Failed flash is NOT a brick. Always recoverable. Reduces flash-day anxiety significantly.

---

### 6.17 Maintenance Minder (Service Light Reset) — CAPTURED

When switching between AFM and race calibrations, the service maintenance reminder can illuminate the dash wrench light and display "service A" or "service B" with negative miles.

**Reset procedure:**
1. Ignition ON, do NOT start engine
2. Hold **SEL/RESET** button for 10 seconds until display starts flashing
3. Release SEL/RESET
4. Hold it down AGAIN for 6 seconds — display clears

**For me:** Worth knowing before/after any race calibration flash.

---

### 6.18 Live Tuning — CAPTURED (MAJOR FEATURE)

**What it is:** Real-time table updates in the ECU while the engine is running. Changes take effect immediately — no re-flash needed.

**Recommended:** Only use Live Tuning while actively tuning the vehicle. **Disable for regular driving.**

**How it works:**
- FPM alters the ECU so it copies table data from flash memory to RAM on reset
- Table edits in FPM get sent to ECU RAM live
- ECU tables update in fractions of a second

**Limitations:**
- FlashPro + laptop MUST be connected to vehicle for changes to take effect
- Not all calibration tables support live tuning (depends on how ECU accesses them internally)
- Only a subset of live-tuning tables can be active simultaneously (RAM limit)
  - Non-VTC engines (e.g., S2000): all live-tuning tables can be used at once
  - **VTC engines (my K20Z3):** 2-3 "major" tables (fuel low cam, fuel high cam, ignition low cam) + many supporting tables (injector latency, etc.)
- **If ignition cycles off/on:** live tuning tables reset to "last calibration upload" values — NOT to stock. FPM detects key-off-key-on if connected and re-uploads live changes.

**Workflow:**
1. Select tables to live-tune (via table window OR Online menu → Select Live Tuning Tables)
2. Upload calibration to ECU
3. Edit/tune tables in real-time
4. When done: de-select live tuning, upload calibration again to bake in changes

**Icons shown next to tables that support Live Tuning:**
- Live Tuning not enabled
- Live Tuning enabled, pending upload
- Live Tuning active

**Practical for my dyno sessions:** this is how tuners iterate fast — make a cell change, see it immediately on the dyno run, no re-flash. Saves hours.

---

### 6.19 Instant Live Tuning — CAPTURED

**What it is:** Live Tuning without the initial upload step.

**Difference from regular Live Tuning:** you don't need to upload a calibration before starting — edits apply directly.

**Same limitations apply:**
- Needs FlashPro + laptop connected
- Not all tables supported
- RAM limit on simultaneous tables
- Ignition cycle resets live values (but FPM re-uploads on key-off-key-on if connected)

**Workflow:**
1. Click the live-tuning icon next to a parameter/table, OR use Select Live Tuning Tables window
2. Edit — takes effect immediately
3. When done: de-select live tuning, upload calibration to bake changes permanent

---

### 6.20 Tuning Your Vehicle (Overall Process for VTC Engines) — CAPTURED

**Dyno tuning principle:** Maintain consistency between runs. Start each run with same coolant temp + intake air temp. Maintain same time interval between runs.

**Tuning a VTC engine (my K20Z3 IS a VTC engine — this procedure applies directly):**

The K20Z3 has 5 copies of each major table, one per cam angle. Standard sets:
- **Angles: 0, 10, 20, 30, 40** OR **0, 15, 30, 40, 50 degrees**

**Step-by-step procedure (Hondata official):**

1. **Start with low cam.** Force ECU into low cam by setting VTEC point HIGH. Only dyno to above expected VTEC point (6500 RPM typically enough). **Do NOT run over 7000 RPM on low-speed cam** — lost motion assemblies can float, damaging spring retainers. Big warning for me.

2. **Lock cam to a single angle.** Find what angles my calibration uses. Starting at first cam angle (e.g., 0°), set the low-speed cam angle table to that value.

3. **Tune fuel for this cam angle** until measured AFR is acceptable.

4. **Tune ignition for this cam angle.** Default ignition settings are usually close to optimum.

5. **Copy fuel and ignition tables** from the tuned cam angle to the next — next cam angle starts tuned.

6. **Lock to next cam angle, repeat.** All 5 angles.

7. **Once all cam angles tuned for fuel + ignition**, tune VTC to generate composite cam angle table.

8. **Switch to high cam.** Set VTEC point LOW. Start each dyno run just past VTEC point, continue to redline. Repeat steps 2-7 for high-speed cam.

9. **Tune the VTEC point**, then the VTEC crossover VTC.

10. **(MAP calibrations only)** Tune part-throttle fuel.

**Advanced tips from Hondata:**
- **More productive to first tune the cam angle where engine makes most power** (usually 30°). Tune 30° fuel+ignition, copy to tables above AND below, then tune remaining tables. Faster than sequential.
- **VTEC smoothing:** Advance VTC cam angle just BEFORE VTEC point so the jump to high cam needs less VTC rotation. See 6.30 VTEC Crossover Tuning below.
- **For fuel tables, edit by selecting ROWS.** Ensures part-throttle fuel is adjusted based on full-load lambda readings — less part-throttle tuning needed later.
- **Forced induction:** start by tuning on minimum boost. Wastegate or bypass held open lets you tune atmospheric columns first, then boost columns. **Never disconnect intercooler pipes — overspeed risk.**

**Implication for my build:** the Sport tune build procedure is exactly this 10-step process executed on a dyno. The tuner handles it. My job is to provide a clean engine, wideband data, and a healthy fuel system.

---

### 6.21 Fuel Tuning (MAF vs MAP Methods) — CAPTURED

**Two calculation methods:**

| Method | Based On | Has VE Tables? |
|--------|----------|----------------|
| **Mass flow (AFM / MAF)** | Air flow meter reading | No — simple mass ratio |
| **Speed/density (MAP)** | Manifold pressure + volumetric efficiency tables | Yes |

**For tuning, a lambda meter is required.**

**Civic Si stock oxygen sensor:**
- **Semi-wideband type** (not narrowband)
- **Range: 10.7:1 to 20:1** (that's a usable range)
- **Reads progressively richer as exhaust gas temperatures increase**
- **Useful for:** partial throttle and naturally aspirated tuning (my K20Z3 at my target power levels)
- **For forced induction:** aftermarket wideband recommended

**For my NA build:** I can partly rely on the stock o2 for baseline tuning, but **AEM X-Series wideband is still the right call** for dyno-session ground truth and E85 verification where richer mixtures matter. Also: AF.Corr (Section 6.35 below) is Hondata's software-corrected channel that partially fixes the rich-reading bias.

---

### 6.22 Tuning Mass Flow (AFM) Fuel — CAPTURED

**⚠️ Hondata's own warning (matches my reliability-first rule):**

> "A lean air/fuel condition will damage the engine. Make sure that you monitor the air/fuel ratio at all times, and abort any dyno run if the air/fuel ratio becomes too lean."

**Mass flow tuning basics:**
- AFM measures mass of air into engine
- Fuel = ratio of fuel to air (no VE tables)
- **Critical: AFM must read incoming air accurately** — aftermarket intakes usually alter AFM readings
- AFM auto-compensates for headers, exhaust, cams, but NOT for intake standing waves / reversion (common with race headers + large cams)

**Low load fuel (part throttle / closed loop):**
- ECU uses AFM reading directly
- No VE adjustment
- If closed-loop fuel isn't at stoich, the AFM is reading wrong — usually from aftermarket intake
- AFM can be re-calibrated (Tuning AFM Flow — Section 6.23)

**High load fuel (WOT / open loop):**
- ECU uses additional enrichment table ON TOP OF AFM-based calculation
- Table name: **WOT compensation table**

**🔴 CRITICAL WARNING FROM HONDATA:**

> "Values in the WOT compensation tables should only be changed within certain limits. The ECU will not switch into open loop correctly if the WOT compensation table values are raised so that less fuel would be required in open loop than closed loop. Generally values should not be increased over the stock values to prevent this from occurring. **As a guide, do not set the WOT air/fuel ratio above 12.50:1.**"

**This directly matches the reliability-first rule I wrote into [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md).** Hondata's own official ceiling is 12.50:1 AFR at WOT. My doc says ≥12.0 — I can tighten to 12.2-12.5 and still be within Hondata's sanctioned range. Never lean past 12.50 per Hondata. Never.

---

### 6.23 Tuning AFM Flow (Calibration Procedure) — CAPTURED

**Prerequisites:**
- Stock injectors
- Stock AFM flow values
- Stock WOT compensation values

**Procedure:**
1. Warm car to normal operating temp
2. Datalog 5-10 minutes of varied driving
3. In FPM → XY Graph (from Advanced Graphs):
   - X-axis: `AFM.v`
   - Y-axis: `S.TRIM`
   - Check 'Show mean', check 'Closed loop', uncheck 'Open loop'
4. Result: graph of AFM reading vs fuel trim
5. Identify trends — alter AFM voltage-to-flow calibration accordingly
6. Example: ECU trims 2-3% from 1.7V to 2.8V? Increase flow numbers on AFM Flow table by 2.5% in that range
7. **Only make 2-3 changes per iteration**
8. Save, upload, re-test until fuel trims are within 1%

**Example:** "AFM is reading approx 15% low, first tuning change would be to increase AFM flow numbers by 15%, across whole table, then re-test."

**For my build:** My K&N Typhoon intake definitely shifts AFM readings. If I'm on an AFM-based calibration, this is the process the tuner will run. If I'm on a MAP-based calibration (see 6.24 and 6.31), the AFM is irrelevant.

---

### 6.24 Tuning Speed/Density (MAP) Fuel — CAPTURED

**⚠️ Same lean warning as mass flow.**

**Method:**
- MAP sensor measures manifold pressure
- **Volumetric efficiency (VE) lookup tables** indexed by engine speed → mass of air in cylinder
- Additional compensations: coolant temp, battery voltage, intake air temp
- Tune by editing VE tables

**Fuel table structure:**
- Typical indices: RPM (bottom axis) × Intake manifold pressure (side axis)
- 3D shape (because K20Z3 has 5 cam angle slices)
- Interpolation between cells

**Fuel table used for BOTH:**
- Part throttle / low load / closed loop — tune to stoich (~14.7:1)
- Full throttle / high load / open loop — tune to safe AFR for max power (≤12.50:1 per Hondata)

**For my build:** if my calibration is MAP-based (more common for aggressive tunes), VE tables are where the main tuning work happens. See 6.25 for part-throttle dyno-less procedure.

---

### 6.25 Part Throttle Fuel Tuning (MAP, No Dyno) — CAPTURED

**Scope:** speed/density (MAP) calibrations only. AFM calibrations skip this.

**Requirements:** quiet, flat, straight road, can accelerate 10→30-40 mph repeatedly.

**Preparation:**
- Open calibration, display low-speed cam fuel tables (F5)
- Identify cam angles (0, 10, 20, 30, 40 OR 0, 15, 30, 40, 50)
- Lock cam to FIRST angle by setting low-speed cam angle table to that value
- Save calibration as DIFFERENT filename (will restore original cam angles later)
- No need to switch o2 off — software reads fuel trims + actual lambda

**Datalogging drive:**
- Start datalog + recording (F9)
- Accelerate in 1st gear, LIGHT throttle to 5000 RPM — keep throttle steady so load column stays consistent (columns 3-4)
- Shift to 2nd, slow to ~1000 RPM
- Repeat in 2nd gear with very light throttle
- Repeat 2nd gear several more times, slightly MORE throttle each time (higher columns)
- Repeats same column OK
- **RPM range:** first + last RPM rows have incorrect lambda (tip-in / release effects). Log from 1000 RPM to VTEC+1000. Typical: 1000-6000 RPM.

**Lambda Overlay display:**
- Load the datalog
- Select low-speed cam fuel table (F5)
- Select 'Fuel Change' (Shift-F3) → shows suggested fuel change

**Edit fuel tables:**
- Aim: suggested fuel change → close to zero
- Zero everywhere isn't practical (temp variations, etc.) — get close
- **Hondata Heatshield intake manifold gasket helps** by keeping IM temps stable
- Before editing: verify correct cam angle selected, uncheck 'All' so changes don't apply to other tables
- **Look for PATTERNS of changes** rather than cell-by-cell — table must stay smooth after
- Example: select whole column 6, add 5% fuel. Then column 7, add 5%. Then 2750-8500 RPM in columns 1-5, add 2%. Etc.
- After changes: view 2D to verify load lines remain smooth and equally spaced. If not, undo and apply fewer changes to larger areas.

**Iterate:**
- Upload, re-test
- Repeat for same cam angle until fuel changes near zero — typically 3-4 cycles per cam angle
- Move to next cam angle, repeat

**Finish:**
- Load original calibration
- Copy cam angles out
- Load tuned calibration
- Paste cam angles back

**For my build:** this is a genuine DIY option for part-throttle tuning if I want to contribute to my own tune between dyno sessions. Requires a MAP calibration. Good practice for understanding the tables. But I'm not doing WOT tuning without a dyno — that's where a tuner + wideband is non-negotiable.

---

### 6.26 Tuning Starting (Cranking) Fuel — CAPTURED

**The starting process:**
1. Engine cranked → large injector pulse (fuel sticks to cold intake walls)
2. Pulse calculated from: cranking fuel table × overall fuel trim × cranking fuel trim × air temp compensation × water temp compensation
3. Fixed ignition timing while cranking (typically 5° or 7° BTDC)
4. As engine cranks, fuel reduced as wall deposits reach equilibrium
5. When engine speed hits 600 RPM, ECU says "engine started"
6. Last closed-loop start-term fuel trim applied to main table fuel
7. **First 10-30 seconds:** injector pulse is BLEND of cranking fuel + main fuel tables, progressively shifting to main

**Troubleshooting:**

| Symptom | Check |
|---------|-------|
| Hard start | Min battery V during cranking (should be ~10.5V, not below 9.2V) |
| | Cranking RPM (should be >150 cold, ~200 hot) |
| Hard cold start | Needs more cranking fuel |
| Hard hot start | Too much cranking fuel OR fuel vapor lock |
| Fires then idles rough for seconds | Needs more cranking fuel |

**Adjustment process:**
- If unclear rich/lean, START by adding fuel
- Increase in 10% increments, up to 30%
- Datalog each start
- Look for: lowest cranking time + quickest fast-idle time
- If adding fuel makes it worse, try subtracting in -10% decrements to -30%

**⚠️ Critical testing rule:** CANNOT start cold, shut off, adjust, and restart. Running engine even briefly changes:
- Intake valve temperature (fuel atomizes differently)
- Fuel deposits on intake walls

**Must leave engine several hours, preferably overnight, between tests.**

**Two adjustment locations:**
- **Cranking fuel trim** — if engine is hard to start at all temps except hot
- **Cranking water temp compensation** — if only hard to start at one temperature range

Formula if adjusting water temp compensation:
`new trim = old trim + ((100 + old trim) × (change% / 100))`

Example: add 10% more cranking fuel at 50°: change trim from -70.0% to -67.0%.

**Cranking Wall Deposits (ADVANCED — only for experienced tuners):**
- Two table groups, each with SEQ and BATCH versions:
  1. **Direct ratio** — fraction of injected fuel reaching cylinder. Higher = less injector duration needed.
  2. **Wall deposit** — fraction of fuel sucked from wall into cylinder. Higher = less injector duration needed.
- ECU fires injectors in BATCH for ~2 revolutions during start, then switches to SEQUENTIAL
- Different wall-deposit rates for batch vs sequential → two tables per parameter

**For my E85 switch (future):**
- E85 needs MORE cranking fuel (~30% more) than gasoline, especially cold
- The cranking fuel trim is what I'd adjust
- Below 40°F ambient on straight E85: expect rough cranking even well-tuned
- Winter-blend E85 (lower ethanol %) helps significantly

---

### 6.27 Tuning Ignition Tables — CAPTURED

**⚠️ Hondata's explicit warning:**

> "Excessive ignition advance will damage the engine. The combustion pressure and load on the engine (especially bearing stress) increase dramatically if the engine is over-advanced. **Do not believe the fallacy that 'more is better' for ignition advance.** Too little ignition advance can also damage the engine by increasing the exhaust gas temperature, especially with turbo-charged engines. **Do not rely on the knock sensor to retard the ignition timing if the engine detonates.**"

**Ignition Advance at Full Load (WOT):**
- Best method: dyno
- **For naturally aspirated engines (my case):** safe to set advance NEAR max power. Aim: run the LEAST amount of timing possible.
- **Procedure:** tune for max power, then RETARD timing until losing ~1 HP. Run just-shy-of-max timing.
- Monitor knock at all times (even for NA)
- Abort dyno run if pinging audible or ECU shows knock

**Ignition Advance at Part Throttle:**
- Harder to determine optimally
- **Default calibrations are suitable for part throttle** — usually don't need touching
- EGT gauge can be used for fine-tuning

**Idle ignition:**
- ECU uses ignition to control idle speed
- **Normal to see -10° to +15° during idle** (actively varying)
- Not a static value — dynamic stabilization

**Honda Knock Control:**
- Only offers LONG-term adjustment of estimated fuel octane
- Does NOT use dynamic ignition timing control (unlike newer vehicles)
- **Knock sensitivity reduced in starting calibrations** so knock control doesn't interfere with tuning
- Cannot rely on knock control to save the engine — it's a slow learner

**For my 170k K20Z3:** this reinforces my reliability-first stance. Run less timing than max-safe as a buffer against the slow-learning Honda knock control. Don't chase the last degree.

---

### 6.28 VTC Tuning (Variable Timing Control) — CAPTURED

**What VTC is:**
- "iVTEC" = VTEC + VTC combined
- VTC: variable intake camshaft advance (0-50 crank degrees, continuous — NOT an on/off like VTEC)
- 5 copies of each major table per cam angle = effectively 3D tables
- Cam phase is positioned by electro-hydraulic mechanism with feedback

**Mechanical limits:**
- Range: 0-45° or 0-50° depending on calibration type
- **Physical stop limits cam advance** (prevents valve-to-valve and valve-to-piston contact)
- **⚠️ Aftermarket cams: up to manufacturer to ensure safe positioning.** Software limits don't guarantee mechanical safety.
- Delay between ECU setting and actual cam rotation: **~0.1 seconds per 10 degrees**

**Tuning guidelines — by application:**

**Naturally aspirated (my build):**
- Cam advance to MAX just after VTEC engagement until ~6500-7000 RPM
- From 7000 RPM to redline: retard back to ~25° (cam near 50° at 7000)
- True for all current aftermarket cams
- Unusual cams may need different settings

**Supercharged:**
- Max (50°) throughout rev range
- Only 10° or so retard above 7000 RPM

**Turbocharged:**
- Less cam than stock
- More back pressure = more cam retard needed
- Small turbos + stock cats: retard fully to 0° at 8000 RPM
- Log-style manifold: high VTEC point, low VTC angles
- Long equal-length runners: lower VTEC point, higher VTC angles (closer to NA)

**Procedure:**
1. Set VTEC point high (6500-7000). Only dyno low-speed cam.
2. Tune fuel + ignition at each cam angle.
3. Dyno each cam angle → 6 dyno curves.
4. Set composite cam angle map to angles giving max power at each RPM.
5. **Bracket the composite map:** +5° re-dyno, -5° re-dyno. Verify optimum.
6. Fine-bracket: ±2° for 1-1.5 HP resolution on NA (small gains).
7. Set VTEC point low (3000), repeat above for high-speed cam.

**Cam Angle at VTEC:**
- If cam needs to rotate a LOT at VTEC (e.g., 20° low-cam to 45° high-cam), you lose 500-700 RPM after VTEC as cam physically rotates
- **Solution: start advancing intake cam in low-cam table BEFORE VTEC point.** Sacrifice a few HP pre-VTEC to gain HP post-VTEC. Done right, reduces the characteristic VTEC sound change.
- See 6.30 VTEC Crossover Tuning for the Hondata-developed technique

**Part-throttle cam angle:**
Below full NA load (column 7 and less):
- Idle and below 1000 RPM: 0° or 5°
- Cruising (columns 2-7, 1500-4500 RPM): 15-30°
- Above normal cruise RPM: same value as under full load (smooths gearshifts — cam doesn't retract to zero during shifts)

**Hints:**
- Cam can't rotate instantly (0.1 sec per 10°). Don't make large cam changes over small RPM intervals.
- **Intake cam is LOCKED at 0° for 10 seconds after hot start.** Let engine run 10+ seconds before any dyno run.

**VTC Cleaning:**
- **Normal behavior:** ECU briefly fully advances cam on overrun to clean VTC mechanism
- Triggers: a few times from cold start, ~5 seconds after throttle release at 2000-3000 RPM
- Shows in datalog as small spikes to 45° or 50°
- **Not a failure — expected behavior.** Don't report VTC cleaning spikes as VTC error.

---

### 6.29 VTEC Point Tuning — CAPTURED

**⚠️ Critical Hondata warnings (hard limits):**

> "Do not set the VTEC point too low as the engine will lose oil pressure and possibly damage the engine. **It is not recommended to set the VTEC point below 2000 rpm.**"

> "Do not set the VTEC point too high as the high speed cam rocker arm may float on the lost motion assembly, damaging the valve spring retainers. **It is not recommended to set the VTEC point over 6500 rpm.**"

**This updates my earlier floor of 4500 RPM:**
- **Hondata's absolute floor: 2000 RPM** (oil pressure limit)
- **Hondata's absolute ceiling: 6500 RPM** (rocker arm float limit)

For my reliability-first approach, staying in the middle of this range (say 4500-5800) is conservative. But Hondata's envelope is wider than I had documented.

**Typical VTEC points:**
- **Stock engine:** 5500-5700 RPM
- **Intake + exhaust:** 4500-4800 RPM
- **Supercharged:** 3000-3200 RPM
- **Aftermarket cams:** generally HIGH VTEC point

**My build plan:**
- Daily map: 5400-5600 (near stock)
- Sport map (FBO pump): 4800-5200
- Sport map (FBO E85): 4800-5000

All within Hondata's 2000-6500 envelope. None too aggressive.

**Determining optimal VTEC point:**
- Two dyno runs: one with VTEC low (3000), one with VTEC high (6500)
- Set VTEC point at intersection of low-cam and high-cam torque curves
- **Sudden power increase after VTEC switch** → LOWER VTEC point
- **Sudden torque dip after VTEC** → RAISE VTEC point
- Small dip at the intersection is normal

**VTEC Window (RPM + Pressure gating):**
- Stops VTEC from engaging at light/medium throttle (fuel economy + driveability)
- Uses BOTH RPM and manifold pressure

**Setting VTEC window:**
1. Determine optimum VTEC point (procedure above)
2. Lower RPM of window = VTEC point
3. Upper RPM of window = 6000-6500 RPM
4. Pressure at lower RPM = 80 kPa (NA) or 110-120 kPa (forced induction)
5. Pressure at upper RPM = 40 kPa
6. Smooth pressure transition

**Forced induction:**
- Lower pressure values: 120-150 kPa at lower RPM, decreasing to 70-80 kPa at upper RPM

**Small dip at VTEC (<5 lbs torque) is normal.** If bigger, try bumping VTEC point up in 100 RPM increments.

---

### 6.30 VTEC Crossover Tuning (Hondata's Technique) — CAPTURED

**What it is:** The optimal VTEC transition method developed by Hondata for K-series engines. Not used in factory Honda maps. Perfected for 06-09 K20 Civics (my platform).

**The problem this solves:**
- Optimum low-cam angle at VTEC point ≠ optimum high-cam angle at VTEC point
- They're often 20-35° apart
- Cam can only rotate 10°/0.1 sec → ~0.3 seconds to rotate 30° at VTEC
- During rotation: engine makes sub-optimal power = "VTEC dip"

**Hondata's three-part technique:**

1. **Advance cam into high-cam VTC angle BEFORE VTEC switch**
2. **Alter RPM indices to make transition as quick as possible**
3. **Keep cam angle constant across high-cam RPM rows**

**Example numbers from Hondata docs:**
- VTEC point: 4350 RPM
- Low cam optimum at 4350: 12° cam angle
- High cam optimum at 4350: 37° cam angle
- Cam needs to rotate 25° → takes 0.25 seconds

**Low-cam VTC table optimization:**
- Above VTEC point (5000-7000), resolution not needed
- Right-click RPM row → edit RPM indices
- Create 3 fine-resolution points around VTEC:
  - 150 RPM below VTEC point
  - 50 RPM below VTEC point
  - 50 RPM above VTEC point
- For 4350 VTEC: 4200, 4300, 4400 indices
- Reduce highest RPM breakpoint from 8100 to 7000
- Set cam angle at HIGHER RPM row to match high-cam angle at same RPM (37° in example)
- Effect: low cam stays at optimum until 4200 RPM (150 below VTEC), rotates rapidly to 37° over a tiny RPM/time interval

**High-cam VTC table optimization:**
- Delete VTC rows below 4000 RPM (engine should never be on high cam below this)
- Add resolution in 6500-10000 RPM range (where cam rotates rapidly)
- Keep cam angle ADVANCED across RPM rows
- Why: stops cam from retarding to zero during gearshifts → keeps car "on power" longer after shift

**Datalog verification:**
- VTC transition from 26° low cam to 50° high cam in ~0.3 seconds
- CAM CMD = target from tables
- CAM = measured cam angle

**For my build:** this is the exact technique my tuner should use for the Sport map VTEC transition. Named drop this to my tuner if they don't already know it. Massive gains in VTEC-transition smoothness and area-under-the-curve.

---

### 6.31 AFM Removal (MAP Conversion) — CAPTURED

**Context:** When using MAP-based calibration, AFM is no longer used for airflow measurement BUT the ECU still needs the air temp sensor in the AFM housing.

**Options:**
1. Leave AFM in place (keeps temp sensor, keeps restriction)
2. Replace AFM with a standalone IAT sensor (removes restriction, relocates sensor)

**Compatible IAT sensors:**
- **OBDI vehicles (1992-2001 Civic/Integra)** — 2-bolt flange, good for FI
- **RSX IAT sensor** — barbed press-in

**Connector:** from harness of same vehicle, need 2-wire plug (not single-wire)

**Wiring:**
- Splice into AFM connector wires (red/yellow and green/black, both at one end of connector)
- Polarity not important
- Insulate, reinstall wire shield
- **Only have IAT OR AFM plugged in, never both** — ECU won't read air temp correctly if both present
- Cover AFM plug to prevent dirt/water if removed

**Sensor placement:**
- NA: anywhere in intake tube
- Turbo: AFTER intercooler (near throttle or in IM)
- Supercharged: AFTER supercharger

**Verification:** before starting, ignition on + datalog to verify sensor reads correct temp.

**No calibration changes needed** — just ensure MAP-based cal.

**For my build:** only relevant if I ever delete my K&N Typhoon and go to a tube-only intake with the AFM eliminated. Not in current plan. Keeping K&N = AFM stays in circuit.

---

### 6.32 Table Indexes (Re-indexing) — CAPTURED

- Tables can be re-indexed for more resolution in specific areas (e.g., around VTEC point per 6.30) OR to expand RPM range
- **Warning:** When index is altered, all tables sharing that index must update too
- For some calibrations, can't alter index if every instance of that index isn't identified
- Detailed procedure: see "changing table indexes" topic (not yet captured)

---

### 6.33 Knock Control Tables (Advanced) — CAPTURED

**⚠️ Warning from Hondata: only for experienced tuners.**

**How Honda's knock control works:**
- Designed for different-quality fuels in a STOCK engine
- Factory tunes engine dyno using automated process:
  1. High-octane fuel → find MBT (mean best torque) ignition timing
  2. 100 RON fuel → find knock ignition limit (max advance before knock likely)
  3. 90 RON fuel → find low-octane knock limit

**Ignition calculation:**
- Normal ignition tables contain MBT values
- Additional table: knock ignition limit values
- If knock limit < MBT: ECU uses lower value (no knock, less power)
- **Key insight:** ECU may run less timing than ignition tables show at certain cells, even with no sensor-detected knock. Doesn't show as "knock retard" — it's considered a "no knock" condition.

**Knock Control Variable (K.Control):**
- Adjusted by ECU from knock sensor noise + knock sensitivity
- Nominal value: estimated fuel octane as % between 100 and 90 RON
- 0% = fuel is 100+ octane
- 25% = fuel is 97.5 octane
- 50% = fuel is 95 octane
- Updated SLOWLY while driving

**If K.Control > 0% AND max timing < MBT:**
- Difference shows as knock retard value

**Ignition formula:**
```
Ignition advance = min(MBT, MBT + knock_ignition_limit - (knock_retard × knock_control))
```

**Knock Tables:**

| Table | What it contains |
|-------|------------------|
| **Knock Ignition Limit** | Max advance before knock likely. **Relative to MBT ignition table.** Positive = higher than MBT. Negative = lower than MBT. |
| **Knock Air Limit** | Cylinder filling limit (mg) based on knock retard. Can be increased without affecting K.Control. Makes boost more consistent. |
| **Knock Sensitivity** | Noise threshold before ECU calls it knock. Low value = more sensitive. |
| **Knock Retard** | Amount of retard (degrees) between high-octane and low-octane limits. Actual retard = table × knock control (e.g., K.Control 50% = half the retard). Only applied if knock limit < MBT. |

**Tuning recommendations (Hondata official):**
- **Main ignition tables:** decrease timing at RPM/load points where knock ignition limit is negative. Helps factory knock control work better.
- **Knock ignition limit:** use LOW values where knock is likely. For forced induction on pump fuel, columns 9-10 should be 5° or less, boost columns zero. ALWAYS adjust main ignition if increasing knock ignition limit values.
- **Knock sensitivity:** INCREASE sensitivity (reduce values) in columns 4+. For noisy cams/headers, reduce sensitivity (increase values).
- **Knock retard:** use SMALLER retard than stock (4-10°). Lower columns (6 and below) will barely affect knock retard (knock ignition limit much higher than MBT there).
- **Knock control:** starts high after flash, comes down slowly as engine runs normal cycles. To decrease on dyno: steady-RPM hold, as long as no pinging, K.Control gradually drops.

**For my build:** these knock tables are deep-tuner territory. I won't touch directly. What I MUST ensure: my tuner understands that **the factory knock control is slow** and won't save the engine from a marginal tune. The ignition tables themselves need to be safe, with the knock system as a secondary safety net.

---

### 6.34 Individual Cylinder Ignition — CAPTURED

**When you'd use it:** unequal cylinder filling (e.g., intake manifold geometry gives more filling to cylinders 2-3 than 1-4 on a Jackson Racing supercharged setup).

**Result of unequal filling:** some cylinders make more cylinder pressure → more knock tendency. Adjusting per-cylinder ignition trim evens the knock count across cylinders.

**Procedure (from Hondata docs):**
1. Baseline test with no cylinder trim, full-load datalog
2. Observe knock count per cylinder
3. Advance timing 3° on all cylinders as a stress test (ONLY for illustration — not a recommendation)
4. Observe which cylinders knock → identify which cylinders are at risk
5. Adjust per-cylinder trim to equalize knock counts
6. Reduce all cylinders by 1° final for reliability buffer

**Alternative method:** use EGT per cylinder (accepted normal method).

**For my NA build:** unlikely to need this unless I develop a specific per-cylinder issue. Skunk2 Ultra Street manifold + Skunk2 Alpha header are well-matched and shouldn't have major imbalance. Worth knowing exists.

---

### 6.35 Lambda Correction (AF.Corr Channel) — CAPTURED (IMPORTANT)

**The problem:** The Civic Si stock oxygen sensor is semi-wideband, BUT it does NOT read accurately richer than lambda 0.88 (13:1 AF).
- Reads over 1 AFR point different with rich mixtures
- Error is CONSTANT (no exhaust gas temp or time effect)

**Hondata's solution:**
- Measured the difference between stock o2 and a true wideband on a dyno
- Created a correction table
- New datalog channel: **`AF.Corr`** (Lambda Corrected)
- Corrected channel reads very close to aftermarket wideband
- **Mixtures leaner than lambda 0.95 (14:1) are NOT corrected** (to preserve closed-loop behavior)

**Disclaimer from Hondata:** results may vary. They recommend dyno tuning (especially for forced induction). But corrected AF will always be LEANER than stock o2 reading — safer to use corrected than raw.

**For my build:**
- Use `AF.Corr` in datalogs instead of raw stock o2
- AEM X-Series wideband remains the ground-truth for WOT tuning
- Stock o2 + AF.Corr is adequate for part-throttle closed-loop verification

---

### 6.36 Rev Hang Reduction — CAPTURED

**What rev hang is:** Engine speed doesn't fall immediately when shifting (manual trans only). Some vehicles have it, some don't.

**Two settings to adjust:**

**1. Overrun throttle:**
- Parameter → Throttle → **Overrun throttle opening enabled** (uncheck)
- Shuts throttle plate quicker on pedal release
- **Note for 2016+ 1.5T Civic:** enabling main cruise control button reverts to stock behavior

**2. Overrun Fuel Cut Delay:**
- Parameter → Fuel → **Overrun fuel cut delay values**
- Table indexed by gear
- **Suggested values: 20-50 ms**
- Shuts injectors off quicker when throttle closes

**Caveat:** if vehicle isn't well-tuned, excessive closed-loop fuel trims give similar symptoms to rev hang. Fix tune first.

**For my build:** I've planned this in my existing [advanced-features.md](advanced-features.md). Daily map = mild reduction (still clean emissions), Sport map = aggressive (sharper response). Tuner dials in during Tune #1 or #2.

---

### 6.37 Cruise Control Lambda Display (Hidden Feature) — CAPTURED

**What it is:** Use cruise control Set button to show current lambda on the tachometer.

**Display format:** AFR × 1000 offset by 10000.
- 14.7:1 AFR = 4700 RPM shown on tach
- 13.2:1 AFR = 3200 RPM shown on tach

**Conditions:**
- Cruise control MAIN switch OFF
- Clutch NOT depressed

**Supported vehicles:**
- **All Civic Si** ✅ (mine qualifies)
- FK8
- 2023 Integra

**For my build:** free backup gauge for lambda monitoring when the LattePanda isn't booted or if I ever want an OEM-dash lambda readout without extra hardware. Worth trying after first flash just to confirm it works on my PRB. Zero cost feature.

---

### 6.38 Active Tuning — CAPTURED (POTENTIALLY GAME-CHANGING)

**What it is:** ECU adjusts tables in real-time AS YOU DRIVE. **No laptop or FlashPro plugged in required** after enabling.

**Tunable tables via active tuning:**
- Fuel tables
- Air flow meter (AFM) tables

**How it works:** ECU uses target lambda tables + wideband o2 reading to alter values in a fuel-table adjustment table. Continuous, repetitive. Over time, fuel tables become tuned to engine needs.

**Example from Hondata:**
- Baseline fuel trim: some spread
- After 5 minutes of active tuning: reduced spread
- After 15 minutes: further reduced

**For my build:** this is massive. If I can enable active tuning, drive a lot, and let the ECU self-tune... I may not need 3 separate dyno sessions. BUT:
- Active tuning requires a WIDEBAND wired in (not available with stock sensor)
- Still need baseline calibrations matched to hardware
- Not a substitute for a professional dyno tune on final hardware
- But: excellent for between-hardware-changes refinement

**Relationship to reliability-first:** active tuning targets LAMBDA (AFR). It doesn't advance timing past dyno-set values. Safe for the engine. Good tool in my box.

---

### 6.39 Active Fuel Tuning Parameters — CAPTURED (DETAILED CONFIG)

**Enable:** Active fuel tuning → check the Enabled option.

**Options (when tuning operates and what target):**

| Option | Purpose |
|--------|---------|
| **Closed loop** | Active in closed loop |
| **Open loop** | Active in open loop |
| **Use fuel trims** | In closed loop, uses current trims to better determine underlying fuel table values |
| **Target Lambda** | Which lambda to target. In closed loop: use ECU's calculated target (AFMCD). In open loop: can use target lambda table for finer control. |

**Settings (how tuning works):**

| Setting | Description |
|---------|-------------|
| **Delay after engine start** | O2 warmup + after-start-fueling settle time |
| **Delay after injector re-start** | After overrun/TPS-out/cam-out events, o2 needs time |
| **Change per tuning cycle** | Adjustment magnitude. Default 2%. Larger = faster but rougher. |
| **Delay in lambda reading** | Compensates for lag between engine lambda and sensor reading. 150-250ms typical. Measure by noting lag after injector re-start. |
| **Update frequency** | Active fuel update delay. 25-200ms typical. |
| **Maximum change** | Max adjustment from original fuel table |
| **Active fuel smoothing** | Limits max delta between adjacent cells. Prevents jagged adjustment tables. |
| **Maximum deltas (cam, load, RPM)** | How far actual values can be from table indices before tuning applies. If cell too far from actual, no update. |

**Conditions (when active):** minimum and maximum for various parameters. Tuning only between all min/max pairs.

**Workflow:**
1. Enable in calibration, upload to ECU
2. Drive for some time period
3. Optional: merge active table into main fuel table via menu operation

**Notes:**
- Target lambda tables ≠ WOT compensation tables (different purpose)
- Live tuning for active tuning table must be enabled (default on)
- Main fuel tables do NOT need live tuning
- **Active tuning resets if battery disconnected**

---

### 6.40 Active AFM Tuning — CAPTURED

**Similar to Active Fuel Tuning but for the AFM (mass flow meter) table.**

**Same options, similar settings:** Closed loop / Open loop / Use fuel trims / Target Lambda / Delays / Change per cycle / Maximum change / Conditions.

**Key difference:** tunes AFM flow table → fuel trims should reduce over time (ECU learns airflow better).

**Update Active Tuning Table button:** downloads AFT table from ECU into current calibration. **Must save calibration after uploading + keep it open or reopen before downloading AFT.**

**Workflow:**
1. Enable in calibration, upload to ECU
2. Save calibration after upload
3. Drive for some time
4. Optional: update active tuning table button → merges changes to main tables

**For my build:** if I'm on an AFM calibration, this auto-calibrates my AFM to my K&N Typhoon's actual airflow. Could run this for a few weeks of daily driving after my next flash and get very accurate AFM baseline for free.

---

### 6.41 Multi-tune — CAPTURED (NOT FOR MY PLATFORM)

**Multi-tune = in-ECU switchable tune slots via cruise control buttons.**

**Supported vehicles:**
- 2017-2021 Civic Si
- 2022+ Civic Si
- FK8 2018-2021 Civic Type R
- FL5 2023+ Civic Type R
- DE5 2024+ Integra Type S

**⚠️ My 2009 Civic Si (PRB K20Z3) is NOT supported.** Multi-tune is a newer-platform feature.

**How it works on supported cars:**
- Cruise control MAIN off for several seconds
- Hold cruise control RESUME button
- Tachometer shows selected tune: 1000 RPM = #1, 5000 RPM = #5
- Change via cruise SET and RESUME buttons
- Exit: press CANCEL or wait several seconds

**Persistence:** tune number retained on key-off, NOT on battery disconnect or ECU reflash.

**Tables that can vary by tune:** traction control target slip, launch slip, boost by gear.

**For my build:** doesn't apply. My Daily/Sport switching uses the **Dual Calibration** feature (Section 6.14) — primary/secondary on the FlashPro unit, switch via button combo on the unit.

**Key distinction:**
- **Multi-tune:** newer platforms, 5 slots, in-ECU, cruise control button switching, NO re-flash needed
- **Dual Calibration:** all FlashPro platforms including mine, 2 slots on FlashPro unit, button-combo switching, 90-second re-flash each switch

Dual Cal is still great for my build. Multi-tune would have been even better but isn't available.

---

### 6.42 Datalogging Overview — CAPTURED

**Two methods:**
1. **To laptop via USB** (real-time)
2. **On-board datalogging** to internal memory (20 hours+)

**File format:** `.fpdl` (extension confirmed — associated with FlashProManager by default).

**If association broken:** Settings dialog → check "Associate calibration and datalog files with FlashProManager".

**About Datalogs:**
- FPM uses **frames** — snapshot of all sensor values at one point in time
- All sensors datalogged per frame
- Some sensors not datalogged if engine not running
- Number of frames + total length shown below menu bar

**Autosave:** datalogs can auto-save when recording finishes. See datalog autosave settings (not yet captured).

---

### 6.43 Laptop Datalogging — CAPTURED

**Basic datalogging (not recording):**
1. FlashPro → vehicle OBDII
2. Laptop → FlashPro via USB
3. Ignition on / engine start
4. Press **F10**, or Datalog menu → Datalog, or click Datalog icon

FPM displays sensor values, error codes, table tracing in real time. **Values NOT saved** during basic datalogging — just monitored.

**Recording (actually saving):**
- Press **F9**, or Datalog menu → Record, or click Record icon
- Saves to disk

**My standard workflow:** always record. F10 then F9.

---

### 6.44 On-board Datalogging — CAPTURED

**Process:**
1. FlashPro → vehicle OBDII
2. Ignition on / engine start
3. Press **Datalog button on the FlashPro unit**
4. Datalog light indicates recording

**Downloading to FPM:**
1. FlashPro → computer (USB)
2. Open FlashPro window (Window menu or toolbar)
3. Select datalog → right-click or click download button
4. **Recommended: save to computer after download**

**Datalogging Rates:**

| Mode | Max recording time |
|------|-------------------|
| **Fast** | ~7.5 hours |
| **Slow** | ~21 hours |

**For my build:** the on-board feature is clutch for track days or long drives where I don't want the laptop in the car. Rotate: enable "Fast" mode before a spirited drive or dyno session. Use "Slow" for long commute monitoring.

---

### 6.45 Sensor Setup — CAPTURED

**Configure sensor display in the Sensors window:**

| Field | Purpose |
|-------|---------|
| **Abbreviation** | Name in Sensors window |
| **Display Name** | Name in printouts |
| **Description** | Function explainer |
| **Type** | Sensor data type |
| **Unit** | Display unit |
| **Display Min / Max** | Graph range, default in display window |
| **Warning Min / Max** | Sensor values turn green-to-red when outside range |

**Import / Export:** sensor configurations can be saved and loaded across computers.

**For my build:** I'd set warning ranges for critical parameters — e.g., knock count warning at anything > 0. ECT warning at > 215°F. IAT warning at > 150°F. Injector duty warning at > 85%. Easy visual alerts during drives.

---

### 6.46 Graphing — CAPTURED

**Open Graph window:** click Graph button in toolbar (after loading a datalog or selecting from Datalog menu).

**Graph window:**
- Plots sensors via graph templates
- Clicking in the Graph Window updates: Sensor Window, Display Window, Error Codes Window

**See:** Graph Window and Graph Templates topics for deeper reference (not captured yet).

---

### 6.47 Security (FlashPro Anti-Theft) — CAPTURED

**Two security levels:**

1. **Owner Information password protection**
   - Prevents owner info/registration from being altered without the password

2. **Calibration upload password**
   - Option to require password for any upload to FlashPro
   - Prevents FlashPro from being used without password
   - Also prevents FlashPro from being unlocked from current vehicle

**Vehicle security (built in):**
- Immobilizer CANNOT be disabled via FlashPro (prevents theft facilitation)
- FlashPro can only be locked to a vehicle that doesn't have a FlashPro already locked to it

**If stolen:** contact Hondata with FlashPro serial number.

**For my build:** I'll set a security password once the FlashPro is in the car (Phase 7 LattePanda era) so a thief can't use my FlashPro for their purposes.

---

### 6.48 Owner Information & Registration — CAPTURED

**Required for:** product registration with Hondata, warranty, update notices, recall notifications.

**Path:** FlashPro window → Registered Owner tab → enter owner details.

**If security password set:** owner info only modifiable with password.

**Critical:** email address must be correct (used to retrieve lost security password).

**Privacy (Hondata's stated policy):**
- Only registration-relevant info transmitted
- Encrypted before transmission
- Info NOT retained by Hondata after registration

**Update registration:** possible if contact details change.

---

### 6.49 Security Password — CAPTURED

**Set password path:** Online → Set Security Password.

**Requirements:** FlashPro connected to computer (USB). No vehicle connection needed.

**Entry states:**
- **Entering first password:** Leave "Current Password" empty. Enter new password twice.
- **Changing password:** Enter current password, then new password twice.
- **Removing password:** Enter current password, leave new password blank. Unlocking FlashPro from vehicle also clears.

**Upload security option:**
- Check "Require security password when uploading" = password requested at every upload
- **Warning:** this option effectively prevents FlashPro from being used on a different vehicle (can't unlock without password)

**If forgotten:** resettable via registered email or phone.

---

### 6.50 Reset Password — CAPTURED

**Process (needs internet):**
1. FlashPro window → Registered Owner tab → Reset Security Password
2. Choose email OR phone (SMS) for reset code
3. Enter 5-digit reset code
4. Leave new password blank (removes password) OR set new password

---

### 6.51 Purchasing a Used FlashPro — CAPTURED

**Before buying used, verify:**
1. Install FlashProManager
2. Plug in FlashPro
3. Open FlashPro window, select FlashPro tab
4. Click License and Security to expand tree
5. Verify:
   - **VIN is unlocked**
   - **Security Password NOT set**

**If not unlocked / password set:** current owner MUST unlock / reset before you can use it.

**For my build:** not relevant since I bought new, but important reference if I ever buy a second unit.

---

### 6.52 Hondata Vault — CAPTURED

**What it is:** cloud storage for calibrations + datalogs, accessible directly from Hondata software.

**Features:**
- Transfer cals between computers
- Backup if computer lost/damaged
- Public repository (add cals for other Hondata users)
- Search by keywords or tuning parameters

**For my build:** I should set this up for redundant backup of stock and any tuned calibrations. Better than relying solely on OneDrive.

---

### 6.53 Searching Vault — CAPTURED

**Access:** Window menu.

**Two search types:**
- **Text Search:** any word in any calibration field (e.g., "Stock" returns cals with stock injectors, stock intake, etc.)
- **Filtered Search:** matches all criteria (e.g., Engine="B18C5" returns only B18C5 cals)

**Results:** list, double-click to download. Sort by clicking column heading (arrow shows current sort).

---

### 6.54 Keyboard Shortcuts (Complete List) — CAPTURED

**Table Editing:**

| Shortcut | Action |
|----------|--------|
| Shift + arrow keys | Select table cells |
| Ctrl + A | Select whole table |
| Ctrl + C | Copy selection |
| Ctrl + V | Paste selection |
| **Ctrl + I** | **Increase selection** (by user-defined step) |
| **Ctrl + D** | **Decrease selection** |
| **Ctrl + J** | **Open Adjust window** |
| **Ctrl + P** | **Interpolate selection** |
| **Ctrl + M** | **Smooth selection** |
| Ctrl + Z | Undo |
| Shift + Ctrl + Z | Redo |

**Graph Viewing (cursor movement):**

| Shortcut | Movement |
|----------|----------|
| Shift + Left / Right arrow | ±10 seconds |
| Left / Right arrow | ±1 second |
| Ctrl + Left / Right arrow | ±0.1 second |
| Shift + Ctrl + Left / Right arrow | ±0.01 second |

**From ini file (function keys):**
- F3 = low-cam ignition, F4 = high-cam ignition
- F5 = low-cam fuel, F6 = high-cam fuel
- F7 = low-cam VTC, F8 = high-cam VTC
- F9 = Record (start datalog recording)
- F10 = Datalog (live monitoring)

---

### 6.55 Settings Window — CAPTURED

**Tabs available:**
- General Settings
- Unit Settings
- Display Settings
- Lambda Overlay Settings
- Sensor Overlay Settings
- Datalog Settings
- Autotune Settings

**Import/Export:** buttons allow transferring settings between computers.

#### General Settings
- **Windows Themes:** XP+ theming on/off. Windows screen scaling enabled = clearer on high-DPI.
- **File Association:** check to associate `.fpcal` and `.fpdl` with FPM. Double-click-to-open.
- **Compress datalog files:** reduces .fpdl size.
- **Automatic check for new version:** checks on first run per day. Update from Help menu if available.
- **Include beta software versions:** I have this ENABLED in my ini. Toggle OFF for max stability.
- **Miscellaneous:** Display message after upload / Show Mod Window / Play Sound (success 2-tone, failure chime) / Send notification / Disable screen saver (GOOD — enabled in my ini) / Calibration load use last vehicle / use FlashPro vehicle
- **USB Driver Check:** balloon hint from status bar if driver problem.

#### Unit Settings
- Vacuum & Pressure units (absolute vs atmospheric reference)
- Temperature units
- Lambda Unit (lambda vs AFR)

**My ini shows:** TempUnit=0 (Fahrenheit likely), LambdaUnit=1 (lambda).

#### Display Settings
- **Main Table Tracing:** shows which cells are active in real-time during datalog. 4 cells shaded by interpolation proportion if enabled. Axis trace indicator shows ECU reading values.
- **Autosize table grid:** expands cells to fit window (good on laptops).
- **Parameter Table Tracing:** same for parameter-window lookup tables.
- **Changed Value Highlight:** table window shows edited values in color (default: green=decreased, red=increased). Reset on save/load.
- **Sensor List:** "Show sensor warnings" changes display window color when sensor outside limits.

#### Lambda Overlay Settings
Overlay of datalogged lambda values on fuel tables.
- **Target Lambda:** used for fuel change calculation (not an ECU table — changing doesn't affect ECU).
- **Overlay Lambda Input:** choose wideband / corrected stock o2 / uncorrected stock o2. Recommendation: uncorrected stock for closed loop, corrected or wideband for open loop.
- **Options:**
  - In closed loop apply fuel trims (more accurate fuel adjustment)
  - Calculate for each cam angle (VTC vehicles only)
  - Transition delay (time after throttle hits minimum before lambda shown — o2 needs time to recover from overrun)
  - Maximum interpolation (distance limit between table cell and actual engine state — filters out "too far" values)
  - Min/max throttle boundaries
  - Min/max gear
  - Min/max cam angle
  - Min/max MAP
  - Minimum samples per cell

#### Sensor Overlay Settings
Show ANY sensor on main tables (not just lambda). Overlay conditions filter unwanted values. Transition delay for sensor settle.

#### Datalog Settings
**Datalog AutoSave:** auto-save when recording stops or ignition off. Configurable directory, filename prefix, suffix.

#### Autotune Settings
**Invoked:** toolbar button or Ctrl+T.

- **Minimum/Maximum Lambda:** boundaries for safe tuning (prevents adjustments during injector cutoff etc.)
- **Maximum change from base map:** % cap to prevent dramatic changes (base set on save/load)
- **Make adjustments every:** time between changes (lambda settle)
- **Autotune strategies:**
  1. **Closest cell:** changes one cell at a time (heaviest weighted)
  2. **4 weighted cells:** changes 4 cells based on interpolation proportion
  3. **Precise cell:** like #1 but only if actual MAP within 15% of load index
- **Play sounds when adjustments made:** high pitch = increase fuel, low pitch = decrease

**My ini defaults:**
- AutotuneMinLambda: 0.75 (~11.0 AFR floor — aggressive)
- AutotuneMaxLambda: 1.22 (17.9 AFR ceiling)
- AutotuneMaxChange: 10%
- AutotuneFreq: 1 (second)

For my reliability-first rule, I'd TIGHTEN AutotuneMinLambda to 0.80 (12.0 AFR minimum) before enabling.

---

### 6.56 Main Window & Status Bar — CAPTURED

**Status bar indicators (bottom of app):**

| Indicator | Meaning |
|-----------|---------|
| Driver | FlashPro USB driver installed (ticked) |
| FlashPro | FlashPro plugged into USB (ticked) |
| OBDII | FlashPro plugged into vehicle OBDII (ticked) |
| ECU | Ignition on + FlashPro can talk to ECU (ticked) |
| Locked | Shows FlashPro lock status to vehicle |
| Live | Live tuning enabled (ticked) |
| Datalog | Shows when datalogging from ECU |
| Record | Shows when recording from ECU |
| Modified | Current calibration has been edited |

These are useful health indicators before attempting any operation.

---

### 6.57 Options Menu — CAPTURED

- **Show Advanced Parameters:** removed in V1.9.2
- **Show Columns:** NA / Boost / All pressure columns in table window
- **Tables Follow VTEC:** live-switches table shown between low/high cam based on current VTEC state (datalog or live)
- **Tables Follow Cam Angle:** live-switches to nearest cam angle table (for VTC engines like mine)
- Settings / Sensors / Graph Templates / Keyboard Shortcuts / Language

For my K20Z3: enable both "Tables Follow VTEC" and "Tables Follow Cam Angle" so I always see the table that's currently being used.

---

### 6.58 Table Window — CAPTURED (IMPORTANT — primary tuning interface)

**Main tables:** ignition, fuel, cam angle, + supporting (cranking fuel, etc.).

**Low vs High Speed Cam:** tables often have separate copies for low/high cam. Window title shows which.

**Major Table toolbar selection:** 6 buttons:
- Low-speed ignition
- High-speed ignition
- Low-speed fuel
- High-speed fuel
- Low-speed cam angle
- High-speed cam angle

**Cam Angle Selection (VTC engines like mine):**
- Row of degree buttons below toolbar (for the 5 cam angle copies)
- Individual angle OR "All"
- When "All" selected:
  - Percentage changes: same percentage applied to all cam angle tables
  - Relative changes: same relative change to all
  - Absolute changes: same value copied to all

**Cell selection:**
- Mouse click-drag
- Arrow keys + Space bar
- Ctrl+A = select all
- Click topmost row = whole column
- Click leftmost column = whole row
- 2D graph: left-click-drag to select range; Shift+click = row; Ctrl+click = column

**Editing cells:**
- Single cell: type new value
- Multiple: select + Ctrl+J Adjust window
- Ctrl+I / Ctrl+D = +/- selection by default step
- 2D graph: drag cell up/down with mouse

**Quick Adjust buttons (toolbar):**
- Adjustment value (absolute or percentage)
- Add button = add value to selection
- Subtract = subtract value
- Set = set all selected to value
- Fuel tables: adjustment value is percentage for add/subtract; other tables: relative change value

**Special Operations:**
- **Interpolate:** interpolates between highest and lowest values in selection
- **Smooth:** smooths inconsistent values

**Right-click menu:**
- Increase/Decrease/Adjust/Interpolate/Smooth
- Revert to last save (resets to save point)
- Import from Calibration (pull table from another .fpcal)

**Live Tuning:** enabled per-table via icon next to table name.

**Graph View (right side):**
- 2D or 3D representation
- 2D: click rectangles, drag up/down to alter values
- 3D: click selects area on grid

---

### 6.59 Changing Table Indexes — CAPTURED

**How:** right-click on load/RPM value in Table Window.

**Operations:**
- **Edit Index:** change current index value (must be between neighbors — indexes must ascend)
- **Insert Index:** adds new row/column; shifts other values; last index removed
- **Delete Index:** removes current; shifts others up/left; new arbitrary index added at end

**Notes:**
- Recommended (not critical) to set indexes before tuning
- Index values must ascend from origin; don't need to start at 0
- When index changes, ALL tables using that index must update (some may be shared)
- Fuel / ignition / knock typically share the same indexes
- Cam angle tables use their own indexes
- Load indexes shared between low and high cam tables of same type
- RPM indexes NOT shared between low and high cam
- Underlying table values auto-compensated: edit/insert uses interpolation; delete shifts cells toward deleted row/column

**For VTEC crossover tuning (Section 6.30):** re-indexing around the VTEC point is the critical technique. Right-click → Edit Index → set 4200, 4300, 4400 for a 4350 RPM VTEC point.

---

### 6.60 Proportional Tracing — CAPTURED

Shows which table cells are being used in real-time via color gradient — darkest on most-weighted cell (ECU interpolates between 4 cells normally). Helps see exactly what the ECU is pulling from during a datalog playback.

**Axis trace indicator:** small mark on table axis shows current ECU reading. Centered on axis cell when datalog value equals axis index.

---

### 6.61 Changed Value Highlight — CAPTURED

Table cells show color to flag changes from last save/load point. Default: decreased = green, increased = red. Colors configurable in General Settings. Makes it easy to review what was edited before saving.

---

### 6.62 Sensor Overlay — CAPTURED

Show lambda (AFR) or any other sensor value overlaid on main tables during datalog playback.

For lambda overlay, tooltip shows: RPM, load, averaged lambda, number of samples used. (Samples not integer because values applied proportionally to neighboring cells.)

---

### 6.63 Calibration Window — CAPTURED (the parameter editor)

Edits calibration parameters (non-table settings).

**Calibration Parameter Groups (all listed):**
- Calibration parameters (revision, notes, gear ratios, permissions)
- Fuel parameters
- Ignition parameters
- VTEC parameters
- VTC parameters
- Closed loop parameters
- Knock control parameters
- Rev limit parameters
- Idle parameters
- Sensor parameters
- Misc parameters
- Ethanol Parameters (FLEX FUEL LIVES HERE)
- Traction Control Parameters

**Parameter default/changed indicators:**
- No dot = unchanged from factory default
- Red dot = edited this session
- Yellow dot = changed from default in PRIOR session

**Table right-click in calibration window:**
- Increase/Decrease/Adjust/Revert/Reset to default/Import from Calibration

---

### 6.64 Calibration Parameters (revision, notes, gear ratios, permissions) — CAPTURED

**Revision:** save a version tag with calibration.

**Notes:** free-text notes in calibration.

**Gear Ratios:** for cruise control if altered from stock. Speed sensor works from 3rd-gear countershaft. Altering final drive / 3rd gear / tooth count changes speed reading. Set gear ratios + speed adjustment.

**Calibration Permissions:** a SECOND password separate from FlashPro security. Prompts on "Change Permissions". No recovery if lost.
- Do not show tables & parameters (hide but still upload)
- Do not show non-tuning modifications
- Do not show tuning modifications
- Do not allow upload to Vault
- Only allow upload to FlashPro serial # (restricts to specific unit)
- Password can be saved on computer where cal was created/edited

For my build: I don't need to set calibration permissions unless I'm distributing tunes. If my tuner ever sends me a protected cal, this is why.

---

### 6.65 Fuel Parameters (DETAILED) — CAPTURED

**Fuel tables (MAP-based systems):** VE tables. AFM systems don't use these.

**WOT lambda adjustment tables:** used when ECU determines engine at WOT. Basic injection assumed stoich; WOT table adds enrichment.

**🔴 REPEATED HONDATA WARNING:**

> "Important note: Do not use values above 12.50 (AF) or 0.85 (lambda), otherwise the ECU will always run closed loop."

This is the upper lean limit AND a functional limit — above 12.50 AFR / 0.85 lambda, the ECU won't switch to open loop properly. Double reason to respect 12.50.

**Injector Size:** changing auto-compensates main fuel, cranking fuel, closed loop. Flow spec is at 3 bar / 43.5 psi nominal.

**Fuel Pressure:** compensates main fuel tables, cranking tables, closed loop for pressure differences (stock vs current, injector test pressures). Different injector brands = different test pressures. Changing these auto-adjusts tables.

**Fuel Trim:** compensation for main fuel (MAP), AFM, cranking. Injector-size change auto-adjusts these; normally don't touch.

**Injector Opening Time (dead time):** injector manufacturer supplies figures.

**Overrun Fuel Cut Delay:** delay between overrun conditions met and injectors off. Long = rev hang. Short = jerky at light throttle. 6MT but table may have 5 columns — 5th gear value used for 5th AND 6th.

**Fuel Table Type:** AFM calibrations can optionally use MAP (VE) lookup for fuel. AFM still needs to be present but flow unused. Can also use AFM at low MAP and MAP at higher pressure — "Minimum pressure for speed/density" crossover setting.

**AFM Fuel Table:** converts AFM air mass per cylinder to injector duration.

**Individual cylinder fuel trim:** separate fuel per injector. Only for setups with individual per-cylinder lambda probes.

**Air temp compensation (IAT):** three tables based on air flow rate (low/med/high). Positive = more fuel. Plus cranking IAT table.

**Coolant temp compensation (ECT):** two tables (below 40 kPa MAP / above). Plus cranking ECT table. Positive = more fuel.

**Fuel Economy:**
- Injector flow for fuel economy = reference value ECU uses
- Injector flow for dash = reference value dash uses
- Not supported on race calibrations

---

### 6.66 Fuel Pump Parameters (HPFP — Direct Injection) — CAPTURED

For direct injection vehicles only — limits air charge/boost based on fuel pump duty to prevent running out of volume.

**Not applicable to my K20Z3** (port injection, no HPFP). Noted for reference.

- Fuel pump target duty = where protection engages
- Fuel pump hysteresis = where protection removes
- Pump volume per duty cycle is NON-LINEAR (sine curve, not triangular) — 90→100% duty = only ~2.5% more fuel

---

### 6.67 Ignition Parameters (DETAILED) — CAPTURED

**Ignition tables:** base ignition timing for low/high cam. Compensations applied on top — final timing may differ from base table.

**EGR Ignition Tables:** RPM × EGR%. Affects partial throttle 12-25% EGR. At WOT (0-3% EGR), first two columns barely matter. For WOT ignition changes: use Knock Ignition Limit tables.

**Individual cylinder ignition trim:** per-cylinder timing. Only adjust with EGT gauge for guidance.

**Air temp (IAT) compensation:** two tables (low load / medium-high load, crossover ~40 kPa MAP). Positive = retard. Negative = advance.

**IAT retard application:** two options (only ONE should be checked):
- "Ignition IAT retard applied to ignition knock limit" = only reduces timing when knock limit close to MBT (default)
- "Ignition IAT retard applied to ignition advance" = applies to commanded advance always

**Coolant temp compensation (cold):** retard when below operating temp. Two tables (low/high load).

**Coolant temp compensation (hot):** retard when overheating. Two tables.

**Ignition parameters:**
- Cold-start retard for catalytic converter warmup — can disable for race cars without cat

**Throttle tip-in retard:**
- By RPM compensation
- By throttle compensation
- By gear compensation

**Gear compensation:** per-gear advance/retard. Advance = positive? No — **positive = advance, negative = retard** in THIS table. Apply requires "Ignition IAT retard applied to ignition advance" option checked.

**Cranking ignition:** base ignition when cranking, indexed by ECT.

---

### 6.68 VTEC Parameters (DETAILED) — CAPTURED

**VTEC window:** variable switch point based on RPM + load.

**VTEC RPM window:** minimum and maximum RPM for activation.
- **Twin cam engines (mine): don't go below 2500 RPM** (revised from the "2000" stated elsewhere — 2500 is the K-series specific floor)
- Single cam: 1800 RPM floor
- R18/R20: 1000 RPM floor
- Upper: **don't exceed 6500 RPM** (rocker float / valve damage)

**VTEC pressure window:** minimum MAP for activation vs RPM.

**VTEC conditions:**
- **VTEC minimum coolant temp:** don't engage below this ECT
- **VTEC engage/disengage minimum speed:** VSS floor. Disengage < engage always.

---

### 6.69 VTC Parameters (DETAILED) — CAPTURED

**Cam angle tables:** target cam angle for low and high cam. **Target should be ZERO around idle area.**

**Deceleration VTC Angle (important for shift feel):**
- Default: cam returns to 0° on throttle release
- 2012 Civic Si exception: returns to 5° above 4000 RPM
- **Problem:** cam at 0° during shift = no power dip + slow recovery to normal 20-30° after next gear engages
- **Solution options:**
  - **Zero VTC upon decel fuel cut** (default): cam → 0° on decel. Uncheck to use:
  - **VTC decel fuel cut angle** (if "Use VTC tables" not available): set intermediate angle, typically 20-30°
  - **Use VTC tables upon decel fuel cut** (preferred if available): uses normal VTC tables during decel

**Recommended settings:**
- Disable Zero VTC
- Enable Use VTC tables
- Zero the idle area
- Set columns 1-2 to intermediate angle (15-35°, typically 20-25°)
- Result: VTC doesn't have to advance from zero when shifting

**VTC Closed Loop Control:** PID parameters adjustable for cam positioning. Won't fix mechanical problems.

**For my build:** my tuner should enable "Use VTC tables upon decel fuel cut" for smoother shifts. Keep idle area zero (don't set VTC at idle).

---

### 6.70 Closed Loop Parameters — CAPTURED (CRITICAL FOR WIDEBAND)

**Primary o2:** ECU uses for closed loop control. Recommend keeping ENABLED during tuning to prevent switching-back-to-open-loop tuning differences.

**Secondary o2:** checks cat performance, alters closed loop target for cat optimization. Enable unless race car with no cat. (I have Berk HFC — enable.)

**WOT determination type:** MAP or TPS. **MAP preferred for most vehicles, required for forced induction.** For my NA: MAP-based WOT determination.

**MAP WOT determination table:** manifold pressure threshold where ECU switches from closed to open loop.

**TPS WOT determination:** two tables (high = closed→open, low = open→closed — hysteresis to prevent oscillation).

**LAF voltage to lambda:** conversion table from stock wideband o2 to lambda. **This is where the Civic Si semi-wideband calibration lives.**

**Wideband lambda interface settings:** cross-reference Section 6.8. Also see Section 6.72.

**Closed Loop Target Lambda:**
- Combination of tables by temp and load
- Actual target = richest (lowest) of: Closed Loop Target Lambda + Target Lambda Limit + Target Lambda Load (transition ~50 kPa MAP)
- **⚠️ Hondata warning:** lean than lambda 1 (~14.6 AFR) increases EGT. Not recommended for vehicles with catalysts.

**Fuel Trim Min/Max:**
- Controls STFT and LTFT percentage range ECU compensates
- AF learned value min/max = range for stored STFT used when switching from open loop to closed loop (calculated over 20 min average)

---

### 6.71 Knock Control Parameters — CAPTURED

**Knock sensor:** can be disabled if not present. **Normally do NOT disable during tuning** — if disabled, ECU uses default advance tables → considerable ignition retard.

**Light control:** flashes check engine light when knock occurs. Useful while tuning.

---

### 6.72 Rev Limit Parameters (DETAILED) — CAPTURED

**Activation vs recovery RPMs:** recovery should be 100-300 RPM lower than activation. Larger diff = slower, rougher limiter.

**Rev limiter type:** ECU uses FUEL CUT (not ignition cut) to protect cylinder walls from wash-down by unburnt fuel. Wet nitrous + fuel cut rev limit = set nitrous to shut off BEFORE rev limiter activates or engine goes lean.

**Overall limiter:** max engine speed under any conditions. Note: lower limiter may operate when cold or on low cam. **Does not protect against mis-shift overrev** (engine mechanically coupled to wheels).

**Overrev RPM:** where ECU generates fault condition. Set ~200 RPM higher than overall limiter.

**Launch limiter:** active when vehicle not moving (drivetrain protection). Fastest when cut RPM = recover RPM. Some vehicles have adjustable launch control (see 6.73).

**Speed limiter:** activates at indicated VSS. To disable: set higher than top speed.

**Boost Cut:** rev limit if MAP rises above threshold. Only active above 2000 RPM (so engine can start). With stock MAP (max ~1.78 bar / 11.5 psi), don't set boost cut above 1.75 bar (11 psi) to ensure voltage trigger works.

**Full Throttle Shift (flat-shift):**
- Detected when clutch depressed + throttle wide open
- ECU cuts fuel to drop RPM for next gear
- **RPM limit:** not critical, 2000-3000 below shift RPM suggested
- **Minimum throttle:** prevents shift limit during part-throttle / slow shifts

**Pops and Bangs:** FK8 and FL5/DE5 specific (not my platform).

---

### 6.73 Launch Control (Adjustable) — CAPTURED

**Concept:** adjust launch RPM via cruise control WITHOUT reflashing ECU.

**Initial value:** from calibration on first flash.

**After altering:** retained until battery disconnect or ECU reflash.

**Adjustment procedure:**
- Clutch depressed + vehicle stationary
- Cruise control Resume = increase launch RPM (100 RPM per press)
- Cruise control Set = decrease launch RPM
- Cancel button = show current launch RPM on tachometer

**Additional fuel/ignition:** activates when launch limiter active + engine speed above threshold. Used to maintain turbo pressure on FI.

**Parameters (launch-adjustable):**
- Launch RPM disengage speed = max VSS for fuel/ignition changes
- Launch min RPM for ignition retard and fuel enrichment = where changes begin
- Launch RPM additional fuel = extra fuel (fuel units)
- Launch RPM ignition retard = retard amount (positive = retard)

**⚠️ Warning:** anti-lag style settings build HEAT in exhaust. Don't use with cat. Only for seconds at a time.

**For my build:** launch control is NA-relevant for consistency off the line. My Sport map launch RPM = 4500. Can adjust in-car via cruise control afterward without flashing.

---

### 6.74 Hondata Mode (Sport/Eco Button) — NOT MY PLATFORM

2017 Civic Si has Sport button → stock power in non-sport, full power in sport.
2016+ Civic Turbo / 2018+ Accord has Eco button → similar inverted.

**Not available on my 2009 Civic Si.** My Daily/Sport switching uses Dual Calibration button combo instead.

---

### 6.75 Sensor Parameters — CAPTURED

**AFM flow table:** AFM voltage to air flow. Normally tuned via flow bench OR by observing fuel trims vs air mass flows.

**MAP Sensor:**
- Stock reads ~1.7 bar absolute (~10 psi boost)
- **Hondata 4-bar MAP sensor** reads to ~40 psi boost
- **Switching MAP sensors does NOT require table retuning**

**For my NA build:** no MAP upgrade needed.

**Speed Adjustment:** ECU receives signal from transmission 3rd-gear countershaft sensor. Calculates internal speed + dash speed. Both adjustable. Positive = increase, negative = decrease.

---

### 6.76 Idle Parameters — CAPTURED

**Idle speed:** two tables indexed by ECT:
- **Idle speed (after start):** higher RPM for 20-60 sec after start
- **Idle speed (normal):** post-warmup target

**Larger injectors trick:** higher idle RPM improves quality. Set tables so no value < desired idle.

**Idle Torque Reserve (Bosch ECUs — newer platforms):**
- Not my platform (PRB is Keihin)
- Torque reserve % at idle via ignition retard
- Too low = ECU raises RPM. Too high = over-retarded ignition. Rule: idle ignition should average ~TDC (0°).

---

### 6.77 Throttle Parameters — CAPTURED

**⚠️ Hondata warning:** advanced tables. Incorrect settings can cause throttle non-response or sudden acceleration.

**Throttle Index Table:** calculates index to main throttle table (some vehicles). Row = VSS, col = throttle pedal.

**Target Throttle Plate:** maps pedal to plate. Row = RPM, col = pedal (or index from above). Plate opened less at low RPM for smoothness. First column values restricted to ensure close on release.

**Throttle parameters:**
- **Throttle dampening:** stock ECU slows throttle opening in 1st gear to prevent jerk. Can disable.

**Overrun throttle:** plate held slightly open on overrun. Described in Section 6.36.

**Minimum throttle opening compensation:** table adjusts overrun opening by ECT. All values -100% = disable overrun opening entirely.

**Throttle Flow:** air flow past throttle for given opening. Only alter for larger-than-stock throttle bodies. **My Phase 3 will involve bored 66mm TB — this table may need a tuner adjustment.**

**Throttle Tip-In Fuel:** extra fuel on quick throttle opening. Tables for ECT compensation + throttle compensation (higher = more fuel).

**Injector Overrun Cutoff:**
- Restart RPM determines engine speed where injectors resume operation
- Two tables (cut / recover) for hysteresis
- Also MAP-based: tables for low/high cam with hysteresis

---

### 6.78 Boost Control Parameters — NOT MY PLATFORM

**NA engine = no boost control.** Detailed docs captured for reference but not applicable to K20Z3.

Summary of boost control docs (for future if I ever go FI):
- 3-way solenoid (normally open or normally closed)
- Connection to ECU pin B2 (Civic Si) or B16 (S2000)
- **Civic Si uses pin B2** — duty cycle controlled current source
- 10A fuse, ground, no relay, no suppression diode
- Duty cycle 15-85% typical effective range
- Frequency 10-60 Hz typical
- Activation pressure ~slightly over atmospheric
- Control methods: fixed duty / duty by RPM & gear
- Air temperature compensation (cooler = more duty)
- Quick Spool: full duty until near target boost
- Stock MAP sensor limit: ~11 psi boost

---

### 6.79 Turbocharger Parameters — NOT MY PLATFORM

For 2016+ DI turbos. Scramble button (Res+ for FK8, Sport for 10th gen Civic Si). Boost by gear table. Not applicable to my K20Z3.

---

### 6.80 Torque Parameters — LIKELY NOT APPLICABLE TO MY PRB

Torque limiting tables for transmission protection (CVT mostly). My 6MT doesn't need this.

**Bosch ECU Torque Tables:** 2016+ DI platforms. Nominal Charge / Reference Torque / Minimum Efficiency. Critical NOT to alter without paired external calculator — throttle control disabled on mismatch. Again, not my platform.

---

### 6.81 Misc Parameters — CAPTURED

- **Immobilizer:** CANNOT be disabled (security)
- **VSA:** enable/disable vehicle stability. **Enable for all VSA-supporting vehicles.**
- **EPS:** idle-up when steering wheel turned. Not on/off for EPS unit itself.
- **Cruise Control:** enable/disable
- **Starter relay:** push-button start vehicles only
- **🔑 Radiator Fan:**
  - **On temp / Off temp settings** — on should be ~3°C/5°F higher than off
  - **Can use second coolant temp sensor (radiator bottom) OR cylinder head coolant sensor** (checkbox)
  - **Stock thermostat:** opens at 85°C/185°F, fully open at 90°C/195°F. Don't set fan below thermostat fully-open temp — fan runs constantly.
- **Air Pump [Euro-S2000]:** disable for boost control.

**For my build:** critical that this is where my fan tables live. My Phase 1 cooling refresh planned Koyorad radiator — I should set fan ON ~190-195°F, OFF ~185°F (still above thermostat's 185°F fully-open).

---

### 6.82 Ethanol Parameters — CAPTURED (🔴 THE CRITICAL FLEX FUEL ANSWER)

**🔑 RESOLVED: THE FLEX FUEL WIRING ANSWER**

Per official Hondata docs, flex fuel / ethanol control on FlashPro uses:

**Input options:**
- **ECT2 (second coolant temp sensor pin)** — available on some vehicles including K-series ECUs
- **CANFlex** — requires Hondata CANFlex module, uses CAN bus (newer vehicles only — NOT my PRB)

**For my K20Z3 PRB ECU: ECT2 is the wiring path.**

**Critical setup:**
1. Wire the ethanol control unit's 0-5V signal output to **ECT2 pin**
2. **Disable ECT2 in misc parameters** (Section 6.81 — uncheck it so ECU doesn't try to read it as coolant temp)
3. Configure **Ethanol percentage table** — voltage to percentage mapping

**⚠️ Important note on ECT2:** the ECU ECT2 input has an internal pull-up resistor to 5V. Some ethanol control units can't pull the voltage down enough for accurate low-ethanol reading.

**Hondata's recommended per-sensor settings:**

| Sensor | 0% voltage | 100% voltage | Limitation |
|--------|-----------|-------------|-----------|
| **Zeitronix ECA** | 0.34V | 4.97V | Will not read below 15% ethanol |
| **Innovate ECF-1, MTX-D, ECB-1** | 0.00V | 5.00V | Will not read below 1.5% ethanol |

**Standard fuel context (US):**
- Pump gas: 0-10% ethanol (typically 10%)
- E85: 55-80% depending on location/season

**Ethanol-adjusted tuning tables:**
- **Ethanol fuel compensation:** delivers more fuel based on ethanol percentage
- **Ethanol ignition multiplier:** multiplier applied to ignition compensation table
- **Ethanol ignition compensation table:** final ignition adjustment = value × multiplier, added to commanded ignition
- **Ethanol WOT fuel compensation:** Hondata testing found DI vehicles respond BETTER to LESS fuel at WOT with high ethanol (11:1 stock goes to 11.8:1 at 85% ethanol for more power / less knock)
- **Boost by ethanol limit table:** more boost with more ethanol (but needs more fuel — may increase or decrease depending on fuel budget)
- **Ethanol advanced mode:** disables simple 2D tables, enables 3D fuel and boost tables for precise tuning

**For my build — THIS UPDATES EVERYTHING:**

**Previous plan (wrong):** wire flex fuel sensor to SO2 (rear O2) pin.
**Correct plan (per Hondata):** wire flex fuel sensor to **ECT2 pin**, disable ECT2 in misc params.

This also means my **wideband wiring** can use SO2 (rear O2) — wait, no, the Wideband topic (Section 6.8) said SO2 is NOT recommended. So:

**Final wiring allocation for my K20Z3:**
- **Wideband (AEM X-Series 30-0300):** **EGRL or ELD** (NOT SO2, NOT ECT2)
- **Flex fuel sensor (Continental 13577429):** **ECT2 pin** (with ECT2 disabled in misc)

**Parts I'll need (updated from [12-Flex-Fuel-and-Fuel-System/overview.md](../12-Flex-Fuel-and-Fuel-System/overview.md)):**
- The sensor itself (Continental 13577429 — verify output is compatible; standard GM sensor outputs frequency, not 0-5V voltage)

**⚠️ HUGE DETAIL: The Continental/GM 13577429 sensor outputs FREQUENCY, not 0-5V voltage.** This is a problem:
- Hondata's ECT2 input expects 0-5V voltage signal
- The GM sensor outputs 50-150 Hz frequency signal
- **Solution: need a frequency-to-voltage converter OR use a dedicated ethanol content controller** (Zeitronix ECA, Innovate ECF-1, MTX-D, ECB-1)

**The controllers Hondata recommends (Zeitronix / Innovate) are NOT just the sensor — they INCLUDE a controller that converts GM sensor frequency to 0-5V voltage for the ECU.**

**Updated BOM component for flex fuel:**
- Continental 13577429 sensor (frequency output)
- Ethanol content controller (converts frequency to 0-5V): Zeitronix ECA, Innovate ECF-1, Innovate MTX-D, or Innovate ECB-1
- Choose Innovate over Zeitronix (reads down to 1.5% ethanol vs 15% — better low-ethanol accuracy, matters for pump-gas-with-some-ethanol mode)

**This is a significant update to the flex fuel build.** The existing doc says Continental sensor is "$50-80" which is true for the sensor, but the TOTAL system needs an ethanol controller too (Innovate ECF-1 runs ~$150-200).

---

### 6.83 Methanol Injection — CAPTURED (NOT PLANNED — reference only)

Uses ECT2 pin like flex fuel. AEM 30-3300 methanol controller + Hondata wiring adapter. Voltage switches (0.65V inactive, 3.1V active) to trigger fuel/ignition changes for methanol injection. **Either flex fuel OR methanol — not both** (both use ECT2).

Not in my plan.

---

### 6.84 Traction Control — LIMITED ON MY PLATFORM

**Hardware TC:** requires Hondata Traction Control module + wheel speed sensor interface.

**Software TC:** uses factory VSA wheel speed data. Available on some vehicles. Ignition retard only. Works with VSA enabled or disabled.

**For my 2006-2011 Civic Si:** unclear if software TC is available for PRB — would need to check in FPM with cal loaded. Hardware TC via Hondata module is option. Neither in my current plan.

---

### 6.85 Graph Window — CAPTURED (datalog analysis)

**Graph display:** sensor values from live recording or past datalog.

**Graph templates:** pre-defined configurations of sub-graphs and sensors.

**Menu options (right-click on graph):**
- Zoom In / Out / Full
- Next/Previous Template
- Define Templates
- Add/Edit/Delete Comment

**Keyboard navigation:**
- Home / End = start/end of datalog
- Page Up/Down = viewable width left/right
- Arrow keys (±1 sec), + Shift (±10 sec), + Ctrl (±0.1 sec), + Shift+Ctrl (±0.01 sec)

**Playback controls:** in Graph window + Datalog menu.

**Datalog → Calibration matching:** datalog can link to matching calibration IF cal was opened in FPM on same laptop AND uploaded before datalog made.

---

### 6.86 Datalog Comments — CAPTURED

Right-click datalog at position → Add Comment. Great for annotating specific events during a drive ("hit VTEC here", "knock at WOT 4th gear"). Comments move by editing time.

---

### 6.87 Advanced Graphs (XY, Histogram) — CAPTURED

**XY Graph:** any two sensors, X vs Y.
- **Critical for AFM tuning** (AFM.v vs S.TRIM, per Section 6.23)
- Options: show mean (blue line), show SD (green line), show X for data points
- Filters: closed loop, open loop, WOT (throttle >80%), OV (overrun filter)

**Histogram:** bar chart of sensor frequency.
- Options: percentage vs count, cumulative
- Same filters as XY

---

### 6.88 Graph Templates — CAPTURED

- 1-4 sub-graphs per window
- Each sub-graph: 1-4 sensors
- Import/Export buttons for sharing templates between computers

---

### 6.89 Sensor Window & Display Window — CAPTURED

**Sensor Window:** list of sensors, live-updated. Right-click for options (properties, right-justify values, group sensors).

**Display Window:** large font for dyno monitoring. Customizable controls:
- **Value control:** numeric sensor value
- **Text control:** fixed text
- **Image control:** bitmap only
- **Gauge control:** analog-style gauge
- **Clock control:** date/time
- **Bar control:** horizontal or vertical bar readout
- **Indicator control:** boolean or threshold warning (e.g., VTEC on/off, over-rev warning)
- **Button control:** start/stop datalog/record buttons (window must be LOCKED for clicks to respond)

Layouts saved/loaded via Display menu. Images embedded.

---

### 6.90 Error Codes Window — CAPTURED

Displays DTCs from live datalog or past log. **Rule: fix any DTC before tuning.** Consult vehicle service manual for diagnostic procedures.

---

### 6.91 FlashPro Window (Tabs) — CAPTURED

**Tabs:**
- **FlashPro:** FlashPro + ECU info. Shows EPA/CARB restriction type.
- **Calibrations:** lists cals ON the FlashPro. Upload/download/remove. **Cal on FlashPro ≠ what's on ECU** — presence doesn't indicate current ECU state.
- **Datalogging:** on-board datalogs stored on FlashPro unit
- **Registered Owner:** user details, Hondata registration
- **Jailbreak:** FK2/FK8 only (not mine)
- **History:** serial numbers of FlashPros connected to this computer. For loss/theft record. Local only, can be cleared.
- **Bluetooth:** FlashPro 2 or post-Dec-2013 FlashProOG. My unit MAY have Bluetooth depending on its manufacture date.

---

### 6.92 EPA/CARB Restrictions — CAPTURED

**Two FlashPro types:**
- **Race FlashPro:** any calibration can be uploaded. Legal ONLY for racing vehicles never used on public highway within USA.
- **CARB FlashPro:** only calibrations that don't affect emissions allowed. EO number D-742-1. Legal on USA street vehicles.

**For my Civic Si:**
- If my FlashPro is a CARB unit (blue), I can only flash CARB-approved calibrations for USA street use
- If Race (grey) or Dealer (black), any calibration
- **Check:** FlashPro window → FlashPro tab shows type

**Key notes:**
- EPA administers Clean Air Act federally
- No direct EPA approval mechanism — they accept CARB approval
- So California-legal = federally legal
- Even no-emissions-test states must comply with Clean Air Act — "49 state legal" concept no longer valid

---

### 6.93 OBDII Diagnostics Window — CAPTURED

**DTCs:** four-digit codes starting with P (powertrain). Fix before tuning.

**Readiness Codes:** OBDII test completion markers.
- **Continuously monitored:** Misfire / Fuel system / Comprehensive component
- **Non-continuous (trip-monitored):** Catalyst / Heated catalyst / EVAP / Secondary air / A/C refrigerant / O2 sensor / O2 heater / EGR

**Reset events that clear readiness:** reprogram ECU / clear DTCs / remove ECU / disconnect battery.

**Driving cycles to set readiness** (rough guide):
- **Catalyst:** ~5 miles stop/go + steady cruise. May take multiple cycles if cat marginal.
- **EVAP:** cold start + stop/go warmup + 5-10 min highway steady throttle, no key-off.
- **Oxygen sensor:** warm engine + ~3.5 miles including 5-sec closed-throttle decel.
- **O2 heater:** 10-20 sec after start.
- **EGR:** warm engine + ~1 mile.

**Cold start defined:** ECT <120°F, IAT + ECT within 7° of each other, min 6 hours off.

**Emissions Check:** simulates smog test for pre-emissions-inspection check.

**Diagnostics tab:** DTCs from all CAN bus modules. Older vehicles: only ECU on CAN; K-line modules not shown. Refresh searches modules (shift+click for exhaustive search ~1 min). Clear DTCs button.

**For my build:** after any calibration flash, I should drive the readiness cycles before any smog test. Budget ~2 tanks of gas on varied driving.

---

### 6.94 Shortcuts Window — CAPTURED

**Custom shortcuts:** any action can be assigned any combination of 1-4 key strokes. Change / Remove / Reset to defaults.

---

### 6.95 Dealer FlashPro Window — NOT MY UNIT

For Hondata authorized dealers managing customer vehicles. License counts, purchase licenses online, reflash history per-vehicle. Not applicable to end-user.

---

### 6.96 G Force Window — CAPTURED

Shows G-sensor data from VSA-equipped vehicles where VSA data is datalogged. Range, trail, style options via right-click.

**For my 2006-2011 Civic Si:** VSA available, but G-force datalogging availability requires testing.

---

### 6.97 Check For Updates / Check Internet Connection — CAPTURED

Help menu → Check For Updates = polls Hondata server for new FPM version (needs internet).
Help → Check Internet Connection = verify Hondata communication.

---

### 6.98 Update Boot Firmware — CAPTURED (Rare Fix)

For FlashPros with boot firmware v7 or earlier (pre-FPM 2.6.3). Some USB3 ports had connection issues. If firmware v8+, this option is hidden.

**⚠️ If boot firmware update interrupted:** FlashPro BRICKED and needs return to Hondata.

**Recommendation:** only run if normal firmware update process is giving problems. Takes a few seconds when it works.

**For my build:** FPM ini shows FlashPro=461004 (a recent firmware). Unlikely I need boot firmware update. Leave alone.

---

### 6.99 Compare Calibration — CAPTURED (useful diff tool)

**Menu:** File → Compare Calibration.

Compares current calibration to any other `.fpcal`. Detects changes. **Useful for:**
- Understanding what a tuner changed
- Diffing Daily vs Sport maps
- Verifying what an "official" cal has vs my working one

---

### 6.100 Sensors (Complete K20Z3 Compatibility) — CAPTURED

For my Civic Si '06 (the row in the Sensors topic):

**Supported for datalogging:**
| Sensor | Description |
|--------|-------------|
| ✅ RPM | Engine speed |
| ✅ VSS | Vehicle speed sensor |
| ✅ GEAR | Calculated gear from VSS × RPM |
| ✅ MAP | Manifold absolute pressure |
| ✅ TPS | Throttle position sensor |
| ✅ TPlate | Throttle plate (DBW — %) |
| ✅ AFM Volt | Air flow meter voltage (not AFM Flow mass units) |
| ✅ INJ | Injector duration (ms) — cylinder #1 |
| ✅ IAT | Intake air temp |
| ✅ ECT | Engine coolant temp |
| ✅ VTC Actual | Actual cam phase (degrees) |
| ✅ VTC Cmd | Commanded cam phase |
| ✅ Lambda | Lambda from stock o2 |
| ✅ Target Lambda | ECU's target lambda |
| ✅ Short Term Trim (STFT) | Closed-loop fuel trim |
| ✅ Long Term Trim (LTFT) | Long-term fuel trim bias |
| ✅ Closed Loop Status | Open/closed loop flag |
| ✅ O2B Volt | Rear o2 sensor voltage |
| ✅ Knock Level | Knock %, from sensor |
| ✅ Knock Retard | Retard applied in degrees |
| ✅ Knock Control | K.Control value (estimated octane %) |
| ✅ PA | Ambient pressure |
| ✅ Batt | Battery voltage |
| ✅ VTS | VTEC state (boolean) |
| ✅ Wide Band Lambda | FPM analog input 1 or 2 (when wired) |
| ✅ Wide Band Voltage | Raw voltage from wideband |
| ✅ Knock Count 1-4 | Per-cylinder knock events |
| ✅ Knock Limit | Ignition advance limit due to knock |
| ✅ Boost Control Duty | Not useful on NA |

**NOT supported for datalogging on Civic Si '06:**
- ❌ ING (no such sensor on my PRB)
- ❌ AFM Flow (mass units) — only voltage available
- ❌ ECT2 (NOT listed as datalog channel — BUT it's what flex fuel USES... means ethanol % datalog is ???)
- ❌ IAT2
- ❌ Lambda 2 / Target Lambda 2 / Short Term Trim 2 / etc. (not my platform)
- ❌ INJ 2 (no second injector reading)
- ❌ BP / BPCMD / Waste Gate (NA vehicle)
- ❌ EXVTC (exhaust VTC — I have intake VTC only)
- ❌ Fuel Pressure
- ❌ Air Charge
- **❌ Ethanol Content** — **this is concerning for flex fuel**
- ❌ Fuel Duty
- ❌ FTP (fuel tank pressure)
- ❌ Purge Duty
- ❌ TC Volts / TC Retard / IAB (traction control)

**⚠️ Flex fuel datalogging question:** Sensors table doesn't show **Ethanol Content** as a datalog channel for my '06 Si. BUT Hondata Ethanol Parameters topic describes ethanol control FOR my platform using ECT2. Possibly:
- Ethanol content may show up as a NEW datalog channel when ethanol control is enabled in the calibration
- OR the ethanol value is read from ECT2 volts and datalogged as the ECT2 voltage (since regular ECT2 is disabled)
- OR the sensors matrix is outdated/incomplete

**Action item:** once I have flex fuel installed, verify in FPM what datalog channels appear. If ethanol content isn't directly visible, derive from ECT2 voltage (linear 0.34-4.97V → 0-100% or whatever my specific controller outputs).

---

### 6.101 Sensor Definitions (Per-Sensor) — CAPTURED

Summary of per-sensor topic descriptions:

| Sensor | Meaning |
|--------|---------|
| **RPM** | Engine speed from crank sensor. Tachometer usually reads 0-5% high; ECU is accurate. |
| **VSS** | Calculated from transmission sensor. Driven-wheels speed — doesn't compensate wheel slip. |
| **Gear** | Calculated by ECU from VSS × RPM. |
| **MAP** | Manifold absolute pressure after throttle plate. |
| **BP / BPCMD** | Boost pressure (turbo) / commanded boost. Not my vehicle. |
| **AIRC** | Air charge % (cylinders filled with air). >100% = under boost. Not my vehicle at my power level. |
| **WG / WGCMD** | Wastegate position (mm) / commanded. Not my vehicle. |
| **TPedal** | Throttle pedal position (%). |
| **TPlate** | Throttle plate position (%). |
| **AFM.v** | Air flow meter voltage. |
| **AFM** | AFM air mass flow (converted from voltage). |
| **INJ** | Injector duration (ms) for injector #1. |
| **Duty** | Injector duty cycle (%). |
| **DIFP / DIFPCMD** | Direct injection fuel pressure (DI only). Not my port injection. |
| **IGN** | Ignition timing (degrees BTDC). |
| **IAT** | Intake air temp (by AFM for NA, by intake manifold for turbo). |
| **IAT2** | Second IAT for turbo vehicles. |
| **ECT** | Coolant temp in cylinder head. |
| **CAM** | Intake cam position (crank degrees from base). **LOCKED at 0° for 10 sec after startup.** |
| **CAMCMD** | Intake cam target. Actual lags 0.1-0.5 sec (closed-loop mechanism). |
| **EXCAM / EXCAMCMD** | Exhaust cam position/command (dual VTC vehicles). Mine is intake VTC only. |
| **AF** | Air/fuel ratio from stock lambda sensor. |
| **S.TRIM** | Short-term fuel trim (%). Normal range -10% to +10%. **Outside = need part-throttle fuel retuning.** Often high during shifts (overrun). |
| **L.TRIM** | Long-term fuel trim. Normal -5% to +5%. |
| **TRIM** | Combined STFT + LTFT. |
| **Fuel Status** | 2 = closed loop, 1 = open (warming up), 4 = open (driving), 8 = open (error). |
| **K.Level** | Knock level (%). |

**Critical for my analysis:**
- STFT out of ±10% → **tuning issue** at part throttle
- LTFT out of ±5% → **underlying consistent issue** (vacuum leak, injector drift, AFM calibration)
- Fuel Status = 8 → ERROR, investigate
- CAM lags CAMCMD sustained > 0.5 sec → VTC actuator failing (matches my existing guidance)

**Additional sensor definitions (from later help topics):**
- **K.Retard:** knock retard (degrees) actually applied to the ignition.
- **K.Control:** knock control value (%) — estimated fuel octane as a percentage between 100 RON and 90 RON. 0% = 100+ octane, 25% = 97.5, 50% = 95.
- **Ign.Limit:** knock ignition limit (degrees). Max advance before knock likely.
- **K.Count:** knock count per cylinder. Incremented every time ECU detects a knock event. NOT affected by knock sensitivity table adjustments. **Common false-knock causes: supercharger noise, exhaust headers.** Worth noting for my Skunk2 Alpha header — early cold-start false-knock is possible; tune sensitivity up if needed.
- **PA:** atmospheric air pressure, measured internally by ECU.
- **BAT:** battery voltage at the ECU.
- **VTS:** VTEC spool valve state — shows when VTEC has engaged the high-speed cam (boolean).
- **Eco:** calculated fuel economy — depends on injector size being set correctly in Fuel parameters.
- **Fuel Used:** per-trip total fuel used by the engine (ECU-calculated).
- **Frame:** datalog frame count.
- **BC Duty:** boost control duty cycle (%). Not applicable to NA.

This closes the loop on all the individual sensor definitions for datalog analysis.

---

## 7. ECU Connectors & Pins — CAPTURED (CRITICAL FOR WIRING)

**Convention:** ECU pins referenced by connector letter + pin number, e.g., `C27` = pin 27 of connector C.

### For My 2006-2011 Civic Si (PRB) — The Pin Allocation Table

| Pin | Stock Function | Repurpose For | Notes |
|-----|----------------|---------------|-------|
| **A23** | ELD (Electrical Load Detector) | Wideband input | ELD must be disabled in misc + factory pin removed from ECU connector |
| **A33** | ECT2 (Second coolant temp sensor) | Wideband OR Flex Fuel input | ECT2 must be disabled in misc + factory pin removed |
| **B2** | EGR output | Boost Control output | Normally unused — open for future FI |
| **B29** | EGRL (EGR lift input) | Wideband input | Normally unused |
| **C27** | SO2 (Secondary/rear O2 sensor input) | — | **NOT recommended for wideband** (ECU voltage clipping). Must be disabled + pin removed if ever used |

### Connector Color Coding (Civic)

- **A Connector — White**
- **B Connector — Grey**
- **C Connector — Green**

### Physical Pin Details

- Each connector has pins numbered 1-40 organized into **5 rows**
- Top and bottom rows use **large pins**
- Middle three rows use **small pins**
- Pin numbers visible on wire side of connector once plastic cover removed

### Inserting / Removing Pins

**To access pins:** slide the white plastic surround upward slightly to unlock pins.

**Inserting pins:**
- Crimp pin onto wire with a crimp tool (Molex tool with 1.6mm crimp recommended)
- Verify correct cavity before inserting (very hard to remove once in)
- Push pin in with open side of crimp UPWARD until it clicks
- Move plastic surround back to locked position

**Removing pins:**
- Very difficult without the correct tool
- Fine screwdriver can work as a makeshift removal tool
- Insert from ECU side, lift sprung plastic catch while pulling wire from behind
- **Don't use force on the wire** — pin digs into plastic catch and becomes much harder to remove

### Cross-Reference to Other Platforms (for context)

| Platform | ELD pin | ECT2 pin | EGRL pin | SO2 pin |
|----------|---------|----------|----------|---------|
| **2006-2011 Civic Si** (mine) | A23 | A33 | B29 | C27 |
| 2012 Civic Si / ILX | A34 | A44 | — | — |
| 2012-2015 R18 AT/MT | A34 | A44 | — | — |
| 2014-2015 R18 CVT | A34 | A46 | — | — |
| S2000 | E15 | E1 | B12 | — |
| 2007-2008 TSX | E15 | E1 | B12 | — |
| 2009-2014 TSX | A24 | — | — | — |

---

## 8. DDE Server — FPM ↔ Excel Integration — CAPTURED

**What it is:** FlashProManager can function as a **DDE (Dynamic Data Exchange) server** — a Windows inter-process data transfer tech. Enables Excel and other apps to pull live datalog values from FPM for further analysis.

### Data I Can Pull from FPM via DDE

**Server name:** `FlashProManager`

**Calibration data:**
- `=FlashProManager|Calibration!Name` — returns loaded calibration name

**Datalog data:**
- `=FlashProManager|Datalog!FrameCount` — live-updates while datalogging

**Sensor data:**
- `=FlashProManager|Sensors!Count` — number of sensors
- `=FlashProManager|Sensors!Names` — array of names (Ctrl-Shift-Enter for array display in Excel)
- `=FlashProManager|Sensors!Values` — array of live values
- `=FlashProManager|Sensors!Units` — array of units
- `=FlashProManager|Sensors!'Knock Retard'` — individual sensor value (single quotes for names with spaces)

### Commands I Can Send to FPM via DDE

**Calibration commands:**
- `Open <filename>` — load a calibration
- `Notes <notes>` — change calibration notes (new line via `$r`)
- `Lock <serial>` — lock cal to FlashPro serial number
- `Save <filename>` — save current cal
- `Close` — close current cal

**Modification commands:**
- `Apply <filename>` — apply a modification to current cal (filename relative to FPM modifications directory)

### Example Use Cases

- **Live dashboard in Excel** — custom gauges, alarms, computed values from live sensor data
- **Auto-build calibration compare reports** — script opens two cals, dumps values to Excel cells
- **Remote monitoring** — Excel sheet pulling from FPM over DDE, shared with a tuner elsewhere

**For my build:** DDE is a lightweight alternative to Lua plugins for simple integrations. If I want a custom dashboard or logger that's quick to set up, this is the path. Not as powerful as plugins but easier for small jobs.

---

## 9. Plugins and Scripting (Lua) — CAPTURED (NEW AUTOMATION PATH)

**⚠️ Major correction to earlier docs:** I previously wrote "Hondata has no public API or documented CLI." **This was wrong.** FPM supports Lua scripts packaged as Plugins — a real programmatic automation path.

### What Plugins Can Do

- Read/write any calibration parameter or table
- Analyze datalogs
- Respond to events (calibration open/close, datalog load, datalog start/stop)
- Interactive dialogs (InputQuery, ShowMessage)
- Access sensor metadata (name, type, unit, min/max)

### How to Install a Plugin

- FPM → Plugins menu → Manage Plugins → Install button

**⚠️ Security warning:** Plugins can change ANY calibration parameter or table. **Only install from trusted sources.**

### Lua Script Object Model (summarized)

Full reference in FPM help; key objects:

**`Application`** — `app`, `version`, `build`, `bit64`, `compiledate`, `locale`, `os`

**`Device`** — name, `connected()`, `hardware()`, `serial()`, `isdatalogging()`, `isrecording()`, `datalogcount()`

**`ECU`** — `ignitionon()`, `startdatalogging()`, `stopdatalogging()`, `startrecording()`, `stoprecording()`

**`Sensor`** — `name()`, `abbreviation()`, `description()`, `min()`, `max()`, `type()`, `unit()`, `live()` (real-time value)

**`SensorList`** — `count()`, `sensor(index)` (also `[]` subscript)

**`Datalog`** — `filename()`, `framecount()`, `length()`, `timestamp(frame)`, `framenumber(timestamp)`, `value(Sensor, frame)`, `sensorcount()`, `sensor(index)`

**`DatalogManager`** — `count()`, `datalog(index)`

**`Table`** — `name()`, `valuename()`, `dimensions()`, `length()`, `size()`, `type()`, `unit()`, `readonly()`, `GetValue(idx, idx, idx)`, `SetValue(value, idx, idx, idx)`

**`Calibration`** — `loaded()`, `filename()`, `update()`, `tablecount()`, `table(index)`

**`ErrorCode` / `ErrorCodeList`** — DTC query and clearing

### Event Callbacks

Lua scripts can respond to:
- `OnCalibrationNew(calibration)`
- `OnCalibrationOpen(calibration)`
- `OnCalibrationClose(calibration)`
- `OnDatalogOpen(datalog)`
- `OnDatalogClose(datalog)`
- `OnDatalogStart()`
- `OnDatalogStop()`

### Functions

- `InputQuery(caption, prompt, default)` — prompt for string input, returns string or nil
- `ShowMessage(message)` — show MessageBox

### Implications for My Build

**This is the automation path I thought didn't exist.** With Lua plugins I can:

1. **Auto-analyze datalogs on close.** `OnDatalogClose(datalog)` fires → script reads all frames for knock count, lean spikes, over-duty-cycle events → writes a summary to a file or shows MessageBox.

2. **Safety guardrails on calibration save/upload.** `OnCalibrationOpen/Close` fires → script inspects WOT AFR cells, timing cells, rev limits, VTEC point → rejects out-of-envelope values BEFORE I flash.

3. **Auto-CSV export of datalogs.** `OnDatalogClose` → script uses `datalog:value()` to iterate all frames/sensors and writes a CSV file to a known folder. Paired with cloud sync, Claude can pull logs within seconds of me ending a drive.

4. **Custom sensor alerts.** Real-time via Lua scripts monitoring `Sensor.live()` values and triggering UI alerts when thresholds cross.

**For my build, I should write (or find a community plugin for):**
- `reliability-guard.lua` — enforces my safety ceilings on calibration save (WOT AFR ≥ 12.0 pump / ≥ lambda 0.82 E85, timing peaks verified, rev limit ≤ 8400 RPM)
- `auto-csv-export.lua` — writes CSV next to `.fpdl` on close
- `log-summary.lua` — post-drive summary of knock events, trim extremes, max IAT/ECT, injector duty peaks

This is a much better workflow than UI automation via AutoHotkey. I'll explore the Plugins community / write my own when I have more dyno data.

### Other Mentions

- **Plugin Graphics** — listed as "Work in progress. Unsupported."
- **Plugin Debugger** — listed as "Work in progress. Unsupported."
- `Writing a plugin` — referenced as another help topic (not yet pasted; worth capturing if available)

---

## 10. Bluetooth — CAPTURED

### Which FlashPros Have Bluetooth

- **Some FlashPros manufactured after July 2013 AND all after December 2013** have built-in Bluetooth
- Compatible serial number cutoff for 2006-2011 Civic Si **US FlashPro: sold after 11/7/2013**
- Compatible cutoff for Civic Si / Type R **International: 9/27/2013**

**For my unit:** the INI shows my FlashPro as a recent model (`FP-SI-US-461004`). If sold after November 2013 it has Bluetooth. **I should check: FPM → FlashPro window → FlashPro tab → expand "Hardware" → look for "Bluetooth present" entry.**

### Bluetooth Types Supported

- **V2.1 (BR/EDR)** — Android supports unrestricted
- **BT4 (BLE — Low Energy)** — slower than V2.1
- **Apple devices with Bluetooth V4** — work
- **Apple devices with V2.1** — DON'T work (Apple requires specific chip in the hardware)

### Communications Protocols

- **FlashPro binary protocol** — datalog from FPM on laptop via Bluetooth
- **Hondata binary protocol** — Android/iOS apps
- **ELM327 emulation** — compatible with many existing scantool smartphone apps

### Android Apps Supported

Car Gauge Lite/Pro, DashCommand, OBDAutoDoctor, OBD Car Doctor, OBD Dashboard, OBD DROIDSCAN PRO, OBDLink, ScanMaster Lite, Torque Lite/Pro — all can read Bluetooth FlashPro.

### Windows Bluetooth Stack Requirement

- FPM requires **Microsoft Bluetooth stack** (shown as "Generic Bluetooth Adapter" in Device Manager)
- Non-Microsoft stacks (chipset-manufacturer stacks) will NOT work with FPM
- If using a non-Microsoft stack, you can uninstall and let Windows re-install with the Microsoft stack (risky — requires driver management comfort)

### Bluetooth Options (FlashPro window → Bluetooth tab)

- **Bluetooth enabled** — enable/disable on FlashPro
- **Local Address** — Bluetooth radio on laptop (blank = no Bluetooth OR wrong stack)
- **FlashPro Address** — Bluetooth address of FlashPro
- **Device Name** — FlashPro Bluetooth name
- **Tuning via Bluetooth enabled** — datalog + change some settings over Bluetooth (uploading NOT supported)
- **Alternative pairing mode** — FlashPro shows as a phone to pair with vehicle head units (2018+ Civic)

### Bluetooth Security

- **PIN code** required on pairing (Windows can try 3 times without PIN before prompting user)
- BLE connections don't use PIN codes → Tuning via Bluetooth DISABLED for BLE
- **Limit access by device address** — most secure, only listed devices can connect

### Connecting From Laptop

- FPM → Online / Bluetooth menu OR Bluetooth toolbar button
- FlashPro plugged into vehicle with ignition ON
- Select Bluetooth Device window — Refresh to find new FlashPros
- Windows remembers paired FlashPros
- Pairing code defaults to FlashPro serial number (changeable in Bluetooth tab)
- Disconnect: same menu/button

### Vehicle Pairing (Hondata Mobile on Head Unit)

For 2018+ Civics running Hondata Mobile on the car's head unit:

1. Unplug FlashPro from vehicle
2. Plug into laptop, run FPM
3. FlashPro / Bluetooth → check "Alternative pairing mode for head unit (2018+ Civic)"
4. Unplug/replug FlashPro USB
5. On vehicle radio, pair to FlashPro (code default 1234)
6. Hondata Mobile app on head unit connects to FlashPro

**Not applicable to my 2009 Civic** (no compatible head unit).

### Bluetooth Test Mode (developers only)

Sends fixed test data:
- RPM varies, speed 100 kph, gear 4, IAT 100°F, ECT 200°F, MAP 110 kPa, Lambda 13.8 AFR, STFT +10%, LTFT -10%, Battery 12V, Ethanol 20%, etc.

### For My Build

**If my FlashPro has Bluetooth:**
- I can datalog from a phone without a laptop — **huge convenience for monitoring**
- Hondata Mobile app pairing for a dash display
- Android apps (Torque Pro, etc.) for custom gauges without FPM

**Action item:** verify Bluetooth on first FPM connection. If present, install Hondata Mobile on my phone — free backup "gauge" that doesn't need the LattePanda.

---

## 11. Vehicle-Specific Notes: Civic Si 2006-2011 (MY CAR) — CAPTURED (DEFINITIVE)

### Supported Models + ECU Part Numbers

| Year | Region | Features | ECU Part Numbers | FlashPro Model |
|------|--------|----------|-----------------|----------------|
| **2006** | USA | No VSA | RRB-A04 to RRB-A05, RRB-305 | Civic Si Americas |
| **2007-2011** | **USA** | **VSA** | **RRB-A060 to RRB-A140** | Civic Si Americas |
| 2007-2011 | Mexico | — | RRB-X110 to RRB-X120 | Civic Si Americas |
| 2007-2011 | Central America | — | RRB-K010 to RRB-K020 | Civic Si Americas |
| 2007-2011 | South America | — | RRD-M110 to RRD-M120 | Civic Si Americas |
| 2007-2011 | South America | — | RRD-M210 to RRD-M220 | Civic Si Americas |
| 2007-2011 | South America | — | RRD-P110 to RRD-P120 | Civic Si Americas |
| 2007-2011 | South America | — | RRD-P210 | Civic Si Americas |

**My car:** 2009, USA = **RRB-A060 to RRB-A140 ECU** family. Has VSA. **FlashPro Model: Civic Si Americas.**

Note: the CLAUDE.md file says my ECU is "PRB." The Hondata Supported Models table here uses **RRB**. These may be different part number prefixes (e.g., PRB could be a shorthand for the family, or RRB is the actual part number). **[VERIFY]** my actual ECU P/N by looking at the sticker on the ECU or in FPM's FlashPro window when connected.

### Feature List (What My Calibration Supports)

**General:**
- ✅ Forced induction support
- ✅ Expanded tables
- ✅ Live tuning
- ✅ Active fuel tuning
- ✅ **Wideband lambda input**
- ✅ **Boost control output** (for future if I ever go turbo)
- ✅ **Ethanol content input (flex fuel!)**
- ✅ Traction control input

**Fuel:**
- ✅ AFM, MAP, OR hybrid AFM/MAP tuning
- ✅ Injector size & fuel pressure parameters
- ✅ Injector voltage compensation
- ✅ MAP fuel tables (VE-based)
- ✅ AFM fuel tables (mass flow based)
- ✅ Full load compensation tables (WOT)
- ✅ Overall fuel trim
- ✅ Cranking fuel trim
- ✅ Cranking fuel table
- ✅ After start fuel table
- ✅ Cylinder fuel trim (per-cylinder)
- ✅ Air temperature fuel trim
- ✅ Coolant temperature fuel trim

**Ignition:**
- ✅ Ignition tables (low + high cam)
- ✅ Tip-in retard compensation
- ✅ Gear ignition compensation (different timing per gear)
- ✅ Cranking base ignition
- ✅ Cylinder ignition trim
- ✅ Air temperature ignition trim
- ✅ Coolant temperature ignition trim

**VTEC/VTC:**
- ✅ VTEC RPM window (low + high)
- ✅ VTEC pressure window (MAP-based)
- ✅ VTEC conditions (min ECT, min VSS)
- ✅ VTEC oil pressure input enable/disable
- ✅ Cam angle tables (VTC target)
- ✅ VTC PID parameters (cam control loop tuning)

**Closed Loop:**
- ✅ Short, medium, long term trim limits
- ✅ Full load determination tables (MAP AND TPS methods)
- ✅ Wideband current to lambda conversion table
- ✅ Target lambda

**Knock:**
- ✅ Knock ignition limit
- ✅ Knock sensitivity table
- ✅ Knock retard table

**Rev Limits:**
- ✅ Overall rev limiter
- ✅ Launch rev limiter
- ✅ Speed limiter
- ✅ Boost cut (if adding FI)
- ✅ Full throttle shift (flat-foot)
- ✅ Anti-lag (for FI)

**Sensors:**
- ✅ AFM calibration
- ✅ MAP sensor selection (stock or Hondata 4-bar)
- ✅ Speed adjustment (ECU-side)
- ✅ Speed adjustment (dash-side)

**Idle:**
- ✅ Idle speed tables
- ✅ After-start idle speed table

**Throttle:**
- ✅ Target throttle plate table
- ✅ Overrun throttle closure (rev hang reduction)
- ✅ Tip-in fuel

**Misc:**
- ✅ Various sensor enable/disable (ELD, ECT2 are the critical ones for me)
- ✅ Various DTC enable/disable
- ✅ Cooling fan sensor selection (radiator bottom sensor or cylinder head sensor)
- ✅ Cooling fan temperature (on/off points)

### Platform-Specific Notes (Hondata official)

1. **Engine oil life not functional with race calibration.** Switching from race to normal calibration → **Maintenance Minder needs to be reset** (see Section 6.17).
2. **Trip meter not functional with race calibration.**

**Implication:** if I run a race calibration (non-CARB) for Sport map, the trip meter won't work and oil-life indicator gets weird. Might be worth keeping both Daily AND Sport as AFM-based / CARB-compliant if possible. Depends on what calibration the Sport map starts from.

---

## 12. Updating Calibrations — CAPTURED

**Why update calibrations:** important that cals are uploaded via the CURRENT FPM version to properly datalog and use current parameters.

**Process:**
1. Last uploaded calibration stored on FlashPro → download via Online menu → Download
2. Re-upload via Online menu OR Ctrl+U
3. For secondary calibration: FlashPro window → Calibrations tab → Download button in Secondary Calibration section, then re-upload via Upload button

**When this matters for me:**
- After FPM version updates
- If I ever move the FlashPro to a different PC
- To verify what's actually flashed on the ECU vs what I think is flashed

---

## 13. Frequently Asked Questions — CAPTURED

### FlashPro Basics

**"Do I need to leave the FlashPro plugged in?"**
No. Once reflashed you may remove the FlashPro.

**"Can I leave the FlashPro plugged in?"**
Yes. When ignition is off, FlashPro enters power-saving mode (~10 mA draw). Will discharge battery faster than normal but should give several weeks of life on a normal-sized battery.

**"Can I use the FlashPro on more than one vehicle?"**
FlashPro can only be locked to one vehicle at a time. Not recommended to switch between vehicles unless selling.

**"What is the difference between FlashPro OG and FlashProMini?"**
**Just physical construction.** The board inside is functionally identical. Same software, same features.

### 2006 Civic Calibrations — Critical for My Build

**"When should I use AFM-based vs MAP-based calibration?"**
- **AFM:** stock with bolt-ons. AFM auto-compensates for different exhausts, minor mods. Works for mild cams. Doesn't work well for FI or large cams that send reversion pulses back to the AFM.
- **MAP:** required for forced induction + large cams. More flexible, more tuning needed.

**For my build:** I can use AFM for my full-bolt-on NA K20Z3 with Skunk2 Alpha + Skunk2 Ultra Street. If I ever went FI or large cams, switch to MAP. **AFM-based calibration is the simpler starting point.**

**"What starting calibration should I use?"**
- **AFM cal:** choose based on INTAKE (affects AFR the most)
- **MAP cal:** choose based on INJECTOR SIZE or specialty (supercharged, etc.)

**"How do I tune fuel for AFM calibration? There are no fuel tables."**
AFM measures airflow; ECU injects to stoich AFR mathematically. No tables. If AFR is off at part-throttle, the AFM is reading wrong from an aftermarket intake — edit the **AFM Flow table** to correct. At WOT, ECU applies the WOT lambda adjustment table on top of the AFM-based calculation.

**"I see knock retard — how is the knock sensor used?"**
Knock sensor tells ECU (over time) what octane fuel it's running. ECU can retard timing even with NO knock events because the highest-octane ignition limit table caps timing. You shouldn't normally see much knock retard for more than a short period.

**"Does 'Use MAP to determine WOT' only work on MAP-based calibrations?"**
**No.** AFM calibrations ALSO use the MAP sensor — for everything except fuel, they use the MAP sensor. The AFM is specifically for fuel calculation only.

**"How accurate is the stock lambda sensor?"**
Fairly sensitive/responsive, but reads progressively richer as it heats up. Dyno run can show gaining 1.0-1.5 AFR points as sensor heats. **Check with your own wideband if possible.** (See Section 6.35 for AF.Corr.)

**"The idle is not quite right after the reflash."**
Takes 3-4 cold-cycle driving cycles for ECU to "learn" the idle. Don't panic after first flash — give it time.

---

## 14. Error Reporting — CAPTURED

FPM can generate error reports when encountering problems. Some are app-level, some OS-level (Windows reports).

**Privacy:** Hondata asks users to send reports for bug tracking. **No personal information sent.** You can see what's being sent before transmission if concerned.

---

## 15. Verified vs. To-Verify Summary (UPDATED)

**✅ VERIFIED from official Hondata help + evidence:**
- FPM 4.6.6.0 changelog (K20Z3 PRB unchanged in 4.6.x)
- FlashProOG physical spec (210g, 6ft cable, 0-70°C)
- 9-16V supply, <100mA active
- **ISO 15765 CAN protocol** (not K-line)
- Windows 10/11, USB, internet required
- 20-hour onboard datalog memory
- 4x faster than OBDII standard
- **Dual calibration support: primary + secondary on unit, button combo switching**
- HTML export for calibrations exists
- `.fpcal` format (magic bytes `41 4B`)
- Calibration files are binary encrypted/compressed (~22KB)
- **Flash time: ~90 seconds** (not 20-45 as estimated)
- **PRB ECU pin allocation:** A23 ELD, A33 ECT2, B2 EGR out, B29 EGRL, C27 SO2
- **Flex fuel wiring: ECT2 (A33) for K-series Civic Si**
- **Wideband wiring: A23 (ELD), A33 (ECT2), or B29 (EGRL) — NOT C27 (SO2)**
- **WOT AFR ceiling: 12.50:1** (Hondata official; above this ECU won't switch to open loop correctly)
- **VTEC bounds: 2500-6500 RPM** (K-series oil pressure / rocker float)
- VTC control: 0-50° crank degrees, ~10° per 0.1 sec rotation rate, locked at 0° for 10 sec after startup
- **Active Tuning exists: ECU-side self-tuning for fuel + AFM tables**
- **Lua Plugins: real automation path (corrects earlier doc)**
- **DDE Server for Excel integration**
- **Bluetooth on FlashPros sold after Nov 2013** (my unit likely has it)
- Civic Si 06-11 supports: forced induction, flex fuel, live tuning, active tuning, wideband input, boost output, TC input

**🟡 TO VERIFY (action items):**
1. Whether my FlashPro has Bluetooth (check FPM → FlashPro tab → Hardware)
2. Whether Hondata Plugins community has a reliability-guard plugin OR I write my own
3. Exact voltage-to-ethanol mapping for my chosen ethanol controller (Innovate ECF-1 vs Zeitronix ECA) once purchased
4. Whether my ECU is RRB-A060 through RRB-A140 (look at sticker on ECU or FPM connection)
5. Whether the `performance tune.fpcal` is AFM-based or MAP-based (affects whether it's appropriate for my current hardware state)
6. Test all major FPM features in a safe order (File → New Calibration, Tables Follow VTEC toggle, F3-F8 shortcuts, Compare Calibration) before first flash

**⚠️ CORRECTED from earlier docs:**
- ~~"Flex fuel wires to SO2 pin"~~ → **Wires to ECT2 (A33) pin**
- ~~"FlashPro has no public API"~~ → **Has Lua Plugins + DDE Server**
- ~~"Original FlashPro is ALL wired, no Bluetooth"~~ → **Post-Nov-2013 units have Bluetooth**
- ~~"20-45 sec flash time"~~ → **~90 seconds**
- ~~".fpc extension"~~ → **.fpcal**
- ~~"VTEC floor is 4500 RPM"~~ → **Hondata official floor 2500 RPM for K-series** (my reliability-first target 4500 is my own stricter rule)
- ~~"Wideband goes to FlashPro analog input"~~ → **Wideband goes to ECU pin (ELD/ECT2/EGRL)**

---

## 16. Vehicle Locking — CAPTURED (from live WebFetch 2026-04-19)

Source: https://www.hondata.com/help/flashpro/vehicle_locking.htm

**Core rule:** "A FlashPro may only be used on one vehicle at a time, where it is locked to the vehicle's ECU."

**Transferring between vehicles:**
- Unlock FlashPro from original ECU BEFORE moving to a different vehicle
- Applies to both selling the unit and swapping to another car

**Vehicle replacement scenario:**
- When replacing vehicle, "the FlashPro should be unlocked from the old ECU before the ECU is removed from the vehicle"

**Damaged ECU edge case:**
- If original ECU is damaged and can't be unlocked normally → send BOTH old ECU + FlashPro to Hondata for unlocking

**Design philosophy:**
- FlashPro is NOT designed to be switched between vehicles regularly
- Multi-vehicle users: buy separate FlashPros per vehicle

**For my build:**
- Unlock BEFORE selling the car (if I ever sell)
- If my ECU ever gets damaged, I need to keep both ECU + FlashPro for Hondata unlock
- Don't plan to move this FlashPro to another car — it's married to this SI

---

## 17. Writing a Plugin (Lua) — CAPTURED (from live WebFetch 2026-04-19)

Source: https://www.hondata.com/help/flashpro/writing_a_plugin.htm (note: page title says "Hondata SManager" — the guide is shared between SManager/S300 and FPM. Path substitution required: use FPM plugin directory instead of SManager's.)

### Plugin Structure

Three files required:
1. **`main.lua`** — primary script
2. **`info.xml`** — metadata / manifest
3. **`desc.rtf`** — description (currently unused by FPM but required)

### Plugin Directory Path

For SManager (per Hondata docs): `C:\Users\<user>\AppData\Local\Hondata\SManager\Plugins`

**For FPM (inferred):** `C:\Users\<user>\AppData\Local\Hondata\FlashPro\Plugins` — **[VERIFY]** exact path on my machine. Likely mirrors SManager's structure.

### Basic Template

```lua
require("utilities")

function main
-- add code here
end
```

`main` executes when I select the plugin from the menu.

### Distribution Manifest (info.xml)

```xml
<id>unique_identifier</id>
<version>1</version>
<name>Plugin Name</name>
<description>What it does</description>
<author></author>
<url></url>
<license>Apache 2.0 License</license>
<depends></depends>
```

**`id` must be unique** across all plugins.

### Packaging

1. Zip all 3 files (main.lua, info.xml, desc.rtf) into a `.zip`
2. Rename extension from `.zip` to `.fplugin`
3. Share / install via FPM's Plugins menu

### Plugin Ideas for My Build

Now that I have the structure, first plugins I'll write:

**`reliability-guard.fplugin`** — fires on `OnCalibrationClose` or `OnCalibrationNew`. Reads all WOT lambda cells (low + high cam), verifies ≥ 0.85 lambda (12.5 AFR). Reads timing table peaks, flags if any cell > 28°. Reads rev limit, flags if > 8400. Shows `MessageBox` with violations before allowing save.

**`auto-csv-export.fplugin`** — fires on `OnDatalogClose`. Iterates all frames × all sensors, writes CSV next to the .fpdl. Includes calibration name and mod list as header comments for future Claude ingestion.

**`log-summary.fplugin`** — fires on `OnDatalogClose`. Post-drive report: max RPM, max knock count, STFT/LTFT peaks, AFR min/max at WOT, ECT max, injector duty max. One-screen summary after every drive.

I'll build these after my first few dyno sessions so I have real data to test against.

---

## 18. Community Tune Landscape (from web research 2026-04-19)

### Off-the-Shelf Tunes Available for My Car

#### **HARDmotion FBO Max Tune** ($199 on sale, MSRP $290)
Source: https://hardmotion.com/2006-2011-honda-civic-si-fbo-hondata-max-tune/

**Calibrated for:**
- 3-3.5" intake (MAP-based — requires MAF removal)
- Race header w/ or w/o cat
- 2.5-3" race exhaust
- Optional J35/J37 throttle body

**Key changes:**
- **MAF removal** — "runs without the maf and allows for a much more aggressive intake pathway"
- **VTEC engagement advanced 500-800 RPM earlier** — smoother transitions, quicker low-end response

**Claims:** +30-40 HP total gain over stock with tune (14 intake + 14 header + 10 exhaust).

**⚠️ Compatibility with my current hardware:**
- My K&N Typhoon intake is AFM-based (keeps the AFM sensor in place)
- HARDmotion tune is **MAP-based, removes the AFM** — **NOT directly compatible with my current setup**
- Would require going to a tube-only intake AND doing AFM→IAT-sensor conversion (see Section 6.31)
- **Verdict: SKIP for now.** Only relevant if I later switch to a tube intake.

#### **zoshmfg 8th Gen Si FBO Tune** ($80)
Source: https://zoshmfg.com/products/8th-gen-si-full-bolt-ons-hondata-flashpro-tune

**Calibrated for:**
- Hybrid Racing CAI (or equivalent)
- Skunk2 Alpha Header + Exhaust (or equivalent)
- Stock K20Z3
- 1000cc or stock 310cc injectors
- Stock RBC intake manifold + stock throttle body
- 93 octane

**⚠️ RED FLAG — One customer review notes:**
> "at WOT, afr shows 13.4-13.7, which is lean"

**13.4-13.7 AFR at WOT EXCEEDS Hondata's 12.50:1 ceiling and violates my reliability-first rule.** This tune is too lean for my engine longevity priorities. Tuner may have done this intentionally for peak power, but it's unsafe for a 170k-mile K20Z3.

**Verdict: AVOID WITHOUT MAJOR MODIFICATIONS.** If I wanted an off-the-shelf tune in this category, I'd need to either:
- Use it as a starting point and have a dyno tuner pull fuel/timing to safe territory
- Skip it entirely and get a custom tune from BrenTuning / HARDmotion / Church

#### **Community base maps on 8thcivic.com forum**

Community-reported experience (from the Hondata FlashPro Base Maps thread):
- **"Skunk2 Alpha + CAI + Skunk2 exhaust" base map:** conservative ignition (low values). Safer for reliability but leaves power on table.
- **Intake-only base map:** users report VTEC engagement around 4500 RPM works well. "Great pull with awesome drivability and gas mileage around 26-28 city."

### FPM Built-in Base Map Library

**Hondata ships 56 built-in starting calibrations** per their product docs. For my platform they include:
- Stock equivalent
- Intake only (various brands — K&N, AEM, Injen, etc.)
- Intake + header
- FBO (intake + header + exhaust + tune)
- Injector-upsize variants
- Supercharged variants (SC)
- Race (non-CARB) variants
- CARB-compliant variants where available

**My starting point:** since my car is K&N Typhoon + stock everything else, I want the **"Stock + K&N intake" AFM calibration** as my first flash. The other 55 base maps exist but aren't relevant until I add more hardware.

### Dyno Numbers to Expect (community-validated)

| State | Dyno type | WHP | WTQ | Source |
|-------|-----------|-----|-----|--------|
| Stock | Well-calibrated | 170-175 | ~135 | k20a.org consensus |
| Stock + CAI | Dynojet | 178-188 | ~140 | 8thcivic threads |
| CAI + header + exhaust + base tune | Dynojet | 200-210 | ~150 | 8thcivic Skunk2 threads |
| **FBO + professional dyno tune** | **Dynojet** | **220-235** | **155-165** | community consensus + 4Piston/HARDmotion results |
| FBO + E85 tune | Dynojet | 230-245 | 165-175 | projected, community estimates |
| Max FBO (built heads/cams) | Dynojet | 240-260 | 170-180 | beyond my scope |

**Reality check:** the earlier reference docs said stock = 185 WHP. **Web research says 170-175 WHP is more accurate for stock on a "well-calibrated" dyno.** Difference = some shop dynos read optimistic. My expectation for FBO should be 220-230 on a honest Dynojet, 215-225 on Mustang/Dynapack.

### WOT AFR + Timing Targets (community-validated)

For NA K20Z3, consensus from multiple sources:

| Parameter | Conservative (my target) | Community typical | Hondata ceiling |
|-----------|--------------------------|-------------------|-----------------|
| **WOT AFR (pump 93)** | 12.0-12.5 | 12.5-13.0 (0.85-0.89 lambda) | 12.50 (won't open-loop above) |
| **WOT ignition (peak)** | 24-26° | 24-26° proven safe; 28° borderline | "Don't rely on knock sensor" |
| **VTEC engagement (stock)** | 5400-5600 | 5700 | 6500 max |
| **VTEC engagement (FBO)** | 4800-5200 | 4475-5100 common | 2500 min |

**Key insight from community (k20a.org / hpacademy):**
> "One K-series engine on the dyno showed timing at WOT was 24-26 degrees, and while a pull at 28 degrees made a couple more HP, it wasn't worth the risk."

This reinforces my reliability-first rule. 24-26° is the street-safe ceiling for pump 93. Leave 28° for dyno-verified special calibrations only.

### Tune Sources to Consider for My Build (ranked by fit)

1. **BrenTuning remote** — community-trusted, $300-450 per revision, works from my datalogs. **Best fit for my reliability priorities.**
2. **Custom dyno session** at Church / 4Piston / HARDmotion for Tune #3 (flex fuel) — $500-800
3. **FPM built-in base map** for initial flash (free) — "Stock + K&N intake" AFM variant
4. **Community base map from 8thcivic** — free but conservative; good fallback
5. ~~HARDmotion FBO Max Tune~~ — incompatible with my AFM-based setup
6. ~~zoshmfg FBO tune~~ — reports lean WOT AFR, violates my safety ceilings

---

## 19. Hondata Vault — Web Research Note

The Hondata Vault help topic URL I tried (`vault_use.htm`) returned generic site nav, not the actual help content. The Vault exists and is covered in Sections 6.52-6.53 of this reference from user pastes, but detailed usage docs (registration, login, file operations, calibration details) remain uncaptured.

**What I know:**
- Accessible from Window menu → Vault Search
- Two search types: Text Search + Filtered Search
- Results sortable by clicking column headings
- Used for uploading/downloading calibrations + datalogs to cloud

**Action item:** browse `hondata.com/help/flashpro/` frame-by-frame in a regular browser to find the actual Vault usage URL, then capture. Not critical for my near-term work.

---

## 7. Topics Still to Capture

Topics I still need from the user's paste workflow (priority order):

1. **ECU Connectors** — pin locations referenced by the Wideband doc (EGRL, ECT2, ELD). Resolves wiring path for Phase 6 flex fuel + Phase 17 wideband.
2. **Tuning Guide** — the core how-to-tune doc
3. **Fuel Tables** — every fuel parameter explained
4. **Ignition Tables** — every ignition parameter
5. **VTEC** — engagement settings detail
6. **Cam Angle (VTC)** — phase target tables
7. **Closed Loop Parameters** — contains the wideband settings per 6.8
8. **Idle Control**
9. **Rev Limits** — per-gear details
10. **Launch Control / Flat-Foot Shift / 2-Step**
11. **Torque Management**
12. **Fan Control**
13. **A/C Control**
14. **EVAP / Canister Purge**
15. **Analog Inputs / Gauges** (generic, not wideband-specific)
16. **Sensors** — complete parameter list with units
17. **Datalogger** — full datalog reference
18. **Graphs / Histograms**
19. **Autotune** — big time-saver, need to understand
20. **DTC / CEL Options**
21. **Race Settings / Race Calibration**
22. **Updates** — firmware update process details
23. **Security / VIN Lock / Registration**
24. **Traction Control** (on my platform?)
25. **Keyboard Shortcuts** (partial list already — Section 10)
26. **Troubleshooting**
27. **On-Board Datalogging** — 20-hr unit-side logs
28. **Flex Fuel** — explicit topic if one exists

---

## 8. FPM Config File (FlashPro.ini) — What It Tells Me

Source: `C:\Users\extra\AppData\Local\Hondata\FlashPro\FlashPro.ini`

Selected notable settings (full file preserved for reference):

### User preferences already configured
| Setting | Value | Meaning |
|---------|-------|---------|
| `FileDir` | `C:\Users\extra\OneDrive\Documents\FlashPro Calibrations` | Default folder for .fpcal files |
| `DatalogDir` | Same as above | Default folder for datalogs |
| `PressureUnit` | 4 | Pressure unit (4 = likely kPa) |
| `TempUnit` | 0 | Temperature unit (0 = likely Fahrenheit) |
| `LambdaUnit` | 1 | Fuel unit display (1 = likely lambda, not AFR) |
| `LanguageCode` | en | English |
| `AutomaticUpdates` | 1 | FPM auto-checks for updates |
| `IncludeBetaUpdates` | 1 | Beta updates enabled — worth considering toggling off for reliability |
| `CompressDatalogs` | 1 | Datalogs saved compressed |
| `DisableScreenSaverWhenDatalogging` | 1 | Good practice |

### Autotune defaults (from ini)
| Setting | Value |
|---------|-------|
| `AutotuneMinLambda` | 0.75 |
| `AutotuneMaxLambda` | 1.22 |
| `AutotuneMaxChange` | 10 |
| `AutotuneFreq` | 1 |

These are the default guardrails if I use FPM's Autotune feature. Lambda floor of 0.75 = ~11.0 AFR on gasoline — aggressive but within safe WOT range. Max change of 10 is a percentage change limit per iteration.

### Target Lambda Display Overlays (user-set)
| Setting | Value | Meaning |
|---------|-------|---------|
| `TargetLambdaLow` | 1.00 | Cruise/low-load target = stoich |
| `TargetLambdaMed` | 0.918 | Mid-load target = ~13.5 AFR (mild enrichment) |
| `TargetLambdaHigh` | 0.850 | High-load target = ~12.5 AFR (WOT enrichment) |

These appear to be the user-configured overlay targets for the lambda display feature. **Note: 0.850 lambda at WOT = 12.5 AFR, which matches my reliability-first recommendation for pump gas (12.0-12.5 range).**

### Recent files in ini
1. `performance tune 1.html` (HTML export of performance tune — file no longer exists on disk but was exported)
2. `performance tune.fpcal`
3. `Factory Flash - Stock Tune.fpcal`

The HTML export is the critical workflow — FPM can export a tune as HTML, which IS readable. File was apparently deleted/moved; can be re-exported at any time.

### Window sizes (from ini)
Main window 1200x900 at position (550, 135) — user's current FPM layout. Multi-display form at 1350x252.

---

## 9. Calibration Files (.fpcal) — What I Know From Evidence

### Observed files
| File | Size | Created | Notes |
|------|------|---------|-------|
| `Factory Flash - Stock Tune.fpcal` | 22,431 bytes | 2026-04-19 20:58 | Stock OEM calibration backup |
| `performance tune.fpcal` | 22,842 bytes | 2026-04-18 19:53 | Performance tune (origin unknown — to confirm with user) |

### Format observations
- **Extension:** `.fpcal` (NOT `.fpc` as older community docs sometimes say — I had this wrong in earlier reference docs, correcting here)
- **Magic number:** First 2 bytes are `41 4B` = ASCII "AK"
- **Size:** Both observed files are ~22KB. This is small — file is likely encrypted+compressed because raw parameter tables for a K-series ECU would be many tens of KB uncompressed.
- **Binary encrypted/compressed:** No readable strings in the file. Cannot be parsed outside FPM.
- **Difference between stock and performance:** ~411 bytes. Suggests meaningful calibration changes (populated non-default cells, different tables) rather than just metadata changes.

### What can be exported (machine-readable)
- **HTML report** — File → Save As HTML (or similar menu — need to confirm exact path). Dumps all table values as readable HTML. `performance tune 1.html` in the recent-files list confirms this feature exists.
- **CSV datalog export** — File → Export Datalog → CSV. For log files, not calibrations.
- **Calibration comparison** — FPM has compare feature that shows cell diffs between two `.fpcal` files ([VERIFY exact menu])

---

## 10. Keyboard Shortcuts (from FlashPro.ini)

The ini file exposes every keyboard shortcut currently mapped. Key ones:

| Action | Key Code | Note |
|--------|----------|------|
| `actIgnitionLowSpeed` | 114 | F3 — low-cam ignition table |
| `actIgnitionHighSpeed` | 115 | F4 — high-cam ignition table |
| `actFuelLowSpeed` | 116 | F5 — low-cam fuel table |
| `actFuelHighSpeed` | 117 | F6 — high-cam fuel table |
| `actCamLowSpeed` | 118 | F7 — low-cam VTC table |
| `actCamHighSpeed` | 119 | F8 — high-cam VTC table |
| `actViewGraph2D` | 120 | F9 — 2D graph view (also `actRecord` — datalog start) |
| `actViewGraph3D` | 121 | F10 — 3D graph view (also `actDatalog`) |
| `actEditUndo` | 16474 | Ctrl+Z |
| `actEditRedo` | 24666 | Ctrl+Shift+Z |
| `actEditCopy` | 16451 | Ctrl+C |
| `actEditPaste` | 16470 | Ctrl+V |
| `actEditSelectAll` | 16449 | Ctrl+A |
| `actEditIncreaseSelection` | 16457 | Ctrl+I — increase values in selection |
| `actEditDecreaseSelection` | 16452 | Ctrl+D — decrease values in selection |
| `actInterpolate` | 16464 | Ctrl+P — interpolate between cells |
| `actSmoothSelection` | 16461 | Ctrl+M — smooth selected cells |
| `actAdjust` | 16458 | Ctrl+J — adjust values |
| `actFileNew` | 16462 | Ctrl+N |
| `actFileSave` | 16467 | Ctrl+S |
| `actFillFuelTables` | 16454 | Ctrl+F — fill fuel tables |
| `actAutotune` | 16468 | Ctrl+T — Autotune |
| `actOnlineUpload` | 16469 | Ctrl+U — upload to ECU (FLASH) |
| `actFileExit` | 32883 | Alt+F4 |

### Implication for my workflow
- **F3 / F4 / F5 / F6 / F7 / F8** = jump directly to ignition / fuel / VTC tables, low-cam vs high-cam. Critical shortcut for any table editing session.
- **F9** = start datalog recording. Single tap in car.
- **Ctrl+I / Ctrl+D** = bump selected cells up/down by a user-defined step. Faster than manual entry.
- **Ctrl+P** = interpolate between selected cells. Smooths out any tables I manually edit.
- **Ctrl+U** = flash to ECU. Know this one cold.
- **Ctrl+T** = Autotune. Worth exploring what this actually does before I use it.

---

## 11. Cross-References to Existing Repo Docs

The six reference files from the 2026-04-18 and 2026-04-19 work remain valid as context and overlap with this master file. This file is the **authoritative** reference going forward; the others are supplementary.

| Existing file | Scope | Relationship to this master |
|---------------|-------|------------------------------|
| [hardware-software-deep-reference.md](hardware-software-deep-reference.md) | Hardware + software deep dive | Being superseded by this file as topics are verified |
| [calibrator-tables-reference.md](calibrator-tables-reference.md) | Table-by-table reference | Being validated against official help as user pastes |
| [datalog-analysis-guide.md](datalog-analysis-guide.md) | Datalog reading guide | Still valid — pattern-focused |
| [advanced-features.md](advanced-features.md) | Launch / flat-foot / per-gear | Needs cross-check vs. dual-cal discovery |
| [troubleshooting-and-faq.md](troubleshooting-and-faq.md) | Issues + DTCs | Still valid — operational |
| [tuner-directory.md](tuner-directory.md) | Shop recommendations | Still valid — unchanged by software research |
| [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md) | Daily/Sport + reliability rules | Anchor document — unchanged |
| [overview.md](overview.md) | Summary overview | Stub — can stay or be replaced |

**Rule:** if this master reference conflicts with an older doc, this master wins (because it's verified against Hondata's own help). Any `[VERIFY]` item in this file that later gets confirmed should be updated to remove the flag AND the corresponding older-doc content should be updated to match.

---

## 12. Verified vs. To-Verify Summary

**VERIFIED from Hondata official help + config evidence:**
- FPM 4.6.6.0 release date and changelog
- FlashProOG physical spec (210g, 6ft cable, 0-70°C operational)
- Supply voltage 9-16V, <100mA active
- ISO 15765 CAN protocol (not K-line)
- Windows 10/11 support, USB any version, internet required
- 20 hours onboard datalog memory (unit-side, independent of PC)
- 4x faster datalog than standard OBDII
- Cam angle aware table editing
- `Dual calibration support` exists as a feature (meaning TBD)
- HTML export for calibrations exists
- `.fpcal` format (not `.fpc`) with 41 4B magic number
- Calibration files are binary encrypted/compressed (~22KB)
- Keyboard shortcut mappings (from ini)

**TO VERIFY (priority order):**
1. ~~**What "Dual calibration support" actually enables**~~ — **RESOLVED:** dual-cal is real, on-unit, primary + secondary slots, switch via button combo (Program alone = primary; hold Datalog + Program = secondary). Huge finding.
2. **Flex fuel sensor wiring pin on PRB ECU** — likely EGRL or ECT2 (not rear O2 because wideband wants ECT2 and SO2 is unusable). Need ECU Connectors topic.
3. **Exact menu path for HTML calibration export** (shown in recent files list so it exists; just need the menu path)
4. **Autotune safety** — what Ctrl+T does, whether it respects reliability ceilings
5. **Full parameter list for PRB datalog**

**CORRECTED from earlier docs (these older claims were WRONG):**
- ~~"Original FlashPro cannot switch calibrations on-unit"~~ — wrong, dual-cal slots exist
- ~~"Flash time ~20-45 seconds"~~ — wrong, ~90 seconds
- ~~"Wideband wires to FlashPro analog input"~~ — wrong, wires to ECU input pin (ECT2, ELD, EGRL)
- ~~".fpc file extension"~~ — wrong, it's .fpcal
- ~~"Original FlashPro uses K-line"~~ — wrong, uses ISO 15765 CAN (newer, faster)

---

*Last updated: 2026-04-19*
*Maintainer: LxveAce, with Claude assistance*
*Status: LIVING DOCUMENT — grows as Hondata help topics are captured*
