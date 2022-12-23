import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        self.vectors = np.zeros(c.numLoop)
        #print(self.vectors)

    def Get_Value(self,t):
        self.vectors[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        # if t == c.numLoop - 1:
        #     print(self.vectors)

    def Save_Values(self):
        np.save('%s.npy' % self.linkName, self.vectors)
