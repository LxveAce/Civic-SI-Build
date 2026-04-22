# Ignition Refresh Install Guide — Plugs + Coils + VTC Actuator

## Status: Pending (Phase 0.5 — before any tune)

This is the clean-baseline job. Plugs, coils, and VTC actuator all get replaced before the FlashPro ever gets plugged in. At 170k miles, any one of the three being tired will lie to a tuner — phantom misfires, drifting cam angle, inconsistent AFR — and I refuse to chase ghosts on the dyno. Fix the hardware first, then tune.

---

## Reality Check

Two jobs under one folder, with an enormous difficulty gap.

**Phase A — Plugs + Coils.** 45 minutes, easy. A 10mm socket, a 5/8" plug socket, and a torque wrench. Zero scary moments unless I cross-thread an iridium plug.

**Phase B — VTC Actuator.** 4-6 hours standalone, much harder. Pull crank pulley (one-time-use yield bolt), pull timing cover, lock cams with a Lisle 37950, release chain tension, break the actuator center bolt with a controlled breaker-bar pull (no impact), fit the revised 14310-RBC-003, rebuild with fresh gaskets and a new crank bolt. Install wrong — bad orientation, cams not locked, reused crank bolt — and I bend valves.

**The single most important decision on this page:** do not schedule the VTC actuator standalone. Bundle it with the timing chain service (see `../05-Timing-Chain-Maintenance/`). The cover is already coming off for chain inspection; the actuator is the first thing behind it. Labor-wise, the actuator goes from "4-6 hours, scary" to "+30 minutes while I'm in there." Doing VTC standalone means 80% of a timing chain job without doing the chain — insane at 170k.

**Rule:** if the timing cover comes off, actuator and chain set both get serviced.

---

## Prerequisites and Cross-References

### Hard rule — do this BEFORE any dyno session or FlashPro flash

Phase 0.5 sits between basic maintenance and the first tune.

- No FlashPro flash until Phase A (plugs + coils) is complete.
- No FlashPro flash until the cold-start rattle is resolved — Phase B done, or confirmed-not-needed via clean cold-start datalog.

### Bundle with timing chain (strongest recommendation here)

See `../05-Timing-Chain-Maintenance/overview.md`. The 14310-RBC-003 actuator is shared labor with the chain service — chain inspection + actuator replacement share the same 4-6 hours of access work. Every downstream decision — FlashPro flash, dyno, headers, E85 — assumes this cover has been opened and both jobs done.

### Related files

- `../05-Timing-Chain-Maintenance/overview.md` — bundle target, labor sharing
- `../05-Timing-Chain-Maintenance/install-guide.md` — master procedure for cover removal, TDC setup, cam lock install, reassembly
- `../10-Hondata-FlashPro/tuning-workflow-and-maps.md` — the tune this unblocks
- `../docs/torque-specs.md` — every fastener in this guide cross-referenced
- `overview.md` — parts picks, reasoning, forum research

---

## Tools Required

### Phase A (plugs + coils)

| Tool | Purpose |
|------|---------|
| 10mm socket, 1/4" drive | Coil hold-down bolts |
| 5/8" spark plug socket (thin-wall, rubber insert) | Iridium plugs |
| 6" and 10" extensions, 3/8" drive | Plug well access |
| 3/8" ratchet | General |
| **Torque wrench, in-lb range (0-250 in-lb)** | Coil bolts at 108 in-lb (9 ft-lb) |
| **Torque wrench, ft-lb range** | Spark plugs at 13 ft-lb |
| Copper anti-seize (sparingly) | Plug threads |
| Dielectric grease | Coil boot interiors |
| Shop vac or compressed air | Plug-well debris |

### Phase B (VTC actuator)

Everything in `../05-Timing-Chain-Maintenance/install-guide.md`, plus:

