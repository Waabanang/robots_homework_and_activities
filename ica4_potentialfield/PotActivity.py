from Myro import *
import PotentialFieldBrain


def wander():  
    return (30.0, pickOne(range(-90, 90, 45)))
    #change so it only goes 'forward'

def obstBehavBuilder(whichSensor = "center", angle = 180):
    def obstacleBehavior():
        """accesses whichSensor to get which one..."""
        val = getObstacle(whichSensor)
        return(100 * (val/3000), angle)
    return obstacleBehavior
    
def clearStall():
    isStalled = getStall()
    return(100 * isStalled, 180)
    
def backSensorBuilder(whichSensor = "left", angle = 90):
    def backSensor():
        isBehind = 50 if getIR(whichSensor)==0 else 0
        print(whichSensor, isBehind)
        return(isBehind, angle)
    return backSensor
    
    
def runDemo(time = 60):
    """This function is really a model to be modified.  It shows how to take a make
    a PotentialFieldBrain, add behaviors to the brain, and then run it for the given time."""
    # add behaviors, in order from lowest to hightest

    brain = PotentialFieldBrain.PotentialFieldBrain()
    brain.add( wander )
    brain.add( obstBehavBuilder() )
    brain.add( obstBehavBuilder("left", 270) )
    brain.add( obstBehavBuilder("right", 90) ) 
    brain.add( clearStall )
    brain.add( backSensorBuilder())
    brain.add( backSensorBuilder("right", 270) )

    for t in timer(time):
        print("======================================")
        brain.step()
    brain.stopAll()