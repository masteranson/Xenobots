import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x= 0
y = 0
z = 0.5

for i in range (0,3):

    x = x + 1
    y = 0
    height = 1
    for j in range (0, 3):

        y = y + 1
        z = 0.5
        height = 1
        for k in range (0, 10):

            height = height * 0.9

            z = z + 1

            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[width,length,height])



pyrosim.End()
