import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(0,4):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

phc = PARALLEL_HILL_CLIMBER()
#phc.parents.Evaluate()
phc.Evolve()

phc.Show_Best()
print("DONE DONE DONE DONE DONE DONE DONE DONE")
