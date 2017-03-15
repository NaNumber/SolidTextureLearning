import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sketch
import texture

mtexture = sketch.sketch()

mtexture.learn()

for i in range(3):
	sketch.paint(mtexture.sample())


