# Built Motor Bottom End Install Guide — Future-Phase Reference

## Status: FUTURE PHASE — NOT Current Purchase Plan

**Do NOT build at the current 240 WHP target. The stock K20Z3 block is overbuilt for this power level.** This document exists as a capability reference for some future version of me who has decided the power ceiling has changed. Nothing in this guide should be purchased, scheduled, or planned for the current build state.

If you're reading this trying to decide whether to do this work: the answer is almost certainly no. Keep reading for the logic.

---

## Reality Check — Why This Doc Exists

This is a reference in case one of the following happens:

1. **I decide to chase power past 270 WHP NA** — stock cast hypereutectic piston ring lands become the risk at that level, and forged pistons become a real requirement, not a nice-to-have.
2. **I decide to go forced induction** — targeting 400+ WHP on E85 boost requires a bottom end designed for peak cylinder pressures the stock rod bolts were not spec'd for.
3. **The bottom end announces itself** — rod knock, sustained oil-pressure drop, spun bearing, piston slap that won't quiet with warm oil. At 170k+ miles this is a non-zero risk even without power chasing.
4. **Oil consumption goes past 1 quart / 1000 miles** — but investigate valve seals and PCV first; rings are usually the last suspect, not the first.

At the current 240 WHP pump-gas target none of the above is on the radar. The stock K20Z3 block has a documented community safety window of roughly **240-270 WHP NA pump gas and ~400 WHP boost on E85** with a proper tune and the supporting mods I already have planned (ATI damper, Hondata tune, cooling refresh, wideband AFR). I don't need to open this engine.

### What a built motor actually is

Before committing, I need to understand that "build the bottom end" is not an install — it is an **engine build**. Specifically:

- **The engine comes OUT of the car.** Not the head off. The entire engine on a stand. That's a 1-2 day job by itself.
- **The short block comes apart on a stand.** Another full day of measured, documented disassembly with inspection at every step.
- **Machine shop work is mandatory.** Nobody reassembles a 170k-mile block without a shop honing under a torque plate, checking deck flatness, Magnafluxing the crank, and balancing the new rotating assembly. Mandatory is not an exaggeration. Skipping this step is how people make $4,500 worth of bearings dust inside 1,000 miles.
- **Reassembly with plastigage clearance check on every bearing.** This is the core skill difference between "swapped parts" and "built an engine." Plastigage every rod journal, plastigage every main journal. Every time.
- **Realistic timeline:** 2 weekends of DIY wrenching bookending 1-2 weeks of machine shop turnaround = **3-4 weeks the car is out of service**. Plan transportation for that month before taking anything apart.

### Cost ballpark

| Path | Cost |
|------|------|
| DIY with machine shop support (my likely path if I go here) | **~$4,444-4,944 parts + ~$800-1,200 machine work** |
| Shop-assembled short block (parts I supply, labor billed) | ~$5,444-6,444 |
| Turn-key 4Piston K-Series Street Short Block (drop in, bolt up) | **~$4,500-5,500 all in** |

The turn-key path is genuinely competitive with DIY once I account for the machine shop bill, the specialty tools I don't own (torque plate, rod bolt stretch gauge, dial bore gauge), and the risk of a first-time engine build. Covered in detail under *Turn-Key Alternative* below.

---

## Decision Tree — WHEN to Build

This is the flowchart that gets checked against reality before any parts are ordered.

| Current state | Decision |
|---------------|----------|
| 240 WHP target, block healthy, no knock | **DO NOT BUILD.** Stock block is overbuilt for this power level. |
| Power target moves to 270+ WHP NA | Build. Forged pistons and upgraded rod bolts earn their cost here. |
| Decision made to go forced induction at 400+ WHP on E85 | Build. Peak cylinder pressures on boost put the OEM rod bolts out of safe margin. |
| Rod knock diagnosed (audible from bottom end, oil pressure normal at idle then drops under load) | Build. Or yank and swap short block — repair labor is the same order of magnitude as a build. |
| Oil consumption >1 qt / 1000 mi | **Investigate first.** PCV system, valve stem seals, turbo seals (if applicable). Only build if a leakdown test confirms rings, not some other simpler failure. |
| Sustained 9000+ RPM NA race use planned | Build. Oil pump cavitation and crank flex become real at that RPM band. |

