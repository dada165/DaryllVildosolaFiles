"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

import time
from adafruit_circuitplayground import cp
while True:
    #TINAMBAN PAGKABUHAT SIR
    # if(cp.light< 32):
    #    cp.pixels[0] = (cp.light, 0, cp.light)
    # elif(cp.light<64 ):
    #     cp.pixels[1] = (cp.light-32, 0, cp.light-32)
    # elif(cp.light < 96 ):
    #     cp.pixels[2] = (cp.light-64, 0, cp.light-64)
    # elif(cp.light < 128 ):
    #     cp.pixels[3] = (cp.light-96, 0, cp.light-96)
    # elif(cp.light < 160 ):
    #     cp.pixels[4] = (cp.light-128, 0, cp.light-128)
    # elif(cp.light < 192 ):
    #     cp.pixels[5] = (cp.light-160, 0, cp.light-160)
    # elif(cp.light < 224 ):
    #     cp.pixels[6] = (cp.light-192, 0, cp.light-192)
    # elif(cp.light < 256 ):
    #     cp.pixels[7] = (cp.light-224, 0, cp.light-224)
    # elif(cp.light < 288 ):
    #     cp.pixels[8] = (cp.light-256, 0, cp.light-256)
    # elif(cp.light < 320 ):
    #     cp.pixels[9] = (cp.light-288, 0, cp.light-288)
    
  
    brightness = cp.light # make a variable name light that stores the value of the light sensor
    if brightness % 32 == 0 and brightness != 0: # condition
        brightness = brightness -1  # subtract 1 to the value of the light sensor
    index = brightness // 32  # make another variable name index that stores the value of light floor division by 32
    if brightness > 32:      # condition
        brightness = brightness - (index * 32)  # light will subtracted by the value of index multiplied by 32
    for i in range  (0, 10): # loop
        if i == index: # condition
            color = int (255 * brightness / 32) # if TRUE, the color is get by 255 multiplied by the value of light divided by 32 then return into an integer since the result of it is float/ double
            cp.pixels [i] = (0, 0, color) # set the color of the pixels into above color
        elif i < index:  # condition
            cp.pixels [i] = (21,247 , 232) # if i is less than index, set the color of the pixels into yellow
        else: # if the condition is FALSE
            cp.pixels[i] = (0, 0, 0) # set the color of the pixels into default

