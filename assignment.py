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
    while True:
        arrowloc = p.locateCenterOnScreen("Arrow.png", grayscale=True, confidence=0.5)
        print(arrowloc)
        if (arrowloc != None):
            break
    print("found arrow location")

    #Click the button
    
    for i in range (0,10):
        p.click(arrowloc, clicks=10, interval=0.12 )
        print(".", end=" ")
    else:
        print("button was clicked 100 times")
    
def upgrade1():
    #Locate computer upgrade
    Cloc=p.locateCenterOnScreen("ug1.png", grayscale=True, confidence=0.65)
    print("found computer upgrade")
    #Click on upgrade
    for i in range (0,4):
        p.click(Cloc)
    print("upgraded computer")
    
def upgrade2():
    #Locate chair upgrade
    CHloc=p.locateCenterOnScreen("ug2.png", grayscale=True, confidence=0.65)
    print("found chair upgrade")
    #Click on upgrade
    for i in range (0,3):
        p.click(CHloc)
    print("upgraded chair")

def upgrade3():
    #Locate desk upgrade
    Dloc=p.locateCenterOnScreen("up3.png", grayscale=True, confidence=0.65)
    print("found desk upgrade")
    #Click on upgrade
    for i in range (0,3):
        p.click(Dloc)
    print("upgraded desk")

def upgrade4():
    #Locate headphones upgrade
    Hloc=p.locateCenterOnScreen("up4.png", grayscale=True, confidence=0.65)
    print("found headphones upgrade")
    #Click on upgrade
    for i in range (0,3):
        p.click(Hloc)
    print("upgraded headphones")

def upgrade5():
    #Locate wall upgrade
    Wloc=p.locateCenterOnScreen("ug5.png", grayscale=True, confidence=0.65)
    print("found wall upgrade")
    #Click on upgrade
    for i in range (0,2):
        p.click(Wloc)
    print("upgraded walls")

def upgrade6():
    #Locate window upgrade
    WIloc=p.locateCenterOnScreen("ug6.png", grayscale=True, confidence=0.65)
    print("found window upgrade")
    #Click on upgrade
    for i in range (0,2):
        p.click(WIloc)
    print("upgraded window")

def upgrade7():
    #Loctae music upgrade
    Mloc=p.locateCenterOnScreen("ug7.png", grayscale=True, confidence=0.65)
    print("found music upgrade")
    #Click on upgrade
    for i in range (0,2):
        p.click(Mloc)
    print("upgraded music")

def upgrade8():
    #Locate furniture upgrade
    Floc=p.locateCenterOnScreen("ug8.png", grayscale=True, confidence=0.65)
    print("found furniture upgrade")
    #Click on upgrade
    for i in range (0,2):
        p.click(Floc)
    print("upgraded furniture")

def upgrades():
    #run through all upgrades
    upgrade8()
    t.sleep(0.5)
    upgrade7()
    t.sleep(0.5)
    upgrade6()
    t.sleep(0.5)
    upgrade5()
    t.sleep(0.5)
    upgrade4()
    t.sleep(0.5)
    upgrade3()
    t.sleep(0.5)
    upgrade2()
    t.sleep(0.5)
    upgrade1()

def main():
    
    while True:
        LofB()
        t.sleep(2)
        upgrades()
        t.sleep(2)
       
main()