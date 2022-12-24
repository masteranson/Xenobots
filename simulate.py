from simulation import SIMULATION
import sys

DirectOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(DirectOrGUI, solutionID)
SIMULATION.run(simulation)
SIMULATION.Get_Fitness(simulation)
