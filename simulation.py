import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
from robot import ROBOT
from world import WORLD

class SIMULATION:

    def __init__(self): #Constructor

        self.physicsClient = p.connect(p.GUI)

        self.world = WORLD()
        self.robot = ROBOT()

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) #gravity
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")

    def run(self): #Run Method

        for i in range(0,c.numLoop):
            #time.sleep(1/60)
            print(i)
            p.stepSimulation()
            ROBOT.Sense(self.robot,i)
            ROBOT.Act(self.robot, i)
            # print(pyrosim.Get_Touch_Sensor_Value_For_Link("Torso"))
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #
            # pyrosim.Set_Motor_For_Joint(
            #
            # bodyIndex = robotId,
            #
            # jointName = "BackLeg_Torso",
            #
            # controlMode = p.POSITION_CONTROL,
            #
            # targetPosition =  c.amplitude * np.sin(c.frequency * i + c.phaseOffset),
            #
            # maxForce = c.motorMaxForce)
            #
            # pyrosim.Set_Motor_For_Joint(
            #
            # bodyIndex = robotId,
            #
            # jointName = "Torso_FrontLeg",
            #
            # controlMode = p.POSITION_CONTROL,
            #
            # targetPosition =  c.amplitude * np.sin(c.frequency * i + c.phaseOffset),
            #
            # maxForce = c.motorMaxForce)

    def __del__(self): #Destructor

        p.disconnect()
