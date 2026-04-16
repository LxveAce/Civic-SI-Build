---
name: LattePanda 3 Delta Car PC Install Guide
description: Complete purchasing, installation, wiring, and usage guide for permanent LattePanda mini PC in 2009 Honda Civic SI FG2 for Hondata FlashPro
type: reference
originSessionId: 71c04218-155d-453c-936e-a01a76dc2782
---
# LattePanda 3 Delta — Permanent In-Car Hondata PC
## 2009 Honda Civic SI Coupe (FG2 / K20Z3)

### Complete Purchasing, Installation, and Usage Guide

---

## Table of Contents

1. [Bill of Materials](#1-bill-of-materials)
2. [Tools Required](#2-tools-required)
3. [System Overview & Wiring Diagrams](#3-system-overview--wiring-diagrams)
4. [FG2 Fuse Box Reference](#4-fg2-fuse-box-reference)
5. [Pre-Installation: Desk Setup](#5-pre-installation-desk-setup)
6. [Step-by-Step Installation](#6-step-by-step-installation)
7. [Windows Configuration for Car Use](#7-windows-configuration-for-car-use)
8. [Usage Guide](#8-usage-guide)
9. [Future: Exhaust Valve Integration](#9-future-exhaust-valve-integration)
10. [Troubleshooting](#10-troubleshooting)
11. [Maintenance](#11-maintenance)

---

## 1. Bill of Materials

### Core Computer

| # | Item | Specific Product | Qty | Price |
|---|------|-----------------|-----|-------|
| 1 | Mini PC | LattePanda 3 Delta (8GB RAM / 64GB eMMC, Win 11 included) | 1 | $260 |
| 2 | Storage Upgrade | Transcend MTS430S 128GB M.2 2242 SATA SSD | 1 | $20 |
| 3 | MicroSD (backup) | SanDisk 32GB Ultra (for calibration file backups) | 1 | $8 |

### Display

| # | Item | Specific Product | Qty | Price |
|---|------|-----------------|-----|-------|
| 4 | Touchscreen | Eyoyo 7" IPS 1024x600 HDMI Touchscreen (USB touch, HDMI video) | 1 | $60 |
| 5 | HDMI Cable | Micro-HDMI to HDMI cable, 1.5ft | 1 | $8 |
| 6 | Screen Mount | RAM Mounts RAM-B-166-UN7U suction cup mount (or similar universal tablet/screen mount) | 1 | $25 |

### Power System

| # | Item | Specific Product | Qty | Price |
|---|------|-----------------|-----|-------|
| 7 | Car PC Power Supply | Mausberry Circuits 3A Car Supply with Auto Shutdown | 1 | $45 |
| 8 | Add-A-Fuse Tap (constant) | Mini blade add-a-fuse tap (for always-on 12V) | 1 | $4 |
| 9 | Add-A-Fuse Tap (ignition) | Mini blade add-a-fuse tap (for ACC 12V) | 1 | $4 |
| 10 | Mini Blade Fuses | 5A mini blade fuses (for new circuits) | 4 | $3 |
| 11 | Automotive Wire (red) | 16 AWG primary wire, red, 15ft (constant 12V) | 1 | $5 |
| 12 | Automotive Wire (yellow) | 16 AWG primary wire, yellow, 10ft (ignition sense) | 1 | $5 |
| 13 | Automotive Wire (black) | 16 AWG primary wire, black, 10ft (ground) | 1 | $5 |
| 14 | Ring Terminal | 16 AWG ring terminal, #10 stud size (for chassis ground) | 2 | $2 |
| 15 | Inline Fuse Holder | 16 AWG inline mini blade fuse holder x2 | 2 | $6 |
| 16 | Crimp Connectors | Assorted insulated crimp connectors (butt splices, spade terminals, ring terminals) | 1 kit | $8 |

### FlashPro Connection

| # | Item | Specific Product | Qty | Price |
|---|------|-----------------|-----|-------|
| 17 | USB Cable | Shielded USB-A to Mini-B, 4ft, braided, dual ferrite cores | 1 | $10 |
| 18 | USB Extension (optional) | USB-A panel-mount bulkhead extension, 1ft | 1 | $7 |

### Input

| # | Item | Specific Product | Qty | Price |
|---|------|-----------------|-----|-------|
| 19 | Wireless Keyboard | Rii i8+ Mini Wireless Keyboard with Touchpad (2.4GHz) | 1 | $18 |

### Mounting & Cable Management

| # | Item | Specific Product | Qty | Price |
|---|------|-----------------|-----|-------|
| 20 | PC Enclosure | Aluminum case or 3D-printed enclosure for LattePanda 3 Delta | 1 | $15 |
| 21 | Velcro Strips | Industrial strength velcro strips (for mounting PC under seat/dash) | 1 pack | $6 |
| 22 | Cable Clips | Adhesive cable clips, assorted sizes | 1 pack | $5 |
| 23 | Split Loom | 1/4" and 3/8" split wire loom, 10ft each | 2 | $8 |
| 24 | Zip Ties | Assorted nylon zip ties | 1 pack | $4 |
| 25 | Electrical Tape | 3M Super 33+ vinyl electrical tape | 1 | $4 |

### Summary

| Category | Subtotal |
|----------|----------|
| Core Computer | $288 |
| Display | $93 |
| Power System | $87 |
| FlashPro Connection | $17 |
| Input | $18 |
| Mounting & Cable Mgmt | $42 |
| **TOTAL** | **~$545** |
| Contingency (10%) | $55 |
| **Realistic Budget** | **~$600** |

---

## 2. Tools Required

### Must Have
- **Digital multimeter** — Testing fuse voltages, verifying ground, checking for parasitic draw
- **Wire stripper/crimper combo tool** — For 16-22 AWG automotive wire
- **Trim removal tool set** — Plastic pry tools for removing FG2 dash panels without scratching
- **Phillips and flathead screwdrivers** — Various sizes
- **10mm socket + ratchet** — For chassis ground bolt
- **Test light or multimeter probe** — To identify hot fuses and verify ignition switching
- **Flashlight / headlamp** — Working under the dash

### Nice to Have
- **Soldering iron + heat shrink** — For permanent, vibration-proof connections (better than crimp butt splices for long-term)
- **Heat gun** — For heat shrink tubing
- **Wire loom tool** — For threading wire through split loom cleanly
- **Panel clip remover** — For popping plastic push clips on FG2 kick panels
- **Sandpaper (120 grit)** — For cleaning chassis ground point to bare metal

---

## 3. System Overview & Wiring Diagrams

### 3.1 Complete System Block Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        FG2 INTERIOR FUSE BOX                        │
│                    (Driver side, under dash)                         │
│                                                                     │
│   ┌──────────────┐         ┌──────────────┐                        │
│   │ Fuse #20     │         │ Fuse #8      │                        │
│   │ BACK UP      │         │ ACC (A)      │                        │
│   │ 7.5A         │         │ 7.5A         │                        │
│   │ (Always On)  │         │ (IGN Switch) │                        │
│   └──────┬───────┘         └──────┬───────┘                        │
│          │                        │                                 │
└──────────│────────────────────────│─────────────────────────────────┘
           │                        │
     ┌─────┴─────┐           ┌─────┴─────┐
     │ Add-A-Fuse│           │ Add-A-Fuse│
     │ Tap + 5A  │           │ Tap + 5A  │
     │ New Fuse  │           │ New Fuse  │
     └─────┬─────┘           └─────┬─────┘
           │ RED wire               │ YELLOW wire
           │ 16 AWG                 │ 16 AWG
     ┌─────┴─────┐           ┌─────┴─────┐
     │ Inline    │           │ Inline    │
     │ 5A Fuse   │           │ 5A Fuse   │
     └─────┬─────┘           └─────┴─────┘
           │                        │
           │    ┌───────────────────│──── BLACK wire ──┐
           │    │                   │                   │
           ▼    ▼                   ▼                   ▼
     ┌─────────────────────────────────────────────────────────┐
     │                  MAUSBERRY CIRCUITS                      │
     │                  Car Power Supply                        │
     │                                                         │
     │  [BATT+]  [GND]  [IGN]              [OUT+] [OUT-] [SIG]│
     └────────────────────────────────┬────────────────────────┘
                                      │
                         ┌────────────┼────────────┐
                         │            │            │
                         ▼            ▼            ▼
                    ┌─────────────────────────────────────┐
                    │         LATTEPANDA 3 DELTA           │
                    │                                     │
                    │  [12V IN]    [GND]    [Arduino GPIO]│
                    │                                     │
                    │  [USB-A] ──── USB Cable ──── [FlashPro] ──── [OBD2 Port]│
                    │                                     │
                    │  [Micro-HDMI] ── HDMI ── [7" Touchscreen]              │
                    │  [USB-A] ────── USB ──── [Screen Touch Input]          │
                    │  [USB-A] ────── Dongle ── [Rii i8+ Keyboard]           │
                    │                                     │
                    │  [Arduino D7] ── (Future: Exhaust Valve Relay)         │
                    └─────────────────────────────────────┘
```

### 3.2 Fuse Tap Detail Diagram

**IMPORTANT: Add-a-fuse tap orientation matters!**

When you insert an add-a-fuse tap into a fuse slot, one side of the tap is connected to the bus bar (always-hot side) and the other side passes through the original fuse. The NEW fuse in the tap should go on the always-hot side, and the ORIGINAL fuse goes in the pass-through side. This way, if your new circuit blows its fuse, it doesn't kill the original circuit.

```
                    FUSE BOX SLOT
                    ┌───────────┐
                    │           │
    Bus Bar ────────┤  Original │──────── Load (original circuit)
    (hot side)      │  Fuse     │
                    │  Slot     │
                    └───────────┘

    REPLACED WITH ADD-A-FUSE TAP:

                    ┌─────────────────────┐
                    │   ADD-A-FUSE TAP    │
                    │                     │
    Bus Bar ────────┤  [New 5A Fuse] ─────────── Wire to Mausberry
    (hot side)      │                     │
                    │  [Original Fuse] ───────── Original Load (unchanged)
                    │                     │
                    └──────────┬──────────┘
                               │
                          Pigtail wire
                          to your circuit
```

**How to identify the hot side:** With the fuse REMOVED, use a multimeter or test light. Touch each contact in the empty fuse slot. The one that reads 12V (to ground) is the bus bar / hot side. The other side is the load side. Your add-a-fuse tap's new fuse pigtail goes on the hot side.

### 3.3 Ground Connection Detail

```
    BLACK 16 AWG Wire
         │
         │
    ┌────┴────┐
    │  Ring   │
    │Terminal │
    │ #10 stud│
    └────┬────┘
         │
    ─────┴───── Chassis bolt (bare metal, sanded clean)
                Located: Under dash, driver side kick panel area
                or passenger side footwell near seat rail bolt

    IMPORTANT:
    - Sand paint off around the bolt hole to bare metal
    - Use a star washer between ring terminal and chassis for bite
    - Torque snug — not gorilla tight, but solid contact
    - Add a thin coat of dielectric grease over the connection to prevent corrosion
```

### 3.4 Wire Routing Diagram (Top-Down View of FG2 Interior)

```
    ┌─────────────────────────────────────────────────────────────┐
    │                      WINDSHIELD                              │
    │                                                             │
    │   ┌──────────┐                         ┌──────────┐        │
    │   │ 7" SCREEN│ (mounted via suction    │          │        │
    │   │ (dash    │  cup or vent clip)      │          │        │
    │   │  mount)  │                         │          │        │
    │   └────┬─────┘                         │          │        │
    │        │ HDMI + USB                    │          │        │
    │   ─────┘                               │          │        │
    │                                        │          │        │
    │  ┌─ FUSE BOX                           │          │        │
    │  │  (behind lower                      │ CENTER   │        │
    │  │   kick panel)                       │ CONSOLE  │        │
    │  │                                     │          │        │
    │  │  RED wire ──┐                       │          │        │
    │  │  YEL wire ──┤                       │          │        │
    │  │             │                       │          │        │
    │  │  ┌──── OBD2 PORT                    │          │        │
    │  │  │   (under dash,                   │          │        │
    │  │  │    left of column)               │          │        │
    │  │  │   [FlashPro plugged in here]     │          │        │
    │  │  │    │ USB cable                   │          │        │
    │  │  │    │                             │          │        │
    │  └──│────│── Route wires along         │          │        │
    │     │    │   driver door sill          │          │        │
    │     │    │   (under carpet/trim)       │          │        │
    │     │    │                             │          │        │
    │  DRIVER  │         ┌──── Wire route ───┘          │        │
    │  SEAT    │         │    under carpet              │ PASS.  │
    │          │         │    along sill                │ SEAT   │
    │          │         │                              │        │
    │          │         │    ┌─────────────────────┐   │        │
    │          │         └───►│   LATTEPANDA 3      │◄──┘        │
    │          │              │   + MAUSBERRY        │            │
    │          └──── USB ────►│   (under pass. seat) │            │
    │                        │   or behind dash      │            │
    │                        └─────────────────────┘             │
    │                                                             │
    │                      REAR SEATS                              │
    └─────────────────────────────────────────────────────────────┘

    RECOMMENDED PC LOCATION: Under passenger seat
    - Good airflow (not enclosed like behind the dash)
    - Hidden from view (theft deterrent)
    - Accessible for maintenance
    - Short runs to both fuse box and OBD2 port
```

### 3.5 Future: Exhaust Valve Relay Wiring

```
    ┌──────────────────────────────┐
    │      LATTEPANDA 3 DELTA      │
    │                              │
    │  Arduino Leonardo GPIO       │
    │  Pin D7 ─────────────────────│──┐
    │                              │  │
    │  5V Pin ─────────────────────│──│──┐
    │  GND Pin ────────────────────│──│──│──┐
    └──────────────────────────────┘  │  │  │
                                      │  │  │
         ┌────────────────────────────┘  │  │
         │  ┌────────────────────────────┘  │
         │  │  ┌────────────────────────────┘
         │  │  │
         ▼  ▼  ▼
    ┌─────────────────┐
    │  5V RELAY MODULE │
    │  (2-channel,     │
    │   optocoupler)   │
    │                  │
    │  IN1 ◄── D7      │
    │  VCC ◄── 5V      │
    │  GND ◄── GND     │
    │                  │
    │  COM ◄── 12V IGN │  (from inline fuse)
    │  NO  ──────────────────►  QTP QTEC25 Motor (+)
    │  NC  ──── (unused)│
    └─────────────────┘
                              QTP QTEC25 Motor (-) ──── Chassis GND

    MANUAL OVERRIDE:
    ┌───────────────┐
    │ DPDT Toggle   │──── Wired in parallel with relay
    │ Switch (dash) │     Can force valve open/closed
    └───────────────┘     regardless of PC state

    NOTES:
    - Relay is NORMALLY OPEN = valve stays CLOSED when PC is off (quiet/safe default)
    - When Arduino sets D7 HIGH, relay closes, valve opens (sport mode)
    - QTP motor draws ~5-8A; use relay rated for 10A+ at 12V
    - Run 14 AWG wire from relay to QTP motor (longer run, under the car)
    - Use weatherproof Deutsch connectors where wiring exits the cabin
    - Protect under-car wiring with split loom and DEI fire sleeve near exhaust
```

---

## 4. FG2 Fuse Box Reference

### Interior Fuse Box Location
The 2008-2011 Honda Civic SI (FG2) interior fuse box is located on the **driver's side, lower left dash area**, behind a removable panel. To access:
1. Open the driver's door
2. Look at the lower left corner of the dashboard, to the left of the steering column
3. Pull the small rectangular cover straight off (it's held by clips, no screws)
4. The fuse box is exposed with the fuse layout diagram printed on the inside of the cover

### Fuse Type
The FG2 interior fuse box uses **MINI blade fuses** (the smaller size, not standard or micro). Make sure your add-a-fuse taps and replacement fuses are MINI blade type.

### Recommended Fuse Taps

#### Constant 12V (Always-On) — Fuse #20 "BACK UP" (7.5A)

| Detail | Value |
|--------|-------|
| Fuse Position | #20 |
| Circuit Name | BACK UP |
| Stock Amperage | 7.5A |
| What it powers | Clock, radio presets, ECU keep-alive memory |
| Why this one | Low current draw on existing circuit (~0.5A), 7.5A fuse has plenty of headroom for the Mausberry's standby draw (~50mA). This fuse is ALWAYS hot, even with key removed. |
| Add-a-fuse new fuse | 5A (for your Mausberry constant input) |

**Alternative constant source:** Fuse #19 "DOOR LOCK" (7.5A) — also always-on. Either works.

#### Ignition-Switched 12V (ACC/RUN) — Fuse #8 "ACC(A)" (7.5A)

| Detail | Value |
|--------|-------|
| Fuse Position | #8 |
| Circuit Name | ACC (A) — Accessory |
| Stock Amperage | 7.5A |
| What it powers | Accessory socket, power outlet (the one in the center console) |
| Why this one | Clean ignition-switched source. Goes live when the key is in ACC or RUN position. Off with key out. Low existing load when nothing is plugged into the power outlet. |
| Add-a-fuse new fuse | 5A (for your Mausberry ignition sense input) |

**Alternative ignition source:** Fuse #15 "A/C" (10A) — switched with ignition. But ACC(A) is cleaner since you control what's plugged into the accessory outlet.

### Verification Procedure (DO THIS BEFORE WIRING)

1. Set multimeter to DC volts (20V range)
2. Connect black lead to a known good ground (bare metal under dash, or negative battery terminal)
3. **With key OUT:**
   - Probe both contacts of fuse #20 slot — BOTH should read ~12V (it's always on)
   - Probe both contacts of fuse #8 slot — BOTH should read 0V (it's switched)
4. **With key in ACC position:**
   - Fuse #20 — still ~12V
   - Fuse #8 — NOW reads ~12V
5. This confirms your constant and switched sources. If these don't match, check a different fuse.
6. **Identify the hot side** of each slot: remove the fuse, probe each contact individually. The one that reads 12V with the fuse removed is the bus bar (hot) side.

---

## 5. Pre-Installation: Desk Setup

**Do ALL of this at home on a desk before putting anything in the car.** You do not want to troubleshoot software issues while contorted under a dashboard.

### 5.1 Install the M.2 SSD

1. The LattePanda 3 Delta has an M.2 2242 slot on the underside of the board
2. Remove the bottom cover screws (small Phillips)
3. Insert the Transcend MTS430S at a 30-degree angle into the M.2 slot
4. Press down and secure with the screw
5. Reassemble

### 5.2 First Boot & Windows Setup

1. Connect the LattePanda to a monitor (micro-HDMI), keyboard, and mouse
2. Power via the included 12V adapter (or any 12V/3A supply)
3. Windows 11 setup wizard will run — complete it (use a local account, skip Microsoft account if desired)
4. Once on the desktop, go to Disk Management and initialize the M.2 SSD
5. Move the Windows page file and temp folders to the SSD for better performance
6. Optionally: clone the eMMC Windows install to the SSD and boot from SSD for better speed

### 5.3 Install FlashProManager

1. Download latest FlashProManager from **hondata.com** (Support > Downloads)
2. Run the installer — it will also install the FTDI USB serial drivers
3. Launch FlashProManager to verify it opens correctly
4. Do NOT connect the FlashPro yet (save that for the car)

### 5.4 Install Mausberry Shutdown Script

1. Download the shutdown script from Mausberry Circuits' website (included with the power supply documentation)
2. The script monitors a GPIO pin (or USB signal) for the ignition-off signal
3. When triggered, it runs `shutdown /s /t 0` to shut Windows down immediately
4. Set the script to run at startup (put shortcut in `shell:startup` folder)
5. Test by simulating the signal (details in Mausberry documentation)

### 5.5 Connect and Test the 7" Touchscreen

1. Connect micro-HDMI to HDMI cable from LattePanda to screen
2. Connect USB cable from screen to LattePanda (for touch input)
3. Windows should detect the display and touch input automatically
4. Adjust display scaling: Settings > Display > Scale — try 100% or 125% for 1024x600
5. Calibrate touch if needed: Control Panel > Tablet PC Settings > Calibrate

### 5.6 Test FlashPro Connection (On Desk, Simulated)

1. Plug in the USB-A to Mini-B cable to the LattePanda
2. Open Device Manager — look for an FTDI serial port under "Ports (COM & LPT)"
3. If the driver loaded, you'll see "USB Serial Port (COMx)"
4. If not, reinstall FTDI drivers from ftdichip.com
5. **NOTE:** FlashProManager won't detect a "FlashPro" until the actual unit is connected and powered via OBD2. This step just verifies the USB/driver chain works.

### 5.7 Configure Windows for Car Use

See Section 7 for detailed steps. Do as much of this as possible on the desk.

---

## 6. Step-by-Step Installation

### Step 1: Verify Fuse Locations (15 min)

1. Open the FG2 interior fuse box (driver side, pull off cover)
2. Reference the fuse diagram on the inside of the cover
3. Locate fuse #20 (BACK UP) and fuse #8 (ACC A)
4. With multimeter, verify voltages as described in Section 4
5. Identify the hot side of each fuse slot
6. Photograph the fuse box and mark positions with tape or marker for reference

### Step 2: Install Add-A-Fuse Taps (10 min)

**Fuse #20 (Constant 12V):**
1. Pull out the 7.5A fuse from position #20 with fuse puller
2. Note which side of the slot was the hot side (from Step 1)
3. Insert the add-a-fuse tap into the slot
4. Place the ORIGINAL 7.5A fuse in the tap slot that connects to the LOAD side (non-hot)
5. Place a NEW 5A fuse in the tap slot that connects to the HOT side (bus bar)
6. The pigtail wire from the tap is your constant 12V output

**Fuse #8 (Ignition-Switched 12V):**
1. Same process — pull 7.5A fuse from #8
2. Insert add-a-fuse tap
3. Original 7.5A on load side, new 5A on hot side
4. Pigtail wire is your ignition-switched output

**Verify:** Turn key to ACC — both pigtail wires should read 12V. Turn key OFF — only the #20 pigtail should read 12V.

### Step 3: Run Inline Fuses (5 min)

1. Crimp or solder the add-a-fuse pigtail wires to your 16 AWG wires (red for constant, yellow for ignition)
2. Install an inline fuse holder on each wire, within 12 inches of the fuse box
3. Insert 5A fuses in each inline holder
4. This gives you double fuse protection (the add-a-fuse fuse + the inline fuse)

### Step 4: Establish Chassis Ground (10 min)

1. Locate a suitable chassis bolt — the best spot in the FG2 is the **bolt on the metal bracket behind the driver's kick panel**, or a **seat rail bolt on the passenger side** (if mounting PC under passenger seat)
2. Remove the bolt
3. Sand the paint off the chassis around the bolt hole — you need bare metal contact (120 grit sandpaper, ~1" diameter circle)
4. Crimp a ring terminal onto your black 16 AWG ground wire
5. Place ring terminal over the bolt, add a star washer for bite, re-tighten the bolt firmly
6. Apply a thin layer of dielectric grease over the connection
7. **Test:** Multimeter from your ground wire to the negative battery terminal — should read less than 0.5 ohms

### Step 5: Route Wires to PC Location (20 min)

**If mounting under the passenger seat (recommended):**

1. Remove the driver's side lower kick panel (pull straight toward you, held by clips)
2. Remove the driver's side door sill trim (pulls up, held by clips along its length)
3. Remove the passenger side door sill trim
4. Bundle the red, yellow, and black wires together with a few zip ties
5. Route along the driver's footwell, behind the kick panel
6. Continue along the driver's door sill, under the carpet
7. Cross under the carpet behind/below the center console (there's space)
8. Come up under the passenger seat
9. Leave enough slack at the PC end for connection (12-18 inches extra)
10. Secure the wire run with adhesive cable clips every 12 inches
11. Wrap exposed sections in split loom for protection

**USB cable from FlashPro/OBD2 to PC:**
1. The OBD2 port is under the dash, left of the steering column
2. The FlashPro plugs into OBD2 and stays there
3. Route the USB cable from the FlashPro along the same path as the power wires
4. Join it into the same wire loom for a clean run
5. Leave enough slack at the OBD2 end that the FlashPro is not stressed

### Step 6: Mount the LattePanda (15 min)

**Under passenger seat mounting:**
1. Place the LattePanda (in its case/enclosure) under the passenger seat
2. Position it so:
   - USB ports face toward the center console (for easy cable access)
   - Micro-HDMI faces the same direction (for screen cable routing)
   - It's not blocking the seat rails
   - It has clearance for airflow on all sides
3. Secure with industrial-strength velcro strips on the bottom of the case and the floor/seat frame
4. Optionally: fabricate a small aluminum L-bracket that bolts to the seat rail and holds the PC

### Step 7: Mount the Display (10 min)

**Options for the FG2:**
1. **Suction cup windshield mount** (RAM Mount) — most flexible, easy to remove, but visible
2. **Vent-clip mount** — clips to the center vents, positions screen near the radio area
3. **Dash-top adhesive mount** — near the base of the windshield, centered
4. **Custom pod/bracket** — 3D-print or fabricate a bracket that positions the screen in the blank area above the center console

For now, a suction cup mount is the easiest to start with. You can upgrade to a cleaner permanent mount later.

1. Attach the RAM mount/suction cup to the windshield, lower-center area
2. Mount the 7" screen in the mount's cradle
3. Route the micro-HDMI cable and USB cable from the screen, along the A-pillar trim or across the dash top, down behind the center console, to the LattePanda under the seat
4. Secure cables with adhesive clips along the route

### Step 8: Connect Mausberry Board (10 min)

1. Place the Mausberry board near the LattePanda (under passenger seat, velcro it to the floor nearby)
2. Connect wires:
   - **BATT+** terminal ← Red wire (constant 12V from fuse #20)
   - **GND** terminal ← Black wire (chassis ground)
   - **IGN** terminal ← Yellow wire (ignition-switched 12V from fuse #8)
   - **OUT+** → LattePanda 12V input positive
   - **OUT-** → LattePanda 12V input negative/ground
   - **SIG** → LattePanda GPIO or USB (depends on Mausberry model — follow their specific wiring guide)
3. Double-check all connections with the multimeter before powering on
4. Ensure no bare wire is exposed — heat shrink or electrical tape all connections

### Step 9: Connect Peripherals (5 min)

1. Plug micro-HDMI cable into LattePanda → goes to 7" screen
2. Plug USB cable from screen touch input into LattePanda USB port
3. Plug USB cable from FlashPro into LattePanda USB port
4. Plug Rii i8+ USB dongle into LattePanda USB port (or leave in glovebox, plug in when needed)
5. If the LattePanda only has 3 USB-A ports and you need more, use a small USB hub

### Step 10: First Power-On Test (10 min)

1. **Do not reassemble trim panels yet**
2. Turn the key to **ACC** (not START)
3. The Mausberry should receive ignition signal and power on the LattePanda
4. Watch for:
   - LattePanda power LED comes on (blue LED on the board)
   - Screen backlight activates
   - Windows boot screen appears
   - Windows reaches desktop
5. Note the boot time: should be 15-25 seconds to desktop
6. Verify the Mausberry shutdown script is running (check system tray or Task Manager)

### Step 11: Test Shutdown Sequence (5 min)

1. With the system booted and at the desktop, turn the key to **OFF**
2. Watch the screen — Windows should begin shutting down within a few seconds
3. The shutdown should complete in 10-20 seconds
4. After shutdown, the Mausberry should cut power completely (LattePanda LED goes off)
5. **Verify zero parasitic draw:** With key off and system fully shut down, measure current draw on the constant 12V wire — should be near zero (< 5mA)

### Step 12: Test FlashPro Communication (15 min)

1. **This step requires the car's ECU to be powered — key in ON position (not ACC, not START)**
2. Turn key to ON (dash lights come on, engine not running)
3. Wait for Windows to boot fully
4. Launch FlashProManager
5. It should detect the FlashPro unit via USB — status bar will show "FlashPro Connected" and display ECU info
6. If this is the first time: FlashPro will register to your ECU (see the Temporary Setup Guide for first-time registration details)
7. If detection fails: check USB cable, try a different USB port on the LattePanda, check Device Manager for FTDI driver

### Step 13: Test Engine-Running Operation (10 min)

1. Start the engine (the Mausberry should ride through the cranking voltage dip without rebooting the PC)
2. If the PC reboots during cranking: this means the Mausberry's capacitors aren't sufficient. Add an external supercapacitor (2.7V 10F caps in series, or a small 12V UPS module)
3. With engine running, FlashProManager should show live data (RPM, coolant temp, etc.)
4. Verify the touchscreen works for navigating FlashProManager

### Step 14: Button Up (20 min)

1. Once everything works, secure all wiring permanently
2. Wrap wire runs in split loom where exposed
3. Zip-tie any loose sections
4. Ensure no wires are near moving parts (seat rails, pedals)
5. Reinstall door sill trim (press firmly, clips snap back in)
6. Reinstall driver kick panel
7. Tidy up cables behind the center console
8. Final cosmetic check — minimize visible cables

---

## 7. Windows Configuration for Car Use

### 7.1 Power Settings

Open **Settings > System > Power & sleep** (or Power & battery):

```
Screen: Never turn off
Sleep: Never
Hibernate after: Never (we'll control hibernate via Mausberry signal)
```

Advanced power settings (Control Panel > Power Options > Change plan settings > Change advanced):
```
Hard disk > Turn off after: Never
USB settings > USB selective suspend: Disabled
PCI Express > Link State Power Management: Off
```

### 7.2 Disable Windows Update Auto-Restart

**Method 1: Group Policy (if Win 11 Pro)**
1. Run `gpedit.msc`
2. Navigate to: Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage end user experience
3. Enable "Configure Automatic Updates" — set to "2 - Notify for download and notify for install"
4. Enable "No auto-restart with logged on users for scheduled automatic updates installations"

**Method 2: Registry (if Win 11 Home)**
1. Run `regedit`
2. Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU`
3. Create DWORD `NoAutoRebootWithLoggedOnUsers` = 1
4. Create DWORD `AUOptions` = 2

### 7.3 Auto-Start FlashProManager on Boot

1. Press `Win+R`, type `shell:startup`, press Enter
2. Create a shortcut to FlashProManager.exe in this folder
3. FlashProManager will now launch automatically when Windows reaches the desktop

### 7.4 Display Scaling

For a 7" 1024x600 screen:
1. Settings > Display > Scale: **100%** (125% makes things too big on this resolution)
2. If text is too small, use 125% and accept some FlashProManager UI clipping, or increase system font size independently

### 7.5 Fast Startup / Hibernate

1. Control Panel > Power Options > "Choose what the power buttons do"
2. Click "Change settings that are currently unavailable"
3. Check "Turn on fast startup (recommended)"
4. The Mausberry shutdown script can be configured to hibernate instead of shutdown:
   - Change the script's shutdown command from `shutdown /s /t 0` to `shutdown /h`
   - This makes resume much faster (~5-10 seconds vs 15-25 seconds cold boot)

### 7.6 Disable Unnecessary Startup Programs

Task Manager > Startup tab — disable everything except:
- Mausberry shutdown script
- FlashProManager (your autostart shortcut)
- FTDI drivers (if listed)

Disable: OneDrive, Microsoft Teams, Xbox Game Bar, Cortana, Edge, widgets, etc.

### 7.7 WiFi Configuration

The LattePanda 3 Delta has built-in WiFi. You won't have internet in the car normally, but:
1. Save your phone's hotspot credentials so you can tether when needed (for FlashProManager updates)
2. Set WiFi to "manual connect only" so it doesn't waste resources scanning

---

## 8. Usage Guide

### 8.1 Daily Workflow

```
START THE CAR
     │
     ▼
Key to ACC/RUN ──► Mausberry powers on ──► LattePanda boots (15-25s)
     │                                          │
     ▼                                          ▼
Start engine ──► Voltage stabilizes ──► FlashProManager auto-launches
     │                                          │
     ▼                                          ▼
Drive ◄──────── Live gauges displayed ◄──── FlashPro detected
     │
     ▼
Key OFF ──► Mausberry signals shutdown ──► Windows shuts down (10-20s)
     │                                          │
     ▼                                          ▼
Walk away ◄──── Power cut completely ◄──── Shutdown confirmed
```

### 8.2 How to Flash a Tune

1. **Engine RUNNING, car in PARK/NEUTRAL, parking brake ON**
2. Open FlashProManager (should already be open)
3. Verify FlashPro is connected (status bar shows ECU info)
4. Go to File > Open and select your calibration file (.fpc)
5. Review the calibration details (fuel maps, timing, VTEC point, etc.)
6. Click **"Upload"** (the button that sends the calibration to the FlashPro/ECU)
7. A progress bar will appear — **DO NOT touch anything, do not bump the USB cable, do not turn off the car**
8. Flash takes ~10-30 seconds
9. Status will confirm "Upload Complete"
10. The new calibration is now active on the ECU

### 8.3 How to Datalog

1. In FlashProManager, click the **"Datalog"** tab or button
2. Select which parameters to log (recommend: RPM, TPS, MAP, IAT, ECT, AFR, Knock, STFT, LTFT, Injector Duty, VTEC)
3. Click **"Start Logging"**
4. Drive normally, do pulls, whatever you want to capture
5. Click **"Stop Logging"**
6. Save the log file (.fpdl) — store on the SSD in a "Datalogs" folder
7. You can review logs later in FlashProManager's log viewer — it shows graphs of all parameters over time

### 8.4 Real-Time Gauges

1. FlashProManager has a **"Gauges"** view
2. You can configure which gauges are displayed and their layout
3. Recommended gauge layout for the 7" screen:
   - **Large center:** Tachometer (RPM)
   - **Top row:** AFR | Coolant Temp | Intake Air Temp
   - **Bottom row:** Knock Count | Short Term Fuel Trim | Battery Voltage
4. Set up a gauge layout you like, then save it as a preset
5. You can have this view auto-display on startup

### 8.5 Swapping Between Daily and Sport Tunes

1. Open FlashProManager
2. File > Open > Select "daily.fpc" or "sport.fpc" (your saved calibrations)
3. Click Upload — flash takes ~15-30 seconds
4. Done — the car is now running the selected tune

**Future enhancement:** A Python script with two big touchscreen buttons that automates this (opens the correct file and initiates upload with one tap, plus toggles the exhaust valve relay).

### 8.6 Safety Rules

- **NEVER flash while driving** — always parked, engine running
- **NEVER disconnect USB during a flash** — wait for completion
- **ALWAYS keep a copy of your stock calibration** — it's your factory reset
- **Engine running = stable voltage** — the alternator provides clean 13.8-14.4V. Flashing on battery alone (engine off) works but voltage can sag on older batteries
- **Don't flash with heavy electrical loads** — turn off AC, headlights, audio before flashing (reduces electrical noise and voltage drop)

---

## 9. Future: Exhaust Valve Integration

### Overview

When you install the QTP QTEC25 exhaust cutout, the LattePanda can control it via the onboard Arduino Leonardo co-processor.

### Hardware Setup

See the wiring diagram in Section 3.5.

**Parts needed:**
| Item | Purpose | Cost |
|------|---------|------|
| 5V 2-channel relay module (SRD-05VDC-SL-C, optocoupler) | Switch 12V to QTP motor | $8 |
| DPDT toggle switch (illuminated) | Manual override on dash | $8 |
| 14 AWG wire, 15ft | Run from relay to QTP motor under car | $5 |
| Deutsch DT 2-pin connector set | Weatherproof connection at cabin floor exit | $8 |
| DEI fire sleeve, 3ft | Protect wiring near exhaust | $15 |

### Arduino Sketch (Basic)

```cpp
// Exhaust Valve Control - LattePanda Arduino Leonardo
// D7 = Relay control pin (HIGH = valve OPEN, LOW = valve CLOSED)

const int RELAY_PIN = 7;
const int VALVE_OPEN = HIGH;
const int VALVE_CLOSED = LOW;

void setup() {
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, VALVE_CLOSED); // Default: closed (quiet)
    Serial.begin(9600); // Communication with Windows side
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();
        if (command == 'O') { // Open
            digitalWrite(RELAY_PIN, VALVE_OPEN);
            Serial.println("VALVE:OPEN");
        } else if (command == 'C') { // Close
            digitalWrite(RELAY_PIN, VALVE_CLOSED);
            Serial.println("VALVE:CLOSED");
        } else if (command == 'S') { // Status query
            int state = digitalRead(RELAY_PIN);
            Serial.println(state == VALVE_OPEN ? "VALVE:OPEN" : "VALVE:CLOSED");
        }
    }
}
```

### Windows-Side Python Script (Concept)

```python
# tune_switcher.py — Runs on LattePanda Windows
# Links tune selection to exhaust valve position

import serial
import subprocess
import tkinter as tk

ARDUINO_PORT = "COM3"  # Check Device Manager for actual port
FLASHPRO_PATH = r"C:\Program Files\Hondata\FlashProManager.exe"
DAILY_TUNE = r"C:\Tunes\daily.fpc"
SPORT_TUNE = r"C:\Tunes\sport.fpc"

arduino = serial.Serial(ARDUINO_PORT, 9600, timeout=1)

def set_daily():
    arduino.write(b'C')  # Close valve
    subprocess.Popen([FLASHPRO_PATH, DAILY_TUNE])
    status_label.config(text="MODE: DAILY", bg="green")

def set_sport():
    arduino.write(b'O')  # Open valve
    subprocess.Popen([FLASHPRO_PATH, SPORT_TUNE])
    status_label.config(text="MODE: SPORT", bg="red")

# Big touch-friendly buttons
root = tk.Tk()
root.title("Tune Switcher")
root.attributes('-fullscreen', False)
root.geometry("600x400")

status_label = tk.Label(root, text="MODE: DAILY", font=("Arial", 32), bg="green", fg="white")
status_label.pack(fill=tk.X, pady=10)

daily_btn = tk.Button(root, text="DAILY\n(Quiet)", font=("Arial", 28),
                       bg="green", fg="white", command=set_daily, height=3)
daily_btn.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

sport_btn = tk.Button(root, text="SPORT\n(Loud)", font=("Arial", 28),
                       bg="red", fg="white", command=set_sport, height=3)
sport_btn.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

root.mainloop()
```

This is a starting concept. We'll refine it when you're ready to build this phase.

---

## 10. Troubleshooting

### PC Won't Boot

| Symptom | Check | Fix |
|---------|-------|-----|
| No LEDs, no screen | Mausberry getting power? Multimeter on BATT+ input | Check fuse #20 and inline fuse. Check ground connection. |
| Mausberry LED on but LP won't boot | Mausberry output voltage? Should be ~12V | Check Mausberry output connections to LattePanda. Try direct 12V to LP to isolate. |
| LP blue LED on but no display | HDMI connection | Reseat micro-HDMI cable. Try a different cable. Check display power (USB). |

### PC Reboots During Cranking

The battery voltage drops to 9-10V during cranking. The Mausberry should ride through this, but if the dip is too severe:
1. Check battery health — a weak battery at 170k miles may drop below 9V during cranking
2. Add a supercapacitor bank across the Mausberry's BATT+ input (6x 2.7V 25F caps in series = ~4F at ~16V)
3. Or: configure the system to boot AFTER cranking (keep key in ACC for 3 seconds before starting)

### FlashPro Not Detected

| Check | Action |
|-------|--------|
| USB cable firmly seated? | Reseat both ends |
| FTDI driver installed? | Device Manager > Ports (COM & LPT) > look for USB Serial Port |
| Try different USB port | LattePanda has 3 USB-A ports, try each |
| FlashPro LED on? | The FlashPro unit itself has LEDs — verify it's powered via OBD2 |
| Key position? | Must be in ON position (not just ACC) for FlashPro to communicate with ECU |

### Screen Flicker or Interference Lines

1. Add ferrite cores to the HDMI cable (clip-on ferrite, $3)
2. Ensure the screen's USB power comes from the LattePanda, not a separate source (ground loop)
3. Route HDMI cable away from the ignition coil wiring and alternator cable

### Parasitic Battery Drain

If the car battery is dying after sitting for a few days:
1. With everything off, measure current draw on the constant 12V wire (should be < 5mA)
2. If the Mausberry is drawing excessive standby current, check that it completed the full shutdown sequence
3. Verify the LattePanda is fully off (no LEDs, no fan spin)
4. As a safety measure, add a master kill switch on the constant 12V wire — flip it off when parking for extended periods

---

## 11. Maintenance

### Monthly
- **Visual check:** Glance at the PC and wiring under the seat. Look for anything that's come loose from vibration.
- **Connection check:** Gently tug USB cables and power connections — they should be snug.
- **Datalog review:** Review recent datalogs for anything unusual (knock events, AFR drift, sensor anomalies).

### Quarterly
- **Windows updates:** Tether to phone hotspot, check for and install Windows updates manually. Reboot and verify everything still works.
- **FlashProManager updates:** Check hondata.com for software updates. Update if available.
- **Fuse check:** Visually inspect the add-a-fuse taps and inline fuses. Replace any that show discoloration.
- **Ground check:** Verify the chassis ground bolt is tight and corrosion-free.

### Seasonal
- **Summer:** Monitor system temps during the first hot days. If the PC is thermal-throttling or shutting down after the car sits in the sun, consider relocating it or adding a small 12V fan.
- **Winter:** If you're in a cold climate, the PC may boot slowly or the LCD may be sluggish on very cold mornings. This resolves as the cabin warms up. No action needed unless temps drop below -10F regularly.

### As Needed
- **SSD health:** Run CrystalDiskInfo occasionally to check SSD health.
- **Recalibrate touchscreen** if touch accuracy drifts.
- **Back up calibration files and datalogs** to the MicroSD card or transfer to your home PC periodically.

---

## Version History

| Date | Change |
|------|--------|
| 2026-04-16 | Initial guide created |
