# Clutch Hydraulics Install Guide — Hybrid Racing HYB-CMC-01-20 + RMS + Throwout + Pilot

## Status: Not purchased yet — priority buy

The Hybrid Racing HYB-CMC-01-20 kit isn't in my garage yet, but it's next in the shopping queue. At 170k miles on the original CMC and slave, the 8th gen SI clutch hydraulic system is living on borrowed time. This is a reliability buy. I don't want to be stranded at a red light because the master cylinder decided today was the day its seals gave up.

---

## Reality Check Before I Start

There are two very different jobs hiding inside "clutch hydraulics." I need to be honest about which one I'm doing before buying parts and clearing a weekend.

### Path A — CMC, line, slave only (no transmission removal)

- **Time:** 3-5 hours
- **Difficulty:** Easy intermediate. If I can bleed brakes, I can do this.
- **What I touch:** Firewall CMC, stainless braided line, bellhousing slave. That's it.
- **What stays put:** Transmission, clutch, flywheel, RMS, throwout, pilot.
- **When:** My clutch and flywheel are healthy and not planned for replacement.

### Path B — Full bundle with transmission out

- **Time:** 8-12 hours realistic for me (5-7 for an experienced tech)
- **Difficulty:** Hard. Pulling the K20Z3 trans is a weekend commitment.
- **What I touch:** Everything in Path A plus RMS, throwout + fork, pilot bearing, plus the [03-Clutch-and-Flywheel](../03-Clutch-and-Flywheel/) work if the clutch is being replaced.
- **When:** The clutch is being replaced anyway. Pulling the trans exposes every wear item that's otherwise inaccessible. Doing RMS/pilot/throwout separately later means pulling the trans again, which I am not doing if I can avoid it.

**My situation:** The Exedy Stage 1 (08806) + HF02 is already installed per [03-Clutch-and-Flywheel/overview.md](../03-Clutch-and-Flywheel/overview.md). The transmission is not coming back out for routine reasons. **Path A is what I'm actually doing on this job.** Path B is documented for completeness in case the clutch ever fails early or I pull the trans for another reason.

### Decision tree

```
Is the clutch/flywheel healthy and already installed?
│
├── YES → Path A (CMC + line + slave only)
│         3-5 hours, no trans out
│
└── NO / also being replaced → Path B (full bundle)
          8-12 hours, trans out, bundle with 03-Clutch-and-Flywheel
          Add RMS, pilot, throwout while trans is out
```

---

## Prerequisites and Cross-references

