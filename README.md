<p align="center">
  <img src="https://raw.githubusercontent.com/visrealm/visrealm/main/assets/banner.svg" width="100%" alt="visrealm - Troy Schrapel - retro computing and hardware emulation">
</p>

I started programming on a TI-99/4A when I was about five, and that got me hooked. I'd moved on to
the PC and picked up C and C++ well before any of it became a job. The career since has been about
90% C++.

I got into building hardware much later. First a breadboard computer, the
**[vrcpu](https://github.com/visrealm/vrcpu)**, then an emulator for it and a web version. Adding a
character LCD to the board meant emulating the LCD too, which became
**[vrEmuLcd](https://github.com/visrealm/vrEmuLcd)**.

After that I wanted to build something around a 65C02, which became the
**[HBC-56](https://github.com/visrealm/hbc-56)**. Writing its emulator meant writing my own
**[6502](https://github.com/visrealm/vrEmu6502)** and
**[TMS9918A](https://github.com/visrealm/vrEmuTms9918)** libraries first, again for desktop and
web. Once those existed, the **[PICO-56](https://github.com/visrealm/pico-56)** was largely the
same emulator with hardware glue around it, running on a single Raspberry Pi Pico.

Then it occurred to me that emulation good enough to run a whole machine was good enough to replace
the real chip. That became the **[PICO9918](https://github.com/visrealm/pico9918)**: a drop-in VDP
replacement powered by an RP2040 or RP2350, with VGA, HDMI or SCART RGB output through swappable
dongles, and the F18A's enhanced modes. It has been tested on over 30 classic machines, and boards
are [available from my store](https://lectronz.com/stores/visrealm).

<img src="https://raw.githubusercontent.com/visrealm/visrealm/main/assets/divider.svg" width="100%" alt="">

## Hardware

| Project | What it does | ★ |
|---|---|---|
| **[pico9918](https://github.com/visrealm/pico9918)** | Drop-in TMS9918A/TMS9929A replacement on a Raspberry Pi Pico, with F18A-compatible enhanced modes and VGA, SCART RGB or HDMI output. [Hackaday](https://hackaday.io/project/196478-pico9918) | [![](https://img.shields.io/github/stars/visrealm/pico9918?style=flat-square&label=%E2%98%85&labelColor=05070a&color=21c942)](https://github.com/visrealm/pico9918/stargazers) |
| **[hbc-56](https://github.com/visrealm/hbc-56)** | Homebrew 65C02 computer on a backplane, with TMS9918A video and dual AY-3-8910 sound | [![](https://img.shields.io/github/stars/visrealm/hbc-56?style=flat-square&label=%E2%98%85&labelColor=05070a&color=21c942)](https://github.com/visrealm/hbc-56/stargazers) |
| **[pico-56](https://github.com/visrealm/pico-56)** | The HBC-56 emulated on a single Raspberry Pi Pico, with VGA and audio output | [![](https://img.shields.io/github/stars/visrealm/pico-56?style=flat-square&label=%E2%98%85&labelColor=05070a&color=21c942)](https://github.com/visrealm/pico-56/stargazers) |
| **[vrcpu](https://github.com/visrealm/vrcpu)** | Ben Eater inspired breadboard computer, with an [emulator](https://cpu.visualrealmsoftware.com) and assembler | [![](https://img.shields.io/github/stars/visrealm/vrcpu?style=flat-square&label=%E2%98%85&labelColor=05070a&color=21c942)](https://github.com/visrealm/vrcpu/stargazers) |
| **[keyboard4a99](https://github.com/visrealm/keyboard4a99)** | Cherry MX compatible upgrade for the TI-99/4A Mitsumi mylar keyboard. [Hackaday](https://hackaday.io/project/195508-keyboard4a-99) | [![](https://img.shields.io/github/stars/visrealm/keyboard4a99?style=flat-square&label=%E2%98%85&labelColor=05070a&color=21c942)](https://github.com/visrealm/keyboard4a99/stargazers) |

## Emulation libraries

All C99 with no dependencies. They build for desktop, Arduino and WebAssembly.

| Project | What it does | ★ |
|---|---|---|
| **[vrEmuTms9918](https://github.com/visrealm/vrEmuTms9918)** | TMS9918A/9928A/9929A VDP emulation. Used by the PICO9918. [Hackaday](https://hackaday.io/project/183849-tms9918-emulator-library) | [![](https://img.shields.io/github/stars/visrealm/vrEmuTms9918?style=flat-square&label=%E2%98%85&labelColor=05070a&color=43ebf6)](https://github.com/visrealm/vrEmuTms9918/stargazers) |
| **[vrEmu6502](https://github.com/visrealm/vrEmu6502)** | 6502, 65C02, R65C02, WDC65C02 and 6510 | [![](https://img.shields.io/github/stars/visrealm/vrEmu6502?style=flat-square&label=%E2%98%85&labelColor=05070a&color=43ebf6)](https://github.com/visrealm/vrEmu6502/stargazers) |
| **[vrEmuLcd](https://github.com/visrealm/vrEmuLcd)** | HD44780 character LCD, with a C99 engine and a web front-end | [![](https://img.shields.io/github/stars/visrealm/vrEmuLcd?style=flat-square&label=%E2%98%85&labelColor=05070a&color=43ebf6)](https://github.com/visrealm/vrEmuLcd/stargazers) |
| **[vrEmu6522](https://github.com/visrealm/vrEmu6522)** | 6522/65C22 VIA emulation | [![](https://img.shields.io/github/stars/visrealm/vrEmu6522?style=flat-square&label=%E2%98%85&labelColor=05070a&color=43ebf6)](https://github.com/visrealm/vrEmu6522/stargazers) |

## Retro software

| Project | What it does | ★ |
|---|---|---|
| **[retroplex](https://github.com/visrealm/retroplex)** | A Supaplex clone for retro computers with a PICO9918 | [![](https://img.shields.io/github/stars/visrealm/retroplex?style=flat-square&label=%E2%98%85&labelColor=05070a&color=c95bba)](https://github.com/visrealm/retroplex/stargazers) |
| **[cx16-supaplex](https://github.com/visrealm/cx16-supaplex)** | Supaplex for the Commander X16, in 6502 assembly | [![](https://img.shields.io/github/stars/visrealm/cx16-supaplex?style=flat-square&label=%E2%98%85&labelColor=05070a&color=c95bba)](https://github.com/visrealm/cx16-supaplex/stargazers) |
| **[retropipe](https://github.com/visrealm/retropipe)** | A Pipe Dreams clone for retro computers | [![](https://img.shields.io/github/stars/visrealm/retropipe?style=flat-square&label=%E2%98%85&labelColor=05070a&color=c95bba)](https://github.com/visrealm/retropipe/stargazers) |
| **[supaplex-tools](https://github.com/visrealm/supaplex-tools)** | Tools to work with the original Supaplex game code | [![](https://img.shields.io/github/stars/visrealm/supaplex-tools?style=flat-square&label=%E2%98%85&labelColor=05070a&color=c95bba)](https://github.com/visrealm/supaplex-tools/stargazers) |

<img src="https://raw.githubusercontent.com/visrealm/visrealm/main/assets/divider.svg" width="100%" alt="">

<p align="center">
  <img src="https://raw.githubusercontent.com/visrealm/visrealm/main/assets/stats.svg" width="100%" alt="GitHub statistics for visrealm">
</p>

## Toolchain

**Languages**

![C](https://img.shields.io/badge/C-5455ed?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-7d75fc?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-21b03c?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-d3c153?style=flat-square&logo=javascript&logoColor=05070a)

**Assembly**

![6502](https://img.shields.io/badge/6502%20%2F%2065C02-21c942?style=flat-square&labelColor=05070a)
![TMS9900](https://img.shields.io/badge/TMS9900-43ebf6?style=flat-square&labelColor=05070a)
![Z80](https://img.shields.io/badge/Z80-5edc78?style=flat-square&labelColor=05070a)
![x86](https://img.shields.io/badge/x86-e5ce80?style=flat-square&labelColor=05070a)
![ARM Thumb](https://img.shields.io/badge/ARM%20Thumb-ff7978?style=flat-square&labelColor=05070a)

**Hardware and build**

![Raspberry Pi Pico](https://img.shields.io/badge/RP2040%20%2F%20RP2350-d3524d?style=flat-square&logo=raspberrypi&logoColor=white)
![PIO](https://img.shields.io/badge/PIO-fd5554?style=flat-square&labelColor=05070a)
![CMake](https://img.shields.io/badge/CMake-21c942?style=flat-square&logo=cmake&logoColor=white)
![PCB design](https://img.shields.io/badge/PCB%20design-e5ce80?style=flat-square&labelColor=05070a)
![WebAssembly](https://img.shields.io/badge/WebAssembly-5455ed?style=flat-square&logo=webassembly&logoColor=white)
![SDL](https://img.shields.io/badge/SDL2-cccccc?style=flat-square&labelColor=05070a)

## Elsewhere

[![YouTube](https://img.shields.io/badge/YouTube-d3524d?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@TroySchrapel)
[![Hackaday](https://img.shields.io/badge/Hackaday-d3c153?style=for-the-badge&logo=hackaday&logoColor=05070a)](https://hackaday.io/visrealm)
[![Store](https://img.shields.io/badge/Buy%20a%20PICO9918-21c942?style=for-the-badge&logoColor=white)](https://lectronz.com/stores/visrealm)
[![X](https://img.shields.io/badge/@SchrapelTroy-05070a?style=for-the-badge&logo=x&logoColor=white)](https://x.com/SchrapelTroy)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-5455ed?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/troy-schrapel)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-ff7978?style=for-the-badge&logo=kofi&logoColor=white)](https://ko-fi.com/visrealm)

<img src="https://raw.githubusercontent.com/visrealm/visrealm/main/assets/divider.svg" width="100%" alt="">

<sub>
The 15 colours above are the TMS9918A palette, taken from
<a href="https://github.com/visrealm/vrEmuTms9918/blob/main/src/vrEmuTms9918Util.c">vrEmuTms9918Util.c</a>.
The banner and stats panel are generated from 5x7 pixel glyphs by the scripts in
<a href="https://github.com/visrealm/visrealm/tree/main/assets">assets/</a>.
</sub>
