# Cooling System Refresh — Radiator, Thermostat, Hoses

## Status: Planned — Do BEFORE headers and BEFORE E85 tune

## Why This Gets Its Own Folder

At 170,000 miles, my radiator is a ticking time bomb. The FG2 OEM radiator has plastic end tanks that crack around 150-180k — the passenger-side end tank is the usual first failure. Symptom is steam from the front of the engine bay and coolant on the driveway, usually on a hot summer day when I least want to deal with it.

On top of that, full bolt-ons + E85 + 240 WHP will dump meaningfully more heat into the cooling system than the car was designed for. More combustion → more heat → higher coolant temps → potential heat soak during a summer dyno session or a hard canyon run.

I'm proactively replacing the whole cooling side of the engine while I'm doing everything else. No surprises, better thermal headroom.

---

## 1. Radiator

### Why I'm Upgrading, Not Just Replacing

If I was staying stock I'd just buy another OEM plastic-tank radiator and drive on. But at my power target, the all-aluminum aftermarket radiator does two things that actually matter:

1. **More heat rejection** — roughly 15-20% larger core volume, full-aluminum end tanks, better fin density
2. **No plastic end tanks to crack** — the #1 failure point on the OEM unit is simply gone

The gain isn't just peace of mind. E85 dumps noticeably more heat into coolant than pump gas (higher fuel volume, more combustion mass). A hot dyno session on pump gas with the stock radiator would probably be fine. On E85 full bolt-on, margins get thinner.

### Options

| Radiator | Core | End Tanks | Fitment | Approx Price | Notes |
|----------|------|-----------|---------|--------------|-------|
| **Koyorad HH060063** | All-aluminum, 36mm core | Aluminum | Direct fit FG2/FA5 | ~$250 | **My pick.** Proven on 8thcivic. No modification needed. |
| Mishimoto MMRAD-CIV-06SI | All-aluminum, 42mm core | Aluminum | Direct fit | ~$370 | Thicker core. Overkill for NA. Lifetime warranty. |
| OEM Honda 19010-RRB-A51 | Plastic/aluminum | Plastic | Direct fit | ~$180 | Same design that failed once already. Don't buy this twice. |
| PWR C-4418 | All-aluminum | Aluminum | Fit requires trimming | ~$450 | Race-grade. Overkill for street. |

**Decision: Koyorad HH060063.** Sweet spot for a street/autox FG2 at 240 WHP on E85 — enough extra capacity to matter, no fitment drama, and $120 cheaper than the Mishimoto for essentially the same functional outcome at my power level. The Mishimoto's thicker core is nice but genuinely unnecessary for NA.

---

## 2. Thermostat

### Stock vs Low-Temp — Why I'm Going Stock

A lot of guys default to a 160F low-temp thermostat with every cooling upgrade. **I'm not doing that.** Here's why:

- FlashPro has full control of the cooling fan tables. I can tune my fan on-point to 185-195F and keep coolant temps right where I want them through software, without hacking the thermostat spec.
- The K20Z3 wants to be at 190-200F for optimal combustion efficiency. Running it cold hurts fuel economy, increases wear, and causes more blow-by (PCV makes more work).
- Honda's 180F-opening stock thermostat is correct for the engine.

**I'll replace with the OEM part and tune the fan tables in Hondata to manage heat.**

| Part | P/N | Price |
|------|-----|-------|
| Honda OEM Thermostat | **19301-RAF-004** (K20Z3 Civic Si/TSX — confirmed. The 19301-RNA-305 part is for the R18 non-Si Civic, do NOT order that) | ~$30 |
| Honda OEM Thermostat O-ring | 19305-PR3-004 | ~$6 |

---

## 3. Hoses

OEM rubber hoses at 170k are almost certainly leaching plasticizer, soft, and overdue. Doing them now while the system is drained means no extra coolant loss and no extra labor.

| Hose | Honda P/N | Price |
|------|-----------|-------|
| Upper radiator hose | 19501-RRB-A00 | ~$30 |
| Lower radiator hose | 19502-RRB-A00 | ~$30 |
| Heater hoses (pair) | 79721-SNA-A00 / 79725-SNA-A00 | ~$40 |

**Silicone hose upgrade?** Functionally unnecessary for NA — OEM rubber at fresh condition is fine and cheaper. But the build has a purple aesthetic theme, and silicone is the only path to a purple coolant system. **If going purple: see the Purple Cooling System section below.**

