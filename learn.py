import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sketch3D
import texture

mtexture = sketch3D.sketch()

print 'I m here'
mtexture.learn()

for i in range(3):
	sketch3D.sketch(mtexture.sample())


