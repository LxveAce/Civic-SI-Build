# Hondata FlashPro Install Guide — First-Flash Procedure

## Status: Purchased, first flash pending

This doc covers ONLY the first flash: unboxing the FlashPro, registering it, reading and saving my stock calibration, flashing a conservative community base map matched to my current mod state (K&N intake only), verifying no CELs, and capturing my first baseline datalog.

It does NOT cover:
- The permanent LattePanda in-car install — see `Permanent-LattePanda-Install/full-guide.md`
- Actual tuning, table edits, or dyno work — see `tuning-workflow-and-maps.md`
- Daily/Sport dual-map creation — that's post-exhaust, covered in the tuning workflow doc

---

## Reality Check Before I Start

**Time budget:** 1-2 hours. ~30 min prep, ~20-30 min connect/read/backup, 2-3 min actual write, the rest for verification and the first datalog drive.

**Technical difficulty:** LOW. Almost no wrenching — plug a cable into OBD2, click buttons in a Windows app, watch a progress bar.

**Cognitive stakes:** HIGH. A mid-write interruption is recoverable (the ECU keeps the old calibration and FPM offers Resume). But flashing on a weak battery can damage the FlashPro-to-ECU pairing and cost me a $200+ Hondata recovery fee. And flashing without a stock backup first is a choice I can't undo — once a new calibration is over the factory one, the only way back is the `.fpc` I saved.

**Rule #1, no exceptions:** Stock backup before any write. That saved file is the factory reset button. Without it, every subsequent decision becomes a bet on "will this work?" instead of "I can always roll back."

**Rule #2:** Stable 12V during the write. Trickle charger on, accessories off, key held steady.

First-time ECU tuner. I take this slow, read every FPM dialog twice, and if anything feels off I stop and ask before clicking Yes.

---

## Prerequisites — Don't Skip

### Cross-references — things that must be done FIRST

| Do First | Why |
|----------|-----|
| [Phase 0.5 Ignition Refresh](../06-Ignition-Refresh/) complete | Fresh plugs, healthy OEM coils, and the revised 14310-RBC-003 VTC actuator. If baseline ECU state is already throwing P0011/P0014 or misfires, my first datalog will be noise and I can't tell if a new calibration made anything better or worse. |
| [K&N Typhoon intake](../01-Cold-Air-Intake/) installed | Already done. This is the one mod driving the need for a base map over factory. |
| FlashPro unboxed, cable verified in bag | USB Mini-B specifically. Don't lose it — original FlashPro uses Mini-B, not Micro or C. |
| Hondata account created at hondata.com | Registration binds the unit to my account. Do this BEFORE I'm sitting in the driveway with the cable in my hand. |
| 93-octane tank, at least half full | Stable fuel pressure matters during idle verification, and any performance calibration wants premium. |

### Vehicle + Environment Prerequisites

- **Stable 12V battery.** 12.6V resting, 13.8V+ with alternator charging. If mine is marginal, I replace it before flashing. A weak battery under ignition-on load for 10+ minutes will sag, and a sagging battery mid-write is the scenario Hondata specifically warns against.
- **Trickle charger / battery tender connected during the flash.** Hondata recommends this explicitly. Clamp to battery terminals (NOT the jump-start points under the hood — those have a fuse that can isolate), set to maintenance mode.
- **Windows x86 laptop or desktop.** FlashProManager (FPM) is Windows-only, x86 only. No Mac, no Linux, no ARM tablet. My Windows laptop is what I'll use for Phase 1 (this first flash) before the LattePanda takes over permanently.
- **Admin rights on the laptop.** FPM installer + FTDI driver both need admin.
- **Antivirus disabled for the flash session.** Windows Defender occasionally quarantines the FlashPro USB-serial driver or flags FPM. Disable for the duration, re-enable after.
- **USB Mini-B cable** — ships in the box. Don't substitute a random drawer cable unless mine is actually damaged; cheap unshielded cables have been blamed for comms dropouts on the 8thcivic.com forum.
- **Key ON, engine OFF during the write.** Do not touch the key, start the engine, or disturb the ignition while the progress bar is moving. Period.

### Don't start this if

