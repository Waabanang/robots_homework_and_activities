# Robotics HW4
# Author: Taylor Keppler
# Computer Vision nonsense. 

import cv2
import numpy

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

vidCapture()

#----------------- Task Two ----------------
