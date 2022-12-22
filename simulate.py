import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8) #gravity
planeId = p.loadURDF("plane.urdf") #floor
p.loadSDF("boxes.sdf")
for i in range(0,6000):
    time.sleep(1/60)
    p.stepSimulation()
    print(i)

p.disconnect()
