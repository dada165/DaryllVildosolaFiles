"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep
while True: 
    count = 0 #This is the variable for x indexes
    while count<=4: #This condition checks the index of x is less than 4 before the block will execute
        dot = 0 #This the variable for y indexes
        while dot <= 4: #This condition checks if the index of y is less than 4 before the block of code below executes
            display.set_pixel(dot,count,9) #This line display the pixels light with the corresponding brightness of 8
            sleep(0.5) #This line indicates the sleep time of every indexes after iteration of y indexes
            display.set_pixel(dot,count,0) #This line indicates the pixel light with the corresponding brightness of 0 means no light
            dot+=1 #This line iterates the index of of y 
        count+=1 #This line iterates the index of x indexes after executing the code block above