| Tool | Purpose | Cost |
|------|---------|------|
| **Lisle 37950 K-series cam lock** | Locks both cams at TDC. Without it the cams spring-rotate and hit valves. Non-negotiable. | ~$40 |
| 19mm socket + 24"+ breaker bar | Crank pulley bolt (131 ft-lb factory, often 200+ after 170k) | Own |
| Crank pulley holder (or impact) | Holds crank while breaking bolt | ~$35 / loaner |
| **Torque wrench to 131 ft-lb+** | Crank bolt step 1 and VTC actuator at 83 ft-lb | Own |
| Torque angle gauge | Crank bolt: 37 ft-lb + 90° | ~$20 |
| 3/8" in-lb torque wrench | Timing cover at 8.7 ft-lb | Own |
| Plastic or brass gasket scraper | Cover mating surfaces — NO STEEL on aluminum | ~$10 |

### Consumables specific to Phase B

| Part | P/N | Notes |
|------|-----|-------|
| Valve cover gasket kit | **12030-PNC-000** | Kit — includes plug tube seals + grommets |
| Timing cover sealant | **Hondabond HT 08718-0004** | RTV, not a paper gasket |
| Front crank seal | **91214-RZY-A01** | Press into cover before cover goes back on |
| Crank pulley bolt (TTY, one-time-use) | **90017-RWC-A01** | Old bolt is scrap the moment it comes off |
| Moly 60 assembly grease | 08798-9010 | VTC vanes, cam nose, crank nose |

---

## Parts List

Per `overview.md`:

| # | Part | P/N | Qty | Notes |
|---|------|-----|-----|-------|
| 1 | NGK iridium spark plug | ILZKR7B-11S (NGK 4912) | 4 | Pre-gapped at 0.043" (1.1mm). **Do NOT re-gap.** |
| 2 | Honda OEM ignition coil | 30520-RWC-A01 | 4 | OEM Denso. Honda dealer or majestichonda.com — eBay has fakes. |
| 3 | Honda VTC actuator (REVISED) | **14310-RBC-003** | 1 | The 003 part only. The old 002 is what I'm removing. |
| 4 | Crank pulley bolt (TTY, one-time-use) | 90017-RWC-A01 | 1 | New every time the pulley comes off. |
| 5 | Front crank main seal | 91214-RZY-A01 | 1 | Press into cover on reassembly. |
| 6 | Valve cover gasket kit | 12030-PNC-000 | 1 | Kit, not bare gasket. |
| 7 | Hondabond HT | 08718-0004 | 1 tube | Timing cover sealing surfaces. |

---

## Step-by-Step — Phase A: Plugs and Coils (45 min)

Standalone, bolt-on. Any time before the FlashPro flash.

### A1. Warm the engine, then cool

Start, bring to operating temp (thermostat open, fan cycles once). Shut off. Cool **at least 20 minutes.** The brief warm cycle expands plug threads in the aluminum head slightly, helping break the seal without galling. Head should be cool enough not to burn my hand.

### A2. Disconnect battery negative

10mm. Electrical safety plus ECU short-term fuel trim reset so post-install datalogs start from zero.

### A3. Pull coil #1

- Unplug the harness connector (press tab, pull gently — 170k connector tabs are brittle).
- Remove the single 10mm hold-down bolt.
- Pull the coil straight up with a gentle twist. If it fights, rotate 1/4 turn both ways to break the boot seal, then lift.

### A4. Vacuum the plug well

Shop vac or compressed air at the top of the well. Debris falling into an open combustion chamber scores cylinder walls. 10 seconds of cleaning prevents hours of regret.

### A5. Break the plug loose

Socket + extension, steady pull. **If resistant, do not force.** Small spray of penetrant, wait 15 minutes, retry. Stripped threads in an aluminum head = pulling the head for a Heli-Coil. Patience is free. Once loose, unscrew by hand.

### A6. Inspect the old plug (free diagnostic)

