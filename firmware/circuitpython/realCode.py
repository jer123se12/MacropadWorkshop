import board
import usb_hid
from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import digitalio

# get the pins
pin1 = digitalio.DigitalInOut(board.GP27)
pin2 = digitalio.DigitalInOut(board.GP26)
pin3 = digitalio.DigitalInOut(board.GP15)

# set their setting
pin1.direction = digitalio.Direction.INPUT
pin2.direction = digitalio.Direction.INPUT
pin3.direction = digitalio.Direction.INPUT

# add debouncer
switch1 = Debouncer(pin1)
switch2 = Debouncer(pin2)
switch3 = Debouncer(pin3)

kbd = Keyboard(usb_hid.devices)

while True:
    # Update Switches
    switch1.update()
    switch2.update()
    switch3.update()

    # Check if switch is pressed and update accordingly
    if (switch1.rose):
        kbd.send(Keycode.LEFT_CONTROL, Keycode.C)
    if (switch2.rose):
        kbd.send(Keycode.LEFT_CONTROL, Keycode.V)
    if (switch3.rose):
        kbd.send(Keycode.LEFT_CONTROL, Keycode.A)