---

## 4. Water Pump

The water pump is driven by the timing chain — inspect when the timing chain comes off, replace proactively if I'm already in there. This is already covered in my [timing chain inspection section](../docs/mod-order-and-maintenance.md#timing-chain-deep-dive).

| Part | P/N | Price | Notes |
|------|-----|-------|-------|
| Honda OEM Water Pump | **19200-RBC-013** (K20Z3 Civic Si — confirmed. 19200-RAA-A01 is a different family) | ~$90 | Replace proactively at 170k timing chain service |
| Honda OEM Water Pump Gasket | 19222-PNA-003 | ~$10 | Fresh gasket mandatory |
| Aftermarket option | Aisin WPH-802 (OEM-quality) | ~$65 | Acceptable substitute if Honda pump isn't available |

---

## 5. Coolant

### Type

Honda Type 2 coolant (blue). Premix, do not dilute further. Using anything else voids the water pump and head gasket longevity guarantees (the additive package is specific).

- **Honda OL999-9011 (Type 2 premix, 1 gallon)** — ~$25/gallon, buy 2 gallons (system holds ~1.3 gallons but I need extra for bleeding/topping)

**Do NOT use:**
- Prestone "universal" — wrong additive package
- Green ethylene glycol — completely incompatible
- "Water Wetter" only — not a standalone coolant, and I don't need it at NA power levels

### Bleeding Procedure

The K20Z3 has an air bleed screw on the upper radiator hose neck. Critical for proper fill:

1. Fill radiator slowly with engine cold, bleed screw open
2. Close cap, run engine with heater full hot, bleed screw cracked open
3. Burp/tilt car as needed until no air comes out
4. Top off expansion tank to MAX cold line

Skip this and I get an air pocket at the thermostat → overheating with a "good" temp sensor reading because the sensor is in a dry spot. Common 8th gen SI fail.

---

## Cost Summary

| Item | Price |
|------|-------|
| Koyorad HH060063 radiator | ~$250 |
| Honda OEM thermostat + gasket | ~$30 |
| Honda OEM upper + lower radiator hose | ~$60 |
| Honda OEM heater hoses | ~$40 |
| Honda OEM water pump (with timing chain service) | ~$80 |
| Honda Type 2 coolant (2 gallons) | ~$50 |
| Bleed/fill consumables | ~$10 |
| **Total (DIY)** | **~$520** |

Labor if I have a shop do the radiator alone: add $150-200. Water pump labor is effectively free during timing chain service.

---

## When To Do This

**Must happen BEFORE:**
- Headers (I want fresh cooling headroom when I add combustion heat from the larger exhaust flow)
- E85 dyno tune (see above — E85 dumps more heat)

**Can happen alongside:**
- Timing chain service (for water pump)
- Any other phase where car is up on stands

**Cannot be skipped:**
- If I see ANY weeping from the plastic end tank
- If coolant temps creep above 205F in summer traffic on the stock setup
- If there's a dye stain on the radiator fins (diagnostic of a seeping end tank)

---

---

## Purple Cooling System (Optional Aesthetic Layer)

The cooling system carries the purple theme more visibly than anywhere else in the engine bay because the hoses are long and prominent. This section is **all optional** — everything above covers the reliability-correct baseline.

### 6.1 Purple silicone hose kit — Samco Sport (custom color order)

**Samco Sport is the only reputable brand that offers purple as a factory color** for silicone hose kits. HPS, Mishimoto, Hybrid Racing, and K-Tuned all ship black/blue/red only for the FG2 kit.

| Item | Brand / Route | Price | Lead Time |
|------|---------------|-------|-----------|
| Samco Civic SI 06-11 (FD2/FG2) silicone kit in purple | Order direct at samcosport.com or through Andy's Autosport | $280-$340 | 4-6 weeks |
| Alt (faster): Mishimoto MMHOSE-CIV-06BL in blue (reads purple-family in certain light) | Mishimoto direct / Amazon | ~$115 | 1-2 days |

Samco kits are 4-ply reinforced, 350°F+, highly reviewed across K-series forums for fit and longevity. The lead time is the only annoyance.

### 6.2 Radium coolant reservoir (custom purple anodize)

