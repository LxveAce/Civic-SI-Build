# Purple Cosmetics Install Guide — Batched Aesthetic Install

## Status: Not started

---

## Reality Check

This is the aesthetic layer. None of it adds a single horsepower. I'm writing this guide because I want the engine bay to look as good as it goes, and because a disorganized purple theme looks worse than no theme — mismatched shades, off-torque bolts, or three different "purples" next to each other will make me regret the spend.

Roughly 80% of the work is trivial: unscrew the old part, screw in the new purple one, 5-15 minutes each. The other 20% is planning:

- **Samco purple silicone hoses** — requires cooling-system drain. Bundles with Phase 09. I am not draining coolant twice.
- **Radium 20-0270-00 reservoir, custom purple anodize** — 4-6 week lead; call Radium direct at 503-244-0990 (custom anodize isn't on their website).
- **Powder-coat batch** — valve cover + fluid caps + any other cosmetic metal. 1-2 weeks at a local shop, parts-off car.
- **G2 G2165 caliper paint** — bundles with the 04-Brakes rear install so I'm not pulling calipers twice.

Honest framing: this is a few hundred to a couple thousand dollars spent on how the car looks. That's fine — I want the bay to look as good as it goes — but it isn't performance work. Reliability-first still applies: if a purple part creates a mechanical conflict (see NST crank pulley), the purple part loses.

---

## Prerequisites / Cross-References — READ FIRST

### CRITICAL: NST crank pulley CONFLICTS with ATI Super Damper

The NST22015K-Purple kit ships as three pieces (crank + alt + idler). Phase 15 (see `15-Pulleys-and-Harmonic-Balancer/overview.md`) puts an **ATI Super Damper 918477** on the crank for proper harmonic damping at 170k miles. Non-negotiable — the NST billet crank pulley deletes the harmonic damper entirely, and I'm not deleting the damper at this mileage.

**What to order:** alternator + idler only, purple, direct from NST (nonstoptuning.co). Contact NST — they'll split the kit on request. Confirm on the order that the crank piece is EXCLUDED. If the seller won't split, buy the full kit and leave the NST crank piece in the spare-parts bin. The ATI 918477 is what goes on the crank, full stop.

Install happens during Phase 15, after the ATI is torqued. See Batch D.

### Cooling parts bundle with Phase 09

Samco hoses, Radium reservoir, Hybrid Racing HYB-TBC-00-10 T-bolt clamps, and Royal Purple Purple Ice 01600 all go in during the Phase 09 cooling refresh (`09-Cooling-System/overview.md`). I am not draining the cooling system twice. Order Samco early enough that it arrives before Phase 09 starts.

### G2 caliper paint bundles with the 04-Brakes rear install

Full procedure in `04-Brakes/purple-calipers.md`. One G2165 kit covers all four corners. Paint during the rear pad/rotor install when the car is already up on stands and all four wheels are off. The fronts were installed 2026-04-20 (Hawk HPS + R1 Concepts) — pull them for paint during that same weekend if practical, or accept asymmetric purple until the next brake service.

### Powder-coat batch includes strut bar — but strut bar is DEFERRED

The Megan Racing strut bar is owned in polished finish, but install is deferred until after BC Racing coilovers (Phase 17) — pillow-ball camber plates change strut-top geometry and the bar may not clear. Don't send the bar for coating until fitment is verified. First powder-coat batch (Batch E) runs without the strut bar.

### Valve cover powder coat bundling

The valve cover comes off during Phase 06 (ignition refresh — plugs, coils, VTC actuator) and again during Phase 16 (head service). Whichever happens first after the coated cover is back from the shop, that's the install moment. Do NOT pull the valve cover just for cosmetics — pair it with mechanical work that's already opening the area.

---

## Tools Required

- Phillips + flathead screwdrivers
- Metric Allen key set (DUB kit uses 4mm, 5mm, 6mm mostly — long-reach helps)
- Metric sockets 8mm-17mm
- Torque wrench, inch-pound range (for low-torque valve cover hardware — a ft-lb wrench is too coarse)
- Torque wrench, 10-50 ft-lb (for pulleys)
- Dielectric grease — for any electrical connector disturbed during dress-up
- Masking tape + painter's paper — caliper paint and general masking
- Blue threadlocker (Loctite 243) — for structural DUB fasteners only, per DUB install notes
- Red Scotchbrite — caliper paint surface prep
- Brake cleaner — caliper prep
- Nitrile gloves — G2 hardener is nasty
- Clean rags and a parts tray

**Do NOT threadlock:** plastic-covered fasteners, heat-critical coil-on-plug area, the Acuity oil cap (o-ring seal — hand-tight), the K-Tuned dipstick (o-ring seal), or the shift knob threads (hand-tight only per Acuity).

---

## Parts List

Full pricing and rationale in `overview.md`. Install-side checklist:

| # | Item | Part # | Price |
|---|------|--------|-------|
| 1 | Oil filler cap | Acuity 1927-PPL Purple Podium | ~$80 |
| 2 | Dipstick | K-Tuned DP2-K20-PRP | ~$72 |
| 3 | Dipstick retention spring | K-Tuned DP2-SPR-KIT | ~$25 |
| 4 | Shift knob | Acuity ESCO-T6 1886-T6P Satin Purple | ~$92 |
| 5 | Engine-bay titanium bolt kit | Dress Up Bolts HON-027-TI (Purple) | ~$125 |
| 6 | Valve cover hardware | Skunk2 649-05-0120-PPL | ~$55 |
| 7 | Accessory pulleys (alt + idler ONLY) | NST22015K-Purple, crank excluded | ~$180 |
| 8 | Fender washer kit | Password:JDM Purple 6-pack | ~$22 |
| 9 | Silicone hose kit | Samco Sport FG2 purple (custom) | ~$280-340 |
| 10 | Coolant reservoir | Radium 20-0270-00 custom purple anodize | ~$310 |
| 11 | T-bolt hose clamps | Hybrid Racing HYB-TBC-00-10 | ~$45 |
| 12 | Radiator cap | Koyorad SK-C13 + local powder coat | ~$55 |
| 13 | Coolant conditioner | Royal Purple Purple Ice 01600 | ~$12 |
| 14 | Caliper paint kit | G2 G2165 Purple epoxy | ~$55-75 |
| 15 | Powder-coat batch | Local shop, candy/illusion purple | $330-565 |

Full program lands around $1,700-2,100.

**Do NOT source from Amazon:** Password:JDM washers (fakes), "purple anodized" T-bolts (corrode on coolant), "purple Mugen" valve covers (all fake — real Mugen K-series covers are red wrinkle only).

---

## Step-by-Step — Batched Install

Five batches. Each attaches to a mechanical job that's already happening, so no assembly opens twice for cosmetic work.

### Batch A: Bolt-On Swaps (1-2 hours, anytime)

No dependencies. A clean Saturday afternoon, engine cold, parts tray, shop rag.

**A-1: Oil filler cap (Acuity 1927-PPL)**

Engine cold. Wipe around the cap, unscrew OEM, verify the Acuity's o-ring is seated in the dovetail groove, thread in clockwise **hand-tight only** — the o-ring seals on the dovetail; overtightening cracks billet or crushes the o-ring. Keep the OEM cap as spare.

**A-2: Dipstick (K-Tuned DP2-K20-PRP)**

Engine cold. Pull OEM straight up — steady pressure, no jerking. Wipe the tube mouth. Verify both o-rings seated on the K-Tuned shaft. Insert until handle bottoms on the tube. If installing the DP2-SPR-KIT retention spring, follow K-Tuned's instructions — headers (Phase 13) raise crankcase pressure and can push a non-retained dipstick up during spirited driving, so the spring is worth $25 any time after headers.

**A-3: Shift knob (Acuity ESCO-T6 1886-T6P)**

Acuity's ESCO-T6 threads onto M10x1.5, same as my Acuity 3-way adjustable shifter. Honda's stock shift shaft is reverse-thread, but the aftermarket adjustable and the ESCO-T6 both use standard M10x1.5 right-hand. **Confirm against Acuity's printed instructions** — their docs are explicit about thread direction per shifter.

Shifter in neutral, parking brake on. Unscrew current knob (CCW on the Acuity shifter). Back off lock ring if present. Clean threads. Thread the ESCO-T6 on by hand CW until it bottoms at the orientation I want. Hand-tight only — 6061-T6 billet doesn't need cranked torque. Snug the lock ring against the knob base to lock angular position.

**A-4: Dress Up Bolts HON-027-TI (24 pieces)**

Slowest sub-step. Rule: **swap one bolt at a time.** Don't pull a whole assembly out.

- Blue threadlocker (Loctite 243) on structural bolts DUB flags — typically strut tower bolts and intake manifold brackets. No threadlocker on plastic-covered, heat-critical, or anywhere DUB says don't.
- Titanium galls. Thin nickel-based anti-seize on every Ti-into-steel or Ti-into-aluminum thread. **Not copper-based** — copper accelerates galvanic corrosion on titanium.
- Follow DUB's published torque per-fastener. For anything also in `docs/torque-specs.md`, use the OEM spec.
- Install the whole kit at once — anodize tone shifts slightly between batches.

**A-5: Skunk2 valve cover hardware (649-05-0120-PPL)**

Two options:

- **Valve cover staying on car:** swap the 8 bolts + washers one at a time in star pattern, torqued to OEM valve cover spec (K20Z3 is ~7-10 ft-lb per `docs/torque-specs.md` — over-torque warps the cover). Engine cold.
- **Valve cover coming off for powder coat or Phase 06:** skip this step now. Install the Skunk2 hardware when the coated or serviced cover is reinstalled. Saves handling twice.

### Batch B: Cooling System Purple (bundled with Phase 09)

Full drain/fill/bleed procedure lives in the Phase 09 install guide. Purple-side additions:

**Advance ordering:**
- Samco order 6 weeks before Phase 09 start (4-6 week custom color lead).
- Call Radium at **503-244-0990** 6-8 weeks ahead to request custom purple anodize on 20-0270-00. Custom anodize is not on their website — phone only.
- Hybrid Racing HYB-TBC-00-10 T-bolt kit — no lead time.
- Royal Purple Purple Ice 01600 — off the shelf.

**At Phase 09 install:**
- Replace each OEM hose with the Samco equivalent in the Phase 09 sequence. Shapes are identical — 8thcivic-confirmed fitment.
- T-bolt clamps on every silicone-to-metal junction (worm-gear fails on silicone). Torque to T-bolt spec (~40-50 in-lb initial), re-check after first heat cycle.
- Radium 20-0270-00 mounts on the passenger strut tower area. Plumb overflow from the radiator cap nipple into the reservoir, pressure-vented return out the top (-6AN fittings, sight tube).
- Fill with Honda Type 2 OL999-9011 per Phase 09 bleed procedure. **Do NOT substitute Engine Ice** for purple tint — propylene glycol chemistry mixed with Honda Type 2 is a hazard to the water pump and head. Purple look comes from the additive, not a different base coolant.
- After system is bled at operating temp, add Royal Purple Purple Ice 01600 per bottle instructions (~12 oz into the 1.3-gal K20Z3 system). Purple Ice is a Type-2-compatible conditioner.

### Batch C: Caliper Paint (bundled with 04-Brakes rear install)

Full procedure in `04-Brakes/purple-calipers.md`. Summary:

- One G2 G2165 kit covers all four corners.
- Prep is the critical part: brake clean, wire-brush loose rust, scuff with red Scotchbrite, final brake-clean wipe. No oil, no fingerprints.
- Mask rotor faces, pads, backing plates, brake hose, **slider boots especially** (heat-sensitive rubber — paint destroys them).
- 2-3 thin coats, 15-20 min tack between coats.
- 2 hr wheel-on cure, wheel back on, torque lugs to **80 ft-lb** (FG2 spec).
- First 50 miles: gentle, no hard stops. Epoxy finishes cross-linking under normal brake heat.
- No power-wash on calipers for 7 days.

Weekend sequence: unbox rear pads + rotors, jack all 4 corners, install rears, **paint all 4 calipers while exposed**, cure overnight, wheels on, Hawk factory bed-in on all four together.

### Batch D: NST Pulleys (bundled with Phase 15)

ATI 918477 is already on the crank when this starts.

1. Release the auto tensioner, remove serpentine belt. Replace with fresh OEM or Gates K070663 if showing wear — new pulleys on a 170k belt invites belt walk I'd misdiagnose as a pulley problem.
2. Swap alternator pulley: hold with correct spanner, back off stock nut, remove stock pulley, install NST purple alt, torque to NST's published spec (~30-35 ft-lb — **verify against NST's instructions**, spec is model-specific).
3. Swap idler: unbolt single center bolt, install NST purple idler, torque to NST's spec (~20-25 ft-lb — **verify**).
4. Route belt per underhood diagram. Verify centered in every groove. Rotate engine one full turn by hand (on the crank bolt) and re-verify tracking.
5. Start engine. No belt noise should be present.
6. Re-check tension and tracking at 100 miles.

