import pyrosim.pyrosim as pyrosim



def Create_World():

    pyrosim.Start_SDF("world.sdf")

    length = 1
    width = 1
    height = 1

    x= 5
    y = 5
    z = 5.5

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[width,length,height])

    pyrosim.End()


def Create_Robot():

    length = 1
    width = 1
    height = 1

    #TODO: make Torso the root cube
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[width,length,height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[width,length,height])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[width,length,height])
    pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,0])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,0])
    pyrosim.End()

Create_World()
Create_Robot()
