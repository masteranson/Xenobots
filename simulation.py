import pybullet as p
import pybullet_data
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

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) #gravity
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")

    def run(self): #Run Method

        for i in range(0,c.numLoop):

            #print(i)
            p.stepSimulation()

            if self.directOrGUI == p.GUI:
                time.sleep(1/600)

            ROBOT.Sense(self.robot,i)
            ROBOT.Think(self.robot)
            ROBOT.Act(self.robot, i)


    def Get_Fitness(self):
        self.robot.Get_Fitness()


    def __del__(self): #Destructor

        p.disconnect()
