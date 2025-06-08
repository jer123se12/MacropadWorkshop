import board
import usb_hid
from adafruit_debouncer import Debouncer
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import digitalio

# Initialize the pin
pin1 = digitalio.DigitalInOut(board.GP27)
# Set direction and pull
pin1.direction = digitalio.Direction.INPUT
pin1.pull = digitalio.Pull.UP
# Add the debouncer
switch1 = Debouncer(pin1)


# do the rest of the pins
pin2 = digitalio.DigitalInOut(board.GP26)
pin3 = digitalio.DigitalInOut(board.GP15)
pin2.direction = digitalio.Direction.INPUT
pin3.direction = digitalio.Direction.INPUT
pin2.pull = digitalio.Pull.UP
pin3.pull = digitalio.Pull.UP

switch2 = Debouncer(pin2)
switch3 = Debouncer(pin3)

# Initailize the keyboard
kbd = Keyboard(usb_hid.devices)

while True:
    # Update Switches
    switch1.update()
    

    # Check if switch is pressed and update accordingly
    if (switch1.rose):
        kbd.send(Keycode.LEFT_CONTROL, Keycode.C)
    
    switch2.update()
    switch3.update()
    if (switch2.rose):
        kbd.send(Keycode.LEFT_CONTROL, Keycode.V)
    if (switch3.rose):
        kbd.send(Keycode.LEFT_CONTROL, Keycode.A)
