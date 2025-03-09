import board
import usb_hid
from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import digitalio

keys = [board.GP27, board.GP26, board.GP15]
keycodes = [
        [Keycode.LEFT_CONTROL, Keycode.C],
        [Keycode.LEFT_CONTROL, Keycode.V],
        [Keycode.F]
        ]

kbd = Keyboard(usb_hid.devices)
pins = [digitalio.DigitalInOut(i) for i in keys]
for pin in pins:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
switches = [Debouncer(i) for i in pins]

while True:
    i = 0
    for switch in switches:
        switch.update()
        if switch.rose:
            kbd.send(*keycodes[i])
        i += 1
