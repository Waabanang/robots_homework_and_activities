from Myro import *
from ColorSetup import * 
#init('sim')

def motorCalibration():
    START_SPEED = 0.5
    queryString = "Yo, what gives?"
    val = raw_input(queryString)
    leftSpeed = START_SPEED
    while val != "end":
        motors(leftSpeed, START_SPEED)
        leftSpeed = START_SPEED
        val = raw_input(queryString)
        if val == "e":
            stop()
        else:
            leftSpeed += .1

def panoramaPicture():
    rotateDist = .09
    count = 0
    allPics = []
    picnum = 0
    while count < .99:
        pic = takePicture()
        allPics.append(pic)
        wait(1)
        #turnBy(rotateAngle)
        turnLeft(0.75, rotateDist)
        count += rotateDist
    for picture in allPics:
        savePicture(picture, 'picture' + str(picnum) + '.jpg')
        wait(1.5)
        picnum += 1
    return allPics
    
def atStartingLocation(thresh):
    refPic = makePicture('yellRef.jpg')
    configureBlob(refPic, 59, 56, 166, 120)
    total, meanX, meanY = getBlob()
    if total > thresh:
        return True
    else:
        return False

def atOtherLocation(thresh):
    refPic = makePicture('redRef.jpg')
    configureBlob(refPic, 74, 53, 174, 145)
    total, meanX, meanY = getBlob()
    if total > thresh:
        return True
    else:
        return False
        
def turnByAmount(n):
    n = n % 4
    if n == 0:
        turnRight(0.75, 0.17)
    if n == 1:
        turnRight(0.75, 0.62)
    if n == 2:
        turnLeft(0.75, 0.62)
    if n == 3:
        turnLeft(0.75, 0.17) 

def seekYellow():
    isHome = atStartingLocation(1000)
    while not isHome:
        turnRight(0.5, 0.1)
        isHome = atStartingLocation(1000)
    show(takePicture())
    
def helloWorld(): #but actually just hi
    turnByAmount(0)
    wait(2)
    seekYellow()
    turnByAmount(1)
    wait(2)
    seekYellow()
    turnByAmount(3)
    wait(2)
    seekYellow()
    turnByAmount(0)
    wait(2)
    seekYellow()
    turnByAmount(2)
    wait(2)
    seekYellow()
    turnByAmount(0)
    wait(2)
    seekYellow()    
    