Radium Engineering 20-0270-00 universal billet coolant tank with custom purple anodize:
- Base price: $294 black; add ~$20-50 for custom anodize
- 750 mL capacity, -6AN fittings, sight tube, 32mm pressure cap receiver
- Fitment: universal — requires bracket fabrication or creative mounting on FG2 (multiple builds use passenger strut tower)
- **Contact Radium direct** (503-244-0990) for custom purple — not published on their website

### 6.3 Radiator cap — no purple factory option

No reputable brand ships a purple-anodized cap rated for K20 system pressure (1.1 bar / 16 psi minimum). Options:
1. **Koyorad SK-C13** ($30, 1.3 bar, correct for the HH060063's Koyo-neck) powder-coated purple by a local shop for ~$20-40. Functionally correct, visually on-theme.
2. Keep Koyorad SK-C13 in factory red finish. Red reads well against purple silicone hoses in classic JDM aesthetic.

⚠️ The Koyo SK-C13 is a **deep-plunger** cap that fits Koyo necks only — it does NOT fit OEM Honda radiator necks. Keep a spare Mishimoto MMRC-13-SM ($25) on hand for any emergency OEM-radiator run.

### 6.4 T-bolt hose clamps — stainless only

Silicone hoses require T-bolt clamps (worm-gear fails on silicone). **No reputable brand ships purple-anodized T-bolts** — Vibrant, HPS, Mishimoto, Hybrid Racing are all stainless. Low-cost Hymee/Amazon anodized purple T-bolts have documented corrosion issues on coolant systems.

**Recommended: Hybrid Racing HYB-TBC-00-10** ($45) — stainless, correct sizes (4x 37-42mm + 2x 31-36mm) for the Civic SI FG2 hose kit.

### 6.5 Coolant — the iconic purple question

| Option | Purple? | Compatibility | Recommendation |
|--------|---------|---------------|----------------|
| **Honda Type 2 OL999-9011 (blue-green)** | No | Factory-correct for Honda aluminum | **Primary coolant.** Non-negotiable for long-term reliability. |
| Royal Purple Purple Ice 01600 (12oz additive) | Slight tint, ~5-10°F real-world summer temp drop | Compatible with Honda Type 2 | **Add.** Low risk, fits theme. |
| Engine Ice HPC1001 (purple, propylene glycol based) | Yes — true purple | Aluminum-safe, but different inhibitor chemistry from Honda Type 2 | **Avoid for full system.** Don't mix with Honda Type 2. Only use if fully flushing to Engine Ice, and even then most K20 builders revert after photos. |

**Decision:** Honda Type 2 ($50 for 2 gallons) + Royal Purple Purple Ice ($12) as the conditioner. Reliability first; purple tint as a bonus.

### 6.6 Skip list (not worth the purple chase)

- **Mishimoto fan shroud kit (MMFS-CIV-06SI)** — street benefit is minimal, $215, no purple. Skip.
- **K-Tuned billet thermostat housing** — adds failure points, $135, no purple for K20Z3. Skip.
- **Low-temp thermostat** — fights ECU, no real benefit with FlashPro fan tuning. Skip (already covered above).
- **Powder-coating the Koyorad radiator core** — reduces cooling efficiency (fin powder acts as insulator). End-tank-only powder is OK (~$75-125) but skip the full radiator.

### 6.7 Purple theme cost summary

| Configuration | Cost |
|---------------|------|
| Critical path (reliability, OEM parts) | ~$660 |
| + Samco purple hoses + Radium reservoir + T-bolt kit | +$665 = ~$1,325 |
| + Purple Ice + powder coat cap | +$40 = ~$1,365 |

---

## Complete Cost Summary (reliability baseline + optional purple)

| Configuration | Total |
|---------------|-------|
| **Reliability baseline (OEM Honda parts, no purple)** | **~$520-670** |
| Reliability baseline + Samco purple silicone kit | ~$900 |
| Reliability baseline + Samco + Radium reservoir | ~$1,250 |
| Full purple theme (Samco + Radium + Purple Ice + Koyo cap powder) | ~$1,400-1,600 |

---

## See Also

- [`21-Purple-Cosmetics/overview.md`](../21-Purple-Cosmetics/overview.md) — overall purple theme plan
- [`05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) — water pump replaced at same job
- [`docs/mod-order-and-maintenance.md`](../docs/mod-order-and-maintenance.md) — master plan sequencing
- [`docs/fluids-and-intervals.md`](../docs/fluids-and-intervals.md) — coolant interval and spec

---

*Last updated: 2026-04-20*
