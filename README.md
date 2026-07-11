<div align="center">

# 2009 Honda Civic SI Coupe — Build Log

### A documentation-first build log for my FG2 K20Z3. Every mod researched, priced, and installed in the open.

![Chassis](https://img.shields.io/badge/Chassis-FG2%20(8th%20Gen)-blue?style=for-the-badge)
![Engine](https://img.shields.io/badge/Engine-K20Z3-red?style=for-the-badge)
![Transmission](https://img.shields.io/badge/Trans-6MT-lightgrey?style=for-the-badge)
![Fuel](https://img.shields.io/badge/Fuel-Flex%20(Pump%20%2F%20E85)-orange?style=for-the-badge)

</div>

---

## The car

| Spec | Value |
|------|-------|
| Chassis | FG2 (8th Gen Coupe) |
| Engine | K20Z3 — 2.0L i-VTEC, 197 HP / 139 lb-ft (stock) |
| Transmission | 6-speed manual |
| Color | Blue |
| Mileage | ~170,000 miles |

Every modification gets its own folder with research notes, part numbers, real prices paid, and install references. It's also a planning tool — a chronological mod order, a 170k-mile maintenance plan, and a small Python script that compiles the whole thing into printable PDFs. Cars are a hobby I picked up in mid-2025, so this repo doubles as my way of learning the platform and keeping myself honest about scope and budget.

---

## What I'm going for

Daily-drivable with a sport mode toggle. Quiet when I need it, loud when I want it. I'm building a full bolt-on NA K20Z3 targeting **220-240 WHP on pump gas, 230-250 WHP on E85** — headers, intake manifold, throttle body, exhaust, pulleys, flex fuel, and a Hondata tune to tie it all together. The exhaust is a DIY valved 3" setup with a QTP cutout, so I can swap between a quiet daily tune and an aggressive straight-piped sport tune. Flex fuel with real-time ethanol sensing lets me run pump gas or E85 without re-tuning. And eventually I'm putting a LattePanda mini PC in the car for permanent Hondata management and exhaust valve control.

---

## Modification status

### Installed

| # | Mod | Part | Actual Cost | Status |
|---|-----|------|------------|--------|
| 1 | [Clutch & Flywheel](01-Clutch/) | Exedy Stage 1 Organic (08806) + Exedy Lightweight Flywheel (HF02) | $960.43* | Installed |
| 2 | [Cold Air Intake](02-Cold-Air-Intake/) | K&N Typhoon 69-1014TS | $504.17 | Installed |
| 3 | [Short Shifter + Bushings](03-Short-Shifter-and-Bushings/) | Acuity 3-Way Adjustable + Trans-Side Bushings | $622.20 | Installed |
| 4 | Tires | Continental ExtremeContact DWS06 Plus 215/45ZR17 91W XL | $715.00 | Installed |

*\*$960.43 includes clutch, flywheel, and strut bar bundled together (incl. tax/shipping)*

### Purchased — awaiting install

| # | Mod | Part | Actual Cost | Status | Notes |
|---|-----|------|------------|--------|-------|
| 5 | [Engine Mounts](04-Engine-Mounts/) | Hybrid Racing 70A | $657.15 | Awaiting install | |
| 6 | [Brakes](05-Brakes/) | Hawk HPS Pads + R1 Concepts Slotted Rotors | $532.14 | Awaiting install | Full 4-corner upgrade |
| 7 | [Strut Bar](06-Strut-Bar/) | Megan Racing Race Spec Front Upper (Polished) | (in #1) | Blocked | Clearance issue — need to diagnose |
| 8 | [Hondata FlashPro](07-Hondata-FlashPro/) | Hondata FlashPro | $859.59 | Awaiting first flash | ECU tuning, datalogging, gauges |

**Total spent to date: $4,850.68** (all prices include tax, shipping, and insurance)

### Planned — not yet purchased

| # | Mod | Details | Notes |
|---|-----|---------|-------|
| 9 | [Valved Exhaust](08-Valved-Exhaust/) | DIY 3" QTP cutout bypass (keep OEM mufflers) | 3" dump, step-down to 2.5" for muffled path |
| 10 | [Headers](09-Headers/) | Skunk2 Alpha 4-2-1 (412-05-1930) + Berk HFC | Best available, stepped primaries, 10-18 WHP |
| 11 | [Intake Manifold](10-Intake-Manifold/) | Skunk2 Ultra Street + bored stock TB (66mm) | Larger plenum, shorter runners, DBW compatible |
| 12 | [Pulleys & Harmonic Balancer](11-Pulleys-and-Harmonic-Balancer/) | ATI Super Damper + NST accessory pulleys | Proper damping + reduced parasitic loss |
| 13 | [Flex Fuel & Fuel System](12-Flex-Fuel-and-Fuel-System/) | Flex fuel sensor + ID725 injectors + Acuity rail + DW300C pump | E85 capable, 5-15 WHP on NA over pump gas |
| 14 | [Clutch Hydraulics](13-Clutch-Hydraulics/) | Hybrid Racing HYB-CMC-01-20 complete kit | 170k-mile reliability upgrade, improved pedal feel |
| 15 | [Suspension](14-Suspension/) | BC Racing BR coilovers + full bushing refresh + sway bars + camber kit | Complete suspension overhaul — coilovers, bushings, geometry correction |
| -- | [In-Car PC](07-Hondata-FlashPro/Permanent-LattePanda-Install/) | LattePanda 3 Delta permanent install | Controls FlashPro + exhaust valve |

---

## How this repo is organized

Each mod has its own folder with:
- **overview.md** — What the mod is, why I chose it, part numbers
- **install-guide.md** — Step-by-step install instructions (where applicable)
- **brainstorm.md** — My research, alternatives I considered, pros/cons
- **purchasing.md** — Parts list with part numbers and prices

### Special folders
- [`07-Hondata-FlashPro/Temporary-Setup/`](07-Hondata-FlashPro/Temporary-Setup/) — Getting started with a laptop before the permanent install
- [`07-Hondata-FlashPro/Permanent-LattePanda-Install/`](07-Hondata-FlashPro/Permanent-LattePanda-Install/) — Full guide for the in-car PC build
- [`08-Valved-Exhaust/`](08-Valved-Exhaust/) — My DIY valved exhaust design, parts, and planning
- [`docs/`](docs/) — General reference documents
- [`docs/vehicle-specs.md`](docs/vehicle-specs.md) — Full stock specification reference
- [`docs/mod-order-and-maintenance.md`](docs/mod-order-and-maintenance.md) — Chronological mod order + 170k-mile maintenance plan
- [`docs/install-references.md`](docs/install-references.md) — Install guides, community links, and search terms for every mod

---

## Documentation PDFs

The whole build log compiles into two printable PDFs so I have everything in one place at the garage:

- **[2009-Civic-SI-Build-Guide.pdf](2009-Civic-SI-Build-Guide.pdf)** — Full build guide: vehicle specs, mod order, every mod overview, and install references, with a title page and table of contents.
- **[2009-Civic-SI-Mod-Order.pdf](2009-Civic-SI-Mod-Order.pdf)** — Standalone chronological mod order + maintenance plan.

Both are generated by [`generate-pdf.py`](generate-pdf.py), a Python script that reads the repo's markdown and renders it — headings, tables with multi-line cell wrapping, bullet/numbered lists, and code blocks — into the two PDFs above. It's the first real coding I've done on this project and it's still rough around the edges. Coding is self-taught for me, so the script is deliberately dependency-light: the only thing you need is fpdf2.

```bash
pip install fpdf2
python generate-pdf.py
```

Re-run it whenever the markdown changes to refresh both PDFs.

---

## Quick reference

| Spec | Value |
|------|-------|
| Engine Code | K20Z3 |
| ECU Code | PRB (Keihin) |
| Displacement | 1998cc (2.0L) |
| Bore x Stroke | 86mm x 86mm |
| Compression | 11.0:1 |
| Stock HP / TQ | 197 HP @ 7800 RPM / 139 lb-ft @ 6200 RPM |
| Redline | 8000 RPM (fuel cut at 8200 RPM) |
| Transmission | 6-speed manual, 4.764:1 final drive, helical LSD |
| Stock Exhaust Diameter | 2.36" (60mm) from cat back |
| Fuel | Premium 91+ octane required |
| OBD2 Port | Under dash, left of steering column |
| Interior Fuse Box | Driver side lower dash, behind removable panel |
| Fuse Type (Interior) | Mini blade |

See [`docs/vehicle-specs.md`](docs/vehicle-specs.md) for the complete stock specification reference.

---

## Connect

- **Discord:** [discord.gg/lxvelabs](https://discord.gg/lxvelabs) — questions, help, or to talk through this project
- **GitHub:** [@LxveAce](https://github.com/LxveAce)
- **Email:** lxveace@proton.me
- **Website:** [lxveace.com](https://lxveace.com)

---

*Personal build log by LxveAce. Not a product — just my car, documented in the open.*
