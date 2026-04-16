# Intake Manifold & Throttle Body — Skunk2 Ultra Street + Bored Stock TB

## Status: Planned (Not Yet Purchased)

## What I'm Going With

**Skunk2 Ultra Street Intake Manifold (307-05-0600)** paired with a **bored stock K20Z3 DBW throttle body (66mm).**

## Why I Chose the Ultra Street

The stock RRC manifold (on my 06-11 SI) has long runners designed for low-end torque and fuel economy. Once I add headers, exhaust, and a tune, the RRC becomes the airflow bottleneck. The Ultra Street shortens the runners, enlarges the plenum, and moves the powerband upward — exactly what I need for a full bolt-on NA K20Z3 targeting 220-240 WHP.

| Spec | Stock RRC | Skunk2 Ultra Street |
|------|-----------|---------------------|
| Runner Length | ~12.5" | ~8.5-9" |
| Plenum Volume | ~2.5L | ~1.8L (expandable with spacers) |
| Runner Diameter | ~45mm | ~55mm |
| Throttle Body Bore | 62mm (stock DBW) | 71mm throttle body opening |
| Power Focus | Low-mid (2500-5500 RPM) | Broad pull from ~4000-8000+ RPM |
| Idle Quality | OEM smooth | Slightly rougher (tunable with Hondata) |

### Skunk2 Manifold Lineup — Why Ultra Street Is the Sweet Spot

| | Pro Series | **Ultra Street** | Ultra Race |
|---|-----------|-----------------|------------|
| Runner Length | ~10-11" | **~8.5-9"** | ~5-6" |
| Plenum Volume | ~3.0L | **~1.8L** | ~3.5L+ |
| Power Focus | Mid-range | **Street/sport balance** | Top-end only (7000-9000 RPM) |
| Idle Quality | Good | **Acceptable** | Poor |
| Best For | Daily + light mods | **Full bolt-on street build** | Track / built motor |

**The Ultra Street is the right one for my build.** The Pro Series leaves performance on the table — not aggressive enough for what I'm doing. The Ultra Race kills low-end torque and idle quality for a street car. I'm not building a track car, so the Ultra Street hits the sweet spot.

## Part Information

| Field | Value |
|-------|-------|
| Intake Manifold | Skunk2 Ultra Street |
| Part Number | 307-05-0600 (black) / 307-05-0605 (silver) |
| Port Pattern | PRB/PRC (direct fit to K20Z3 head) |
| Material | Cast aluminum, black powder coat |
| Price | ~$550-620 |

## Throttle Body — CRITICAL: DBW Compatibility

### The Problem

My K20Z3 uses **drive-by-wire (DBW)** — an electronically controlled throttle body with an internal motor and position sensors. **Most aftermarket K-series throttle bodies are cable-throttle only and WILL NOT work.** I learned this early and I'm glad I did, because it would be an expensive mistake.

| Throttle Body | DBW Compatible? | Notes |
|---------------|-----------------|-------|
| Stock K20Z3 62mm | Yes (OEM) | Baseline — restricts Ultra Street's potential |
| **Bored stock 64-66mm** | **Yes** | **Best option — retains full DBW, proven** |
| Skunk2 Pro Series 68mm | NO (cable only) | Would require full DBW-to-cable conversion |
| Blox 68mm DBW | Possibly | Must verify exact part is DBW-specific |
| Ktuned 72mm | NO (cable only) | Cable only |
| Hybrid Racing | NO (cable only) | Adapter-based, cable conversion needed |

### My Choice: Bored Stock Throttle Body (66mm)

Several Honda specialist shops (Drag Cartel, HeelToe Auto, and others) will bore the stock K20Z3 DBW throttle body from 62mm to **64-66mm**.

- **66mm is the maximum safe bore** — the housing walls get too thin beyond that
- Retains full DBW function — no wiring changes, no adapter hassles
- Proven reliability, used by hundreds of K20Z3 builds
- **Cost:** ~$100-175 (boring service, I ship my TB)
- **The stock 62mm TB isn't a major restriction** at the 220-240 WHP level, but a bored TB eliminates it as any bottleneck and lets the Ultra Street breathe freely

Honestly this is the move. No headaches, no wiring nightmares, just a slightly bigger hole in a part I already have.

### Does a Larger TB Actually Help?