**At 240 WHP with a healthy block, this entire folder stays closed.** The money belongs to other phases.

---

## Prerequisites and Cross-References

Before this work starts, these things are either already done or on the same schedule:

- **Cylinder head is either already done or bundled into this job.** See [`../16-Cylinder-Head/overview.md`](../16-Cylinder-Head/overview.md). It's inefficient to do the head once, then pull the whole engine a second time for the bottom end. Ideally the head is already installed on the fresh short block before the engine goes back in the car. If I already did the head in-car as Phase 16, this built-bottom phase pulls everything back apart.
- **Engine out of the car.** Much bigger job than the head-off-in-car approach documented in the head install guide. The transverse K20 can lift either with or without the transmission attached; I'd take it out with the trans for clearance to drop onto a stand cleanly.
- **Machine shop identified and vetted** — specifically for K20 work. Not every engine shop does K-series builds correctly. 4 Piston (Indianapolis), Portflow (Harbor City CA), King Motorsports (Wisconsin), Drag Cartel all qualify. A local generic machine shop may or may not — verify they've done K20s before I hand them a $900 crank.
- **Torque plate available for hone.** This is non-negotiable and the shop should own it. Honing the block without a torque plate simulates unclamped geometry; the bore distorts when the head is bolted back down and the rings don't seal. If a shop says they don't use a torque plate for K20 honing, walk out.
- **Plastigage, telescoping gauge, micrometer, feeler gauges on hand.** These are consumable/inexpensive and live in my toolbox after this.
- **Engine assembly lube** — Royal Purple Max-Tuff or equivalent. Not standard engine oil. Assembly lube stays in place for first fire; oil will drain off bearings and result in a dry start.
- **Clean assembly area.** Not the garage floor. Not next to the grinder. A cleaned workbench with a lint-free surface, no cardboard shedding, no dust, no debris. Bearing failure at 1,000 miles is almost always a cleanliness failure from assembly, not a parts failure.

---

## Tools Required

This is a materially different tool list from anything else in this build. The engine-out, short-block-apart scope needs specialty hardware I don't own.

### Critical specialty tools

| Tool | Why | Approximate Cost |
|------|-----|------------------|
| Engine crane / cherry picker | To lift the engine out. Rentable at AutoZone / O'Reilly for free with deposit. | Rental $0, purchase $150-250 |
| Engine stand (750+ lb rated) | Block mounts to stand for disassembly and assembly. Own this. | $80-150 |
| Tapered ring compressor, 86mm | Compresses piston rings for insertion into bore. Must be 86mm specific. | $35-60 |
| Torque plate for hone | **Shop owns this.** If they don't, find a different shop. | N/A (shop tool) |
| Rod bolt stretch gauge | BC ProH625+ rods are torqued to **stretch**, not torque value. Stretch gauge measures bolt elongation during torque. | $150-250 |
| Plastigage assortment | Bearing clearance measurement. Multiple ranges. | $15 |
| Telescoping gauge set + 2-3" micrometer | Measure bore and big-end ID. Needed for clearance verification. | $80-120 |
| Feeler gauge set, 0.001"-0.025" | Ring gap measurement. | $10 |
| Engine assembly lube (Royal Purple Max-Tuff or equivalent) | Coats bearings at assembly. | $15 |
| Tap set, chase block threads | Main bolt holes, head bolt holes, oil pan threads — all get chased before assembly. | $40-80 |
| Piston ring filer | If Wiseco rings need gap adjustment. | $40-90 |
| Dial bore gauge (ideal, rentable) | Precise bore measurement. Shop may do this step anyway. | Rental or $150-300 |
| Bore gauge / snap gauge for big-end | If assembling rods myself. | Included with telescoping set |
| Dial indicator + magnetic base | Deck height, crank endplay, runout checks. | $40-80 |

