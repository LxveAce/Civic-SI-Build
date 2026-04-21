# 2009 Honda Civic SI Coupe — My Build Log

**Chassis:** FG2 (8th Gen Coupe)  
**Engine:** K20Z3 — 2.0L i-VTEC, 197 HP / 139 lb-ft (stock)  
**Transmission:** 6-Speed Manual  
**Color:** Blue  
**Mileage:** ~170,000 miles  

---

## What I'm Going For

Daily-drivable with a sport mode toggle. Quiet when I need it, loud when I want it. I'm building a full bolt-on NA K20Z3 targeting **220-240 WHP on pump gas, 230-250 WHP on E85** — headers, intake manifold, throttle body, exhaust, pulleys, flex fuel, and a Hondata tune to tie it all together. I'm doing a valved 3" exhaust with a QTP cutout so I can switch between a quiet daily tune and an aggressive straight-piped sport tune. Flex fuel with real-time ethanol content sensing lets me run pump gas or E85 seamlessly. And eventually, I'm putting a LattePanda mini PC in the car for permanent Hondata management and exhaust valve control.

**The rule that overrides everything:** engine longevity comes before power. Every tune ships as two calibrations (Daily + Sport), and Sport means "squeeze the engine for everything it's got WITHIN the reliability envelope" — not "push it to the edge." See [10-Hondata-FlashPro/tuning-workflow-and-maps.md](10-Hondata-FlashPro/tuning-workflow-and-maps.md) for the tuning rules I'll live by.

---

## Modification Status

### Installed

| # | Mod | Part | Actual Cost | Status |
|---|-----|------|------------|--------|
| 1 | [Clutch & Flywheel](03-Clutch-and-Flywheel/) | Exedy Stage 1 Organic (08806) + Exedy Lightweight Flywheel (HF02) | $960.43* | Installed |
| 2 | [Cold Air Intake](01-Cold-Air-Intake/) | K&N Typhoon 69-1014TS | $504.17 | Installed |
| 3 | [Short Shifter + Bushings](02-Short-Shifter-and-Bushings/) | Acuity 3-Way Adjustable + Trans-Side Bushings | $622.20 | Installed |
| 4 | Tires | Continental ExtremeContact DWS06 Plus 215/45ZR17 91W XL | $715.00 | Installed |

*\*$960.43 includes clutch, flywheel, and strut bar bundled together (incl. tax/shipping)*

### Purchased — Awaiting Install