### Batch E: Powder-Coat Batch (1-2 weeks, parts-off)

Long wall-clock time but almost all of it is parts sitting at the coater.

**Batch contents (first batch):**
- Stock K20Z3 valve cover. Mask mating surfaces (gasket rail, coil-on-plug seats, breather fittings) before coating. Mark masking points with Sharpie before dropoff; show the coater exactly.
- Brake master cylinder cap OEM 46662-S9A-003 — **buy a spare** so the car stays drivable during the batch.
- Power steering reservoir cap OEM 53697-SB3-952 — spare.
- Washer fluid cap — spare.
- Any other purely cosmetic metal decided by batch day.

**Batch exclusions:**
- **Megan strut bar — DEFERRED** until Phase 17 coilover fitment verified.
- **Koyorad radiator core — NEVER.** Powder on fins acts as thermal insulator, reducing cooling efficiency — directly at odds with Phase 09's E85 heat-headroom goal. Core stays bare aluminum. End-tank-only powder ($75-125) is tolerated but I'm skipping even that.
- **Exhaust-exposed parts** — paint fails at exhaust temp. Ceramic coat (silver, not purple) for any exhaust part.

**Shop selection:**
- Local coater with color-match capability.
- Experience with candy/illusion purple over silver base.
- Bring the Acuity oil cap to the shop for in-person color matching against already-installed purple parts.

