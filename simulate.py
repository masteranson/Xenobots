# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import time
# import numpy as np
# import random
# import constants as c
from simulation import SIMULATION


simulation = SIMULATION()
SIMULATION.run(simulation)


# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8) #gravity
#
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf") #robot
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
#
# backLegSensorValues = np.zeros(c.numLoop)
# frontLegSensorValues = np.zeros(c.numLoop)
#
# for i in range(0,c.numLoop):
#     #time.sleep(1/60)
#     p.stepSimulation()
#     print(pyrosim.Get_Touch_Sensor_Value_For_Link("Torso"))
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#
#     pyrosim.Set_Motor_For_Joint(
#
#     bodyIndex = robotId,
#
#     jointName = "BackLeg_Torso",
#
#     controlMode = p.POSITION_CONTROL,
#
#     targetPosition =  c.amplitude * np.sin(c.frequency * i + c.phaseOffset),
#
#     maxForce = c.motorMaxForce)
#
#     pyrosim.Set_Motor_For_Joint(
#
#     bodyIndex = robotId,
#
#     jointName = "Torso_FrontLeg",
#
#     controlMode = p.POSITION_CONTROL,
#
#     targetPosition =  c.amplitude * np.sin(c.frequency * i + c.phaseOffset),
#
#     maxForce = c.motorMaxForce)
#
#
#
# p.disconnect()
#
# np.save('dataBack.npy',backLegSensorValues)
# np.save('dataFront.npy',frontLegSensorValues)
