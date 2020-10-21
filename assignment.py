#!python3 

#Step 1: Pick location for mouse to start clicking
#Step 2: click for x amount of second
#Step 3: pause for x amount of seconds
#Step 4: go to one of the choices and click it
#Step 5: pause for x amount of seconds
#Step 6: go back to clicking

import pyautogui as p
import time as t

def LofB():
    #Locate place to click
    arrowloc = p.locateCenterOnScreen("Arrow.png", grayscale=True, confidence=0.8)
    print("found arrow location")

    #Click the button
    for i in range (0,10):
        p.click(arrowloc, clicks=10, interval=0.2 )
        print(".", end=" ")
    else:
        print("button was clicked 100 times")
    
def time():
    pass

def upgrade1():
    pass
    #Locate computer upgrade
    Cloc=p.locateCenterOnScreen("ug1.png", grayscale=True, confidence=0.8)
    print("found computer upgrade")

def upgrade2():
    pass
    #Locate chair upgrade
    CHloc=p.locateCenterOnScreen("ug2.png", grayscale=True, confidence=0.8)
    print("found chair upgrade")

def upgrade3():
    pass
    #Locate desk upgrade
    Dloc=p.locateCenterOnScreen("ug3.png", grayscale=True, confidence=0.8)
    print("found desk upgrade")

def upgrade4():
    pass
    #Locate headphones upgrade
    Hloc=p.locateCenterOnScreen("ug4.png", grayscale=True, confidence=0.8)
    print("found headphones upgrade")

def upgrade5():
    pass
    #Locate wall upgrade
    Wloc=p.locateCenterOnScreen("ug5.png", grayscale=True, confidence=0.8)
    print("found wall upgrade")

def upgrade6():
    pass
    #Locate window upgrade
    WIloc=p.locateCenterOnScreen("ug6.png", grayscale=True, confidence=0.8)
    print("found window upgrade")

def upgrade7():
    pass
    #Loctae music upgrade
    Mloc=p.locateCenterOnScreen("ug7.png", grayscale=True, confidence=0.8)
    print("found music upgrade")

def upgrade8():
    pass
    #Locate furniture upgrade
    Floc=p.locateCenterOnScreen("ug8.png", grayscale=True, confidence=0.8)
    print("found furniture upgrade")

def main():
    LofB()
    
main()