### Optional but useful

- **ARP 208-4701 head stud kit** — if going this far, the head studs are getting upgraded if they aren't already from the head phase.
- **ARP main stud kit** — **skip for NA or moderate boost.** OEM Honda TTY main bolts are documented safe to ~500 WHP. Main studs only become necessary for sustained 500+ WHP on boost or race use. Not part of this build tier.
- **Good droplight, clean rags by the box, latex gloves.**

### Tools I already have that carry over

Everything from the head install — torque wrenches (in-lb and ft-lb), standard metric sockets, the Lisle 37950 cam alignment tool, in-lb torque wrench for small fasteners. The engine build adds to the collection, not replaces it.

---

## Parts List (From `overview.md`)

Full detail lives in [`overview.md`](overview.md). Short-form for this install guide:

| Category | Part # | Price | Notes |
|----------|--------|-------|-------|
| Pistons | **Wiseco K573M86AP** 86mm 11.6:1 ArmorGlide | ~$760 | Stock bore. Forged 2618. |
| Rods | **Brian Crower BC6044** ProH625+ H-beam | ~$934 | ARP 625+ bolts included, stretch-torqued. |
| Rod bearings | **ACL 4B1946H-STD** Race tri-metal | ~$90 | Standard clearance; verify with plastigage. |
| Main bearings | **ACL 5M1959H-STD** Race tri-metal | ~$140 | Standard clearance; verify with plastigage. |
| Oil pump | **Honda 15100-PRB-A01** RSX Type S pump | ~$300 | OEM Honda upgrade. Rated to 9500 RPM. |
| Head gasket | **Cometic C4561-030** .030" MLS | ~$120 | Stock-bore 86mm. Confirm deck height first. |
| Head studs | **ARP 208-4701** | ~$200 | Carried over from head phase if already installed. |
| Crank | Reuse stock, **micropolish + balance + Magnaflux** | ~$500 shop labor | Do not skip Magnaflux on a 170k crank. |
| Harmonic damper | **ATI 918477 Super Damper** | $0 (already owned from Phase 15) | Internally balanced K20 compatible. |
| Complete gasket kit + seals | Miscellaneous OEM | ~$150 | Cam seals, VCT seal, valve cover, oil pan, water pump, etc. |
| Timing chain kit | **14401-PNA-004** + guides + tensioner | ~$170 | Fresh chain on fresh bottom end. Non-negotiable. |

**Parts subtotal ~$3,364. Machine shop ~$800-1,200. Grand total DIY ~$4,444-4,944.**

Alternative: see Turn-Key section at end of this guide.

---

## Alternative: Turn-Key 4Piston Short Block

Before committing to DIY assembly: the 4Piston K-Series Street Short Block ships fully assembled for **$4,500-5,500 delivered** — Wiseco/CP forged pistons, H-beam rods with upgraded bolts, race bearings, Honda RSX Type S pump, honed under torque plate, balanced assembly, plastigaged and ship-tested.

| Factor | DIY | 4Piston Turn-Key |
|--------|-----|------------------|
| Cost | $4,444-4,944 | $4,500-5,500 |
| Time | 3-4 weeks out of service + my labor | Ships ready; install is engine R&R only |
| Risk of failure in first 1,000 mi | Non-zero (first-time builder) | 4Piston owns warranty |
| Specialty tools needed | Stretch gauge, bore gauge, assembly tools | None additional |
| Skill acquired | Engine-building experience | None |

**Honest recommendation:** DIY only if I want the experience and have the time. If the goal is "have a built motor," turn-key is equivalent quality at similar money and dramatically lower risk. DIY for learning, turn-key for pure outcome.

---

## Step-by-Step — The Phases

