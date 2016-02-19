from Myro import *

def isWallClose():
    close = 700
    obs = getObstacle()
    pos = reduce(lambda x, y: x+y, obs) / len(obs)
    print(pos)
    if pos >= close:
        return True
    else:
        return False

def findWall():  
    is_close = False     
    while not (is_close):
        motors(0.79, 0.75)
        wait(0.7)
        stop()
        is_close = isWallClose()  
    turnRight(0.75, 0.72)
    keep_going = raw_input("Keep going? y/N")
    if (keep_going == "y"):
        findWall()
       