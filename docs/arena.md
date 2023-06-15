---
title: Arena
parent: Acquisition
grand_parent: Generation 4
nav_order: 7
---

1. TOC
{:toc}

# Arena Board

The arena board organizes panels in a geometry and provides structural integrity to the whole setup. Different shapes of cylindrical arenas have been built. They are often described by their number of panel columns populated and the virtual ones forming a full circle. An _arena 12-12_ is a closed cylinder formed by 12 columns in total. All columns can be populated in this design, but typically between 1 and 3 are left empty to access the center of the arena.

Most functional designs will have two separate bill of material (BOM). One of the BOM should refer to _BOTTOM_, another to _TOP_. For a single setup, you will need two arena bards of the same type, one acting as the bottom board, one as the top board.

The BOM for the bottom arena board will usually contain more components. The bottom arena board is where the interconnect board and power are connected to and where the signals from the computer are distributed to the different columns. The top arena board gives structural integrity to the whole setup, it terminates signals, and sometimes provides additional power connectors.

## arena 12-12 board {#a12-12}

![Arena 12-12 board v1](assets/arena_12-12_front_photo.jpg){:standalone .ifr data-img-class="pop"}

A 12-12 Arena places twelve columns of panels in a regular dodecagon, forming an approximate cylindrical display with 170mm diameter. These are type of arenas are useful for behavioral experiments.

Currently, the most recent version 2 is the most widely used version. Nevertheless, version 4 has some improvements and is designed to minimize noise. This should work, but is not yet widely adapted. All other versions are either deprecated or prototypes.

The __Arena 12-12 Version 1__ (OrCAD design file at `arena_12-12/arena_12-12_v1.brd`, see [schematics](assets/arena_12-12_v1_schematic.pdf)) was developed in June 2017 as a 6 layer board. In addition to the connectors approximating an inner circle with 170mm diameter, it had a second row of connectors about 180mm apart. Another visible distinction are eight vias inside the connector ring, which are used for the chip selects. The image on the right shows such an arena board with the ribbon connector on the top left and the power connector on the bottom left.

![Rendering of an Arena 12-12 Version 2](assets/arena_12-12_v2_front_iso-render.png){:standalone .ifr data-img-class="pop"}

The __Arena 12-12 Version 2__ (OrCAD design file at `arena_12-12/arena_12-12_v2.brd`) is similar to version 1 in [schematics](assets/arena_12-12_v1_schematic.pdf) and most of the pcb layout, but is missing the outer ring of potential connectors. Development on the 6 layer version 2 started in February 2018. If you want to repair a version 1 or version 2 board, we recommend the production files for __Arena 12-12 v2.4__ archived at `arena_12-12/production_v2/arena_12-12_v2p4.zip` as it includes incremental improvements like a more helpful silkscreen. While most of the arenas were hand-assembled and with parts that our machine shop had lying around. Version v2.4 is an attempt to fill in some of the gaps and is a step towards being able to give the assembly job to an external contractor. [Contact us]({{site.baseurl}}/Contact) about the progress if you have questions.

__Arena 12-12 Version 2C__ (OrCAD design file at `arena_12-12/arena_12-12_v2C`) is a prototype to length match all signal lines and decrease electric noise by routing them on individual layers. As a result the board has 12 (hex: `0xC`, hence 2C) layers. In our hands it didn't show improvements over other version 2 boards, but if you are looking to debug timing issues this could be a helpful starting point.

__Arena 12-12 Version 3__ (OrCAD design file at `arena_12-12/arena_12-12_v3.brd`, see [schematics](assets/arena_12-12_v3_schematic.pdf)) is a 6 layer prototype with two rings of connectors and additional changes to the physical shape of the PCB. It never left prototyping stage and is here only for historical purposes. This version was designed in June 2019.

__Arena 12-12 Version 4__ (OrCAD design file at `arena_12-12/arena_12-12_v4.brd`, see [schematics](assets/arena_12-12_v4_schematic.pdf)) is the attempt to minimize noise in the system further. To achieve that, the electronic design of this 6 layer PCB was changed in August 2019 so that the clock signal is now actively driven by a fanout instead of a simpler voltage translator as in previous versions. Furthermore, the chip select lines are isolated from each other through active components. The circular PCB was physically interrupted to avoid timing issues through circular traces.

