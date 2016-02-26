import cv2
import os
import numpy

def showImages():
	img1 = cv2.imread("TestImages/SnowLeo1.jpg")
	cv2.imshow("Leopard 1", img1)
	img2 = cv2.imread("TestImages/SnowLeo2.jpg")
	cv2.imshow("Leopard 2", img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def oneAtATime():
	for filename in os.listdir(os.getcwd() + "/TestImages"):
		if ".jpg" in filename:
			img = cv2.imread("TestImages/" + filename)
			cv2.imshow("Current", img)
			cv2.waitKey(0)
			cv2.destroyWindow("Current")
			
def drawWithNumpy():
	draw1 = numpy.zeros((300, 500, 3), numpy.uint8)
	draw2 = 255 * numpy.ones((500, 300, 3), numpy.uint8)

	cv2.line(draw2, (50, 50), (150, 250), (0, 0, 255))
	cv2.rectangle(draw1, (10, 100), (100, 10), (0, 180, 0), -1)
	cv2.circle(draw2, (30, 30), 30, (220, 0, 0), -1)
	cv2.ellipse(draw1, (250, 150), (100, 60), 30, 0, 220, (250, 180, 110), -1)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(draw1, "Hi, there", (10, 270), font, 1, (255, 255, 255))

	cv2.imshow("Black", draw1)
	cv2.imshow("White", draw2)

	cv2.imwrite("blackPic.jpg", draw1)
	cv2.imwrite("whitePic.jpg", draw2)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

def leopardMarkUp():
	img = cv2.imread("TestImages/SnowLeo2.jpg")
	cv2.circle(img, (145, 130), 80, (0, 180, 200), 0) 
	cv2.rectangle(img, (185, 136), (560,293), (0, 180, 0), 0)
	cv2.line(img, (557, 137), (598, 273), (0,0,255))
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, "SnowLeo2.jpg", (10, 30), font, 1, (255, 255, 255))
	cv2.imshow("Leopard 2", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def playingWithCam():
	vidCap = cv2.VideoCapture(0)
	x = -1
	while x < 0:
	    ret, img = vidCap.read()
	    cv2.imshow("Webcam", img)
	    x = cv2.waitKey(10)

	cv2.destroyAllWindows()
	vidCap.release()


playingWithCam()
