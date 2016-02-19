#Scribbler Activites
#Waab Hermes, 

from Myro import *


def pace ():
    forward(0.75, 2)
    turnRight(0.75, 0.60)
    forward(0.75, 2)
    turnRight(0.75, 0.60)
def driveCircle():
    move(0.75, 0.5)
    wait(10)
    stop()
def driveSquare():
    for i in range(4):
        forward(0.75, 1)
        turnLeft(0.75, 0.2)
def randomWalk(m, n):
    for i in range(n):
        forward(0.75, m)
        turnRight(randomNumber(), 0.75)