- Battery is old or weak and I haven't put the tender on it for 2+ hours
- My laptop's battery is <50% and no charger is plugged in
- I'm rushed — can't give this an uninterrupted 90 minutes
- There's a pending Windows Update that wants to reboot
- Any existing CEL is lit (diagnose and clear first — a stored P0011 or P0300 will poison my first datalog)

---

## Tools Required

| Item | Notes |
|------|-------|
| Windows x86 laptop | Dedicated for Phase 1. Will be replaced by LattePanda in Phase 2. |
| FlashProManager (FPM) software | Latest version from hondata.com/downloads. Free, requires account. |
| FTDI VCP driver | From ftdichip.com/drivers/vcp-drivers/. FPM installer usually includes it, but a fresh install from FTDI is the troubleshooting-proof path. |
| USB Mini-B cable | From the FlashPro box. |
| OBD2 cable | BUILT INTO the FlashPro unit — the opposite end of the housing from the USB port. No separate cable needed. |
| Trickle charger / battery tender | OEM-style or CTEK. 2A maintenance mode is plenty. |
| Multimeter (optional but wise) | Verify battery voltage before flashing rather than trusting the dash gauge. |
| Notepad | Physical or digital. Write down serial numbers, dialog text, any error codes. I don't want to be searching my browser history later. |

---

## Parts List

| # | Item | Source | Status |
|---|------|--------|--------|
| 1 | Hondata FlashPro (original, not FP2) | Hondata retailer | Owned |
| 2 | USB Mini-B cable | In FlashPro box | Owned |

That's it. Everything else (laptop, charger) is existing gear.

---

## Step-by-Step — Phase A through Phase H

### Phase A: Pre-Flash Setup (Laptop Prep) — 20-30 min, done the day before

Done on the couch, not in the car. Getting software and drivers right ahead of time means I'm not troubleshooting Windows in the driveway.

1. **Create a Hondata account** at hondata.com. Use a real email — registration mail goes there.
2. **Download FlashProManager (FPM)** from hondata.com/downloads. Install with admin rights; accept FTDI driver prompts; reboot if asked.
3. **Launch FPM once, no FlashPro connected.** Confirm it opens cleanly, then close.
4. **Plug the FlashPro into a direct USB-A port** (NOT a hub, dock, or USB-C adapter — FTDI serial comms are latency-sensitive).
5. **Open Device Manager → Ports (COM & LPT).** I should see "USB Serial Port (COMx)". Yellow warning or under "Other Devices" = reinstall the FTDI VCP driver from ftdichip.com/drivers/vcp-drivers/.
6. **Disable Windows Update auto-restart, sleep timers, and antivirus** for the session. Revert immediately after.
7. **Register the FlashPro.** In FPM, open the registration dialog, enter the unit serial (from the housing sticker) and my Hondata credentials. This binds the unit to my account. No flashing works until registration is done, and re-registering it onto a different ECU later is a $200 fee.
8. **Verify FPM shows FlashPro as connected** via View → FlashPro Status — unit serial and firmware version visible.
9. **Let FPM update FlashPro firmware if prompted.** Do this with the unit on USB only (NOT plugged into OBD2), on laptop AC power.

Close FPM, unplug the FlashPro, set it aside with the cable.

### Phase B: Vehicle Prep — 10 min

Car parked in the garage, cool, overnight if possible. Cold sensors give the cleanest first datalog.

10. **Park nose-in on a flat surface.** Parking brake on.
11. **Connect trickle charger to the battery** per its manual. Verify 12.6-13.8V maintenance reading. Leave connected the entire session.
12. **Hood up** for battery access and engine-bay eyeballing on first start.
13. **All accessories OFF.** Radio, climate, headlights, cabin lights. Every amp the accessories pull is an amp the ECU doesn't get.
14. **Verify battery voltage** via multimeter or dash gauge at key-ON: 12.6V+ resting.
15. **Set up driver's-seat workstation.** Laptop on passenger seat or lap desk, charger plugged in, water/coffee ready. I'll be sitting here 45-60 min.
16. **Confirm no dash CELs lit** at key-ON. Any existing stored code gets written down now before I touch anything.

### Phase C: Initial Connection + ECU Read — 10-15 min

