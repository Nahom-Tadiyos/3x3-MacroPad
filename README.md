# FrogPad 🐸

The FrogPad is a 3x3 macropad designed for simple desk use. It functions as a customizable shortcut controller, allowing quick access to keybinds and media controls.

The macropad is powered by a Seeed XIAO RP2040 and includes a rotary encoder for volume control, making it a versatile addition to any setup. Its small form factor keeps it unobtrusive while still providing useful functionality.

I designed this project for personal use to improve my productivity and reduce repetitive keyboard actions. The green color and frog theme were chosen simply because I like frogs and wanted something unique on my desk.

## Features:

This design comes with an EC11 Rotary encoder for volume control, and 9 keyswitches with customization available. Powered by Seeed XIAO RP2040, this device will handle any shortcut or command like a pro.

##  How to Use

1. Plug the FrogPad into your computer using a USB-C cable  
2. Flash the firmware onto the Seeed XIAO RP2040  
3. Customize keybinds and macros using KMK firmware on any text editor
4. Use the macropad to trigger shortcuts, macros, or media controls  
5. Rotate the encoder to adjust volume

##  Project Files
This repository includes:
- PCB design files 
- Gerber files for manufacturing
- CAD files
- Firmware source code in python

## Full Assembly in Cad:

![Screenshot](https://i.postimg.cc/pV0PJyrs/Screenshot-2026-03-16-at-6-27-39-PM.png)

## PCB:

![Screenshot](https://i.postimg.cc/DzVv4D0n/Screenshot-2026-03-16-at-6-26-59-PM.png)

## Schematics:

![Screenshot](https://i.postimg.cc/HL5LSmR2/Screenshot-2026-03-16-at-6-25-31-PM.png)


## BOM:

| Component | Quantity | Description | Link |
|----------|--------|-------------|------|
| Seeed XIAO RP2040 | 1 | Microcontroller board | https://www.seeedstudio.com/XIAO-RP2040-p-5026.html |
| Custom PCB | 1 | 3x3 macropad PCB | Gerber files in repo |
| Cherry MX Switches | 9 | Mechanical key switches | https://www.amazon.com/dp/B0CBS25YJ1 |
| DSA Keycaps (Blank) | 9 | Keycaps for switches | https://www.amazon.com/dp/B0BWDTBF1L |
| EC11 Rotary Encoder | 1 | Rotary encoder for volume control | https://www.aliexpress.us/w/wholesale-ec11-rotary-encoder.html |
| M4 x 16mm Screws | 4 | Mounting hardware | https://www.mcmaster.com |

## Future Improvements

- Add RGB lighting
- Bluetooth support
- OLED display to display info