| # | Mod | Part | Actual Cost | Status | Notes |
|---|-----|------|------------|--------|-------|
| 5 | [Engine Mounts](08-Engine-Mounts/) | Hybrid Racing 70A | $657.15 | Awaiting install | |
| 6 | [Brakes](04-Brakes/) | Hawk HPS Pads + R1 Concepts Slotted Rotors | $532.14 | **Front installed 2026-04-20** — rear pending | Full 4-corner upgrade |
| 7 | [Strut Bar](18-Strut-Bar/) | Megan Racing Race Spec Front Upper (Polished) | (in #1) | **Deferred until coilovers** — BC Racing camber plates will change strut-top geometry anyway |
| 8 | [Hondata FlashPro](10-Hondata-FlashPro/) | Hondata FlashPro | $859.59 | Awaiting first flash | ECU tuning, datalogging, gauges |

**Total spent to date: $4,850.68** (all prices include tax, shipping, and insurance)

### Planned — Not Yet Purchased

| # | Mod | Details | Notes |
|---|-----|---------|-------|
| 8 | [Valved Exhaust](12-Valved-Exhaust/) | DIY 3" QTP cutout bypass (keep OEM mufflers) | 3" dump, step-down to 2.5" for muffled path |
| 9 | [Headers](13-Headers/) | Skunk2 Alpha 4-2-1 (412-05-1930) + Berk HFC | Best available, stepped primaries, 10-18 WHP |
| 10 | [Intake Manifold](14-Intake-Manifold/) | Skunk2 Ultra Street + bored stock TB (66mm) | Larger plenum, shorter runners, DBW compatible |
| 11 | [Pulleys & Harmonic Balancer](15-Pulleys-and-Harmonic-Balancer/) | ATI Super Damper + NST accessory pulleys | Proper damping + reduced parasitic loss |
| 12 | [Flex Fuel & Fuel System](19-Flex-Fuel-and-Fuel-System/) | Flex fuel sensor + Bosch EV14 550cc injectors + Acuity rail + DW300C pump | E85 capable, 5-15 WHP on NA over pump gas |
| 13 | [Clutch Hydraulics](07-Clutch-Hydraulics/) | Hybrid Racing HYB-CMC-01-20 complete kit + rear main seal + throwout bearing | 170k-mile reliability upgrade + "free labor while trans is out" bonus items |
| 14 | [Suspension](17-Suspension/) | BC Racing BR coilovers + full bushing refresh + sway bars + camber kit | Complete suspension overhaul — coilovers, bushings, geometry correction |
| **15** | **[Ignition Refresh](06-Ignition-Refresh/)** | **NGK plugs + OEM Honda coils (30520-RWC-A01) + VTC actuator (14310-RBC-003 updated part)** | **New.** Critical before any tune. Fixes cold-start rattle. |
| **16** | **[Cooling System](09-Cooling-System/)** | **Koyorad HH060063 aluminum radiator + OEM thermostat + hoses + water pump** | **New.** Plastic end tank failure insurance + headroom for E85 heat. Must precede headers. |
| **17** | **[Wideband AFR](11-Wideband-AFR/)** | **AEM X-Series 30-0300 wideband UEGO** | **New.** Required before any dyno tune. Integrates with FlashPro analog input. |
| **18** | **[Timing Chain Maintenance](05-Timing-Chain-Maintenance/)** | **Honda OEM chain 14401-PNA-004 + tensioner 14510-PRB-A01 + guides + VTC actuator (bundled with Ignition Refresh)** | **New.** Phase 0 maintenance at 170k. Decision rule: 13.5mm tensioner rod = go/no-go. |
| **19** | **[Cylinder Head (Drop-In)](16-Cylinder-Head/)** | **4 Piston Pro 156v2 All Motor Package + ARP 208-4701 studs + Cometic C4561-030 + Skunk2 Tuner Stage 2 cams + Skunk2 Pro cam gears** | **New.** "Go all out" decision. ~$4,130 parts + tune. Bundle with headers, IM, pulleys, VTC install. |
| **20** | **[Built Motor Bottom End](20-Built-Motor-Bottom-End/)** | **Future phase appendix — Wiseco + BC625+ + ACL Race + PRB-A01 pump** | **New.** Not current purchase. Reference for future 400–500 WHP E85 or ultra-high-RPM NA. |
| **21** | **[Purple Cosmetics](21-Purple-Cosmetics/)** | **Acuity 1927-PPL oil cap + K-Tuned DP2-K20-PRP dipstick + Acuity ESCO-T6 knob + Dress Up Bolts HON-027-TI + NST22015K-Purple alt/idler + Samco purple hoses + powder-coat batch** | **New.** Aesthetic layer. Tier-1 package ~$966; full purple theme ~$1,836. |
| -- | [In-Car PC](10-Hondata-FlashPro/Permanent-LattePanda-Install/) | LattePanda 3 Delta permanent install | Controls FlashPro + exhaust valve |

---

## How This Repo Is Organized

Each mod has its own folder with some subset of:
- **overview.md** — What the mod is, why I chose it, part numbers, status
- **install-guide.md** — Step-by-step install instructions
- **brainstorm.md** — Research, alternatives I considered, pros/cons, things I ruled out
- **purchasing.md** — Parts list with part numbers and prices

Simple bolt-ons might only have an overview. Complex mods (valved exhaust, LattePanda, headers) have all four.

### Special Folders
- [`10-Hondata-FlashPro/Temporary-Setup/`](10-Hondata-FlashPro/Temporary-Setup/) — Getting started with a laptop before the permanent install
- [`10-Hondata-FlashPro/Permanent-LattePanda-Install/`](10-Hondata-FlashPro/Permanent-LattePanda-Install/) — Full guide for the in-car PC build
- [`10-Hondata-FlashPro/tuning-workflow-and-maps.md`](10-Hondata-FlashPro/tuning-workflow-and-maps.md) — Daily/Sport map rules, reliability-first ceilings, and how I work with Claude on tune changes
- [`12-Valved-Exhaust/`](12-Valved-Exhaust/) — My DIY valved exhaust design, parts, and planning
- [`docs/`](docs/) — Cross-cutting reference documents

### Docs

- [`docs/mod-order-and-maintenance.md`](docs/mod-order-and-maintenance.md) — Chronological mod order + 170k-mile maintenance plan
- [`docs/vehicle-specs.md`](docs/vehicle-specs.md) — Stock specs for the FG2
- [`docs/install-references.md`](docs/install-references.md) — Guides, videos, and community threads I've collected
- [`docs/torque-specs.md`](docs/torque-specs.md) — **New.** K20Z3 / FG2 torque reference for every fastener I'll touch
- [`docs/maintenance-parts-catalog.md`](docs/maintenance-parts-catalog.md) — **New.** OE + aftermarket part numbers in one place
- [`docs/baseline-logs.md`](docs/baseline-logs.md) — **New.** A/B datalog protocol for every mod

---

## Quick Reference

| Spec | Value |
|------|-------|
| Engine Code | K20Z3 |
| ECU Code | PRB (37820-RRB-A58 or similar) |
| Displacement | 1998cc (2.0L) |
| Compression | 11.0:1 |
| Stock HP / TQ | 197 HP @ 7800 RPM / 139 lb-ft @ 6200 RPM |
| Redline | 8000 RPM (fuel cut at 8200 RPM) |
| Stock Exhaust Diameter | 2.36" (60mm) from cat back |
| Fuel | Premium 91+ octane required |
| OBD2 Port | Under dash, left of steering column |
| Interior Fuse Box | Driver side lower dash, behind removable panel |
| Fuse Type (Interior) | Mini blade |

---

## Build Principles I'm Living By

1. **Reliability over power, always.** At 170k I'd rather leave 10 WHP on the table than risk a bearing.
2. **Every tune = Daily + Sport maps.** Quiet daily mode, aggressive-but-safe sport mode.
3. **Cross-reference every decision.** If Mod X changes the situation for Mod Y, the Y doc says so explicitly.
4. **Phase 0 maintenance comes first.** A sick engine can't be tuned well no matter what parts go on.
5. **No lean WOT fuel, ever, on any tune.** Pump gas = 12.0 AFR minimum; E85 = lambda 0.82 minimum.
6. **Dyno verification for every timing change.** No armchair advances.

---

## Contributing / AI Assistant Reference

See [CLAUDE.md](CLAUDE.md) for the AI assistant reference file containing full context about this build, conventions, and instructions for AI tools assisting with this project.

---

*Last updated: 2026-04-20*
