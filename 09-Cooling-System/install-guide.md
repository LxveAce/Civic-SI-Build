# Cooling System Install Guide — Koyorad + OEM Pump/Thermostat + Purple Hoses

## Status: Pending — Phase 1F; must precede headers and E85

The FG2's OEM plastic-tank radiator is at the back half of its life at 170k, and thermal load goes UP when I add headers and E85. Doing it now, in my garage, beats a 95-degree breakdown three states from home.

**Coolant bleeding is the #1 DIY-caused failure on the K20Z3.** Rushed bleed = air pocket at the thermostat = sensor reads fine while a hot spot warps the head. That's a $2,000 mistake that takes an extra 20 minutes to avoid.

---

## Reality Check

- **Radiator + thermostat + hoses (no water pump):** 2-3 hours wrench time, plus drive/cool cycles for the bleed.
- **Water pump added:** +2-3 hours standalone. But the water pump is timing-chain-driven — **don't do it standalone.** Bundle with timing chain service in `05-Timing-Chain-Maintenance/`. Incremental labor there is ~30 minutes because the cover is already off.
- **Purple cosmetic add-on:** no additional wrench time, but Samco kit has a **4-6 week lead** and Radium custom anodize needs a phone call (503-244-0990). Order parts before picking up a tool.

Full Saturday first time through. Fresh coolant, slow bleed, two drive cycles, check next morning, check again in a week.

---

## Prerequisites / Cross-references

| Do First | Why |
|----------|-----|
| Order Samco purple hose kit if going purple | 4-6 week lead — call Samco direct or Andy's Autosport |
| Order Radium 20-0270-00 w/ purple anodize | Call Radium at 503-244-0990; not on website |
| Have all OEM part numbers in hand | No substituting. See Parts List below. |
| Decide on water pump timing | Standalone = don't bother. Bundle with `05-Timing-Chain-Maintenance` |

| Must Happen Before | Why |
|--------------------|-----|
| [`13-Headers/install-guide.md`](../13-Headers/install-guide.md) | Skunk2 Alpha dumps serious heat into the bay. I want cooling headroom in place before I add heat. |
| E85 tune (see [`19-Flex-Fuel-and-Fuel-System/`](../19-Flex-Fuel-and-Fuel-System/)) | E85 needs more fuel mass per combustion event → more heat rejected to coolant. |
| Any summer dyno session | Dyno cells get hot and still air doesn't cool a failing radiator. |

| Can Happen At The Same Time | Why |
|------------------------------|-----|
| [`05-Timing-Chain-Maintenance/`](../05-Timing-Chain-Maintenance/) water pump replacement | Timing chain comes off anyway; water pump becomes a 30-min add |
| [`21-Purple-Cosmetics/`](../21-Purple-Cosmetics/) Samco + Radium + Koyorad cap powder | This IS the purple cooling execution phase |

---

## Tools Required

**Critical:**
- 2-gallon drain pan, clean, labeled "COOLANT"
- 10mm, 12mm, 14mm sockets on a 3/8" ratchet
- Extension set (3", 6", and a wobble end for the block drain)
- Long-handled flathead screwdriver for the bleed screw on the upper rad hose neck
- Hose clamp pliers (OEM spring clamps are a pain without them)
- Torque wrench, 3/8" drive, 10-80 ft-lb range
- Coolant funnel kit with rad neck adapters (Lisle 24680 or similar — this is what makes the bleed not-awful)
- Spill mats or cardboard under the car — Honda Type 2 stains concrete
- 1 gallon of distilled water (for 50/50 mix if using concentrate; none needed if using premix)
- Jack + 4-ton stands — I need the car up to reach the lower hose and the block drain
- Chassis-safe jack pad for the subframe pinch weld