| Document | Why |
|----------|-----|
| [overview.md](overview.md) | Source of truth for parts and rationale |
| [03-Clutch-and-Flywheel/overview.md](../03-Clutch-and-Flywheel/overview.md) | Only relevant for Path B — the clutch that would be swapped in the same session |
| [Hybrid Racing official guide](https://guides.hybrid-racing.com/Guide/Hybrid+Racing+Clutch+Master+Cylinder+Upgrade+(06-11+Civic+Si)/8) | Manufacturer's published torque and routing specifics |
| [docs/torque-specs.md](../docs/torque-specs.md) | CMC mounting nuts, slave bolts, line banjo |

### Cross-reference interactions

- **[03-Clutch-and-Flywheel](../03-Clutch-and-Flywheel/)** — already installed. **If it weren't, I'd bundle this entire job with that one.** Transmission removal is the expensive step; everything accessible with the trans out should happen simultaneously.
- **[02-Short-Shifter-and-Bushings](../02-Short-Shifter-and-Bushings/)** — no hydraulic interaction. Separate subsystem.
- **DOT 4 fluid** — Motul RBF 600 is shared across brakes and clutch.

### Decision rule

- **Clutch OK, not planned for replacement:** Path A standalone.
- **Clutch needs work, or planned within next 30k miles:** Wait, bundle as Path B. Pulling the trans twice is a bad trade against waiting a few months.
- **CMC actively failing right now (pedal to floor, no disengagement):** Path A immediately.

---

## Tools Required

### Critical

- **Flare nut / line wrenches** — 10mm and 12mm. A regular open-end wrench will round the flare fittings.
- **10mm, 12mm, 14mm sockets + wrenches**
- **Clear vinyl bleed hose (3/16" ID) + catch bottle**
- **Motive Power Bleeder 0100** — $50-70, one-person bleeding, also works for brakes
- **Floor jack + 4-ton jack stands**
- **Cotter pin pliers / pick set**
- **Magnetic pickup tool + headlamp** — the under-dash clevis pin loves to disappear
- **Turkey baster or fluid syringe** (dedicated to brake fluid, not kitchen use)
- **Torque wrench, 3/8" drive, 10-80 ft-lb**

### Fluids and consumables

- **Motul RBF 600 DOT 4** — minimum 500mL, I'd buy 1L
- **Brake cleaner + spray bottle of water** — DOT 4 eats paint on contact
- **Clean shop rags** — more than I think I need
- **New copper crush washers** — every banjo I disconnect gets fresh washers, no exceptions
- **Blue painter's tape** — mask the firewall around the CMC before starting

### Path B additional tools

- Seal driver sized for the rear main seal. **Do not hammer directly on the seal.**
- Pilot bearing puller (slide-hammer style) or the bread-packing trick
- Pilot bearing installation driver
- Transmission jack (O'Reilly/AutoZone rental)
- Everything else [03-Clutch-and-Flywheel](../03-Clutch-and-Flywheel/) calls for

---

## Parts List

| # | Item | Part Number | Source |
|---|------|-------------|--------|
| 1 | Hybrid Racing CMC kit (CMC, slave, SS braided line, firewall seal, PTFE grease, hardware) | **HYB-CMC-01-20** | [hybrid-racing.com](https://www.hybrid-racing.com/products/hybrid-racing-cmc-upgrade-acura-tsx) |
| 2 | Motul RBF 600 DOT 4 (500mL x2) | — | Amazon / BimmerWorld |
| 3 | Clutch pedal bushing, OEM | **46991-S5A-004** | Honda dealer |
| 4 | Motive Power Bleeder | 0100 | Amazon |

### Path B additional parts

| # | Item | Part Number |
|---|------|-------------|
| 5 | Rear main seal, OEM | **91214-RDA-A01** |
| 6 | Throwout bearing, OEM Koyo | **22810-RWC-003** |
| 7 | Pilot bearing | **91006-RWC-003** |
| 8 | Honda MTF-3 (2.2 qt) | **08798-9031** |
| 9 | Fresh clutch kit (if replacing) | See [03-Clutch-and-Flywheel](../03-Clutch-and-Flywheel/) |

---

## Step-by-Step — Path A: CMC / Line / Slave Only

### Phase A1: Drain the reservoir (20 min)

1. Park on level ground, wheels chocked. Pop the hood.
2. Mask the firewall, strut tower, and fender around the clutch reservoir with blue painter's tape. DOT 4 eats paint and I will spill some.
3. Locate the clutch reservoir — smaller of the two on the driver-side firewall, separate from the brake reservoir on the 8th gen SI.
4. Suction out as much old fluid as possible with a dedicated turkey baster. It will be brown or amber — confirmation I'm doing this job for the right reason.
5. Cap the reservoir loosely.
6. Lift the front of the car onto 4-ton jack stands on subframe pinch points. Never work under a jack alone.

### Phase A2: Disconnect CMC under the dash (30-45 min)

7. Sit in the driver's seat, head and shoulders in the footwell. Headlamp > flashlight.
8. Locate the clutch pedal pushrod where it comes through the firewall and terminates at a clevis/clevis pin with a cotter pin into the pedal arm.
9. Remove the cotter pin. Save only if clean and unbent.
10. Slide the clevis pin out. The pushrod drops free. Magnetic pickup tool catches the pin when it tries to escape.
11. In the engine bay, locate the 2 CMC mounting nuts (on engine-bay side, threading onto studs through the firewall). These torque to **10 ft-lb** on reassembly per [docs/torque-specs.md](../docs/torque-specs.md).
12. Unclip any hard line retainers from the CMC body.

### Phase A3: Remove the old line (20-30 min)

13. Rags under the CMC and slave.
14. At the CMC end, use a flare nut wrench to crack the line fitting loose. Support the CMC with my other hand.
15. Thread the fitting off by hand.
16. At the slave (under the car, at the bellhousing), same procedure — flare nut wrench, crack loose, unthread by hand.
17. If either end is a banjo instead of a flare, use a 12mm socket on the banjo bolt and **throw away the old crush washers**.
18. Remove the old line. Note the routing so I can replicate it with the new braided line.

### Phase A4: Install the new HR CMC (30-45 min)

19. With line off and pushrod disconnected, pull the old CMC off the firewall studs. Rag underneath for the last fluid dribbles.
20. Inspect and replace the firewall grommet/seal with the fresh one from the HR kit.
21. **Bench bleed the new CMC before installing.** This single step decides whether my final bleed is smooth or an afternoon of cursing. Clamp the CMC in a soft-jaw vise. Fill the reservoir. Using the included bench bleed tubing (short hoses looped back into the reservoir), slowly stroke the piston 20-30 times until no more bubbles come out. Cap the outlet port immediately.
22. Install the new CMC onto the firewall studs. Thread the 2 mounting nuts hand-tight.
23. Torque both CMC mounting nuts to **10 ft-lb**.
24. Reattach the pushrod to the pedal with the clevis pin. **Install a NEW cotter pin** and bend the legs apart. This is the one fastener whose failure puts me on the side of the road — no skipping.

### Phase A5: Install the new stainless braided line (30 min)

25. Route the new HR line along the same path as the old one.
26. **Keep it well clear of the exhaust manifold/header.** Stainless braid transmits heat into the PTFE liner. 1+ inch of clearance, more with the Skunk2 Alpha per [13-Headers](../13-Headers/).
27. Thread the upper fitting into the CMC by hand first, then snug with a flare nut wrench.
28. Thread the lower fitting into the slave (or banjo if that's what the HR kit uses). New crush washers on any banjo.
29. Torque banjo fittings to **25 ft-lb**. Flare fittings per HR's printed spec — typically hand-tight plus 1/6 to 1/4 turn with a flare nut wrench.
30. Secure the line at the original clip points; zip ties if clips don't match the braid profile.

### Phase A6: Install the new slave cylinder (20 min)

31. The HYB-CMC-01-20 kit includes a slave. I'm installing it — no reason not to with 170k on the old one.
32. From under the car, remove the 2 slave mounting bolts at the bellhousing.
33. Pull the slave off. Note whether the pushrod stays in the bellhousing or comes with the slave; match on reassembly.
34. Install the new slave. Torque mounting bolts to **16 ft-lb**.

### Phase A7: Fill and bleed (45-60 min — see bleed section below)

### Phase A8: Verify pedal feel + disengagement test (15 min)

35. Lower the car off jack stands.
36. Key ON, engine OFF. Pump the pedal 10 times. Should feel progressively firmer with a clean, consistent engagement point. Spongy or sinking = air still in the system, redo the bleed.
37. Start the engine. Clutch in, shift into 1st. Release slowly — car should want to move. Back to neutral. Reverse. Repeat.
38. Short test drive, 5 minutes, residential. Work through every gear. Confirm clean disengagement, no grinding, no dragging.
39. Back home, check every fitting for weeping. Top off if the level dropped.

---

## Step-by-Step — Path B: Full Bundle with Transmission Out

Documented for completeness. My clutch is already fresh so I'm not doing Path B now. If the clutch ever fails early or I swap in a higher-capacity unit, this is the sequence.

### Step 1: Pull the transmission per 03-Clutch-and-Flywheel

Everything up through "transmission separated and on the floor" is covered there. Don't duplicate it here.

### Step 2: Rear main seal (trans out, flywheel off)

- Remove the flywheel per the 03 guide. The RMS is now visible around the crank snout at the back of the block.
- Extract the old seal with a seal pick. **Do not gouge the block or crank.**
- Clean the seal bore with brake cleaner.
- Install the new **91214-RDA-A01** using a proper seal driver matched to the seal OD. **Do not hammer directly on the seal.** Hammering distorts the lip and guarantees a leak inside a year. Driver seats the seal flush with the block face.
- Light coat of fresh oil on the seal lip before installation.

### Step 3: Pilot bearing

- Pull the old pilot bearing with a slide-hammer puller or the bread-packing trick (pack the cavity with white bread, insert a dowel, tap — hydraulic pressure pushes the bearing out).
- Clean the bore.
- Install the new **91006-RWC-003** with a driver that contacts the outer race only. Drive squarely until fully seated.

### Step 4: Throwout bearing and fork

- Remove old throwout bearing and fork from the transmission.
- Inspect the fork pivot for wear. Replace if worn.
- Install new OEM Koyo **22810-RWC-003**. Light PTFE grease on the fork contact points (HR kit includes a packet; otherwise Honda moly paste).

### Step 5: CMC, line, slave per Path A

Everything in Path A Phases 1-6 still applies. With the trans out, slave swap is even easier from above.

### Step 6: Reassemble per 03-Clutch-and-Flywheel

Trans back on, bellhousing bolts to **47 ft-lb**, refill with fresh Honda MTF-3, everything per [docs/torque-specs.md](../docs/torque-specs.md).

### Step 7: Bleed per procedure below

Same bleed either path.

---

## Bleed Procedure (do not rush this)

Air in the clutch hydraulics is the #1 post-install failure mode. Spongy pedal, sinking pedal, fine-cold-soft-hot pedal — almost always trapped air, not a bad part. I do this right the first time.

### Step 1: Gravity bleed (15 min, zero effort)

1. Fill the CMC reservoir to MAX with fresh Motul RBF 600.
2. Clear vinyl hose on the slave bleeder nipple. Other end into a catch bottle with an inch of fresh fluid in it (submerged tip prevents air siphoning back in).
3. Crack the bleeder 1/2 turn. Leave it.
4. Gravity works for 15 minutes. Keep the reservoir topped off — if it runs dry, I start over.
5. Close the bleeder.

### Step 2: Pedal bleed (20+ cycles)

**Two-person manual:**

1. Helper in the driver's seat.
2. Helper pumps the pedal slowly 3-4 times, holds to the floor.
3. I crack the bleeder. Fluid and air bubbles exit through the clear hose.
4. I close the bleeder.
5. Helper releases the pedal slowly.
6. Repeat 20+ cycles. Top off every 5 cycles — NEVER run dry.
7. When I see zero bubbles for 3 cycles in a row, I'm done.

**One-person Motive power bleeder:**

1. Attach Motive cap to the reservoir (verify adapter fits 8th gen SI).
2. Pump to 10-15 PSI. Do not exceed 15.
3. Crack the slave bleeder. Fluid flows continuously.
4. Close when clear with zero bubbles. Top off Motive reservoir as needed.

### Step 3: Final verification

1. Watch the bleed hose on the last cycle — any bubble activity at all, keep going.
2. Pump the pedal 20 times with engine OFF. Firm, consistent, engagement point in the upper third of travel.
3. Pedal sinks when held or feels mushy? Back to Step 2.

### Alternative: vacuum bleeder (Mityvac)

Pulls fluid from the bleeder directly. Faster than gravity + pedal alone, but power bleeder is still superior for keeping positive pressure on the system while fluid flows.

---

## First Drive Checklist

- [ ] Pedal firm from fully released to fully depressed, no mushy spot
- [ ] Engagement point consistent, upper third of pedal travel
- [ ] Clean disengagement at idle — 1st and reverse without grinding
- [ ] No pedal fade after 10+ minutes of stop-and-go (the classic 8th gen symptom I'm curing)
- [ ] No weeping at CMC, line fittings, or slave
- [ ] Reservoir level stable after a 20-30 minute drive
- [ ] Pedal returns fully with no stickiness (pedal bushing 46991-S5A-004 swap helps here)
- [ ] Path B only: no slip under WOT load after the 500-mile break-in per [03-Clutch-and-Flywheel](../03-Clutch-and-Flywheel/)

---

## Common Mistakes I'm Watching For

1. **DOT 4 on paint.** Strips clearcoat on contact. If I spill, flush with water immediately, then wipe with a damp rag. Painter's tape up front catches the worst.
2. **Cross-threading a flare fitting.** Start by hand, never with a wrench. Back off if it doesn't thread smoothly — cross-threading destroys the aluminum port.
3. **Air left in the system.** Spongy pedal = air = redo the bleed. Don't convince myself "firm enough" is firm. It gets worse with heat cycles.
4. **Skipping the bench bleed.** Getting a dry CMC air-free in-car is miserable and often incomplete.
5. **Forgetting a new cotter pin on the pedal clevis.** Old cotter is bent or corroded. New pin, legs spread. No skipping.
6. **Not torquing the CMC mounting nuts.** 10 ft-lb is gentle but specific. Loose = pedal feel drift + firewall seal weep.
7. **Hammering the RMS in (Path B).** Fragile seal lip. Use a proper driver. Hammered = weeps oil onto the clutch within 10k miles and I'm pulling the trans again.
8. **Letting the reservoir run dry during bleeding.** One lapse and the CMC sucks air. Top off every 5 cycles.
9. **Reusing old crush washers.** Work-hardened copper doesn't seal the second time. $0.50 beats a weeping banjo.
10. **Routing the braided line near the exhaust.** Heat shortens PTFE liner life. 1+ inch clearance, more with headers.

---

## See Also

- [overview.md](overview.md) — part selection rationale and OEM part numbers
- [03-Clutch-and-Flywheel](../03-Clutch-and-Flywheel/) — the "bundle!" cross-reference; if clutch ever needs service, everything in Path B happens in the same session
- [02-Short-Shifter-and-Bushings](../02-Short-Shifter-and-Bushings/) — different subsystem, but relevant if I'm already under the dash
- [docs/torque-specs.md](../docs/torque-specs.md) — CMC 10 ft-lb, slave 16 ft-lb, clutch line banjo 25 ft-lb, bellhousing 47 ft-lb (Path B)
- [Hybrid Racing CMC install guide (06-11 Civic Si)](https://guides.hybrid-racing.com/Guide/Hybrid+Racing+Clutch+Master+Cylinder+Upgrade+(06-11+Civic+Si)/8) — manufacturer's published procedure

---

*Last updated: 2026-04-20*
