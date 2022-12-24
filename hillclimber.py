import solution as SOLUTION
import constants as c
import copy

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION.SOLUTION()


    def Evolve(self):
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):

        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

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
            solutions[i].Wait_For_Simulation_To_End()


    def Show_Best(self):
        bestkey = 0
        bestFit = self.parents[0].fitness
        for key in range(len(self.parents)):
            if self.parents[key].fitness < bestFit:
                bestFit = self.parents[key].fitness
                bestkey = key
        self.parents[bestkey].Start_Simulation("GUI")