**Sequence at coater:** strip → sandblast → powder (base + color + clear for candy purple) → oven cure 375-400°F 15-20 min → QC inspection.

**Reinstall:**
- Valve cover goes back on with **fresh gasket** (OEM 12341-RBC-003 or equivalent), fresh half-moon seals, and Skunk2 649-05-0120-PPL hardware. Pair with Phase 06 or Phase 16 — whichever is first.
- Fluid caps are 30-second swaps whenever.

**Don't rush the cure.** Hot powder handled with bare hands or recontaminated by oil, fuel, or coolant bubbles at the first real heat cycle. If a coat looks bad at pickup, send it back.

---

## Timing / Batch Planning

Stack the batches so no mechanical job opens twice:

1. **Batch A (bolt-ons) — anytime.** No dependencies. Do it whenever the kit arrives; delivers visible purple immediately, which makes the slow batches feel less like pure waiting.
2. **Batch E (powder-coat) — start when the valve cover is expected to come off next.** 1-2 week coater lead; parts are off-car during the window. Pair with Phase 06 ignition refresh (typically first to pull the valve cover). Ship the day it comes off; by reassembly time the coated cover is back.
3. **Batch C (caliper paint) — during the 04-Brakes rear install weekend.** All four corners in one weekend, bed-in together.
4. **Batch B (cooling purple) — during Phase 09.** Samco and Radium orders placed 6-8 weeks ahead of Phase 09 start.
5. **Batch D (NST pulleys) — during Phase 15.** Alt + idler only; ATI on the crank.

