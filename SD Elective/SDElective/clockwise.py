"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
# """
from adafruit_circuitplayground import cp
from time import sleep
 
cp.pixels.brightness = 1.0

temp = 9
while True:
    if cp.switch == True:
        cp.pixels[temp] = (200, 0, 0)
        sleep(.2)
        cp.pixels[temp] = (0,0,0)
        temp +=1
        if temp == 9:
            temp = -1
    elif cp.switch == False:
        cp.pixels[temp] = (200,0,0)
        sleep(.2)
        cp.pixels[temp] = (0,0,0)
        temp-=1
        if temp == -1:
            temp = 9