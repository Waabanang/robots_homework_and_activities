from Myro import *

def light_test():
    for i in range(3):
        print("Light value is:" , getLight(i), "at pos: ", i)
 
def bright_test():
    print("Brightness is: ", getBright())

def IR_test():
    for i in range(3):
        print("IR value is : ", getIR(i), "at pos: ", i)

def obst_test():
    for i in range(3):
        print("Distance From Obstacle is: ", getObstacle(i), "at pos: ", i)

def light_test():
    for i in range(3):
        print("Light value is: ", getLight(i), "at pos: ", i)

def master_test(n):
    for i in range(n):
        light_test()
        bright_test()
        IR_test()
        obst_test()
        light_test()
        show(takePicture('color'))