**Nice to have:**
- Inspection mirror + headlamp for the bleed screw (it's tucked behind the upper hose)
- Small pick for teasing old gasket material off the thermostat housing
- Shop rags (a lot — coolant gets everywhere no matter what)
- Latex or nitrile gloves — Honda Type 2 is not friendly to skin

---

## Parts List (verified against overview.md)

| # | Item | Part Number | Notes |
|---|------|-------------|-------|
| 1 | Koyorad aluminum radiator | **HH060063** | All-aluminum, direct fit FG2/FA5 |
| 2 | Honda OEM thermostat (K20Z3) | **19301-RAF-004** | **NOT 19301-RNA-305** — that's R18 non-Si |
| 3 | Honda OEM thermostat O-ring | 19305-PR3-004 | Fresh every install. No reuse. |
| 4 | Honda OEM water pump (K20Z3) | **19200-RBC-013** | **NOT 19200-RAA-A01** — different family |
| 5 | Honda OEM water pump gasket | 19222-PNA-003 | If doing the pump |
| 6a | Samco purple silicone hose kit | Samco Civic SI 06-11 custom purple | 4-6 week lead; Samco direct or Andy's |
| 6b | OR Honda OEM upper hose | 19501-RRB-A00 | Non-purple reliability baseline |
| 6c | OR Honda OEM lower hose | 19502-RRB-A00 | Non-purple reliability baseline |
| 6d | OR Honda OEM heater hoses (pair) | 79721-SNA-A00 + 79725-SNA-A00 | Non-purple reliability baseline |
| 7 | Radium coolant reservoir | **20-0270-00** w/ custom purple anodize | Call 503-244-0990 direct |
| 8 | Hybrid Racing stainless T-bolt clamps | **HYB-TBC-00-10** | 4x 37-42mm + 2x 31-36mm |
| 9 | Primary coolant | Honda Type 2 OL999-9011 | Buy 2 gallons premix |
| 10 | Coolant additive | Royal Purple Purple Ice **01600** | Additive only, not a coolant |
| 11 | Koyorad rad cap | SK-C13 | **Koyorad necks only — will NOT fit OEM** |
| 12 | Backup rad cap | Mishimoto **MMRC-13-SM** | Emergency OEM-neck cap; keep one in the trunk |

**Part number discipline:** Honda cross-year K20 parts look similar. No substituting 19301-RNA-305 (R18) or 19200-RAA-A01 (wrong pump family) because "the dealer had it in stock." Wrong P/N = wrong temperature, wrong flow, wrong fit.

---

## Step-by-Step

### Phase A: Drain the System

1. **Engine MUST be cold.** Overnight ideal. Warm coolant under 16 psi will burn me and give false bleed readings. Non-negotiable.
2. Lift the front onto jack stands on the subframe. Chock the rear wheels.
3. Drain pan under the radiator.
4. Remove radiator cap slowly. Any hiss = not fully cold; wait.
5. Open the drain petcock (plastic thumbscrew, driver-side lower corner). Drains ~1 gallon from the radiator.
6. Move pan under the block drain — small hex bolt on the drive-belt (passenger) side, near the oil filter housing. Another ~0.3 gallon comes out of the block.
7. Reinstall block drain with fresh washer, hand tight + 1/8 turn (soft bolt).
8. Close the radiator petcock.

Skipping the block drain keeps 30% of the old coolant in the system and dilutes the fresh fill.

### Phase B: Radiator Swap (if no water pump this session)

9. Disconnect both fan shroud electrical connectors (rad fan + condenser fan), push-tab release.
10. Remove 4 fan shroud bolts (10mm). Shroud transfers to the Koyorad — don't trash it.
11. Loosen upper hose clamp at the radiator. Twist off gently (cracked plastic neck = new problem).
12. Loosen lower hose clamp at the radiator.
13. Remove the 2 upper radiator mount brackets (10mm, 1 per side).
14. Lift the radiator straight up and out.
15. **Dry-fit the fan shroud to the Koyorad HH060063 before bolting.** Koyorad publishes direct fitment; I verify anyway. Shroud tabs should line up. If not, confirm I have HH060063 (not the 42mm Mishimoto).
16. Transfer shroud to Koyorad. Re-bolt.
17. Lower Koyorad into the lower rubber mounts. Bolt upper brackets down.
18. Reconnect fan shroud harnesses.
19. Slide upper and lower hoses onto Koyorad necks. **Use NEW Hybrid Racing HYB-TBC-00-10 T-bolt clamps.** Don't reuse OEM spring clamps on silicone — they cold-flow through and leak.
20. Torque T-bolts to HR spec (~35-45 in-lb). Silicone deforms easily; if the hose "gives," back off 1/4 turn.

### Phase C: Water Pump (IF bundled with timing chain service — see `05-Timing-Chain-Maintenance/`)

**If I'm doing this standalone, stop and reschedule for timing chain service.** Water pump solo is 2-3 hours of timing cover work for a $90 part. Bundled, it's 30 minutes.

21. Front cover should already be off per `05-Timing-Chain-Maintenance/install-guide.md`. If not, go execute that phase first.
22. Remove the 3-4 water pump bolts (10mm). Pump pulls off with the gasket.
23. Clean the block mating surface with a plastic razor. No metal — aluminum gouges become leak paths.
24. Brake cleaner + lint-free cloth. Let flash off.
25. Dry-fit Honda **19200-RBC-013** with new gasket 19222-PNA-003. Honda spec is no RTV; I'm following it. (Thin film of Permatex Ultra Grey optional — OEM gasket dry is warranty-correct.)
26. All bolts hand-tight in cross pattern, then torque.
27. Torque water pump bolts to **9 ft-lb** (per `docs/torque-specs.md`), star pattern, 2 passes.
28. Return to `05-Timing-Chain-Maintenance/` to reinstall chain, tensioner, cover.

### Phase D: Thermostat Swap

29. Thermostat housing is on the block, driver side, near the lower rad hose. 2 bolts (10mm).
30. Disconnect lower rad hose from the housing. Residual coolant drips — rag ready.
31. Remove the 2 housing bolts. Lift off.
32. Pull old thermostat. Note orientation: **jiggle valve UP** (12 o'clock). The jiggle valve is the small spring-loaded pin that lets air escape when closed. Wrong orientation = chronic air pocket.
33. Scrape old O-ring residue from the housing groove. Brake cleaner on mating surface.
34. Install NEW **19301-RAF-004** thermostat into the block recess. Jiggle valve UP.
35. Install NEW **19305-PR3-004** O-ring. Do NOT reuse — it's 170k miles compressed.
36. Reinstall housing, both bolts hand-tight first, then torque.
37. Torque housing bolts to **9 ft-lb** (per `docs/torque-specs.md`).
38. Reconnect lower rad hose with NEW T-bolt clamp.

### Phase E: Hose Installation (if doing Samco purple set)

39. Lay out Samco set on cardboard — upper, lower, heater pair, any small bypass hoses. Verify kit matches Samco's FG2 06-11 list.
40. Upper hose first — radiator neck, then engine side. Clock so Samco logo faces forward.
41. Lower hose next — routes past alternator. **Confirm ≥1" clearance from the alternator case.**
42. Heater hoses — run to firewall. Route away from header area; leave slack for post-header re-route.
43. Install HYB-TBC-00-10 T-bolts. Torque to spec — **don't crank down on silicone.** Overclamping = permanent deformation and pressure-cycle weeping.
44. Confirm no hose contacts alternator case, exhaust manifold, AC compressor, or any sharp edge.

### Phase F: Reservoir Swap (Radium 20-0270-00 with purple anodize)

45. Drain the stock plastic reservoir — unclip, invert over drain pan.
46. Disconnect overflow hose at the reservoir.
47. Remove stock reservoir bracket from chassis. Save hardware.
48. Mount Radium 20-0270-00 per supplied instructions. Most FG2 builds mount on the passenger-side strut tower; verify no conflict with [`18-Strut-Bar/`](../18-Strut-Bar/).
49. Install -6AN fittings per Radium's diagram. Thread sealant per their spec.
50. Route overflow line from rad cap neck to Radium inlet. Trim to length; zip-tie away from hot surfaces.
51. Torque Radium mount hardware to supplier spec.

### Phase G: Fill + Bleed — THE CRITICAL PROCEDURE

This is where a lazy DIY becomes a head job. Read it twice.

52. Walk the system — confirm all clamps torqued, hoses seated, drains closed.
53. Coolant: **Honda Type 2 OL999-9011 premix — do NOT dilute.** If I bought concentrate by mistake, mix 50/50 with distilled (not tap) water.
54. Add Royal Purple Purple Ice **01600** per bottle (~12oz for this system). **Purple Ice is an additive, not a coolant replacement.** Goes IN ADDITION to Honda Type 2.
55. Install Lisle funnel kit on the radiator neck — the key to filling without air lock.
56. Pour coolant slowly into the funnel.
57. **Open the bleed screw** on the upper hose junction (small plastic screw on the metal fitting near the thermostat). Close when coolant streams without bubbles.
58. Keep topping the funnel. When it stops draining, system is approximately full cold — air pockets remain.
59. **Start the engine, cap OFF** (Lisle funnel sealed to the neck). Idle.
60. Heater to FULL HOT, fan low — opens the heater core loop and pulls air from there.
61. Rev to ~2000 RPM, hold 30 sec, release to idle. Pumps coolant, breaks air pockets loose.
62. Repeat every minute. Coolant drops suddenly when the thermostat opens (upper hose gets hot). Top off immediately.
63. Continue until no bubbles in the funnel, upper hose fully hot, heater blows HOT, level stable.
64. Remove funnel carefully (it's full). Install the Koyorad SK-C13 cap (Koyorad cap on Koyorad neck only — Mishimoto MMRC-13-SM stays in the trunk for OEM-neck emergencies).
65. Top off Radium reservoir to MAX COLD.
66. Drive gently 10 min — no WOT, no sustained high RPM. Full heat cycle.
67. Park. Cool COMPLETELY — 4 hours minimum, overnight better.
68. Re-check Radium reservoir. It will have dropped as remaining air purged. Top up to MAX COLD.

### Bleed Verification

- **+1 day:** Check reservoir, top off, look for drips.
- **+1 week:** Check reservoir. Cold engine, pop the cap, verify the radiator neck is full.
- **+1 month:** Check again. Still dropping = slow air-pull or leak; investigate.

Stable at MAX COLD after a week = properly purged.

---

## First Drive Checklist

- Temp gauge reaches normal (dead center / slightly below) in ~5 min and stays there.
- Heater blows HOT with temp knob full hot. Cold = air pocket in heater core, back to bleed.
- No coolant smell, cabin or engine bay.
- Radium reservoir stable (slow drop in first week = residual air purge, OK).
- No drips after drive + overnight sit.
- Rad fan cycles on and off correctly.
- No steam from the engine bay — ever. Steam = hot spot or leak, shut down immediately.

---

## Common Mistakes (Don't)

1. **Wrong thermostat P/N.** 19301-RNA-305 is R18 non-Si — NOT K20Z3. Verify **19301-RAF-004** on the box.
2. **Wrong water pump P/N.** 19200-RAA-A01 is a different K-family. Verify **19200-RBC-013**.
3. **Koyorad SK-C13 cap on OEM neck.** SK-C13 is a deep-plunger cap for Koyorad necks only. On an OEM neck it won't seal — lose system pressure, boil below normal temp. That's what the Mishimoto MMRC-13-SM backup is for.
4. **Mixing Engine Ice with Honda Type 2.** Different inhibitor chemistry. Reacts, drops out of solution, clogs the heater core. Full flush first if switching.
5. **Skipping the block drain.** Keep 30% old coolant, dilute the fresh fill. 5-minute step.
6. **Skipping or rushing the bleed.** Air pocket at the thermostat = sensor reads fine while a hot spot warps the head. Most common DIY-caused K20 death. Spend the full hour.
7. **Powder-coating the Koyorad core.** Fin powder = insulator = 10-20% less heat rejection. **End tanks only** for powder coat.
8. **Over-torquing T-bolts on silicone.** Silicone cold-flows — crank down, clamp loosens at the first heat cycle, weeps. Spec only.
9. **Reusing the thermostat O-ring.** 170k miles compressed. $6 new.
10. **Tap water.** Minerals coat the water pump impeller and head jackets. Distilled only.

---

## Purple Cosmetics Integration Note

The cooling system is the most visible purple layer because hoses run half the bay. Two lead-time gotchas:

1. **Samco Sport purple silicone kit:** 4-6 week lead, custom color run. Samco direct or Andy's Autosport. **Don't start this phase with OEM hoses planning to "swap to Samco later"** — filling the system twice is wasted coolant and an extra bleed.
2. **Radium 20-0270-00 custom purple anodize:** not on Radium's website. Call **503-244-0990**. ~$20-50 surcharge over black, 2-3 week lead.

Plan both orders at least 6 weeks before install day. For the rest of the purple theme, see [`21-Purple-Cosmetics/overview.md`](../21-Purple-Cosmetics/overview.md).

---

## See Also

- [`overview.md`](overview.md) — parts decision rationale, including the full purple cooling section (source of truth)
- [`../05-Timing-Chain-Maintenance/`](../05-Timing-Chain-Maintenance/) — water pump labor bundles here; do not replace water pump standalone
- [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) — must happen AFTER this phase (heat dependency)
- [`../19-Flex-Fuel-and-Fuel-System/`](../19-Flex-Fuel-and-Fuel-System/) — E85 tune must happen AFTER this phase (heat dependency)
- [`../21-Purple-Cosmetics/overview.md`](../21-Purple-Cosmetics/overview.md) — Samco + Radium + rad cap powder-coat under the broader purple theme
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — thermostat housing (9 ft-lb), water pump (9 ft-lb), coolant bleed screw (hand tight)
- [`../docs/fluids-and-intervals.md`](../docs/fluids-and-intervals.md) — coolant spec and replacement interval

---

*Last updated: 2026-04-20*
