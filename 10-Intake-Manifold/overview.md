# Intake Manifold & Throttle Body — Skunk2 Ultra Street + Bored Stock TB

## Status: Planned (Not Yet Purchased)

## Recommendation

**Skunk2 Ultra Street Intake Manifold (307-05-8000)** paired with a **bored stock K20Z3 DBW throttle body (66mm).**

## Why the Ultra Street

The stock RRC manifold (on the 06-11 SI) has long runners designed for low-end torque and fuel economy. It becomes the airflow bottleneck once you add headers, exhaust, and a tune. The Ultra Street shortens the runners, enlarges the plenum, and moves the powerband upward — the right choice for a full bolt-on NA K20Z3 targeting 220-240 WHP.

| Spec | Stock RRC | Skunk2 Ultra Street |
|------|-----------|---------------------|
| Runner Length | ~12.5" | ~8.5-9" |
| Plenum Volume | ~2.5L | ~3.5-4.0L |
| Runner Diameter | ~45mm | ~55mm |
| Throttle Body Bore | 62mm (stock DBW) | 68mm mounting pattern |
| Power Focus | Low-mid (2500-5500 RPM) | Broad pull from ~4000-8000+ RPM |
| Idle Quality | OEM smooth | Slightly rougher (tunable with Hondata) |

### Skunk2 Manifold Lineup

| | Pro Series | **Ultra Street** | Ultra Race |
|---|-----------|-----------------|------------|
| Runner Length | ~10-11" | **~8.5-9"** | ~5-6" |
| Plenum Volume | ~3.0L | **~3.5-4.0L** | ~5.0L+ |
| Power Focus | Mid-range | **Street/sport balance** | Top-end only (7000-9000 RPM) |
| Idle Quality | Good | **Acceptable** | Poor |
| Best For | Daily + light mods | **Full bolt-on street build** | Track / built motor |

**The Ultra Street is the correct choice.** The Pro Series leaves performance on the table. The Ultra Race kills low-end torque and idle quality for a street car.

## Part Information

| Field | Value |
|-------|-------|
| Intake Manifold | Skunk2 Ultra Street |
| Part Number | 307-05-8000 |
| Port Pattern | PRB/PRC (direct fit to K20Z3 head) |
| Material | Cast aluminum, black powder coat |
| Price | ~$550-620 |

## Throttle Body — CRITICAL: DBW Compatibility

### The Problem

The K20Z3 in the FG2 uses **drive-by-wire (DBW)** — an electronically controlled throttle body with an internal motor and position sensors. **Most aftermarket K-series throttle bodies are cable-throttle only and WILL NOT work.**

| Throttle Body | DBW Compatible? | Notes |
|---------------|-----------------|-------|
| Stock K20Z3 62mm | Yes (OEM) | Baseline — restricts Ultra Street's potential |
| **Bored stock 64-66mm** | **Yes** | **Best option — retains full DBW, proven** |
| Skunk2 Pro Series 68mm | NO (cable only) | Requires full DBW-to-cable conversion |
| Blox 68mm DBW | Possibly | Must verify exact part is DBW-specific |
| Ktuned 72mm | NO (cable only) | Cable only |
| Hybrid Racing | NO (cable only) | Adapter-based, cable conversion needed |

### Recommended: Bored Stock Throttle Body (66mm)

Several Honda specialist shops (Drag Cartel, HeelToe Auto, and others) will bore the stock K20Z3 DBW throttle body from 62mm to **64-66mm**.

- **66mm is the maximum safe bore** — the housing walls get too thin beyond that
- Retains full DBW function — no wiring changes, no adapter hassles
- Proven reliability, used by hundreds of K20Z3 builds
- **Cost:** ~$100-175 (boring service, you ship your TB)
- **The stock 62mm TB is not a major restriction** at the 220-240 WHP level, but a bored TB eliminates it as any bottleneck and lets the Ultra Street breathe freely

### Does a Larger TB Actually Help?

| Power Level | Stock 62mm | Bored 66mm | 68mm+ |
|-------------|-----------|------------|-------|
| Stock-220 WHP | Fine, not a restriction | Marginal gain (1-3 WHP) | Unnecessary |
| 220-240 WHP | Mild restriction up top | Measurable gain (3-7 WHP) | Diminishing returns |
| 240+ WHP | Noticeable restriction | Good | Needed |

**For your build (targeting 220-240 WHP): a bored 66mm is the sweet spot.** Larger than 68mm on an NA K20Z3 loses throttle response at low RPM for minimal gain.

## Power Gains (With Supporting Mods + Tune)

- **Ultra Street alone (no tune):** 3-7 WHP, may lose low-end torque. Not recommended without a tune.
- **Ultra Street + 66mm TB + full bolt-ons + Hondata tune:** **15-22 WHP over stock manifold** on a similarly-modded car
- **Peak power shifts** from ~6800-7200 RPM (stock) to ~7400-7800 RPM with the Ultra Street

## Installation Notes

- **Difficulty:** Moderate. 3-5 hours first time.
- **Vacuum lines:** Take photos of ALL vacuum line routing before removal. Label everything. The Ultra Street has provisions but routing differs from stock RRC.
- **Coolant bypass:** The stock RRC has a coolant passage (throttle body heater). Block off the ports on the engine side and run a short bypass hose between them. Takes 5 minutes.
- **MAP sensor:** Relocates to the Ultra Street plenum. Stock sensor works, just moves.
- **IACV:** Ultra Street retains IACV provision — important for idle on a street car.
- **Fuel rail:** Confirm the Ultra Street is compatible with the stock K20Z3 fuel rail, or check if Skunk2 includes one.
- **Fuel injectors:** Stock 310cc injectors are adequate to ~230 WHP. No upgrade needed.
- **No permanent modifications** to the car are required.

## Tuning — MANDATORY

**The intake manifold swap and Hondata tune are inseparable. Do NOT drive aggressively on the stock calibration.**

After installing:
- Load a conservative base map (Hondata community or tuner's starting point)
- Drive gently to the dyno shop
- Key calibration changes:
  - Fuel tables: Full recalibration (4000-8000 RPM range especially)
  - VTEC point: Advance to ~5200-5400 RPM (from stock ~5800)
  - Ignition timing: Can advance in mid/upper RPM with better airflow
  - Idle target: May need slight increase (750 -> 800 RPM) for larger plenum
  - Tip-in enrichment: Adjust to prevent lean stumble from larger plenum volume

## Budget Alternative: RBC Manifold Swap

The OEM RBC manifold (from 02-06 RSX Type S) is the most popular budget intake manifold for the K20Z3. 70-80% of the Ultra Street's gains at 30-40% of the cost.

| Factor | RBC (Used) | Skunk2 Ultra Street |
|--------|-----------|---------------------|
| Price | $100-250 | $550-620 |
| Power Gain (w/ tune) | 10-18 WHP | 15-22 WHP |
| DBW Compatibility | Needs $60-100 adapter plate | Designed for aftermarket TB |
| Community Support | Massive (thousands of builds) | Large |

## Purchasing

| # | Item | Price |
|---|------|-------|
| 1 | Skunk2 Ultra Street 307-05-8000 | ~$575 |
| 2 | Stock TB boring service (to 66mm) | ~$150 |
| 3 | TB adapter plate (if needed for 66mm on 68mm inlet) | ~$30-50 |
| 4 | Dyno tune (mandatory) | ~$400-600 |
| | **Total** | **~$1,155-1,375** |

---

*Last updated: 2026-04-16*
