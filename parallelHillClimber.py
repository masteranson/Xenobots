import solution as SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        #os.system('rm brain*.nndf')
        os.system('rm fitness*.nndf')
        self.parents= {}
        self.nextAvailableID = 0

        for i in range(0,c.populationSize):
            self.parents[i] = SOLUTION.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):

        self.Evaluate(self.parents)
        print("Im here 1")
        for currentGeneration in range(0,c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):

        self.Spawn()

        self.Mutate()

        print("Im here 2")

        self.Evaluate(self.children)

        print("Im here 3")

        self.Print()

        self.Select()

    def Spawn(self):
        self.children = {} #Instantiate children dictionary
        for i in range(0,len(self.parents)):
            self.parents[i].Set_ID()
            self.children[i] = copy.deepcopy(self.parents[i])
            self.nextAvailableID += 1

    def Mutate(self):
        for i in range(0,len(self.children)):
            self.children[i].Mutate()

    def Select(self):
        for i in range(0,len(self.parents)):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print('\n')
        for i in range(0, len(self.parents)):
            print("Parent: ", self.parents[i].fitness, " ", "Child: ", self.children[i].fitness)
        print('\n')

    def Evaluate(self, solutions):
        for i in range(0,len(solutions)):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(0,len(solutions)):
            print("Waiting for end")
            solutions[i].Wait_For_Simulation_To_End()

    def Show_Best(self):
        bestkey = 0
        bestFit = self.parents[0].fitness
        for key in range(len(self.parents)):
            if self.parents[key].fitness < bestFit:
                bestFit = self.parents[key].fitness
                bestkey = key
        self.parents[bestkey].Start_Simulation("GUI")
