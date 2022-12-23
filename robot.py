
from sensor import SENSOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR


class ROBOT:

    def __init__(self):

        self.sensors = dict()
        self.motors = dict()
        self.robotId = p.loadURDF("body.urdf") #robot

        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)

    def Prepare_To_Sense(self):

        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)

    def Prepare_To_Act(self):

        for jointName in pyrosim.jointNamesToIndices:
            #print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):

        for jointName in pyrosim.jointNamesToIndices:
            #print(self.motors[jointName])
            self.motors[jointName].Set_Value(self,t)
