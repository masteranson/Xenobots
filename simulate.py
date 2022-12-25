from simulation import SIMULATION
import sys
print("FUCK")
DirectOrGUI = sys.argv[1]
solutionID = sys.argv[2]
print("WTF")
simulation = SIMULATION(DirectOrGUI, solutionID)
print("Running Simulation")
SIMULATION.run(simulation)
print("Getting Fitness")
SIMULATION.Get_Fitness(simulation)
