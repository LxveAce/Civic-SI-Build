# Intake — K&N Typhoon (Short Ram)

## Status: Installed

## Part Information

| Field | Value |
|-------|-------|
| Part | K&N Typhoon Short Ram Intake |
| Part Number | 69-1014TS |
| Fitment | Honda Civic SI 2.0L (2006-2011) |
| Filter Type | K&N high-flow cotton gauze |
| Finish | Polished aluminum intake tube |
| **Actual Cost (incl. tax/shipping)** | **$504.17** |

**Note:** K&N markets this as a "Cold Air Intake," but it is technically a **short ram intake** — the filter mounts in the engine bay (hot side) near the exhaust manifold, not in a cold air location behind the bumper/fender. It uses the stock fresh air duct to feed cooler outside air to the filter area.

## Why This Mod

The K&N Typhoon replaces the stock airbox with a high-flow intake tube and cone filter. On the K20Z3, the stock airbox is reasonably well-designed, but the Typhoon provides:
- Slightly improved airflow at high RPM
- More aggressive intake sound (the K20 sounds great with an open intake)
- A modest 3-8 HP gain (varies by dyno and conditions)
- Better throttle response feel

## Installation Notes

- **Placement:** Hot side of the engine bay. The filter sits near the exhaust manifold side, which means it's exposed to engine heat.
- **Heat Shield:** The kit includes a partial heat shield, but it doesn't fully isolate the filter from engine bay temps.
- **Fresh Air Duct:** The stock fresh air duct (routes air from behind the bumper/fender toward the filter area) is retained and utilized. This helps feed cooler outside air to the filter despite the hot-side placement.
- **Intake Air Temps:** Real-world IATs will be higher than a true cold-side setup. The fresh air duct mitigates this, but on hot days or in traffic, IATs will climb. Monitor IAT via Hondata datalogging.

## Tuning Impact

**This is the only installed mod that affects the ECU tune.**

The changed airflow characteristics (different tube diameter, less restriction, different sensor placement) mean the stock ECU calibration is not perfectly matched. The car will run fine on the stock tune (closed-loop O2 correction handles the difference), but a Hondata base map calibrated for an intake will:
- Correct fuel tables for the intake's airflow characteristics
- Optimize timing for the slightly different charge characteristics
- Potentially adjust VTEC engagement for the modified intake flow

A base map for "stock + intake" on the 8th gen SI is available from Hondata's downloads.
