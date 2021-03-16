"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep
values = [[0,0],[1,0],[2,0],[3,0],[4,0], # I put the pattern in a multidimensional array, then arrange the values in spiral like pattern so that it will be easy.
        [4,1],[4,2],[4,3],[4,4],[3,4],
        [2,4],[1,4],[0,4],[0,3],[0,2],
        [0,1],[1,1],[2,1],[3,1],[3,2],
        [3,3],[2,3],[1,3],[1,2],[2,2]
       ]
count = len(values) # I put the lenght of my variable values in the count variable
counter = 0  # I make a variable counter to count the length of the values     
while True: # While the statement is true it will not stop
    while counter < count: # I put a condition here that while my counter variable is less than the length of the values variable
        display.set_pixel(values[counter][0],values[counter][1],9) # I make the first value of my pattern light in a brightness of 9
        sleep(0.3) # If the line above is executed the light will sleep in 0.3 seconds
        display.set_pixel(values[counter][0],values[counter][1],0) # Then I make first value of my pattern turn to 0 means no light
        counter+=1 # Then my counter will iterates until the end of my pattern
    counter = 0 # If my counter is equal to the length of my values then my counter value is back to zero then it will the while condition will execute again 
           
    