17. **Plug FlashPro's OBD2 end into the OBD2 port** (under dash, driver's side, left of steering column on FG2). Push firmly — connector clicks when fully seated. A loose OBD2 seat is the #1 cause of mid-session comms dropout.
18. **Plug USB Mini-B into FlashPro, USB-A into the laptop's direct port** (same port I tested in Phase A).
19. **Key to ON (position II), engine OFF.** Dash wakes up, ECU powered. Do NOT crank.
20. **Verify FlashPro LEDs.** Power LED solid (USB enumerated); OBD/ECU link LED solid within a few seconds (K-line handshake established).
21. **Launch FPM.** Auto-detects the FlashPro — confirm via View → FlashPro Status.
22. **Run Tools → Read from ECU.** Pulls the factory PRB calibration off the ECU into FPM as a saveable file.
23. **WAIT.** The read is slower than a write — 2-5 minutes is realistic. DO NOT interrupt, touch the key, or wiggle the cable. Watch the progress bar.
24. **FPM displays ECU type.** Should read PRB (any sub-rev like PRB-A00 or PRB-A58 is fine). Anything else = STOP; wrong car or comms issue.

### Phase D: STOCK BACKUP — 5 min, critical

The single most important step in this document.

25. **File → Save As** in FPM.
26. **Name it** `STOCK_PRB_2026-04-20_pre-any-flash.fpc`. YYYY-MM-DD for clean sort order.
27. **Save to local disk** under my build folder (`C:\Users\extra\OneDrive\Desktop\Civic-SI-Build\10-Hondata-FlashPro\calibrations\`). OneDrive syncs to cloud automatically — but I don't trust that alone.
28. **Copy the file to a second location** — external USB or a fresh cloud upload. Two independent copies.
29. **Verify file size non-zero** (typical `.fpc` is a few hundred KB).
30. **Close FPM, reopen FPM, open the saved `.fpc`** to confirm it loads and shows tables. An unreadable backup is no backup.
31. **Write the filename and save location in my build notes.**

This file is now my factory reset button. If anything downstream goes wrong, flashing this file returns the car to factory ECU state.

### Phase E: Base Map Selection — 10 min

Current mod state is stock everything + K&N Typhoon intake, so I want an "intake-only, 91/93 pump gas" 8th-gen SI community base map. Hondata ships a library of these with FPM, plus more on 8thcivic.com.

32. **Open the base map library** (File → Open, typically `Documents\Hondata\FlashProManager\Calibrations\`).
33. **Pick the closest match to my hardware.** Intake-only, pump gas, no other mods. DO NOT pick anything assuming exhaust, headers, intake manifold, or E85 — mismatched maps run lean or pig-rich and CEL or worse.
34. **Review the base map in FPM before flashing:**
   - **AFR at WOT:** commanded >= 12.0. Leaner on pump gas = red flag.
   - **Rev limiter:** <= 8200 RPM (stock). A 9000 RPM rev limit is not a first-flash map.
   - **Ignition timing at WOT:** not more aggressive than stock.
   - **VTEC engagement:** stock-ish (~5400-5800 RPM).
   - **Knock correction:** enabled, not disabled.
35. **Save a working copy** as `BASE_intake-only_<date>_working.fpc`. Never flash the original base file — keep the source pristine.

If no community base map is a perfect match, I'd rather flash the stock backup right back and wait for a tuner recommendation than flash something mismatched.

### Phase F: THE FLASH — 5 min, no touching anything

36. **Verify battery voltage still 12.6V+.** Below 12.3V = STOP, fix, restart.
37. **Close all other Windows programs.** FPM only. No browser, no Slack, no background updaters.
38. **In FPM: Tools → Flash Calibration** (or Program ECU, version-dependent). Select the working copy of my base map.
39. **Read the confirmation dialog.** Should show calibration name, ECU type (PRB), and not-interrupting warning. Accept.
40. **Progress bar starts.** Write takes ~20-45 seconds.
41. **DO NOT TOUCH ANYTHING.** Not laptop, key, OBD2 connector, or USB. Hands in lap.
42. **Wait for "Program Complete" dialog** — flash is done when it appears.
43. **Do NOT immediately power cycle the key.** Let the ECU settle a few seconds, dismiss the dialog, then touch the key.

**If the flash fails mid-write:** DO NOT restart the flash on my own. The ECU keeps its previous (stock) calibration. FPM detects incomplete flashes on next connection and offers Resume. If Resume fails or anything feels wrong, call Hondata support BEFORE further action.

### Phase G: First-Start Verification — 10-15 min

44. **Cycle key OFF, wait 10 sec, back to ON.** Listen for 2-second fuel pump prime from the rear. No prime = stop, something's wrong.
45. **Start the engine.** Should fire cleanly on first crank. Long crank or rough start = yellow flag.
46. **Idle 3-5 min, hands off throttle.** Watch dash for CEL.
47. **If a CEL lights:** shut off, connect FPM, pull the code, do not drive. P0301-P0304 = likely mismatched base map; flash stock backup and regroup. P0420 = base-map rear-O2 settings; not dangerous but worth understanding. P0011/P0014 = base-map issue OR pre-existing VTC actuator issue that Phase 0.5 should have fixed.
48. **No CEL = good.** Verify basics:
   - Idle RPM stable 700-800
   - ECT climbing normally toward 190-200F
   - No exhaust smoke (brief cold-start vapor is normal)
   - No unusual ticking, pinging, rattle
49. **Short test drive, 5-10 min mixed conditions.** Neighborhood streets, gentle acceleration. NO WOT, NO VTEC pulls. Verifying the car behaves normally, not tuning.

### Phase H: First Datalog — 20-40 min

First real log with the FlashPro. Goal is a clean baseline I can compare future drives against, not a performance session.

50. **Open FPM → Datalogger view.**
51. **Configure datalog parameters.** Explicitly include: RPM, VSS, TPS, APP, MAP, IAT, ECT, Commanded AFR, STFT, LTFT, Primary O2, Rear O2, Knock Count, Knock Retard, Commanded Ignition Advance, Actual Ignition Advance, Battery Voltage, VTEC state, VTC target, VTC actual, Injector Duty %. I can't recover data I didn't log.
52. **Datalog → Start.**
53. **Drive 15-30 min of mixed conditions:**
   - 2-3 min idle in driveway before pulling out (cold-start behavior)
   - Low-speed neighborhood (25-35 mph, light throttle)
   - Highway cruise (60-70 mph, steady throttle) for 5+ min to stabilize trims
   - Light-to-moderate partial throttle, 2500-4500 RPM
   - **NEVER WOT.** Not without a wideband, not before Tune #1 on the dyno.
   - **DO NOT hit VTEC deliberately.** Keep under 5000 RPM.
54. **Back home, engine idling: Datalog → Stop.**
55. **File → Save Datalog As** → `baseline_intake-only_<YYYY-MM-DD>.fpdl`. Double-save (local + cloud + external).
56. **File → Export → CSV** for a human-readable copy I can paste into Claude.
57. **Quick review in FPM:**
   - Knock Count = 0 across entire log. Any non-zero = investigate.
   - STFT within +/- 8% during closed-loop cruise.
   - LTFT still learning — will drift for the first few drives.
   - ECT 190-210F at cruise.
   - Commanded vs actual ignition advance track together. Large gap = knock correction active.
   - No limp mode, no CEL, no stored codes.

Clean across the board = verified success. Subsequent work (headers, exhaust, dyno tunes) lives in other docs.

---

## First-Start Checklist

- [ ] Stock calibration saved locally AND to a second location
- [ ] Stock `.fpc` file opened and verified readable
- [ ] Base map reviewed for safe AFR, rev limit, timing, VTEC
- [ ] Battery 12.6V+ with tender connected
- [ ] Accessories off, hood up, key to ON only (not crank)
- [ ] Flash completed with "Program Complete" dialog
- [ ] Engine starts cleanly, idles stable 3-5 min
- [ ] No CEL after 10 minutes of idle + gentle driving
- [ ] First datalog captured, exported to `.fpdl` + `.csv`
- [ ] Knock count = 0 across the entire first log
- [ ] STFT within +/- 8% during closed-loop cruise

---

## Troubleshooting Shortlist

| Symptom | First Check |
|---------|-------------|
| FPM won't see the FlashPro | FTDI driver in Device Manager → reinstall from ftdichip.com if missing or yellow-flagged. See `troubleshooting-and-faq.md` for the full walkthrough. |
| FPM sees FlashPro but can't read ECU | Key at ON (not ACC, not OFF). OBD2 connector fully seated. Battery above 12.5V. No other scantool sharing the port. |
| Flash fails partway through | STOP. Do not start another flash. Reconnect; FPM will detect incomplete flash and offer Resume. If Resume fails or anything feels off, call Hondata support before further action. |
| CEL after flash | Read the code in FPM, compare against the code table in `troubleshooting-and-faq.md`. For anything I don't understand: flash the stock backup back, regroup. |
| Car won't start after flash | Most likely a base-map mismatch. Flash the stock `.fpc` backup to return to factory. Verify start. Re-evaluate which base map I picked. |
| Rough idle after flash | Give the ECU 5-10 minutes of runtime to adapt trims. If persistent, base-map mismatch — revert. |
| USB cable feels loose | Try the other known-good USB Mini-B cable before assuming the FlashPro port is damaged. Never flash on a wobbly connection. |

Full troubleshooting coverage lives in `troubleshooting-and-faq.md`.

---

## Common Mistakes I Am Specifically Watching For

1. **Skipping the stock backup** because "the base map is fine." No. Stock backup every time, before every write. Rule #1.
2. **Flashing on a weak battery.** The one scenario that damages unit-to-ECU pairing and lands me in Hondata's paid recovery. Tender on, 12.6V+, verified.
3. **USB hub or dock** instead of a direct laptop USB-A port. FTDI serial comms are latency-sensitive. Direct only.
4. **Flashing a FlashPro 2 calibration onto my original FlashPro.** Feature flags differ. Only use `.fpc` files confirmed compatible with FlashPro original + 06-11 Civic SI PRB.
5. **Aggressive base map** (headers/exhaust/E85) on an intake-only car. Intake-only community map or nothing.
6. **Interrupting a flash to "check something."** Nothing checks better than letting the write finish.
7. **Antivirus still running** — Windows Defender can quarantine a driver mid-session. Disable explicitly before Phase F.
8. **Losing the USB Mini-B cable** that came in the box. FlashPro original uses Mini-B specifically.
9. **Not writing down the stock filename and backup locations.** Three months from now, finding my stock backup should be a 10-second task.
10. **First-flash + first-datalog in a rushed 30-min window.** This deserves an unhurried afternoon.

---

## Dual-Map Pre-Flight

This guide covers ONLY the first flash of a single, conservative community base map. Daily/Sport dual-map setup is NOT part of the first flash:

- Daily and Sport maps are the product of Tune #1 on a dyno, after headers + HFC + exhaust cutout are installed.
- Full dual-map rules (AFR targets, timing ceilings, VTEC crossover, rev limiter strategy) live in `tuning-workflow-and-maps.md`.
- Switching calibrations on original FlashPro requires a fresh flash each time (~20-45 sec). That's a LattePanda-install concern, not a today concern.

If I catch myself thinking "let me just try a Sport map right now" — no. Not without a wideband, a dyno, a tuner, or knock monitoring during real WOT pulls. First flash is the conservative community base map, full stop.

---

## See Also

- [overview.md](overview.md) — FlashPro hardware basics, cost, and my setup plan
- [hardware-software-deep-reference.md](hardware-software-deep-reference.md) — full engineering detail on the unit and FPM software
- [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md) — Daily/Sport map rules, reliability-first ceilings, how tune sessions are planned
- [troubleshooting-and-faq.md](troubleshooting-and-faq.md) — full code/problem reference
- [../06-Ignition-Refresh/](../06-Ignition-Refresh/) — required prerequisite (plugs + coils + VTC actuator)
- [../11-Wideband-AFR/](../11-Wideband-AFR/) — required before any dyno tune; bung gets welded during header install
- [../19-Flex-Fuel-and-Fuel-System/](../19-Flex-Fuel-and-Fuel-System/) — flex fuel sensor wiring is a separate install, future phase
- [Permanent-LattePanda-Install/full-guide.md](Permanent-LattePanda-Install/full-guide.md) — the in-car PC install this laptop workflow bridges toward
- [../docs/baseline-logs.md](../docs/baseline-logs.md) — A/B datalog protocol I should follow for every mod milestone after this first log

---

*Last updated: 2026-04-20*
