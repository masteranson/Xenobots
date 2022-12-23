import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import os
import random

class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(3,2)*2 - 1
        self.fitness = 0

        #print(self.weights)


    def Evaluate(self):

        SOLUTION.Create_World()
        SOLUTION.Create_Body()
        SOLUTION.Create_Brain(self.weights)
        os.system("python3 simulate.py")
        f = open("fitness.txt", "r")
        self.fitness = float(f.readline())
        f.close()

    def Create_World():

        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[5,5,5.5] , size=[c.width,c.length,c.height])
        pyrosim.End()


    def Create_Body():

        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[c.width,c.length,c.height])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[c.width,c.length,c.height])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[c.width,c.length,c.height])
        pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,0])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,0])
        pyrosim.End()

    def Create_Brain(weights):

        pyrosim.Start_NeuralNetwork("brain.nndf")

        for i in range(0,2):

            pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
            pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
            pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

            for j in range(3,4):
                pyrosim.Send_Motor_Neuron( name = 3 , jointName = "BackLeg_Torso")
                pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

                pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = weights[i][j-3])
        #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)

        self.weights[randomRow][randomColumn] = random.random()*2 - 1
