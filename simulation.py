import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import time
from robot import ROBOT
from world import WORLD

class SIMULATION:

    def __init__(self, mode, solutionID): #Constructor

        self.solutionID = solutionID
        self.directOrGUI = mode #p.GUI or p.DIRECT

        if mode =="GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.DIRECT)


        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)


    def run(self): #Run Method

        for i in range(0,c.numLoop):

            #print(i)
            p.stepSimulation()

            if self.directOrGUI == p.GUI:
                time.sleep(1/600)

            ROBOT.Sense(self.robot,i)
            ROBOT.Think(self.robot)
            ROBOT.Act(self.robot, i)

        print("Finish Running")

    def Get_Fitness(self):
        self.robot.Get_Fitness()


    def __del__(self): #Destructor

        p.disconnect()
