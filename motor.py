import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName;
        self.motorValues = np.zeros(c.numLoop);
        self.amplitude = 1;
        self.frequency = 1;
        self.offset = 0;
        MOTOR.Prepare_To_Act(self)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude;

        if (self.jointName == "Torso_FrontLeg"):
            self.frequency = c.frequency / 2
        else:
            self.frequency = c.frequency

        self.offset = c.phaseOffset;


    def Set_Value(self, robot, desiredAngle):

        #self.motorValues[t] = self.amplitude * np.sin(self.frequency * t + self.offset)

        pyrosim.Set_Motor_For_Joint(

        bodyIndex = robot.robotId,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,

        targetPosition =  desiredAngle,

        maxForce = c.motorMaxForce)

    def Save_Values(self):
        p.save('%s.npy' % self.linkName, self.motorValues)