This is a big enough job that it's broken into phases. Each phase is a multi-hour or multi-day chunk. Don't try to chain them — the mental fatigue of 12 straight hours on an engine build is the enemy of bearing clearance precision.

### Phase A: Engine Removal (1-2 days)

The biggest single mechanical step and easily outsourced to a shop ($400-800 to R&R an engine). DIY summary:

1. Disconnect battery negative. Drain coolant, engine oil, transmission oil.
2. Remove intake, exhaust downpipe, any mid-pipe blocking engine lift.
3. Remove all accessories: alternator, A/C compressor (refrigerant must be discharged at a shop first — don't release it yourself), starter, throttle body, intake manifold, valve cover.
4. Disconnect all engine harness connectors and tag them. Photos of everything.
5. Disconnect fuel line at rail, shift cables at trans, clutch hydraulic line at slave.
6. Remove axles from hubs. Remove all engine and transmission mounts.
7. With hoist on factory lift points, lift slowly while rocking the engine/trans out. Drop front subframe if needed for clearance.
8. Split the trans from the engine on the ground — lighter lifts than pulling the assembly as a unit.
9. Mount bare engine to stand via four-bolt plate.

Realistic time: 1 day if cooperative, 2 days with seized bolts. At 170k miles, assume everything is seized.

### Phase B: Short Block Teardown (1 day)

With the engine on the stand (head already off — see head install guide):

1. Remove timing chain cover and chain (see [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md)). Chain replaced on reassembly — not reused.
2. Invert block on stand. Remove oil pan, pickup tube, windage tray. Stock oil pump is saved for comparison measurement only; new **Honda 15100-PRB-A01 RSX Type S pump** goes in on reassembly.
3. **Plastigage the OLD rod bearings before removing them** — baseline data. Was the block in spec before teardown? A journal measuring 0.004" clearance pre-teardown means crank or bearings were already past spec; good data for the machine shop.
4. Remove rod bearing caps one at a time. Bag each cap with its matching rod — caps are matched to rods from the factory, never swap.
5. Push each piston + rod UP through the top of the block. K20 is designed top-out, not bottom-out; rods won't clear crank counterweights if driven down.
6. Plastigage the OLD main bearings — same baseline exercise, all 5 mains.
7. Remove main caps (numbered — photograph anyway). Lift crank out onto clean padded surface, journals contacting nothing.
8. Block is stripped. Bag all hardware, label everything, photograph the block from all sides.
9. **Send to machine shop** with the full service menu: hone to Wiseco 86mm spec under torque plate, deck check/resurface if needed, line hone mains, hot tank clean, Magnaflux block, pressure test coolant passages. Crank: micropolish, chamfer oil holes, full rotating-assembly balance with new rods + pistons + damper, Magnaflux for cracks.

### Phase C: Machine Shop Work (1-2 weeks, shop handles)

Shop checklist (pricing in [`overview.md`](overview.md) Machine Shop Menu):

- **Block:** hot tank clean, Magnaflux, pressure test coolant passages, deck flatness check (resurface if warped — may need thicker gasket to restore deck height), hone to Wiseco spec (typically 400-450 grit plateau cross-hatch), line hone mains.
- **Crank:** polish journals to ≤0.0002-0.0005" taper, chamfer oil holes, Magnaflux, full balance with new pistons + rods + ATI damper.
- **Rods (BC):** shop weighs the pair, verifies big-end matches crank journal + bearing combo.
- **Pistons (Wiseco):** inspect for shipping damage, measure ring gaps against actual bore.

**If bores are worn beyond hone spec:** machine shop quotes an overbore. K573M86AP is stock-bore 86mm — any overbore needs a different piston P/N (86.5mm or 87mm) and different Cometic gasket bore. Full re-quote event; verify with Wiseco that matched pistons exist at the overbore size before signing off.

### Phase D: Pre-Assembly Prep (full day of careful work)

Before a single bolt goes back in, everything gets cleaned and measured.

1. **Thread-chase every bolt hole in the block** — main, head, oil pan, accessory brackets. Debris in a bolt hole gives false torque reading and bottoms bolts before proper clamp load.
2. **Brush all oil passages** with a long bottle brush. Air-blow clean. Brush again. Grit trapped in a main oil feed comes out at 3,000 RPM and starves a bearing.
3. **Wipe cylinder bores** with ATF on a lint-free cloth until cloth comes out clean white. Twice. Hone residue is invisible and scores piston skirts inside 100 miles.
4. **Crank prep:** journals wiped with assembly lube, verified round to ≤0.0002", taper ≤0.0005".
5. **Main bearing clearance:** install ACL main halves dry, torque caps to Honda (or ARP) spec, plastigage each journal. **Target: 0.0015-0.0018"** per ACL spec sheet. Out of spec = stop, diagnose with shop. Never "install and see."
6. **Rod bearing clearance:** assemble each BC rod with ACL 4B1946H-STD dry, torque rod bolts to BC stretch spec (~0.005-0.006" — verify with BC instruction sheet), plastigage each journal. **Target: 0.0015-0.0025"** per ACL spec sheet.
7. **Ring gap verification in the actual honed bore:** push ring square with a piston, measure top ring gap. **Target 0.018-0.022" for NA pump gas**; wider (0.024-0.028") for E85/boost heat expansion. Follow Wiseco sheet, not rules of thumb. File with ring filer 1-2 strokes at a time if under spec — never over-gap (under-gap is fixable, over-gap = new rings).
8. **Piston-to-wall clearance:** measure with micrometer + dial bore gauge. **Target 0.0025-0.0035" for Wiseco ArmorGlide** per Wiseco spec sheet.
9. **Deck height:** assemble one piston + rod on crank, measure at TDC. Zero or slight positive deck normal; excessive negative deck kills quench.

Document everything on a build sheet. If something comes apart later, the build sheet is the diagnostic baseline.

### Phase E: Short Block Assembly (1-2 days careful work)

Clean bench. Latex gloves. Everything lubed. Don't rush.

1. **Main bearing upper halves into block.** Bearing backs DRY (oil between shell and block blocks heat transfer). Assembly lube on the face that contacts the crank.
2. **Lower crank into mains.** Two-person lift — crank is heavy, bearings don't appreciate being dropped on.
3. **Main bearing lower halves into caps** with assembly lube on the face. Caps numbered and directional — arrows to front of block.
4. **Torque main bolts per Honda spec** (or ARP if using main studs). Multi-step torque-plus-angle on TTY main bolts. Follow FSM exactly — see [`../docs/torque-specs.md`](../docs/torque-specs.md).
5. **Rotate crank by hand** — smooth with moderate resistance. Any bind = STOP, remove caps, diagnose.
6. **Plastigage one main journal** post-final-torque as sanity check.
7. **Install piston rings** with gap orientations 120° apart — never aligned (creates blow-by path).
8. **Rod bearings into big-ends** with assembly lube on face, tang seated in rod notch.
9. **Piston + rod into bore through top of block** with ring compressor. Rod cap OFF. Lower with gentle thumb pressure — NEVER force. If it doesn't slide, stop: check ring orientation in compressor, check skirt coating isn't catching a bore edge.
10. Guide rod onto crank journal. Install cap + lower bearing half + assembly lube. Factory tang orientation.
11. **Torque rod bolts by STRETCH.** BC ProH625+ specs stretch, not torque. Initial torque to BC's starting value (~40 ft-lb typical), measure bolt length with stretch gauge, torque more, re-measure, until stretch = BC target (~0.005-0.006"). Verify with BC instruction sheet.
12. **Rotate crank after each rod.** Resistance increases slightly per rod, never BINDS. Binding = stop, diagnose — one tight bearing tang = seized engine at first start.
13. Repeat 7-12 for all 4 pistons.
14. **Oil pump (new Honda 15100-PRB-A01)** torqued to Honda spec. New oil pump chain. New pickup, new gasket.
15. **Windage tray** (reuse stock unless damaged).
16. **Oil pan with fresh gasket.** Small Hondabond bead at case-half corners — too much clogs the pan.

Short block assembled. Photograph before inverting for head install.

### Phase F: Head Install

At this point, follow [`../16-Cylinder-Head/install-guide.md`](../16-Cylinder-Head/install-guide.md) (when written) or the equivalent procedure documented in head/overview.md. Whether the head is the 4Piston Pro 156v2 drop-in from Phase 16 or a refreshed stock head, the install procedure on a fresh short block is the same as on an in-car head swap. One difference: cam timing is set while the engine is still on the stand (easier than in-car), and I can verify cam timing by turning the crank through multiple rotations and confirming no valve-to-piston contact.

Timing chain goes on fresh per Phase 5 procedures.

### Phase G: Engine Back In The Car (~1 day)

Reverse of Phase A. Mount engine to transmission (or install alone and mate trans after), lift into bay with crane, drop onto mounts, connect axles, reconnect all harnesses, refill all fluids.

Check oil level TWICE before first crank. Prime the oil system before first start — see Phase H.

### Phase H: First-Start Break-In (CRITICAL)

A fresh engine lives or dies in the first 30 minutes. Do not rush this.

1. **Prime the oil system before first crank.** Pull coil relay so engine can't fire. Crank starter in 10-second bursts (30-second cool breaks) until oil pressure gauge reads positive — typically 20-30 seconds total cranking. This sends real oil through bearings (assembly lube has been holding them over).
2. **Non-synthetic break-in oil.** Joe Gibbs Driven BR30 or Brad Penn. Synthetic is too slippery for ring-to-bore seat-in. Break-in oil for first 500 miles minimum.
3. **First start.** Plug coils back in. Should fire within 3 seconds. If it cranks past 5 seconds: STOP, re-verify cam timing, fuel, spark.
4. **Hold 2000-2500 RPM for 20 minutes immediately on first fire.** No idle, no rev — steady RPM. Cam break-in window (same procedure as fresh head in [`../16-Cylinder-Head/`](../16-Cylinder-Head/)). Watch coolant rising normal, oil pressure holding, no unusual sounds. Light smoke from assembly-lube burn-off on headers is normal; thick blue-white smoke past 5 minutes is NOT.
5. **Shut off at 20 minutes, cool to room temp, drain break-in oil, refill with fresh break-in oil.** First 20 minutes captures assembly debris and ring-seat metal fines — throw it away.
6. **Drive 500 miles on break-in oil with VARIED load.** Not steady cruise — rings need load variation to seat. Accelerate moderately to 4000 RPM, back off, engine brake. No WOT, no sustained high RPM.
7. **Change oil at 500 miles.** Cut filter, inspect. Sparkles normal (bearing break-in); chunks demand investigation.
8. **Switch to full synthetic at 500 miles.** Normal oil cycle resumes.
9. **No WOT until 1000 miles.** Ring seat completion window.
10. **At 1000 miles:** compression + leak-down test all 4 cylinders. Record numbers — baseline for every future comparison. If rings not seated (compression low, leakdown high), extend break-in 500 more miles and retest.

---

## Post-Build Dyno Retune (MANDATORY)

A fresh engine has materially different operating characteristics than the engine that was on the dyno before teardown. Do not drive on the old calibration past break-in. Book a dyno session immediately after 1000-mile break-in.

What changes:
- Volumetric efficiency curve is different (fresh bore seal, different compression ratio if built CR differs from stock)
- Ignition timing sensitivity — built motor with forged pistons has more tolerance for advance but also more consequence for detonation
- Fuel requirements shift with any compression change
- New oil pump pressure curve affects VTC response

Budget **$500-800 for a proper dyno retune** — same as the head-install retune budget in [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md). This is the non-negotiable finish line on the build cost.

---

## First Drive Checklist

Before driving beyond the immediate neighborhood after break-in procedures:

- [ ] Oil pressure normal at idle (20+ PSI hot), rises to 45-60 PSI at 3000 RPM
- [ ] Coolant temp stabilizes at thermostat setpoint, no runaway
- [ ] No unusual knocks, taps, or ticks at any RPM (light top-end tick from VTA is normal; bottom-end knock is NOT)
- [ ] No smoke at any throttle position past the first 2 minutes of running
- [ ] No coolant loss over first 30 miles
- [ ] No oil loss over first 100 miles (some consumption during ring seat is normal; leaking is not)
- [ ] No CEL, no pending codes on OBD scan
- [ ] Fuel trims within normal range (±5% LTFT)

Anything that fails this checklist gets diagnosed BEFORE the next drive, not deferred.

---

## Common Mistakes in K-Series Builds

Bearing failure at 1,000 miles is almost always one of these. Every one is preventable.

1. **Assembling without plastigage verification.** "It felt right" is not a measurement. Every bearing gets plastigaged.
2. **Reusing rod bolts.** BC ProH625+ bolts are NEW ONLY. Stretch-torquing yields the bolt; reusing a yielded bolt is how rod caps exit the block.
3. **Wrong ring gap.** Under-gap closes at operating temp and breaks rings; over-gap leaks blow-by. Follow Wiseco sheet, measure in the honed bore, file conservatively.
4. **Skipping torque plate during honing.** Unclamped bore geometry differs from head-torqued geometry — no torque plate = non-round bores at operating condition = rings don't seal.
5. **WOT before break-in complete.** Rings don't fully seat until 1000 miles of varied load. WOT at 200 miles glazes the bore permanently.
6. **Dirty assembly area.** Dust in an oil passage becomes bearing dust in 1000 miles. Clean bench, lint-free rags, latex gloves, no cardboard.
7. **Skipping machine shop inspection.** A 170k block can have water-jacket cracks, deck warp, bore taper past hone spec. Pressure test, Magnaflux, deck check — all of it.
8. **Wrong torque spec for hardware.** Hardware spec overrides block spec. ARP follows ARP torque-with-lube; BC rods follow BC stretch. Always the HARDWARE'S sheet.
9. **Pistons in wrong orientation.** Wiseco marks front-of-engine direction. Flipped 180° = valve reliefs misaligned = bent valves on first crank.
10. **Skipping oil prime before first start.** Assembly lube covers seconds, not 5+ seconds of firing without pressure. Crank with coils disconnected until gauge reads.
11. **Wrong oil for break-in.** Synthetic too slippery for rings to seat. Break-in oil first 500 miles, no exceptions.
12. **Swapped rod caps or main caps.** Caps are matched from the factory — bag everything at teardown.

---

## See Also and Cross-References

- [`overview.md`](overview.md) — the parts I'd pick and the rationale, with full pricing and alternatives
- [`../16-Cylinder-Head/overview.md`](../16-Cylinder-Head/overview.md) — head side of the puzzle; ideally done before or bundled with this phase
- [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) — timing chain install during reassembly, same procedure on fresh block
- [`../15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) — ATI Super Damper already owned, transfers unchanged to built motor
- [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — mandatory post-build dyno retune
- [`../11-Wideband-AFR/overview.md`](../11-Wideband-AFR/overview.md) — wideband critical for safe break-in AFR monitoring
- [`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) — upgraded cooling is prerequisite for built motor power level
- [`../19-Flex-Fuel-and-Fuel-System/overview.md`](../19-Flex-Fuel-and-Fuel-System/overview.md) — fuel system re-evaluation at built-motor power level
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — main bolt, rod bolt, ARP, cam cap, head stud torque values
- [`../docs/maintenance-parts-catalog.md`](../docs/maintenance-parts-catalog.md) — add built-motor part numbers when the phase goes live

---

*Last updated: 2026-04-20*
