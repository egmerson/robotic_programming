# Universidade Federal de Pernambuco
# ME653 Programacao Robotica
# 2021.1

from random import randrange
from plotlib_original import plotRealEnv, plotRobEnv, plotPlanningMap

class envClass:

    def __init__(...):
        self.nbRow =
        self.nbCol =
        self.map =

    def addObstacle(...):
        pass


class robotClass:

    def __init__(...):
        self.nbRow =
        self.nbCol =
        self.row =
        self.col =
        self.map =
        self.sensorRange =
        self.path =

    def setGoal(...):

    def updateMap(...):

    def pathPlanner(...):

        # To plot grid filled with numbers:
        # func: plotPlanningMap(arg1. arg2, arg3)
        # arg1: matrix object representing the grid filled with values
        # arg2: number of row
        # arg3: number of col

    def move(...):



#----------------------------------------------


# MAIN FUNCTION

# To plot the real environment with the robot position
# func: plotRealEnv(arg1,arg2)
# arg1: object type envClass
# arg2: object type robotClass

# To plot the environment known by the robot and the computed path
# func: plotRobEnv(arg1)
# arg1: object type robotClass