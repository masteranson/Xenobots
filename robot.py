from sensor import SENSOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
from motor import MOTOR



class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.sensors = dict()
        self.motors = dict()
        self.robotId = p.loadURDF("body.urdf") #robot
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("rm "+"brain"+str(solutionID)+".nndf") #to avoid too many files

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

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self,desiredAngle * c.motorJointRange)
                #print(neuronName, jointName)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):

        self.sensors["FrontLowerLeg"].Save_Values()
        self.sensors["BackLowerLeg"].Save_Values()
        self.sensors["LeftLowerLeg"].Save_Values()
        self.sensors["RightLowerLeg"].Save_Values()

        FrontLowerLegVal = np.load('FrontLowerLeg.npy')
        BackLowerLegVal = np.load('BackLowerLeg.npy')
        LeftLowerLegVal = np.load('LeftLowerLeg.npy')
        RightLowerLegVal = np.load('RightLowerLeg.npy')

        LegVal  = [FrontLowerLegVal, BackLowerLegVal, LeftLowerLegVal, RightLowerLegVal]

        # Combining all four into vectors

        meanVal = np.mean(LegVal, axis = 0)
        condition = meanVal == 0

        val = np.diff(np.where(np.concatenate(([condition[0]],
                                     condition[:-1] != condition[1:],
                                     [True])))[0])[::2]

        meanVal = val[0]

        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(meanVal) + "\n")
        f.close()
        os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
