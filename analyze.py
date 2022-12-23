import matplotlib.pyplot as matplotlib
import numpy as np

dataBack = np.load('dataBack.npy')
dataFront = np.load('dataFront.npy')

matplotlib.plot(dataBack,linewidth=4)
matplotlib.plot(dataFront)
matplotlib.legend(['Back Leg', 'Front Leg'])
matplotlib.show()
