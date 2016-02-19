from Myro import *



def scanLightSensor(totalTime):
    values = []
    for secs in timer(totalTime):   # repeats totalTime seconds
        nextValue = getLight("center")
        values.append(nextValue)
    return values
#light sensor takes four readings per second
#looks pretty consistant, varying be 1-2 units per reading

def scanLightSensorMulti(totalTime):
    values = []
    for secs in timer(totalTime):   # repeats totalTime seconds
        nextValue = (getLight("center") + getLight("left") + getLight("right"))/3
        values.append(nextValue)
    return values

def scanObstSensor(totalTime):
    values = []
    for secs in timer(totalTime):   # repeats totalTime seconds
        nextValue = getObstacle("center")
        values.append(nextValue)
    return values
#five readings per second
#there is a lot more varience, but the there is a greater range
#so that's kind of to be expected. There are 'random' spike of
#up to 1600

