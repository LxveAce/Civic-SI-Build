# Cylinder Head Install Guide — 4Piston Pro 156v2 All Motor + ARP 208-4701 + Skunk2 Stage 2

## Status: Planning — Phase 4.5 (bundle with headers, IM, VTC, pulleys, cooling)

This is the highest-stakes install on the entire build. A timing chain or header job going sideways costs me a weekend. A head job going sideways costs me the engine. I'm reading this guide six times before I touch a wrench, and re-reading Phase G (head stud torque) the morning of.

---

## Reality Check Before I Start

**Head-off-in-car, not engine-pull.** Bottom end stays put, trans stays bolted, subframe stays in place. The rest is not weekend-DIY territory without prior head-gasket experience.

| Skill Tier | Time Estimate | Notes |
|------------|--------------|-------|
| First-time DIY, no head-gasket experience | **12–20 hours over 3–5 days** | Not a single-day job. Mistakes compound. |
| DIY with prior head-gasket experience | 8–12 hours over a long weekend | Still slow — cam degreeing adds time |
| Honda specialist shop | 10–14 hours @ $100–150/hr = $1,200–2,100 | Includes block prep, stud install, break-in |

**The shop option is legitimate here.** Unlike the header job, the worst-case on this install is a bent valve or warped head — pulling the engine and paying machine-shop rates. If I don't already know what a straight-edge flatness check on an aluminum deck feels like, **pay the shop.**

What tips me DIY: I've planned this as a one-shot teardown with headers, IM, VTC, pulleys, and cooling bundled in. One careful week beats three weekend jobs stacked. What tips me shop: this is the one mod where "shop owns it if it breaks" has real teeth.

**Decision checkpoint:** quote from a K-series specialist (not a generic indie). Under $2,000 labor for the bundle + they've done 4P Pro 156v2 before = hire out. Otherwise DIY with the ARP torque sheet taped to the fender.

---

## Prerequisites / Cross-references — BUNDLE TEARDOWN

Not a standalone mod. The labor to get the head off is the same labor to do six other things. Pulling the head twice is the most expensive mistake I could make on this build.

### Must be planned into the same teardown

| Bundled Mod | Cross-reference | Why Bundle |
|-------------|----------------|------------|
| **Timing chain service** | [`../05-Timing-Chain-Maintenance/`](../05-Timing-Chain-Maintenance/overview.md) | Chain cover is off anyway. Measure tensioner rod, replace chain/arm/guides/tensioner if ≥10 mm extension. At 170k, assume full replacement. |
| **VTC actuator 14310-RBC-003** | [`../06-Ignition-Refresh/`](../06-Ignition-Refresh/overview.md) | Lives directly under the timing cover. Replace every time. -003 part only — no -002. |
| **Headers (Skunk2 Alpha + Berk HFC)** | [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) | Exhaust manifold studs get pulled during head removal. Header install happens before head reinstall — same teardown. |
| **Intake manifold (Skunk2 Ultra Street + 66mm TB)** | [`../14-Intake-Manifold/overview.md`](../14-Intake-Manifold/overview.md) | IM bolts to the head. Install at head reinstall, not separately. |
| **Cooling system refresh (Koyorad + hoses + WP + thermostat)** | [`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) | Coolant is already drained. Water pump accessible. Do not skip. |
| **Pulleys and harmonic balancer (ATI Super Damper)** | [`../15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) | Crank pulley is off for timing cover access. NEW crank bolt yield procedure happens once, not twice. |
| **Ignition refresh (plugs + OEM coils)** | [`../06-Ignition-Refresh/overview.md`](../06-Ignition-Refresh/overview.md) | Coils and plugs come out to clear cams and valve cover. Replace with fresh parts before reinstall. |

### Confirmed before ordering anything

