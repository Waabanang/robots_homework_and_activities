# Robotics HW4
# Author: Taylor Keppler
# Computer Vision nonsense. 

import cv2
import numpy
import copy

#------------- Task One: Motion Tracking ----------------
# from video capture, determine areas of movement
# quality of program varies widely with qaulity of light in vidCam area

def vidCapture():
    vidCap = cv2.VideoCapture(0)
    ret, practiceImg = vidCap.read()
    h, w, c = practiceImg.shape
    stopBool = True
    img1 =  numpy.zeros((h, w, 3), numpy.uint8)
    
    while stopBool:
        blank = numpy.zeros((h, w, 1), numpy.uint8)
        img2 = img1
        ret, img1 = vidCap.read()
        subtraction = findMovement(img1, img2)
        contours = cv2.findContours(subtraction, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(contours) > 0:
            c = max(contours, key = cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            if radius > 30:
                cv2.circle(img1, (int(x),int(y)), int(radius), (0,0,255))
        cv2.imshow("subtract", img1)
        #cv2.imshow("blank", blank)
        quit = cv2.waitKey(1)
        if (quit > -1) and (chr(quit) == 'q'):
            stopBool = False

    cv2.destroyAllWindows()
    vidCap.release()
    return

def findMovement(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    newImg = cv2.subtract(gray1, gray2)
    newImg = cv2.blur(newImg, (30,30))
    cv2.threshold(newImg, 5, 255, cv2.THRESH_BINARY, newImg)
    #newImg = cv2.adaptiveThreshold(newImg, 150, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 201, -11)
    # use 90, 200 in good light
    #newImg = cv2.Canny(newImg, 90,200) #newImg, 90,200)
    return newImg

# vidCapture()

#----------------- Task Two ----------------
'''
A = cv2.imread("Apic.jpg")
cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
B = cv2.imread("Bpic.jpg")
cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)
C = cv2.imread("Cpic.jpg")
cv2.cvtColor(C, cv2.COLOR_BGR2GRAY)
'''


def vidCapture2():
    vidCap = cv2.VideoCapture(0)
    ret, practiceImg = vidCap.read()
    h, w, c = practiceImg.shape
    stopBool = True
    countList = []
    font = cv2.FONT_HERSHEY_DUPLEX
    while stopBool:
        ret, img1 = vidCap.read()
        rectArray = findBox(img1)
        xStep = 10
        for x, y, w, h in rectArray:
            crop, color = examineBox((x, y, w, h), img1)
            crop, count = identifyLetter(crop)
            countList.append(count)
            if len(countList) >= 5:
                writeStr = ''
                avg = int(sum(countList) / len(countList))
                if avg == 0:
                    writeStr = 'C'
                elif avg == 2:
                    writeStr = 'A'
                elif avg == 3:
                    writeStr = 'B'
                if writeStr != '':
                    cv2.putText(img1, writeStr, (xStep, h - 20), font, 3, (255, 255, 255), thickness=3)
                    xStep += 30
                countList.pop(0)
            cv2.imshow("crop", crop)
            cv2.rectangle(img1, (x,y), (x+w, y+h), color, 2)
        cv2.imshow("img", img1)
        quit = cv2.waitKey(1)
        if (quit > -1) and (chr(quit) == 'q'):
            stopBool = False
    cv2.destroyAllWindows()
    vidCap.release()
    return

def findBox(img):
    rectArray = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    white = copy.copy(gray)
    white.fill(255)
    blur = cv2.blur(gray, (3, 3))
    subtract = cv2.subtract(white, blur)
    cv2.threshold(subtract, 40, 255, cv2.THRESH_BINARY_INV, subtract)
    contours = cv2.findContours(subtract, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for contour in contours:
        rect = cv2.boundingRect(contour)
        if rect[2] > 90 and rect[3] > 90:
            rectArray.append(rect)
    return rectArray

def examineBox(rect, img):
    x, y, w, h = rect
    crop = img[y:(y+h), x:(x+w)]
    colors = cv2.split(crop)
    for color in colors:
        cv2.threshold(color, 100, 255, cv2.THRESH_BINARY_INV, color)
    bestIndex = 0
    bestVal = float("inf")
    for i in range(len(colors)):
        currVal = numpy.sum(colors[i])
        if currVal < bestVal:
            bestIndex = i
            bestVal = currVal
    color = [0, 0, 0]
    color[bestIndex] = 255

    return crop, tuple(color)

def identifyLetter(crop):
    crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    cv2.threshold(crop, 150, 255, cv2.THRESH_BINARY, crop)
    crop = cv2.Canny(crop, 150, 225)
    image, contours, hierarchy = cv2.findContours(crop, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(crop, contours, 0, (0, 255, 0), 2)
    count = 0
    if hierarchy != None:
        for item in hierarchy[0]:
            if item[2] > 0:
                count+= 1
    return crop, count


vidCapture2()