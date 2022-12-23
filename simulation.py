import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
from robot import ROBOT
from world import WORLD

class SIMULATION:

    def __init__(self): #Constructor

        self.physicsClient = p.connect(p.DIRECT)

        self.world = WORLD()
        self.robot = ROBOT()

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) #gravity
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")

    def run(self): #Run Method

        for i in range(0,c.numLoop):
            #time.sleep(1/60)
            #print(i)
            p.stepSimulation()
            ROBOT.Sense(self.robot,i)
            ROBOT.Think(self.robot)
            ROBOT.Act(self.robot, i)


    def Get_Fitness(self):
        self.robot.Get_Fitness()


    def __del__(self): #Destructor

        p.disconnect()
