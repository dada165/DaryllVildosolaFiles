"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
from adafruit_clue import time # I import time so that i can use sleep function in block of code below

clue_data = clue.simple_text_display(title="Message Streamer", text_scale=2, title_color=clue.RED) # This is a title, then I make the all text size to 2 and then I colored the title to Red.
firsttext = "This message moves from right to left" # I make a string of word "This message move from right to left" and then store it on a variable firsttext.
secondtext = "This message moves from left to right" # I make a string of word "This message move from left to right" and then store it on a variable secondtext.
thirdtext = "This message blinks" # I make a string of word "This message blinks" and then store it on a variable thirdtext.
while True: # While the statement is true, the block of codes will continue to execute forever.
    #Putting a text on index[1]
    clue_data[1].text = firsttext # On index[1] in clue_data, I store my variable firstext.
    removetext = firsttext[0:1] #I make a variable removetext then I put the value of firsttext to it. The value of this variable is now "T".
    firsttext = firsttext[1:]+removetext # So in these line the value of the firsttext is now " his message moves from right to leftT " because I add the value of the variable removetext to the end of the value of the new firsttext. 
    clue_data[1].color = clue.YELLOW #This area indicate the color of the firsttext
    #Putting a text on index[3]
    clue_data[3].text = secondtext # On index[3] in clue_data, I store my variable secondtext.
    addtext = secondtext[:-1] #I make a variable addtext then I put the value of secondtext to it. The value of this variable is now "This message moves from left to righ".
    secondtext = secondtext[-1]+addtext  # So in these line the value of the secondtext is now " tThis message moves from left to right " because I add the value of the variable addtext to the first index of the value of the new secondtext. 
    clue_data[3].color = clue.WHITE #This area indicate the color of the secondtext
    #Putting a text on index[5]
    clue_data[5].text = thirdtext # On index[5] in clue_data, I store my variable thirdtext. 
    clue_data[5].color = clue.SKY  #This area indicate the color of the thirdtext
    time.sleep(.3) #This code make the thirdtext disappear in 0.3 seconds
    clue_data[5].color = clue.BLACK # When the third text appear again in index[5] in clue_data the color of it is black
    clue_data.show() #Of course the show function is always there so that in every execution is made it will always display the result
   
