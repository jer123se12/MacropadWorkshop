# Circuitpython
## Installing Circuitpython
1. To install circuit python, first got to [here](https://circuitpython.org/board/waveshare_rp2040_zero/) and download the `.UF2` file.
2. Plug in the macropad to the computer
3. Hold the `boot` button and press the `reset` button. a drive named `RPI-RP2` should show up on your computer
4. Copy `.UF2` file downloaded to the drive. It should automatically reset and a `CIRCUITPY` drive should show up on your computer.

## Installing Dependencies
1. Go [here](https://circuitpython.org/libraries) to download `Bundle for Version 9.X`
2. Extract the folder
3. Copy the following files from `/lib` from the extracted folder to the `/lib` in `CIRCUITPY` folder from your macropad
    - `adafruit_debouncer.mpy`
    - `adafruit_hid` (the whole folder)
    - `adafruit_ticks.mpy`


## Uploading Code
1. Copy code from `firmware/circuitpython/code.py` in github to `code.py` in `CIRCUITPY`
2. Save
3. Code should auto-reload and you can press the right-most button to test. it should press `f`