- **Light tan ceramic, mild wear:** healthy.
- **Black sooty carbon:** rich — leaky injector, failing O2, or tired coil misfiring.
- **White/bleached ceramic:** lean or hot — potential pre-ignition.
- **Oily fouling:** valve stem or plug tube seals leaking. Tube seals in kit 12030-PNC-000.
- **Damaged/missing electrode:** detonation. **Stop.** Diagnose before continuing. Do not tune.

Photograph each plug in cylinder order (1 on left) for the record.

### A7. Prep the new plug

Confirm ILZKR7B-11S on box, electrode intact, ceramic clean. **Gap is pre-set at 0.043". Do NOT re-gap iridium** — the fine electrode is fragile. If gap looks wrong, the plug is defective — return it.

### A8. Anti-seize (sparingly)

NGK says skip it on plated threads; on a fresh engine I'd agree. On a 170k engine where previous plugs fought coming out, I apply a thin film of copper anti-seize on threads only — not the electrode, not the first thread from the tip. "Barely visible sheen," not "coated." Over-anti-seize over-torques the plug at a given wrench reading and cracks iridium.

### A9. Hand-thread and torque

Hand-start, all the way down, until seated. **If it binds, back it out and restart.** Cross-threaded iridium in aluminum = head-off repair. Torque wrench to **13 ft-lb (156 in-lb).** Firm click. Do not "give it a little extra."

### A10. Coil back in

- Small dab of dielectric grease inside the coil boot. Keeps moisture out, helps the boot release next service.
- Coil straight down, feel it seat. Reinstall 10mm bolt.
- **Torque to 108 in-lb (9 ft-lb)** with the in-lb wrench. M6 strips easily.
- Reconnect harness, listen for the click.

### A11. Repeat for 2, 3, 4

One cylinder at a time. Never all four out simultaneously — if I'm interrupted, I know exactly where I stopped.

### A12. Reconnect battery, verify start

Battery (-) back on. Key to ON 5 seconds (fuel prime), then start. Idle smooths within 10 seconds as the ECU relearns trims. Any misfire, rough idle, or CEL = a coil connector isn't fully seated. Pull and re-seat.

---

## Step-by-Step — Phase B: VTC Actuator (4-6 hrs standalone, or +30 min bundled with timing chain)

**The master procedure for timing cover removal, TDC verification, and cam lock install lives in `../05-Timing-Chain-Maintenance/install-guide.md`.** I am not duplicating it. This section covers actuator-specific steps, assuming the cover is off and the cams are locked with a Lisle 37950.

If doing the actuator standalone, follow `../05-Timing-Chain-Maintenance/install-guide.md` Phases A-G to get the cover off, come back here, then return to that document's Phases L-P for reassembly.

### B1. Crank pulley removal (see 05 guide)

Loosen crank pulley bolt (131 ft-lb factory, expect more after 170k). Breaker bar + holder tool or impact. Bolt is **discarded** — TTY one-time-use. Slide pulley off.

### B2. Timing cover removal (see 05 guide)

13 bolts of varying lengths. Three are on the oil-pan face and easy to miss. Score the old Hondabond, tap the cover off gently, clean both mating surfaces with a plastic scraper + brake cleaner to bare aluminum. No steel scrapers.

### B3. TDC, cam marks, cam lock — prerequisite state

- Crank at TDC cylinder 1 (pulley mark to pointer).
- Both cam gear marks (triangles/dots) point straight up, parallel to head surface.
- **Install Lisle 37950 now.** Cams must be mechanically locked before any torque touches the actuator bolt. Without the lock, cams spring-rotate under valve spring pressure and valves hit pistons.

### B4. Release chain tension

Locate the cam chain auto-tensioner on the passenger side. Retract the piston per its design (small lever/pin; see 05 guide Phase H). Insert the retainer pin. Chain is now slack enough to work.

### B5. Break the VTC actuator center bolt