The __Arena 12-12 Version 5__ (OrCAD design file at `arena_12-12/arena_12-12_v5.brd`, see [schematics](assets/arena_12-12_v5_schematic.pdf)) is an experimental 6 layer design without a [interconnect board](#interconnect) but instead with a direct VHDCI connector. Development is ongoing since Summer 2020, but the design does not work yet.

![Rendering of a notched Arena 12-12 Version 6](assets/arena_12-12_v6p0_front_render.png){:standalone .ifr data-img-class="pop"}

The __Arena 12-12 Version 6__ (OrCAD design file at `arena_12-12/arena_12-12_v6.brd`, see [schematics](assets/arena_12-12_v6_schematic.pdf)) from June 2019 is technically the same as Version 2 (hence the schematic is literally the same), but has a cutout in the PCB to fit under a specific microscope (see image of _notched_ arena). The latest production files are at `arena_12-12/production_v6/arena_12-12_v6p0.zip`. This version was previously know as version v2.2, but since later improvements to v2.1 lead to confusion, we rebranded it as version v6.0.

## 12-18 arena board {#a12-18}

The Arena 12-18 populates 12 out of 18 sides of a regular octadecagon with panel connectors. This means the approximated cylinder can cover up to 240° of the visual field with a diameter of around 250mm. This type of arena is particularly useful for electrophysiology and imaging experiments.

__Arena 12-18 Version 1__ and 2 are based on the same [schematic](assets/arena_12-18_bottom_schematics.pdf), differences are in routing. Also, __Arena 12-18 v2.0__ uses hidden vias, is more difficult and expensive to manufacture, and has not been used as often as boards from version 1 (and we cannot share the design files at this point). Consequently we recommend using the newest version 1 at the moment, archived at `arena_12-18/production_v1/arena_12-18_v1p1.zip`. The Arena 12-18 v1.1 is a 7 layer PCB with a footprint of 299×206mm². For a more detailed description and changelog see the `README.mdown` file in `arena_12-18/production_v1/`.

![Rendering of the 12-18 arena holder](assets/arena_12-18_holder_render.png){:standalone .ifr data-img-class="pop"}
For some arenas, one board required physical but not electrical connection. In this case a laser cut board, for example from acrylic, is good enough. We share a file `Arena_holder.svg` that can be used to laser cut this type of board inside the arena_12-18 folder.

## Arena Interconnect Board {#interconnect}

![Assembled interconnect board](assets/interconnect_v1_iso_photo.jpg){:standalone .ifr data-img-class="pop"}

Some of the arenas are rotated during experiments and a direct connection of the stiff VHDCI cables would put unnecessary physical stress on the arena board and connector. Therefore the majority of arena boards use a 40pin header which can be used with flexible ribbon cables. The arena interconnect board acts as an adapter between 40pin arena connector and 68pin VHDCI connector from the computer PCIe card. Unfortunately, recent tests suggest, that the ribbon cable introduces noise in the communication. The ribbon cable should be as short as possible to reduce the noise.

The __Arena Interconnect Board Version 1__ (OrCAD design file at `interconnect/interconnect_v1.brd`, see [schematics](assets/interconnect_v1_schematic.pdf)) is a simple 2 layer PCB within the dimensions of 4.9×8.4mm². The most recent production files are archived at `interconnect/production_v1/interconnect_v1p2.zip`.

We also share the OrCAD design files (`interconnect/interconnect_v2.brd`) for an __Interconnect Board Version 2__ (see [schematics](assets/interconnect_v2_schematic.pdf)). This board is designed as 4-layer PCBs with additional power connectors and 15pin connector. In theory, they could be used to drive a single column of panels directly. This design is currently untested and we recommend using version 1.

# Historic

## 12-18 arena board v0.2

![12-18 arena initial design v0.2 (front)](assets/arena_12-18_v0_front.png){:.ifr .pop}

![12-18 arena initial design v0.2](assets/arena_12-18_v0_back.png){:standalone .ifr .clear data-img-class="pop"}

The initial version of an 12-18 arena was designed in KiCad (see [schematic](assets/arena_12-18_v0_schematic.pdf) and [pcb](assets/arena_12-18_v0_pcb.pdf)), but the production never exceeded the version 0.2. The project is at `arena_12-18_v0`.

## 12-18 arena board v0.1

![12-18 arena initial design v0.1 (front)](assets/arena_12-18_s_v0_front.png){:.ifr .pop}

![12-18 arena initial design v0.1](assets/arena_12-18_s_v0_back.png){:standalone .ifr .clear data-img-class="pop"}

Early on, there was a 12-18 arena that was called _with shifters_ was designed in KiCad (see project at `arena_12-18_s_v0` and [schematic](assets/arena_12-18_s_v0_schematic.pdf), but the production in `arena_12-18_s_v0/production_v0` never exceeded the version 0.1.

## 6 connector arena prototype (6-inf arena)

![6 Connector arena (6-inf) with an Arduino prototype controller](assets/arena_6-inf_v0p1_controller_photo.jpg){:standalone .ifr data-img-class="pop"}

The test arena with 6 panel connectors in a row (called a _6-inf arena_) is used to connect the panels with the controller and to supply power to the panels. There are three different headers which can be used to connect the panels to the display controller.

- P22 40-Pin (2x20) single SPI bus header.
- P23 60_Pin (2x30) six SPI bus header.
- P30 40-Pin (2x20) six SPI bus w/ common chip select lines.

5V power is supplied to the panels via 2.1mm DC jack, polarity is center positive.

There are three different versions for the ATmega328 based panels, one for the MAX6960 panels.
{:.clear}

![6-inf arena PCB for ATmega328 v0.3 (front)](assets/arena_6-inf_v0p3_front.png){:.ifr .pop}

![6-inf arena PCB for ATmega328 v0.3](assets/arena_6-inf_v0p3_back.png){:standalone .ifr .clear data-img-class="pop"}

Design files for version 0.3 of the 6-inf arenas for a ATmega328 (see [schematic](assets/arena_6-inf_v0p3_schematic.pdf)) are available in `arena_6-inf_v0p3`, production files in the subfolder `arena_6-inf_v0p3/production_v0`.

![6-inf arena PCB for ATmega328 v0.2 (front)](assets/arena_6-inf_v0p2_front.png){:.ifr .pop .clear}

![6-inf arena PCB for ATmega328 v0.2](assets/arena_6-inf_v0p2_back.png){:standalone .ifr .clear data-img-class="pop"}

Design files for version 0.2 of the 6-inf arenas for a ATmega328 (see [schematic](assets/arena_6-inf_v0p2_schematic.pdf)) are available in `arena_6-inf_v0p2`, production files in the subfolder `arena_6-inf_v0p2/production_v0`.

![6-inf arena PCB for ATmega328 v0.1 (front)](assets/arena_6-inf_v0p1_front.png){:.ifr .pop .clear}

![6-inf arena PCB for ATmega328 v0.1](assets/arena_6-inf_v0p1_back.png){:standalone .ifr .clear data-img-class="pop"}

![6-inf arena prototype in version v0.1](assets/arena_6-inf_v0p1_front_photo.jpg){:standalone .ifr .clear data-img-class="pop"}

Design files for version 0.1 of the 6-inf arenas for a ATmega328 (see [schematic](assets/arena_6-inf_v0p1_schematic.pdf)) are available in `arena_6-inf_v0p1`, production files in the subfolder `arena_6-inf_v0p1/production_v0`. There are 5 sets of jumpers which can be used to configure the arena.

![6-inf arena PCB for MAX6960 (front)](assets/arena_6-inf_max6960_v0p1_front.png){:.ifr .pop .clear}

![6-inf arena PCB for MAX6960](assets/arena_6-inf_max6960_v0p1_back.png){:standalone .ifr .clear data-img-class="pop"}

There is also a 6-inf arenas for a MAX6960 driver (see [schematic](assets/arena_6-inf_max6960_v0p1_schematic.pdf)) available in `arena_6-inf_max6960`. This specific one only made it to version 0.1 and production files in the subfolder `arena_6-inf_max6960/production_v0`.

## Prototype Controller

![Arduino based prototype controller](assets/controller_arduino_photo.jpg){:standalone .ifr .clear data-img-class="pop"}

A demonstration controller, based on an Arduino Uno, is provided with the arena and panels. The demonstration controller connects to header P22 on the arena and will display a moving stripe pattern in 16-level gray scale mode.  The panels (up to four) should be connected to header P1 when using the demo controller. Note, the demo controller requires 5V power via the USB connector on the Arduino Uno in order to operate.

The firmware for an Arduino Uno, Arduino Due, and Teensy 3 are in the [Firmware repository]({{site.baseurl}}/Generation%204/Firmware/docs/). We cannot find the shields to connect these boards to the test arena at the moment, but they should be fairly easy to reverse engineer. But then again, we cannot think of a use case for the prototype controller or the prototype arena.