- [ ] **RBC fitment on 4P Pro 156v2 All Motor Package** — email reply in writing from Luke at 4Piston confirming this specific assembled package fits K20Z3 RBC casting
- [ ] Cometic C4561-030 ordered (not C4561-036 — the thicker gasket is for decks that were surfaced, which mine wasn't)
- [ ] ARP 208-4701 ordered (not 208-4303 — that's B-series GSR, wrong engine)
- [ ] Skunk2 Tuner Stage 2 cams 305-05-0220 + Skunk2 Pro adjustable cam gears 304-05-0300 ordered and in hand
- [ ] Fresh OEM gaskets: IM 17115-RAA-A01, exhaust 18115-RRB-A01, valve cover kit 12030-PNC-000, front cam seals 91213-PLA-003 x2, half-moon plug, oil seal
- [ ] Cooling system parts staged (Koyorad HH060063 + OEM hoses + thermostat + water pump + coolant)
- [ ] Header bundle staged ([`13-Headers/install-guide.md`](../13-Headers/install-guide.md) parts list complete)
- [ ] IM bundle staged (Skunk2 Ultra Street + bored 66mm TB + RBC-to-Ultra-Street adapters as needed)
- [ ] Dyno session pre-booked for ~14 days after install day
- [ ] Break-in oil on the shelf (Driven BR30 or Brad Penn, 5 qt) + fresh synthetic for post-break-in

If any of these are NO, I'm not starting the teardown.

---

## Tools Required

Not the header tool list. Several are single-use specialty tools. Budget accordingly — the shop option starts looking rational right about here.

### Absolutely Required

| Tool | Purpose | Cost / Source |
|------|---------|---------------|
| **Lisle 37950 cam lock** | Locks both cams at TDC cyl 1. Non-negotiable. | ~$40 |
| **ARP stud installer tool** | 5–10 in-lb install torque on ARP studs | ~$25 |
| **ARP Ultra-Torque lube** | Ships with 208-4701 kit. Do not substitute. | Included |
| Torque wrench, 30–150 ft-lb, 1/2" | ARP final-pass head stud torque (75–80 ft-lb typical) | Calibrated <1 yr |
| Torque wrench, 10–80 ft-lb, 3/8" | Cam caps, IM bolts, header nuts, crank pulley first-pass | Own |
| Torque wrench, 20–200 in-lb, 1/4" | Valve cover (87 in-lb), timing cover, coil hold-down | Own |
| Torque angle gauge | Crank bolt +90°, possibly ARP final angle | ~$20 |
| Crank pulley holder tool | Crank bolt breakaway at 181 ft-lb + 170k heat cycles | ~$35 |
| Breaker bar, 24"+ | Crank + header nut breakaway | Own |
| Valve spring compressor | Only if troubleshooting a dropped keeper | ~$60 rental |
| Straight edge (18"+, precision) | Deck flatness check, 0.002"/6" max warp spec | ~$40 Starrett 385 |
| Feeler gauge set (to 0.0015") | With straight edge | Own |
| Micrometer (0–1") + depth gauge | Verify ARP stud protrusion is consistent | Own or rent |
| Engine crane OR 2 people + head cradle | 4P assembled head ~45 lb — one-person lift risks dropping onto deck | Crane rental ~$35/day |
| Plastic razor blades (NOT metal) | Gasket residue removal without gouging aluminum | ~$10 pack |
| Compressed air + safety glasses | Blow stud holes clean — oil in hole = false torque reading | Shop compressor |
| Lint-free rags + shop vac thin nozzle | Final deck wipe + bore debris removal | Own |

### Also Needed (Bundled Mods Draw On These)

| Tool | Cross-reference |
|------|-----------------|
| Crank pulley harmonic balancer puller | [`../15-Pulleys-and-Harmonic-Balancer/`](../15-Pulleys-and-Harmonic-Balancer/overview.md) |
| O2 sensor socket (22mm slotted) | [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) |
| Coolant funnel kit + bleed procedure | [`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) |
| Fuel line disconnect tool + rag for fuel spill | IM removal |

### All Fresh Gaskets (none reused, ever)

See Parts List below.

---

## Parts List

### The Head Package

| Part | P/N | Qty | Price | Notes |
|------|-----|-----|-------|-------|
| **4Piston Pro 156v2 All Motor Package (RBC-compatible, assembled)** | 4P-PRO-156V2-AMP | 1 | **$2,740** | Ferrea valves + Supertech 82lb dual springs + Ti retainers + locks, NEWEN 5-angle valve job, ~360 CFM. **Confirm RBC fitment before clicking buy.** |
| Cometic MLS head gasket .030" | **C4561-030** | 1 | $85 | MLS layer — NO sealer. |
| **ARP head stud kit (K-series K20/K24)** | **ARP 208-4701** | 1 | ~$200 | 8740 chromoly, 190k PSI. Ships with ARP Ultra-Torque lube. **DO NOT ORDER 208-4303** — that is B-series GSR, wrong engine entirely. |
| Skunk2 Tuner Stage 2 cams (intake + exhaust) | **305-05-0220** | 1 pair | ~$550 | Community default for FBO NA K20Z3. 22–25 HP published. |
| Skunk2 Pro adjustable cam gears | **304-05-0300** | 1 pair | ~$270 | Required with aftermarket cams for dyno-dialed cam timing. |

### Gaskets + Seals (All New)

| Part | P/N | Qty | Price |
|------|-----|-----|-------|
| Valve cover gasket kit (incl. plug tube seals + grommets) | **12030-PNC-000** | 1 | $40 |
| Intake manifold gasket (head-to-IM) | 17115-RAA-A01 | 1 | $15 |
| Exhaust manifold / header gasket | **18115-RRB-A01** | 1 | $20 |
| Front cam seals | 91213-PLA-003 | 2 | $30 |
| Cam cap half-moon plug (rear) | 90041-PNA-000 | 1 | $8 |
| Cam chain case oil seal | 91319-P0Y-003 | 1 | $12 |
| Front crank main seal | 91214-RZY-A01 | 1 | $18 |

### Consumables

| Item | P/N | Notes |
|------|-----|-------|
| Break-in oil | Driven BR30 or Brad Penn 10W-30, 5 qt | First fire only, drained after cam break-in |
| Oil filter | 15400-PLM-A02 | New |
| Moly 60 assembly grease | Honda 08798-9010 | Cam journals, VTC vanes, crank nose |
| ARP Ultra-Torque lube | Included with 208-4701 | Stud threads + stud top + washer underside |
| Hondabond HT | Honda 08718-0004 | Timing cover corners, cam cap corners |
| Honda Type 2 coolant OL999-9011 | — | System refill |
| Brake cleaner (non-chlorinated) + lint-free rags | — | Deck cleanup |

### Bundled (Covered in Other Mod Docs' Parts Lists)

- Timing chain kit — see [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md)
- VTC actuator 14310-RBC-003 — see [`../06-Ignition-Refresh/overview.md`](../06-Ignition-Refresh/overview.md)
- Header bundle (Skunk2 Alpha 412-05-1930 + Berk HFC + ARP 208-4301 + header gasket + copper nuts) — see [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md)
- IM bundle (Skunk2 Ultra Street 307-05-0600 + bored 66mm TB + adapter as needed) — see [`../14-Intake-Manifold/overview.md`](../14-Intake-Manifold/overview.md)
- Cooling bundle (Koyorad + hoses + thermostat + WP) — see [`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md)
- Pulleys + NEW crank pulley bolt 90017-RWC-A01 — see [`../15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md)
- Fresh plugs (NGK ILZKR7B-11S x4) + fresh coils (30520-RWC-A01 x4) — see [`../06-Ignition-Refresh/overview.md`](../06-Ignition-Refresh/overview.md)

---

## Step-by-Step — Major Phases

12 phases (A through L), each with a checklist. I do not skip ahead. I do not start Phase D before Phase C is verified.

---

### Phase A: Pre-Teardown (Day −7 through Day 0)

Everything here is preventive.

1. **All parts in hand.** Unbox, count, verify part numbers. I do not discover I got 208-4303 instead of 208-4701 on teardown day.
2. **Unbox and inspect 4P head.** Verify assembled 156v2 All Motor Package, RBC-compatible. Inspect combustion chambers, valves, seats. Photograph the 4P documentation card (chamber CC, flow numbers, valve job spec) and file it in the repo.
3. **Torque wrench calibration.** Any wrench older than 12 months since calibration = send out or replace. Wrong head stud torque kills engines.
4. **PB Blaster on exhaust manifold studs** starting Day −7, per [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) schedule. Thermal cycling + penetrant daily.
5. **PB Blaster on IM bolts** Day −3 through Day 0.
6. **Clear the garage.** Engine crane space, parts staging shelves, labeled zip-lock bags + Sharpie.
7. **Review ARP 208-4701 instruction sheet** end to end. Current spec is typically 30/50/75 ft-lb three passes with Ultra-Torque, star pattern from center. **Use the sheet that shipped with MY kit** — ARP spec changes between revisions.
8. **Review Skunk2 Tuner Stage 2 + Pro cam gear notes.** Know whether I'm degreeing static or letting the tuner dyno-degree.
9. **Confirm dyno appointment** 10–14 days out.

### Phase B: Disassembly (4–6 hours)

1. Battery negative off. Car sits overnight — capacitor drain, fuel pressure bleed.
2. Drain coolant ([`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) bleed procedure in reverse). Drain oil.
3. Engine cover + K&N intake tube off (label/photograph every vacuum line).
4. Ignition coils (9 ft-lb) + plugs out — these get replaced with Ignition Refresh parts anyway.
5. Valve cover off: 9 M6 bolts in spiral-inward pattern. Lift, inspect cams.
6. Fuel rail pressure bleed (Schrader valve, rag over it, depress with small screwdriver). Unbolt rail (9 ft-lb), disconnect fuel line, lift rail with injectors attached onto a clean rag. Do NOT let injector tips touch the ground.
7. IM off: see [`../14-Intake-Manifold/overview.md`](../14-Intake-Manifold/overview.md) Phase C. Disconnect TPS/IAT/MAP/IACV/brake booster/PCV. Unbolt IM star pattern 17 ft-lb release.
8. Exhaust manifold nuts off: see [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) Phase D. Slow, back-and-forth, more PB Blaster. Stop if a stud feels like it's turning with the nut.
9. Crank pulley off: see [`../15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) Phase E. **Discard the old bolt — 90017-RWC-A01 is one-time-use.**
10. Timing chain cover off: see [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) Phase F. 13 bolts of varying lengths — document bag layout.
11. **Rotate crank clockwise to TDC cyl 1.** Crank pulley mark to pointer, both cam gear triangle marks point straight up parallel to deck.
12. **INSTALL LISLE 37950 CAM LOCK TOOL.** Non-negotiable. Cams will spring-rotate under valve spring pressure without it.
13. Measure tensioner rod protrusion. Record. At 170k, assume full chain replacement.
14. Remove tensioner, chain arm, fixed guide, chain off cam gears, crank gear off.
15. **Cam caps off in REVERSE torque sequence** (FSM sequence, three passes outside-in). Wrong order = bent cam from uneven spring load.
16. Lift cams out. Set on clean rag with paint-mark orientation notes.
17. **Head bolts out in REVERSE torque sequence** — three passes, outside-in. Don't break torque on one bolt while others hold full load. Patience.
18. **Head lift off — two people or engine crane with sling.** ~45 lb plus valvetrain. Lift STRAIGHT UP. Tilting drags dowels across the gasket surface.
19. Set head combustion-chamber-up on a head stand or clean wood blocks. Never on its deck surface.

### Phase C: Block Prep (1–2 hours)

Every second here pays off at first-start.

20. **Plastic razor to remove old gasket material.** NEVER metal. Steel gouges aluminum = permanent leak path.
21. Rags stuffed in cylinder bores and oil passages. Do not skip.
22. Wipe deck with brake cleaner + lint-free rag until rag comes away clean.
23. **Straight edge across the deck in 6 directions:** longitudinal center, both diagonals, and at each cyl boundary. Feeler gauge under. **Max 0.002" warp over any 6" span.** More than that = machine shop.
24. **Compressed air into each stud hole** — blow out oil/coolant/debris. Oil in a blind stud hole hydro-locks the stud and fakes out torque readings. #1 ARP install mistake.
25. Shop vac thin nozzle into each bore. Pull the rags from step 21.
26. Final deck wipe with brake cleaner. Let flash off.
27. Inspect block dowels — both present, not bent, not mushroomed. Damaged = machinist.

### Phase D: Install ARP 208-4701 Head Studs

28. **Re-read the ARP instruction sheet that shipped with the kit.** The sheet is truth, not this doc.
29. Clean each stud with brake cleaner + dry rag. No packing grease, no shipping oil.
30. Clean each block stud hole: bottle brush, brake cleaner, compressed air, twice. Cotton swab at the bottom should come up dry.
31. **Drop of Ultra-Torque on the bottom 3–4 threads of each stud.** Not a coating. Lets the stud seat without galling but doesn't fake out top-end torque.
32. Thread each stud in by hand until it bottoms. Back off a hair.
33. ARP stud installer tool, snug to **5–10 in-lb**. Bottomed, not stretched.
34. Micrometer or depth-gauge check all 10 studs — protrusion within 0.010" of each other. Outlier = not seated, pull and re-inspect.
35. Verify top threads on each stud are clean and undamaged.

### Phase E: Install Cometic C4561-030 Head Gasket

36. Final deck wipe with brake cleaner. Zero residue, zero fibers.
37. **"TOP" / part-number side of the Cometic UP.** MLS has a correct orientation — reversed = compression leak.
38. Lower gasket over studs. Align block dowels through gasket dowel holes. Sits flat, zero edge gap.
39. **NO sealer, NO Hondabond, NO copper spray.** Cometic MLS is dry-install. Sealer on MLS creates a leak.
40. Verify coolant passages, oil passages, and bolt holes align to block features. Gasket installed backwards blocks coolant to one bank — yes, this happens, the asymmetry is subtle.

### Phase F: Install 4P Pro 156v2 Head

41. Final wipe of the 4P head deck, combustion chambers clean, valves seated.
42. **Two people OR engine crane with sling.** No solo-lift of 45 lb onto studs at chest height.
43. Lower head straight down. Feel for block dowels catching head dowel sockets.
44. Verify SQUARELY seated — drops the last 1/4" under its own weight, studs protrude evenly through bolt holes.
45. **Do NOT rock or wiggle once down.** MLS is sensitive. If it doesn't drop flat first try, lift straight up and re-align.

### Phase G: Head Stud Torque Sequence (CRITICAL)

This phase is where engines get killed. Read every word.

46. **Ultra-Torque on each stud:** one drop on top threads, one drop on the washer surface the nut rides on. Two drops per stud, not a glob.
47. ARP washers — beveled side up (chamfer facing the nut).
48. ARP nuts finger-tight on all 10 studs.
49. **Follow the ARP sheet that shipped with MY kit.** Typical current spec:
   - **Pass 1:** 30 ft-lb, star from center outward
   - **Pass 2:** 50 ft-lb, same sequence
   - **Pass 3 (final):** 75 ft-lb (verify — some revisions spec 80 ft-lb)
   - If the sheet says angle-torque instead, use the angle gauge exactly.
50. **Star pattern from center outward.** Cyl 2/3 bolts first, working out to cyl 1 and cyl 4. Even gasket loading, no warp.
51. Between passes, no binding. Smooth progression.
52. **After final pass:** let sit 10–15 minutes, retorque the final pass once more. Gasket takes a minute to fully compress.
53. Paint-pen dot each nut aligned to a dot on the stud top — visual "has this moved?" reference for break-in re-check.

### Phase H: Install Skunk2 Tuner Stage 2 Cams

54. **Moly 60 on each cam journal.** All five surfaces per cam. Generous — cams run dry 2–3 sec on first fire.
55. Moly 60 on each cam lobe nose. Stage 2 cams wipe out in 20 seconds without it.
56. **Cam orientation per FSM TDC cyl 1 diagram:** intake triangle mark up-and-slightly-exhaust-side, exhaust triangle mark up-and-slightly-intake-side — mirrored, both generally UP, parallel to deck. Both cams parked between lobe pushes.
57. Lay cams in. Skunk2 Stage 2 labeled I (intake) / E (exhaust) — do not mix.
58. Install Skunk2 Pro adjustable cam gears loose — final torque at chain install.
59. Cam caps in OEM sequence, three passes, **inside out** (cap 3 first, then 2+4, then 1+5), **final 9 ft-lb (108 in-lb)**. Over-torque crushes cam into journal; under-torque wrong clearance.
60. Rotate each cam slightly by hand — spins free, no binding. Tight feel = STOP.
61. **Lisle 37950 back on** now that caps are torqued.
62. Cam degreeing decision: Skunk2 Pro gears are made for dyno-degreeing. Most FBO builds let the tuner degree on the dyno — don't pre-degree unless the Stage 2 instruction says to.

### Phase I: Chain, VTC Actuator, Tensioner

63. **VTC actuator 14310-RBC-003:** see [`../06-Ignition-Refresh/overview.md`](../06-Ignition-Refresh/overview.md) and [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) Phase I. Moly 60 on vanes, slide onto intake cam nose, hold cam on the flats (not a lobe), center bolt **83 ft-lb dry, no impact**.
64. **Route new chain** per [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) Phase J: single colored link to crank mark, two colored links (9 apart) to cam gear marks. Verify cam gear triangles still point up AND colored links align.
65. Fixed chain guide in, then pivoting chain arm.
66. **Tensioner piston reset:** compress with retainer pin through lock hole. Verify pin holds.
67. Tensioner installed with bolts at **8.7 ft-lb**. **Pin STAYS IN until everything is bolted down.**
68. **Pull retainer pin.** Piston extends, chain tensions.
69. **Rotate crank 2 full turns clockwise by hand** (old bolt finger-tight for leverage).
70. **Verify cam marks return to TDC cyl 1.** Not aligned = chain off a tooth — STOP, re-route.
71. **Remove Lisle 37950** once timing is verified correct.
72. Final torque Skunk2 Pro cam gear center bolts per Skunk2 spec (typically 37 ft-lb with blue Loctite). Discs stay at static — tuner dyno-adjusts.

### Phase J: Reassembly

73. **Timing cover:** press new crank seal in, Hondabond HT bead per [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) Phase L, install within 5 min, bolts crisscross from center out **8.7 ft-lb**.
74. **Crank pulley:** NEW bolt 90017-RWC-A01, Moly 60 on crank nose, **131 ft-lb → loosen fully → 37 ft-lb → +90°** per [`../15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) Phase G. Do not reuse old bolt.
75. **Valve cover:** fresh 12030-PNC-000 kit + plug tube seals + grommets. Hondabond HT dabs at the 4 cam cap corners. **7.2 ft-lb (87 in-lb)** spiral out from center.
76. **Plugs:** fresh NGK ILZKR7B-11S, anti-seize sparingly (or none), **13 ft-lb**. Never muscle iridium.
77. **Coils:** fresh 30520-RWC-A01 x4, dielectric grease on boots, hold-down **9 ft-lb**.
78. **Headers:** per [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) Phase E–F. New 18115-RRB-A01, 3-pass star **23 ft-lb**.
79. **IM with RBC-compatible adapters:** per [`../14-Intake-Manifold/overview.md`](../14-Intake-Manifold/overview.md). New 17115-RAA-A01, 17 ft-lb star from center. Reconnect vacuum lines per teardown photos. Coolant bypass block-off plate on.
80. **Fuel rail + injectors:** rail bolts 9 ft-lb, fuel line quick-connect, Schrader cap back on.
81. Intake tube + K&N filter on, vacuum lines reconnected per photos.
82. **Coolant refill + bleed** per [`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md). Honda Type 2 OL999-9011. Bleed properly — air in the system hurts first-start.
83. New oil filter 15400-PLM-A02, **break-in oil** (Driven BR30 or Brad Penn 10W-30) 4.4 qt.
84. Battery reconnect. Key ON — verify dash, no CELs, fuel pump primes.

### Phase K: First-Start Protocol (Cam Break-In)

This phase is the difference between 200k-mile cams and 2,000-mile cams.

85. **Oil pump prime:** pull the main relay (driver footwell), crank 10 sec, rest 30 sec, crank 10 more sec. Spins the oil pump without firing — pressurizes the top end before cams try to run.
86. **Reinstall main relay.** Verify fuel pressure primes on key-ON.
87. **Start the engine.** Should fire within 3 seconds. Long cranking = diagnose, don't keep cranking.
88. **IMMEDIATELY elevate to 2000–2500 RPM and HOLD for 20 minutes.** Cam break-in. Cams need splash AND RPM-driven lobe loading to seat. **Do NOT idle during break-in.**
89. **Watch coolant temp continuously.** ECT above 220°F = shut down, diagnose bleed/thermostat/air pocket.
90. **Listen for anomalies:** cam-lobe tap (wrong lash), valvetrain clatter (dropped keeper), exhaust leak hiss, coolant smell, oil smoke (pinched gasket). Any = shut down, fix.
91. **After 20 min:** idle 2–3 min, then shut down.
92. **Drain break-in oil + filter.** Break-in deposits metal fines — do not circulate. Refill with fresh break-in oil or 5W-30 synthetic per tuner's call.
93. Let engine cool fully before any further driving.

### Phase L: First Drive + Mandatory Dyno Retune

94. **First 100 mi: partial throttle only.** No WOT, no VTEC crossovers if I can help it. Heat cycle, stud settle, gasket seat.
95. **Flash a conservative base map** before first drive — community FBO + 4P + Stage 2 map with timing pulled 2° safety, or previous cal with safety pull. **Do NOT drive on the old pre-head cal.** Wrong cam/head on old fuel map = lean WOT = cracked piston.
96. **Re-torque valve cover at 100 mi** per [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) Phase P. 7.2 ft-lb, 10 minutes.
97. **Optional but smart at 100 mi:** compression + leak-down test. All 4 cyl within 10% of each other, leak-down under 10% each. Fail = do not go to dyno yet.
98. **Confirm dyno session** (booked in Phase A). Mandatory $500–800 at a Hondata-capable shop.
99. **At the dyno:** tuner re-baselines VE, rebuilds fuel 4000–8000 RPM, max-safe timing with zero knock, VTC crossover for new cam/head, degrees Skunk2 Pro cam gears for the flow curve, produces BOTH daily + sport maps per [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md).
100. **Do not drive hard between install and dyno.** That 10-mile window is where engines get hurt.

---

## Why 4P Pro 156v2 All Motor Package (RBC-Compatible)

$2,740 assembled is expensive. Here's why I'm not saving money here.

**Ferrea valves + Supertech 82lb dual springs + Ti retainers + locks** matched and installed by the shop that built the head. No mix-and-match risk. I don't trust myself to spec a valvetrain and set spring height without a machine shop; 4P delivers shop-grade precision.

**NEWEN 5-angle valve job** — CNC-repeatable seat geometry. Smoother throat-to-chamber transition than a 3-angle. ~360 CFM at stock valve size vs ~290 CFM for a stock refreshed head — 25% more flow, which is exactly what Skunk2 Ultra Street + Stage 2 cams will demand on the intake side.

**Manganese bronze guides + oversized steel intake seats** — durable for E85 moisture over the next 200k miles. Important because I'm going E85 in Phase 7; stock aluminum guides get chewed up on ethanol-rich fuel over time.

**RBC-compatible assembled package.** Bare 4P Pro 156v2 CNC is PRB-base and would need custom RBC work. The All Motor Package assembled version is RBC-compatible per 4P's fitment list. **Verified in writing from Luke before I click buy.**

**Flow match to the build:** 360 CFM is what Skunk2 Ultra Street IM + bored 66mm TB + Skunk2 Alpha + Stage 2 cams want. Stock 290 CFM would bottleneck the rest of the FBO. 4P Pro 163 at 400 CFM is ceiling I don't need for 250 WHP.

---

## Pre-Order Verification Email Template

Before clicking buy on the $2,740 package, I send this to **Luke@team4piston.com**:

> Subject: RBC Fitment Confirmation — Pro 156v2 All Motor Package for 2009 Civic Si K20Z3
>
> Hi Luke,
>
> I'm planning to order the 4P Pro 156v2 All Motor Package (assembled — Ferrea valves + Supertech springs + Ti retainers) for my 2009 Civic Si (FG2, K20Z3, RBC casting).
>
> Confirming before ordering: is the Pro 156v2 **All Motor Package** (assembled, not bare CNC) direct-fit on K20Z3 RBC? I know the bare CNC Pro 156v2 is PRB-base; I want the All Motor Package RBC compatibility in writing before buying.
>
> Build context: 220–250 WHP NA, pump then E85. Skunk2 Ultra Street IM, bored 66mm DBW TB, Skunk2 Alpha + Berk HFC, Skunk2 Tuner Stage 2 cams + Pro adjustable cam gears, ARP 208-4701 studs, Cometic C4561-030. 100% stock bottom end.
>
> Questions: (1) Drop-in fit on K20Z3 RBC, no casting work? (2) Current lead time? (3) As-machined chamber CC documentation? (4) Known issues pairing with Skunk2 Tuner Stage 2?
>
> Thanks,
> LxveAce

Written reply confirming RBC fitment = archive the email, file in repo, order. No verbal "yeah it'll fit."

---

## First Drive Checklist

Gentle 10-mile loop after break-in, then verify every item. Any NO = no dyno yet.

- [ ] Smooth idle (slight Stage 2 cam lope acceptable, not rough)
- [ ] No cam-lobe tapping or valvetrain clatter under the valve cover
- [ ] No exhaust leak hiss at header-to-head flange
- [ ] Oil pressure reads normal range at idle + 2500 RPM
- [ ] No coolant weep at head-to-block deck
- [ ] No oil weep at valve cover, timing cover, or front crank seal
- [ ] Coolant temp stabilizes at thermostat spec (~185–195°F) — no runaway heat
- [ ] No CEL, no pending OBD2 codes
- [ ] Datalog at idle + 2500 RPM shows stable fuel trims (±5%), commanded vs actual cam phase within 2°
- [ ] No compression loss (even firing, no startup smoke)
- [ ] Spark plugs clean and even when pulled (optional at 100 mi)

---

## Common Mistakes

Every one of these is a documented forum failure mode.

| Mistake | Consequence | Prevention |
|---------|-------------|------------|
| **Ordering bare 4P Pro 156v2 CNC for an RBC engine** | PRB-base casting won't mate to K20Z3 RBC deck + coolant routing | ONLY the All Motor Package is RBC-compatible. Confirm in writing via Luke. |
| **Ordering ARP 208-4303 instead of 208-4701** | 208-4303 is B-series GSR — wrong engine entirely | Verify at click time. 208-4701. Not 208-4303. |
| **Reusing old OEM TTY head bolts instead of ARP studs** | Stretches past yield, clamp drops, gasket blows | ARP 208-4701 every time. $200 is cheap insurance. |
| **Dry-assembling ARP studs without Ultra-Torque** | False torque reading, galled block threads | Ultra-Torque ships with kit. One drop bottom, one drop top, one drop washer. Not optional. |
| **Oil in stud holes during install** | Hydro-lock, false torque, clamp far under spec | Compressed air + brush + brake cleaner + cotton swab. Dry holes. |
| **Skipping cam break-in RPM hold** | Cam lobes wiped in 20 seconds of idle | 20 min at 2000–2500 RPM first start. Non-negotiable. |
| **Head studs not following ARP star pattern** | Uneven clamp, warped head | 3-pass star from center outward per the sheet shipped with MY kit. |
| **Skipping angle gauge when ARP calls for it** | +90° is ~12–15 ft-lb actual, not visual | $20 angle gauge, use it. |
| **Rotating crank with chain off, no cam lock** | Valve-to-piston contact, bent valves | Lisle 37950 in BEFORE chain out. Stays in until verified correct after 2 rotations. |
| **Pre-degreeing cams wrong before dyno** | Tuner wastes 2 dyno hours re-degreeing | Let the dyno tuner degree Skunk2 Pro gears — that's what they're for. |
| **Sealer on the Cometic MLS gasket** | Creates leak path between layers | Dry install only. No Hondabond, no copper spray. |
| **Reusing crank pulley bolt 90017-RWC-A01** | TTY stretch, loosens, crank damage | New bolt every time. ~$12. |
| **Reusing OEM exhaust manifold gasket** | Crush pattern wrong for new geometry, leaks | Fresh 18115-RRB-A01. OEM only. |
| **Driving to dyno on pre-head tune** | Lean WOT = cracked piston | Conservative base flash before first drive. 10-mile gentle loop. |

---

## Confirm-Before-Buy Checklist

Read this list the morning of the day I click buy on the $2,740 package:

- [ ] **RBC fitment confirmed via email from Luke@team4piston.com** for the 4P Pro 156v2 All Motor Package (assembled)
- [ ] **All parts in hand** or firm shipping ETAs that fit the install week:
   - [ ] 4P head package
   - [ ] Cometic C4561-030 gasket
   - [ ] ARP 208-4701 stud kit (VERIFIED P/N, not 208-4303)
   - [ ] Skunk2 Tuner Stage 2 cams 305-05-0220
   - [ ] Skunk2 Pro adjustable cam gears 304-05-0300
   - [ ] All fresh OEM gaskets (valve cover kit, IM, exhaust, cam seals, half-moon)
   - [ ] Timing chain bundle (see [`05-Timing-Chain-Maintenance/`](../05-Timing-Chain-Maintenance/overview.md))
   - [ ] VTC actuator 14310-RBC-003 ( -003, not -002)
   - [ ] Header bundle (see [`13-Headers/`](../13-Headers/install-guide.md))
   - [ ] IM bundle (see [`14-Intake-Manifold/`](../14-Intake-Manifold/overview.md))
   - [ ] Cooling bundle (see [`09-Cooling-System/`](../09-Cooling-System/overview.md))
   - [ ] NEW crank bolt 90017-RWC-A01
   - [ ] Break-in oil + filter
- [ ] **Lisle 37950 cam lock tool** on my bench, not in a cart somewhere
- [ ] **ARP stud installer tool** on my bench
- [ ] **Torque wrenches calibrated** within last 12 months (or replacement bought)
- [ ] **Straight edge + feeler gauges** for deck flatness check
- [ ] **Machine shop backup identified** in case deck warp check fails or a bolt hole strips — specific shop name, phone number, ballpark quote for resurface ($400–600) and for thread repair ($200–400)
- [ ] **Dyno session pre-booked** for ~14 days after install day with a Hondata-capable K-series tuner
- [ ] **Shop option quote** on the table: Honda specialist shop quote for bundled install. If under $2,000 and the shop has done 4P head installs before, seriously reconsider DIY at this complexity level.
- [ ] **Clear weekend + vacation days** scheduled. This is not the job I crash-squeeze into a Saturday.

---

## See Also / Cross-references

- [`overview.md`](overview.md) — the research behind picking 4P Pro 156v2 All Motor, cost breakdown, alternatives rejected
- [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) — full chain service procedure (measure tensioner rod, replace chain/arm/guides)
- [`../05-Timing-Chain-Maintenance/install-guide.md`](../05-Timing-Chain-Maintenance/install-guide.md) — Phase F through Phase L of timing cover + chain work references here
- [`../06-Ignition-Refresh/overview.md`](../06-Ignition-Refresh/overview.md) — VTC actuator 14310-RBC-003 (revised part), fresh plugs, fresh OEM coils
- [`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) — coolant drain + refill, Koyorad + hoses + thermostat + water pump bundle
- [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) — Skunk2 Alpha header install (exhaust stud prep + install happens during same teardown)
- [`../14-Intake-Manifold/overview.md`](../14-Intake-Manifold/overview.md) — Skunk2 Ultra Street IM + bored 66mm TB install at head reinstall
- [`../15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) — ATI Super Damper + NEW crank pulley bolt 90017-RWC-A01 + yield torque procedure
- [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — mandatory dyno retune, daily/sport two-map requirement, reliability-first ceilings
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — every fastener spec cross-referenced here
- [`../docs/maintenance-parts-catalog.md`](../docs/maintenance-parts-catalog.md) — head P/Ns added to build-wide catalog

---

*Last updated: 2026-04-20*