Every batch attaches to a mechanical job that's happening anyway. No cosmetic-only teardown. That's the whole design.

---

## First Impression Checklist

Walk-around inspection after all five batches are complete:

- [ ] All purple items are the same shade family under natural daylight — no Prince-purple anodize next to lavender powder-coat next to Crown-Royal caliper paint.
- [ ] Engine bay reads clean from the passenger side with the hood up (that's where people look first at a show).
- [ ] Caliper paint edges sharp; no overspray on rotor, hub, pad backing plate.
- [ ] Every DUB fastener torqued to spec. Re-check at 1k miles — titanium bolts settle.
- [ ] No coolant weep at any silicone hose junction after the first heat cycle. Re-torque T-bolts.
- [ ] Shift knob angle correct for hand position; lock ring tight if used.
- [ ] Valve cover gasket not weeping oil, especially at corners.
- [ ] Radium reservoir mounted square, sight tube shows correct level.
- [ ] Samco hose routing does not contact alternator, pulleys, belt, or steering linkage.

---

## Common Mistakes

1. **Ordering the full NST kit without excluding the crank pulley.** Either a paid-for spare in a box, or (worse) the NST billet crank ends up on the engine deleting the harmonic damper I explicitly chose ATI for. Always order NST22015K with crank EXCLUDED.
2. **Powder-coating the radiator core.** Fin powder acts as thermal insulator — directly undermines the Phase 09 upgrade. Koyorad stays bare aluminum.
3. **Engine Ice instead of Honda Type 2 + Purple Ice.** Propylene glycol with a different inhibitor package. Mixing voids the water pump and head gasket longevity guarantees. Type 2 OL999-9011 is the coolant; Purple Ice 01600 is the conditioner for the tint.
4. **Overlooking Samco lead time.** 4-6 weeks custom. If Phase 09 starts before Samco arrives, I either sit with a drained system (bad for seals) or fill with rubber and drain again later.
5. **Rushing Batch E reinstall.** Slapping the coated valve cover on the engine before full cure bubbles at the first coil-on-plug heat cycle. Let the coat cure fully.
6. **Copper anti-seize on titanium DUB bolts.** Accelerates galvanic corrosion on titanium. Use nickel-based for Ti-into-steel or Ti-into-aluminum.
7. **Amazon Password:JDM fender washers.** Minefield of fakes. Tecnocraft, CorSport, or Password:JDM authorized only.
8. **"Purple anodized" T-bolt clamps on coolant.** Documented corrosion. Stainless only — Hybrid Racing HYB-TBC-00-10.

---

## Maintenance Notes

- **Park covered if possible.** Direct UV fades purple anodize and purple paint over years. The hood shields most of the bay; cabin UV hits the shift knob, and the calipers see full sun through the wheel.
- **G2 caliper epoxy** — durable but not forever. Plan on touch-up or repaint every 3-5 years on a regularly driven car. One G2165 kit at each interval.
- **Samco silicone hoses** — 7-10 year lifespan like any quality silicone. Inspect for surface cracking or age-hardening at every coolant change.
- **Dress Up Bolts titanium** — anodize on titanium is an oxide-layer interference effect, not dye. Color is indefinitely stable. **Re-torque at 1k miles** (Ti settles) and annually thereafter.
- **Skunk2 valve cover hardware** — re-torque at 1k miles after install, then at every valve cover gasket replacement.
- **Acuity oil cap** — billet is stable, o-ring is the wear item. Replace o-ring at oil-change cadence if it shows compression set or cracking. Acuity sells replacements individually.
- **Radium reservoir** — hard-anodize will outlast the silicone around it. Inspect -6AN fittings for seep at every coolant service.
- **NST pulleys** — idler bearings are the life-limited item. Listen for whine or rumble at idle; NST sells bearing service kits. The alt pulley has no wear surfaces.

---

## See Also / Cross-References

- [`overview.md`](overview.md) — full parts list, pricing, tier breakdown, rationale
- [`../04-Brakes/purple-calipers.md`](../04-Brakes/purple-calipers.md) — G2 caliper paint full procedure
- [`../09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) — Samco + Radium + Purple Ice integration
- [`../15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) — ATI rationale + NST alt/idler install
- [`../18-Strut-Bar/`](../18-Strut-Bar/) — Megan bar deferred until post-coilover; powder-coat after Phase 17 fitment check
- [`../06-Ignition-Refresh/`](../06-Ignition-Refresh/) — valve cover pull point; pair with powder-coat install
- [`../16-Cylinder-Head/`](../16-Cylinder-Head/) — alternate valve cover pull point if Phase 06 already done
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — OEM torque values for Batches A, B, D
- [`../CLAUDE.md`](../CLAUDE.md) — project-wide context

---

*Last updated: 2026-04-20*
