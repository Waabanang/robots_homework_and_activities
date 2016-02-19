
from Myro import *
import PotentialFieldBrain


def keepMoving():
    """This is a very simple behavior that reports a fixed magnitude and a
    heading that matches the robot's current heading"""

    return (30.0, 0.0)


def obstBehavBuilder(whichSensor = "center", angle = 180):
    def obstacleBehavior():
        """accesses whichSensor to get which one..."""
        val = getObstacle(whichSensor)
        if val == 0:
            return (0, angle)
        elif val > 2000:
            return(100, angle)
        else:
            return (30, angle)
    return obstacleBehavior


# -----------------------------------------------------
# Run the demo using something like this:

def runDemo(time = 120):
    """This function is really a model to be modified.  It shows how to take a make
    a PotentialFieldBrain, add behaviors to the brain, and then run it for the given time."""
    # add behaviors, in order from lowest to hightest

    brain = PotentialFieldBrain.PotentialFieldBrain()
    brain.add( keepMoving )

    for t in timer(time):
        print("======================================")
        brain.step()
    brain.stopAll()

runDemo(5)

