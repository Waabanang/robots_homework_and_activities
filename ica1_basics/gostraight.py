from Myro import *

START_SPEED = 0.5

def motorCalibration():
    val = raw_input("Yo, what gives?")
    leftSpeed = START_SPEED
    while val != "e":
        motors(leftSpeed, START_SPEED)
        leftSpeed = START_SPEED
        val = raw_input("Yo, what gives?")
        if val == "e":
            stop()
        else:
            leftSpeed += .01  
        print(leftSpeed)

#.54 left, .5 right is straight
motorCalibration()