| Power Level | Stock 62mm | Bored 66mm | 68mm+ |
|-------------|-----------|------------|-------|
| Stock-220 WHP | Fine, not a restriction | Marginal gain (1-3 WHP) | Unnecessary |
| 220-240 WHP | Mild restriction up top | Measurable gain (3-7 WHP) | Diminishing returns |
| 240+ WHP | Noticeable restriction | Good | Needed |

**For my build (targeting 220-240 WHP): the bored 66mm is the sweet spot.** Going larger than 68mm on an NA K20Z3 loses throttle response at low RPM for minimal gain. Not worth it.

## Power Gains (With Supporting Mods + Tune)

- **Ultra Street alone (no tune):** 3-7 WHP, may lose low-end torque. I'm not running it without a tune.
- **Ultra Street + 66mm TB + full bolt-ons + Hondata tune:** **15-22 WHP over stock manifold** on a similarly-modded car
- **Peak power shifts** from ~6800-7200 RPM (stock) to ~7400-7800 RPM with the Ultra Street

## Installation Notes

- **Difficulty:** Moderate. 3-5 hours first time.
- **Vacuum lines:** I need to take photos of ALL vacuum line routing before removal. Label everything. The Ultra Street has provisions but routing differs from stock RRC.
- **Coolant bypass:** The stock RRC has a coolant passage (throttle body heater). Block off the ports on the engine side and run a short bypass hose between them. Takes 5 minutes.
- **MAP sensor:** Relocates to the Ultra Street plenum. Stock sensor works, just moves.
- **IACV:** Ultra Street retains IACV provision — important for idle on a street car.
- **Fuel rail:** I need to confirm the Ultra Street is compatible with the stock K20Z3 fuel rail, or check if Skunk2 includes one.
- **Fuel injectors:** Stock 310cc injectors are adequate to ~230 WHP. No upgrade needed.
- **No permanent modifications** to my car are required. Fully reversible.

## Tuning — MANDATORY

**The intake manifold swap and Hondata tune are inseparable. I will NOT drive aggressively on the stock calibration.**

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

I looked at the OEM RBC manifold (from 02-06 RSX Type S) as a budget option. It's the most popular budget intake manifold for the K20Z3 — 70-80% of the Ultra Street's gains at 30-40% of the cost. I seriously considered it.

| Factor | RBC (Used) | Skunk2 Ultra Street |
|--------|-----------|---------------------|
| Price | $100-250 | $550-620 |
| Power Gain (w/ tune) | 10-18 WHP | 15-22 WHP |
| DBW Compatibility | Needs $60-100 adapter plate | Designed for aftermarket TB |
| Community Support | Massive (thousands of builds) | Large |

Ultimately I decided the Ultra Street is worth the extra money for the cleaner install and slightly better gains. But the RBC is a genuinely great option for anyone on a tighter budget.

## Where I'm Buying

| # | Item | Product | Price | Link |
|---|------|---------|-------|------|
| 1 | **Intake Manifold** | Skunk2 Ultra Street 307-05-0600 | ~$565-620 | [Hybrid Racing](https://www.hybrid-racing.com/products/skunk2-k20a2-ultra-street-intake-manifold) |
| | | | | [TF-Works — $565](https://tf-works.com/skunk2-ultra-street-intake-manifold-k20-k24/) |
| | | | | [JHPUSA](https://jhpusa.com/products/skunk2-ultra-series-street-intake-manifold-k-series) |
| | | | | [Headgames Motorworks](https://headgamesmotorworks.com/products/skunk2-ultra-series-street-k20a-a2-a3-k24-engines-intake-manifold-black) |
| 2 | **TB Boring Service** | Stock K20Z3 DBW TB bored to 66mm | ~$100-175 | Contact [Drag Cartel](https://dragcartel.com) or [HeelToe Auto](https://www.heeltoeauto.com) — send my stock TB |
| 3 | **TB adapter plate** | If needed for 66mm on 68mm inlet | ~$30-50 | Sourced with manifold purchase |
| 4 | **Dyno tune** | Mandatory after install | ~$400-600 | Local K-series Hondata tuner |
| | **Total** | | **~$1,095-1,445** | |

TF-Works at $565 looks like the best price I've found for the manifold.

**Note on part number:** The Ultra **Street** is 307-05-0600 (black) or 307-05-0605 (silver). The Ultra **Race** is 307-05-8000. These are different manifolds — the Ultra Street has longer runners and is the correct one for my build.

---

*Last updated: 2026-04-16*
