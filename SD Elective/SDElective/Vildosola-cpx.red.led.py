"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""


from adafruit_circuitplayground import cp
from time import sleep
if (CircuitPlayground.slideSwitch()==False):
    cp.pixels[9] = (0,255,0)
    e
    # sleep(1)
    # cp.red_led = False
    # sleep(1)
# import time
 
# import board
# import neopixel

# pixpin = board.A3
# numpix = 128

# strip = neopixel.NeoPixel(pixpin, numpix, brightness=1.0, auto_write=False)
# # strip = []
# while CircuitPlayground.slideSwitch(True):

#     # set brightness to a high value.  1.0 is the maximum value, 0.0 is the lowest

    
#     strip[9] = (50,50,0)
#     sleep(1)
#     strip[8] = (50,50,0)
#     sleep(1)
#     strip[7] = (50,50,0)
#     sleep(1)
#     strip[6] = (50,50,0)
#     sleep(1)
#     strip[5] = (50,50,0)
#     sleep(1)
#     strip[4] = (50,50,0)
#     sleep(1)
#     strip[3] = (50,50,0)
#     sleep(1)
#     strip[2] = (50,50,0)
#     sleep(1)
#     strip[1] = (50,50,0)
#     sleep(1)
#     strip[0] = (50,50,0)
#     strip.write()
#     if CircuitPlayground.slideSwitch(True):
#         s


# from adafruit_circuitplayground.express import cpx
# import board
# import neopixel
# import random
# import time
# import pulseio
# import array

# pulseIn = pulseio.PulseIn(board.IR_RX, maxlen=59, idle_state=True)
# pulseIn.clear()
# pulseIn.resume()