# Built Motor Bottom End — Future Phase

## Status: Aspirational / Future Planning Only

## What This Is (and Isn't)

This folder is **not a current purchase plan**. Nothing on this list is being bought at 170k miles with a 220-250 WHP target. The stock K20Z3 block + rods + crank + cast pistons live forever at that power level with a proper tune.

**This is the reference for when I cross these thresholds:**
- Power target passes ~270 WHP (stock hypereutectic piston ring lands become the risk)
- I decide to go forced induction (turbo K20 on E85, targeting 400–500 WHP)
- Sustained 9000+ RPM NA race use (not street)
- The bottom end finally announces itself after another 30–50k miles and wants rebuilding

At that point, this file is the build sheet. For now: **don't open this folder for purchasing decisions — it's a capability plan, not a shopping list.**

## Why The Stock Block Is Fine At Current Target

Community consensus (8thcivic.org, k20a.org, HondaTech): stock K20Z3 block is safe to approximately:
- **240–270 WHP NA on pump gas** with a proper tune
- **~350 WHP with moderate boost on pump gas**
- **~400 WHP with moderate boost on E85**

Stock-block failure modes (when they happen):
1. **Cast hypereutectic pistons crack ring lands** under detonation (the #1 failure — tune-related, not block-related)
2. **Oil pump cavitation** above ~8500 RPM sustained (fixable by upgrading pump, block still fine)
3. **Piston ring gap closure** under sustained boost (ring pack issue, not block)
4. **Rod bolt stretch** under sustained boost >15 psi (rod failure, not block)
5. **Crank flex** above 9000 RPM sustained race use (niche, not street-relevant)

**At 220-250 WHP NA, not one of those failure modes is on my radar.** The mods that actually protect the stock block at this power level are already planned:
- Hondata FlashPro tune — prevents detonation (the #1 piston-killer)
- ATI Super Damper — torsional vibration control
- Cooling system refresh — thermal stability
- Wideband AFR — data to verify safe AFR under load

When this folder becomes real, it's because my goals changed.

---

## Target State (If I Go Here Someday)

A bottom end that can reliably handle approximately:
- **400–500 WHP with turbo on E85** (if I ever go forced induction)
- **Sustained 9000+ RPM NA** (if I go race NA)
- **"Forever" reliability** at current or slightly higher NA power levels

Non-negotiable rule (still): reliability over power, always.

---

## Recommended Build Sheet

This is the "if it were done today" recipe, based on current (2025-2026) market research. Prices subject to change.

### Pistons — Wiseco K573M86AP 86mm 11.6:1 ArmorGlide

| Spec | Value |
|------|-------|
| Part # | **K573M86AP** |
| Price | ~$760 |
| Bore | 86mm stock |
| Compression | 11.6:1 |
| Material | Forged 2618 aluminum |
| Coating | ArmorGlide skirt (street durability) |
| Ring pack | Wiseco standard |
| Valve reliefs | Flat-top with reliefs |

Why this compression ratio: 11.6:1 runs well on pump 93 NA (slight improvement over 11.0:1 stock). If I turbo later on E85, 11.6:1 is manageable with conservative timing (community runs K20 turbos at 10-12 psi, 350-400 WHP on 11-12:1 E85). If I go big boost (15+ psi, 500+ WHP), I'd swap to 9.6:1 pistons then — but spending money NOW on low-comp pistons I may never use is poor planning.

Alternatives considered:
- CP-Carrillo SC7145 87mm 10.1:1 (~$885) — future-proof for turbo but soft NA feel; also requires block overbore
- JE FSR 309411 86mm 10.0:1 (~$700) — turbo-focused, fine alternative to Wiseco
- Manley Platinum 610100-4 11.5:1 (~$640) — cheaper than Wiseco, quality comparable

### Rods — Brian Crower BC6044 ProH625+ H-Beam

| Spec | Value |
|------|-------|
| Part # | **BC6044** |
| Price | ~$934 |
| Material | 4340 forged H-beam |
| Bolts | ARP Custom Age 625+ (280,000 PSI tensile) |
| Rated | ~900 HP |
| C-to-C | 139.00mm (correct K20Z3 stock length) |
| Pin | 22mm (matches stock) |
| Weight | ~514g |

Why this rod:
- 600+ HP safe — massive headroom above 500 WHP target
- ARP 625+ bolts handle E85 peak cylinder pressures (cylinders pressures, not beams, are usually what fails)
- Overwhelming K-series community track record at 500+ WHP
- Saving ~$560 vs K1 Technologies H-beam ($372) isn't worth it — the bolt upgrade is cheap insurance

**Budget alternative:** K1 Technologies 015BW17139L ARP 2000 H-beam at ~$372. Still safe to ~600 WHP crank. Use if budget is the constraint.

### Rod Bearings — ACL Race 4B1946H-STD

| Spec | Value |
|------|-------|
| Part # | **ACL 4B1946H-STD** |
| Price | ~$90 |
| Series | Race Tri-metal (hard alloy) |
| Clearance | Standard (shoot for ~0.0018–0.0022" target) |

Why: proven to 500+ WHP, standard clearance appropriate for reused crank. **King XPG** (~$150) is the "one step up" option with graphite coating — worth it if budget allows but not necessary.

### Main Bearings — ACL Race 5M1959H-STD

| Spec | Value |
|------|-------|
| Part # | **ACL 5M1959H-STD** |
| Price | ~$140 |
| Target clearance | 0.0015–0.0018" |

### ARP Head Studs — 208-4701

| Spec | Value |
|------|-------|
| Part # | **ARP 208-4701** |
| Price | ~$185–210 |
| Material | 8740 chrome-moly, 190,000 PSI |

Same as the cylinder head phase (see [`../16-Cylinder-Head/overview.md`](../16-Cylinder-Head/overview.md)).

**Note on main studs:** K20 main caps are well-engineered. Main studs are NOT required at 500 WHP — skip. Honda OEM main bolts (TTY, one-time-use) are fine.

### Oil Pump — Honda PRB-A01 (RSX Type S)

| Spec | Value |
|------|-------|
| Part # | **Honda 15100-PRB-A01** |
| Price | ~$250–350 |

Why this part:
- Drop-in OEM Honda quality (no aftermarket-knockoff risk)
- Good to 9500 RPM — covers future NA high-rev ambitions and all boost scenarios
- The K-series community's "cheap insurance" for high-RPM use — prevents the classic cavitation-induced bearing death at 8500+ RPM

Skip: Melling high-volume (not K20-specific), Boundary (limited K20 offering), aftermarket knockoffs. 4Piston ported RSX Type S pump ($450-550) is the "better" choice but overkill below 600 WHP.

### Crank — Reuse Stock K20Z3, Prep & Balance

Honda-forged steel crank from the factory. Excellent to 600+ crank HP and 9500 RPM.

Required prep work:
- Magnaflux inspection (mandatory on 170k crank)
- Micropolish journals to standard
- Journal chamfering (teardrop oil holes)
- Full rotating-assembly balance with new pistons/rods/damper: ~$300-500

**Total crank prep: ~$400-700 including balance.**

Don't buy an Eagle/K1 forged billet crank unless targeting 700+ WHP — stock is better for this use.

### Harmonic Damper — ATI 918477 Super Damper

**Already owned / planned** from Phase 15 (Pulleys & Harmonic Balancer). Same part carries over to built motor unchanged. Internally-balanced K20 is compatible with the street 918477 or race 918478.

*Note: P/N 917270 sometimes referenced in online discussions is actually a GM LT1/LT4 damper — not K20. Use **918477**.*

### Head Gasket — Cometic C4561-030 .030" MLS

| Spec | Value |
|------|-------|
| Part # | **Cometic C4561-030** |
| Price | ~$120 |
| Thickness | .030" |
| Bore | 86mm |

.030" thickness matches stock deck height on a stock-bore 11.6:1 CR calc. If block is decked during machine work, step up to C4561-036 (.036") to restore deck clearance.

### Misc Consumables

- Timing chain + tensioner + guides (if not done earlier): ~$170
- Water pump (OEM 19200-RBC-013): ~$90
- Valve cover gasket kit: ~$40
- All other cam seals, coolant, oil, Hondabond, Moly 60, assembly lube: ~$200

---

## Machine Shop Menu

Standard prep for a 170k block going back together:

| Service | Cost |
|---------|------|
| Hot tank / ultrasonic clean | $75–150 |
| Magnaflux block (crack check) | $75–150 |
| Pressure test block (coolant passages) | $75–150 |
| Deck resurface | $100–200 |
| Bore + hone to 86mm piston spec (plateau finish) | $200–400 |
| Line hone mains | $150–250 |
| Crank polish + chamfer oil holes | $125–250 |
| Balance full rotating assembly (crank + rods + pistons + damper) | $300–500 |
| **Total machine work** | **~$1,100–2,000** |

Plan on ~$1,200 for a competent shop doing the full menu.

### Sleeving — Only If I Go This Route

**Not needed for 500 WHP on stock iron liners.** Stock K20Z3 block is safe to that level with iron liners intact. Sleeves become necessary only at:
- Sustained 500+ WHP on boost
- Bore size >89mm (overbore builds)
- Already-cracked stock block

If I ever need sleeves:
- **Darton MID (P/N 400-190-P)** for 86mm–90mm bore range — $800 parts + $800-1200 install
- **Golden Eagle** — similar pricing, lifetime warranty on sleeves

---

## Assembly — DIY vs Shop

### DIY (if I've done an engine build before)

**Required tools beyond current kit:**
- Plastigauge (multiple clearance ranges)
- Feeler gauges 0.001–0.015"
- Dial bore gauge (ideal — rental or buy)
- Tapered ring compressor (86mm)
- Piston ring filing tool (or buy pre-gapped rings)
- Clean assembly lube
- ARP Ultra-Torque lube (for stud torques)
- Torque wrench accurate to 100 ft-lb
- Torque angle gauge

**Savings: ~$800-1,200 labor. Risk: one mistake = spun bearing / crushed ring / scored bore / ruined build.**

### Shop Assembly (recommended for first built K20)

Reputable K-series builders:
- **4 Piston Racing** (Indianapolis) — industry leader, $1,000-1,500 assembly
- **King Motorsports** (Wisconsin) — K-specialist, premium
- **Drag Cartel** — race-focused
- **Portflow Design** (Harbor City CA) — head+short block
- **Bisimoto** — premium, long lead times
- **Pro Import Tuners**, **1to1 Tuning** — mid-sized builders

Typical: $1,000–1,500 short block assembly labor, 4–8 week lead time.

### Turn-Key Short Blocks (skip parts sourcing entirely)

| Builder | Product | Approx Price |
|---------|---------|--------------|
| 4Piston | K-Series Street Short Block (K20) | $4,500–5,500 |
| Drag Cartel | DC N/A K20 Street | $4,800–5,500 |
| Drag Cartel | DC Turbo K20 Street | $5,200–6,000 |
| Golden Eagle | Sleeved K20A Stage 2 | $5,500–6,500 |
| SpeedFactory | OEM K20A built 900HP-capable | $6,500–7,500 |

Customer supplies core. Shipping core one-way ~$150–250.

---

## Total Cost Estimate

### Mid-Range DIY Build (my likely target when the time comes)

| Item | Cost |
|------|------|
| Wiseco K573M86AP pistons | $760 |
| Brian Crower BC6044 ProH625+ rods | $934 |
| ACL Race rod + main bearings | $230 |
| ARP head studs 208-4701 | $200 |
| Honda PRB-A01 oil pump | $300 |
| Cometic C4561-030 head gasket | $120 |
| Timing chain set + water pump + misc | $400 |
| ATI Super Damper | $0 *(already owned)* |
| Crank prep (inspect/polish/balance) | $500 |
| **Parts subtotal** | **~$3,444** |
| Machine work (full menu) | $1,000-1,500 |
| DIY assembly | $0 |
| **TOTAL DIY** | **~$4,444–4,944** |

### Mid-Range Shop Build

Same parts + shop assembly $1,000–1,500.
**Total: ~$5,444–6,444**

### Turn-Key 4Piston K-Series Street Short Block

~$4,500–5,500 (my core supplied).

### High-End Build (if going boost past 500 WHP)

| Upgrade | Cost Delta |
|---------|-----------|
| CP-Carrillo SC7145 87mm + Tec-Coat | +$300 |
| Carrillo CARR rods | +$400 |
| King XPG bearings | +$120 |
| ARP 625+ head studs | +$250 |
| ARP main studs | +$175 |
| Darton sleeves + install | +$1,800 |
| 4Piston ported oil pump | +$200 |
| **High-end total delta** | **+~$3,245** |
| **Grand total high-end** | **~$7,700–9,200** |

---

## Common Mistakes in K-Series Builds

1. **Using cast pistons** — never acceptable. Always forged 2618.
2. **Mixing rod bolts on OEM rods without resize** — ARP bolts have different clamp load than OEM; skipping resize = spun bearing.
3. **Skipping full rotating-assembly balance** — benefit becomes obvious above 7500 RPM.
4. **Wrong bearing clearance** — too tight = seize, too loose = low oil pressure, knock.
5. **Reusing TTY head bolts instead of ARP studs** — always upgrade to ARP studs on built motor.
6. **Skipping block pressure test** — 170k block may have hairline cracks in water jackets that only show under test.
7. **Cheap oil pump or aftermarket knockoff** — stick to genuine Honda PRB-A01 or verified 4Piston ported.
8. **Wrong compression ratio for fuel** — 12:1+ on pump gas = detonation = destroyed pistons. Plan fuel before choosing CR.
9. **Skipping the ATI damper** — stock damper's bonded rubber ring fails on high-RPM use.
10. **No tune or wrong tune after assembly** — the cheapest build dies fastest without proper tuning.

---

## Parts Interactions With Current Build

Everything I'm already planning carries forward to built motor phase:
- **ATI Super Damper** (Phase 15) — same part, no change
- **Hondata FlashPro** (Phase 10) — required for built motor tune, custom tables per build CR
- **Ignition refresh** (Phase 6) — spark energy scales well; revisit plug gap with boost later
- **Wideband AFR** (Phase 11) — critical sensor for tuning built motor
- **Cooling system** (Phase 9) — 500 WHP requires the upgraded cooling
- **Flex fuel** (Phase 19) — required for E85 on built motor

New purchases needed if/when built motor happens:
- Clutch + flywheel re-evaluation — the current Exedy Stage 1 / LW flywheel is rated to ~280-300 WHP / ~200-210 lb-ft. At 500 WHP, needs Stage 2 or Competition Clutch equivalent.
- Injectors upgrade — EV14 550cc (current plan) handles 300 WHP NA E85 max. At 500 WHP on E85, need 1000cc+ (ID1050x or similar).
- Fuel pump upgrade — DW300C (current plan) adequate to 400 WHP. At 500 WHP on E85, DW400 or DW450 required.
- **Turbo kit** (if forced induction route) — entirely separate ~$3,000–6,000 purchase
- **Intercooler + piping** (if boost) — ~$600–1,500

---

## Cross-References

- [`16-Cylinder-Head/overview.md`](../16-Cylinder-Head/overview.md) — head side of the puzzle; drop-in head is phase before this
- [`05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) — chain + VTC done during any major teardown
- [`15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) — ATI damper transfers to built motor
- [`09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) — upgraded cooling is prerequisite for built motor power
- [`19-Flex-Fuel-and-Fuel-System/overview.md`](../19-Flex-Fuel-and-Fuel-System/overview.md) — fuel system needs re-evaluation at built-motor power
- [`docs/torque-specs.md`](../docs/torque-specs.md) — ARP torque sequences, bearing clearances
- [`docs/maintenance-parts-catalog.md`](../docs/maintenance-parts-catalog.md) — add built-motor part numbers when the time comes

---

## Sources

### Pistons
- [Wiseco K20 86mm Professional Series — Summit](https://www.wiseco.com/shop/auto/pistons/professional-honda-k20-piston-86-00-mm-bore-2/)
- [Wiseco K573M86AP 86mm 11.6:1 ArmorGlide — K Series Parts](https://www.kseriesparts.com/WIS-K573M86AP.html)
- [CP SC7145 K20 87mm 10.1:1 — Real Street](https://www.realstreetperformance.com/cp-forged-pistons-set-honda-civic-si-acura-rsx-type-s-k20a2-k20z1-k20z3-87mm-1-0mm-0-2-cc-10-11.html)
- [JE 86mm FSR K-Series 10.0:1 — K Series Parts](https://www.kseriesparts.com/JE-309411.html)
- [Manley 610100-4 K20 86mm 11.5:1 — CNC Motorsports](https://cnc-motorsports.com/catalog/product/view/_ignore_category/1/id/44862/)

### Rods
- [Brian Crower BC6044 K20 625+ — K Series Parts](https://www.kseriesparts.com/BC-BC6044.html)
- [BC K20/K20Z rods line](https://briancrower.com/makes/honda/k20ak20z_rods.shtml)
- [K1 Technologies K20 139mm H-Beam Kit](https://www.k1technologies.com/shop/connecting-rods/connecting-rod-kits/connecting-rod-kits-sport-compact/015bw17139l/)
- [Manley Turbo Tuff 14404-4 K20 — K Series Parts](https://www.kseriesparts.com/MAN-14404-4.html)
- [Eagle K20A2/Z H-Beam CRS5470K3D — K Series Parts](https://www.kseriesparts.com/EGL-5470K3D.html)

### Bearings
- [ACL Race Bearing Set K20 — IPGparts](https://ipgparts.com/products/acl-race-series-bearing-set-main-rod-thrust-for-the-honda-acura-k20a-k20a2-k20z-engines)
- [ACL 5M1959H-STD Mains — K Series Parts](https://www.kseriesparts.com/ACL-5M1959H-STD.html)
- [King XP K-series — King Engine Builders](https://kingenginebuilders.com/king-racing-rod-bearings-honda-k-series-k20-k24-cr4542xp)

### Oil pump
- [4Piston Ported Type S Oil Pump](https://4pistonracing.com/products/4p-kpump)
- [4Piston Ported RRC Type R Oil Pump](https://4pistonracing.com/products/4p-ported-rrc-type-r-oil-pump-k20-k24)

### Other
- [ARP 208-4701 K-Series Head Studs](https://arp-bolts.com/kits/arpkit-detail.php?RecordID=1270)
- [Cometic C4561-030 K20Z3 .030" MLS](https://www.cometic.com/products/C4561-030)
- [ATI K20 Super Damper 918477 — Hybrid Racing](https://www.hybrid-racing.com/products/ati-super-damper-for-k-series-acura-and-honda-engines)
- [Darton MID Sleeves K20 86–90mm](https://www.amazon.com/Darton-400-190-P-Cylinder-Sleeve-86mm-90mm/dp/B0BP8CBQVL)
- [Golden Eagle K20A Sleeved Short Block](https://goldeneaglemfg.com/products/golden-eagle-k20a-sleeved-short-block-stage-2)
- [4Piston K-Series Street Short Block (turn-key)](https://4pistonracing.com/products/kshortblock_street)

### Forum research
- [k20a.org — stock block HP limit thread](https://www.k20a.org/threads/how-much-horsepower-do-you-think-a-stock-k20z3-can-handle.86685/)
- [8thcivic — K20Z3 handling boost](https://www.8thcivic.com/threads/k20z3-handling-boost.5698/)
- [8thcivic — 9000 RPM oil pump cavitation](https://www.8thcivic.com/threads/9000rpms-on-k20z3-oil-pump.308566/)
- [k20a.org — rod bearing clearance](https://www.k20a.org/threads/rod-bearing-clearance-need-help.229913/)
- [k20a.org — compression for turbo pump vs E85](https://k20a.org/forum/showthread.php?t=78780)

---

*Last updated: 2026-04-20*
