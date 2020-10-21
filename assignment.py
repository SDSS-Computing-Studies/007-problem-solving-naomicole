#!python3 

#Step 1: Pick location for mouse to start clicking
#Step 2: click for x amount of second
#Step 3: pause for x amount of seconds
#Step 4: go to one of the choices and click it
#Step 5: pause for x amount of seconds
#Step 6: go back to clicking

import pyautogui as p
import time as t

def LocofButton():
    #Locate place to click
    arrowloc = p.locateCenterOnScreen("Arrow.png", grayscale=True, confidence=0.8)
    print("found arrow location")

    #Click the button
    p.click(arrowloc, clicks=10, interval=0.2 )
    
LocofButton()

    