# Wideband AFR Gauge — AEM X-Series

## Status: Planned — Install BEFORE first dyno tune, MANDATORY before E85

## Why I Need This

FlashPro datalogs the car's existing narrowband O2 sensor, which is plenty accurate *in the closed-loop cruising range* (~14.0-15.0 AFR). It does NOT give useful data outside that range — which means during WOT, hard transients, flex-fuel blending, or E85 operation, the ECU is essentially guessing and the narrowband reads pegged.

For any real tuning — especially flex fuel — I need a **wideband O2 sensor** that reads 10:1 to 20:1 AFR accurately. This is non-negotiable for E85 work. The tuner needs it, I need it to verify their work, and I want to see real-time numbers on the LattePanda touchscreen eventually.

---

## Part I'm Going With

**AEM X-Series Wideband UEGO Gauge (30-0300)**

| Field | Value |
|-------|-------|
| Part Number | AEM 30-0300 |
| Sensor | Bosch LSU 4.9 |
| Response Time | <1s full range (fastest in class) |
| Display | 52mm (2-1/16") analog + digital |
| Output | 0-5V analog (to FlashPro) + OBD-II serial |
| Accuracy | 0.1 AFR |
| Price | ~$230 |

### Why the AEM X-Series

I compared this to:

| Gauge | Price | Sensor | Notes |
|-------|-------|--------|-------|
| **AEM X-Series 30-0300** | **~$230** | **Bosch LSU 4.9** | **My pick.** Fastest response. Clean mount. Well-integrated with Hondata. |
| Innovate LC-2 | ~$200 | Bosch LSU 4.9 | Older gauge design. Slower digital display. Cheaper bracket quality. |
| Innovate MTX-L Plus | ~$220 | Bosch LSU 4.9 | Good. Slightly uglier display. |
| AEM X-Series OBD-II | ~$290 | N/A (reads OBD-II narrowband) | **Do NOT buy this one for tuning.** It only displays the stock narrowband. |
| PLX Devices SM-AFR | ~$180 | Bosch LSU 4.9 | Budget. Slower response. Fine for monitoring only. |

The AEM X-Series is overwhelmingly the community's pick on 8thcivic and in the Hondata forum for FlashPro users. Not going to overthink it.

---

## Installation — Three Parts

### 1. Bung Welding

I need a 18mm O2 bung welded into the exhaust **upstream** of the catalytic converter. Two common options:

- **In the aftermarket header collector** — best position, fastest response, most accurate. Skunk2 Alpha has a provision for this. This is what I'm doing.
- **In the mid-pipe before the cat** — acceptable if I can't get to the collector.

Post-cat mounting is fine for long-term sensor life (less thermal stress) but less responsive to transient changes. I'll accept the hotter placement for tuning accuracy and just budget for a new sensor every 2-3 years of heavy driving.

### 2. Wiring to FlashPro

The AEM X-Series outputs a 0-5V analog signal that I'll wire to one of the FlashPro's analog inputs. This lets the wideband reading appear directly in the FlashPro datalog alongside RPM, timing, fueling, etc. — which is what the tuner will actually use.

**FlashPro analog input wiring:** Hondata publishes a diagram in their FlashProManager help docs. The 8th gen SI FlashPro has two analog inputs available. Wideband goes on one; future flex fuel sensor goes on the other (or via the rear O2 signal wire — see [12-Flex-Fuel-and-Fuel-System/](../12-Flex-Fuel-and-Fuel-System/)).

### 3. Display Mounting

Where the gauge physically goes:

- **A-pillar pod** — cleanest. Autometer A-pillar pod for 06-11 Civic, fits one gauge. ~$40.
- **Vent pod** — uses the passenger-side dash vent. Doesn't block airflow to me. ~$30.
- **LattePanda display (later)** — once the LattePanda is in, I can log the AEM reading to the touchscreen via the same 0-5V input through an Arduino ADC. The physical gauge becomes redundant. I'll keep it for analog redundancy.

---

## Parts List

| # | Item | Part/Source | Price |
|---|------|-------------|-------|
| 1 | AEM X-Series Wideband | AEM 30-0300 | ~$230 |
| 2 | 18mm O2 bung (stainless) | Universal weld-in | ~$10 |
| 3 | Bung welding | Muffler shop, 15 min job | ~$20-40 |
| 4 | A-pillar gauge pod | Autometer 20400 (black) | ~$40 |
| 5 | 18 AWG wire (power, ground, signal) | ~15 ft each | ~$10 |
| 6 | Inline fuse holder + 5A fuse | | ~$5 |
| | **Total** | | **~$315-335** |

---

## Buy Links

| Item | Source | Link |
|------|--------|------|
| AEM 30-0300 | Summit Racing | [summitracing.com — search AEM 30-0300](https://www.summitracing.com/search?SearchTerm=AEM+30-0300) |
| | Amazon | Search "AEM 30-0300" |
| | Hondata forum / Direct | aem.com |

---

## When To Install

**Must be installed before:**
- First dyno tune (tuner will require it — most won't tune without one)
- Any E85 map work
- Any attempt to run richer/leaner AFR targets manually

**Can be installed alongside:**
- Headers (bung welded into header collector)
- Any exhaust work where the system is off the car

**Replacement interval:** The Bosch LSU 4.9 sensor is rated ~50,000 miles of exposed life. On E85 it can go sooner (ethanol is rough on the sensor). Budget $90 for a replacement sensor every 2-3 years of active use. Gauge itself is a buy-once item.

---

## What This Enables

Once wired into FlashPro's analog input, the tuner can see real-time AFR alongside every other parameter in the datalog. This is what lets me:

- Verify the 93-octane tune is hitting target AFR in both valve-open and valve-closed cutout modes
- Validate the E85 calibration interpolates correctly as the flex fuel sensor reports ethanol content changes
- Catch lean-out conditions under WOT before they cause damage
- A/B compare before/after changes with real data instead of butt dyno

It's the single most important tuning tool on the car after FlashPro itself.

---

## See Also

- [07-Hondata-FlashPro/](../07-Hondata-FlashPro/) — FlashPro setup that this feeds into
- [12-Flex-Fuel-and-Fuel-System/](../12-Flex-Fuel-and-Fuel-System/) — ethanol sensor shares FlashPro analog inputs
- [docs/baseline-logs.md](../docs/baseline-logs.md) — logging plan

---

*Last updated: 2026-04-18*
