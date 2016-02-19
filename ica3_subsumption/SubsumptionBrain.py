""" -------------------------------------------------------------------
File: SubsumptionBrain.py
Author: Susan Fox
Date: March 2014

This file contains classes that implement the subsumption architecture for use with the Scribbler robots. The
main class it the SubsumptionBrain, which keeps a set of behaviors and manages their recommendations. There
is also a SubsumptionBehavior class, which can be used by the SubsumptionBrain to manage behaviors that
the programmer wants."""

from Myro import *
import random

# ---------------------------------------------------------------------
# First, the SubsumptionBrain class.  


class SubsumptionBrain:
    """A class that implements the Subsumption reactive architecture. It
    keeps a list of behavior objects. The higher the index in the list, the
    more important the behavior is. Wander, as the most basic behavior, will
    be in position 0. The brain includes methods for adding behaviors to the
    list. It then has a step method, which runs one cycle of sensor to action,
    and a run method that just repeats the step."""
    
    def __init__(self):
        """set up the Brain with an empty list of behaviors, and attach
        the robot that this brain is controlling."""
        self.behaviors = []
        

    def add(self, behavior):
        """Takes a behavior object as input, and initializes it, and
        adds it to the list"""
        self.behaviors.append( behavior )

    def run(self, numSteps):
        """Takes in a number of steps, and runs the that many cycles"""
        for i in range(numSteps):
            self.step()
        stop()

    def stopAll(self):
        """Stops the robot from moving, and could shut down anything else that was requried"""
        stop()

    
    def step(self):
        """Runs one cycle/step of the reactive actions. It figures out the
        highest-level behavior that is currently applicable, and takes its
        recommendation for motor values"""
        (translate, rotate, behavName) = self._updateBehaviors()
        controlTemplate = "{0:s} is in control"
        print (controlTemplate.format(behavName))
        move(translate, rotate)


    def _updateBehaviors(self):
        """A private helper method that determines the highest applicable
        behavior, and returns it, in the process updating all the higher
        behaviors. Note that lower behaviors aren't updated at all."""

        # starting at the end and working backwards,
        for b in range(len(self.behaviors) - 1, -1, -1):
            behav = self.behaviors[b]
            resp = behav()
            # If the behavior fired, then return its response
            if resp != None:
                return (resp[0], resp[1], behav.__name__)
        return (0, 0, "None")  # if all else fails, stop the robot

# end of SubsumptionBrain Class