- Reinstall torque is **83 ft-lb.** Coming out after 170k it may be tighter.
- **NO IMPACT WRENCH.** Actuator internals (vane, spring) are shock-sensitive, especially on a failing unit. Controlled pull only.
- Cam is held by the Lisle 37950. Breaker bar on the bolt, steady pull, break loose. Spin off by hand.
- Remove the old actuator — it slides off the intake cam nose. Keep for comparison (002 and 003 look nearly identical externally, but 003 is what I'm installing).

### B6. Chain off old actuator, clean cam nose

Slip chain off the actuator sprocket. **Zip-tie chain to the head** so it doesn't fall into the oil pan. Wipe cam nose, inspect for scoring/galling. Expected: light wear. If chewed, the old actuator was failing a while and may have contaminated oil — early oil change at break-in.

### B7. Install the new 14310-RBC-003

- **Verify part number on the box.** 14310-RBC-003. Not 002. Not an aftermarket knockoff.
- Light coat of Moly 60 on the cam nose and the actuator's internal vane surface.
- Slide the actuator onto the cam nose. **Orientation matters.** The actuator has an alignment dot/arrow that must match the cam reference feature. **Wrong orientation = bent valves the instant the chain is loaded.** See Honda service manual or `../05-Timing-Chain-Maintenance/install-guide.md` Phase I for exact mark locations.
- Route chain over the actuator sprocket, keeping colored alignment links on the cam marks if reusing the chain.

### B8. Torque actuator center bolt to 83 ft-lb

- Hand-thread fully.
- Torque wrench to **83 ft-lb (113 N·m).** One steady click. Cam held by Lisle 37950 throughout — the lock absorbs torque reaction, not the chain or valvetrain.
- **No impact. Dry threads** (unless Honda FSM page that ships with the actuator specifies Moly 60 on threads — some years do).

### B9. Release chain tensioner, verify slack

Pull the tensioner retainer pin. Tensioner extends and pulls chain slack. Visually inspect: taut on tension side, free on slack side. Cam marks still aligned. Crank still at TDC.

### B10. Release cam lock, rotate crank 2 full turns, re-verify

- Remove Lisle 37950.
- Using a 19mm on the crank bolt hole (or snug the pulley temporarily for grip), **rotate crank BY HAND, clockwise only, two full turns (720°).**
- Return to TDC cylinder 1. Verify cam marks still aligned with each other AND the crank TDC mark.
- **If marks don't line up, STOP.** Chain is one tooth off. Re-lock cams, release tension, correct, torque again, repeat. Do not start the engine until right.

### B11. Timing cover back on with fresh Hondabond

- Press new **91214-RZY-A01** front crank seal into the cover (lip inboard, clean press — see 05 guide).
- 2-3mm bead of Hondabond HT around the mating surface. Extra dab at corners (cover-to-head-to-block junctions).
- Cover on within 5 minutes (skin-over time).
- **Torque bolts to 8.7 ft-lb (12 N·m)** crisscross center-outward. In-lb torque wrench — the big ft-lb one can't measure this low accurately.

### B12. Crank pulley reinstall — NEW yield bolt

- Moly 60 on crank nose.
- Slide pulley on.
- **NEW 90017-RWC-A01 bolt.** Old one is trash.
- Sequence per Honda FSM: **131 ft-lb, then loosen fully, then 37 ft-lb, then +90° angle.** The breakaway-then-retorque cycle is how TTY bolts reach correct preload.

### B13. Reassemble accessories, coolant (if drained), oil

Follow `../05-Timing-Chain-Maintenance/install-guide.md` Phases L-N for full reassembly order. Valve cover with new 12030-PNC-000 kit, torque 7.2 ft-lb spiral-out, Hondabond HT dabs at the 4 cam cap corners. Fresh oil + filter. Coolant top-off if the cooling system was opened.

---

## First Start Checklist

1. **Key to ON, listen for fuel pump prime (2-3 sec buzz).** Cycle 3 times (ON, pump stops, OFF, ON).
2. **Start.** Should catch within 3 seconds. If cranking past 5-6 seconds, stop — something is wrong, likely cam timing or a disconnected sensor.
3. **Listen at idle for:**
   - **No cold-start rattle** in the first 1-3 seconds. If I hear the familiar K20Z3 rattle, the new actuator isn't working — wrong orientation, wrong part (002 vs 003), or install fault. Shut down, pull the cover.
   - **Smooth idle within 10-20 seconds.** Rough idle usually means a loose coil connector or ECU relearning trims — give it a minute.
   - **No CELs.** P0341/P0344 = cam position. P0011/P0014 = VTC phase error. Any of these = pull cover, verify timing.
4. **Idle 3-5 minutes.** Watch for leaks — valve cover, timing cover, coolant if water pump was touched.
5. **Short drive, 5-10 min, below 4000 RPM.** Verify it drives. No WOT, no VTEC engagement.

---

## Dyno-Ready Verification (Before FlashPro Tune #1)

Before the first flash, I pull a baseline datalog on the factory calibration with fresh ignition hardware. Three things must be true:

1. **Short-term fuel trim (STFT) within ±8%** at idle and 2500 RPM cruise. Larger = vacuum leak or fuel/air issue, fix before tuning.
2. **Misfire counters zero** over a 10-minute mixed-RPM log (Mode 6 via FlashPro datalog viewer). Any cylinder misfiring = bad coil connector or unseated plug.
3. **Cam angle actual tracks commanded** within ~2°, no oscillation at idle-to-2500 transitions. VTC health check — weak actuator shows lag/oscillation, healthy -003 tracks cleanly.

All three clean = dyno-ready baseline. `../10-Hondata-FlashPro/tuning-workflow-and-maps.md` is the next file to open.

---

## Common Mistakes

| Mistake | Consequence | Prevention |
|---------|-------------|------------|
| Cross-threading iridium into aluminum head | Stripped threads = Heli-Coil or head removal | Hand-thread fully before any wrench touches it |
| Re-gapping an iridium plug | Broken electrode = defective plug | Pre-gapped from factory. Don't touch the electrode. |
| Over-torquing the plug | Cracked ceramic, broken tip in cylinder | **13 ft-lb.** Torque wrench only. |
| Over-torquing coil hold-down bolt | Stripped M6 in head | **108 in-lb (9 ft-lb).** In-lb wrench. |
| Over-torquing VTC center bolt | Actuator damage, phantom VTC DTCs | **83 ft-lb.** Hand wrench. Cam held. |
| Reusing the crank pulley bolt | Stretches past yield, loosens, eats crank gear | Always new 90017-RWC-A01. Old is scrap. |
| Not locking cams during actuator install | Cams spring-rotate, valves hit pistons, bent valves | **Lisle 37950 before the actuator bolt gets touched.** Non-negotiable. |
| Wrong actuator orientation | Cam phase impossible, bent valves on first start | Verify alignment marks per FSM. Slow-rotate 2 turns by hand before starting. |
| Installing superseded 002 instead of -003 | Cold-start rattle doesn't go away; job wasted | Verify part number on the box. Order by VIN from Honda dealer. |
| Impact wrench on the actuator bolt | Damages internal spring and vane | Breaker bar only. Cam lock absorbs torque. |
| No dielectric grease in coil boots | Water intrusion, arcing, stuck boots next service | Small dab inside every boot. |

---

## See Also

- `overview.md` — part selection, forum research, cost summary
- `../05-Timing-Chain-Maintenance/overview.md` — **bundle target.** Chain service shares 100% of the actuator's access labor.
- `../05-Timing-Chain-Maintenance/install-guide.md` — master procedure for cover removal, TDC verification, cam lock install, reassembly
- `../10-Hondata-FlashPro/overview.md` — first flash only after Phase A and Phase B complete and the dyno-ready checklist passes
- `../10-Hondata-FlashPro/tuning-workflow-and-maps.md` — daily/sport map rules, datalog workflow
- `../docs/torque-specs.md` — build-wide torque reference
- `../docs/maintenance-parts-catalog.md` — full OEM part number catalog

---

*Last updated: 2026-04-20*
