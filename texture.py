import rock
import numpy as np 
from sklearn.neighbors.kde import KernelDensity
import math


'''
2D Texture.

self.rocks: list of rock.Rock
self.data: a minimized version of self.rocks
'''
class Texture:
	def __init__(self):
		self.rocks = []
		self.data = []

	'''
	add a rock to the texture if the rock doesn't any rock in self.rocks 
	returns bool
	'''
	def add(self, rock):
		if not self.intersect(rock):
			self.rocks.append(rock)
			self.data.append(rock.data())
			return True
		return False

	'''
	Create the tree for the kernelDensity
	'''
	def learn(self):
		self.kde = KernelDensity(kernel='gaussian', bandwidth=0.02).fit(self.data)

	'''
	samples rocks from kde one by one making sure there are no intersection
	returns a Texture
	'''
	def sample(self, n_rocks=None):
		length = n_rocks
		if length == None:
			length = len(self.data)

		mtexture = Texture()
		i=0
		while i < length:
			new_rock = rock.dataToRock(self.kde.sample(1, random_state=None)[0])

			if mtexture.add(new_rock):
				i = i+1

		return mtexture

	'''
	compute the distance between two points
	return float
	'''
	def __distance(self, center1, center2):
		center1 = np.array(center1)
		center2 = np.array(center2)

		sub = center1 - center2
		sub = sub**2

		return math.sqrt(np.sum(sub))

	'''
	Test if two rocks intersect. 
	returns bool
	'''
	def __intersect(self, rock1, rock2):
		return self.__distance(rock1.center, rock2.center) < rock1.radius + rock2.radius

	'''
	Test if a rock intersects another rock in self.rocks
	'''
	def intersect(self, rock):
		for r in self.rocks:
			if self.__intersect(rock, r):
				return True
		return False


'''
3D Texture.

self.rocks: list of rock.Rock
self.data: a minimized version of self.rocks
self.size: the size of the texture
'''
class Texture3D:
	def __init__(self, size):
		self.rocks = []
		self.size = size
		self.data = []

	'''
	add a rock to the texture if the rock doesn't any rock in self.rocks 
	returns bool
	'''
	def add(self, rock):
		if not self.intersect(rock):
			self.rocks.append(rock)
			self.data.append(rock.data())
			return True
		return False


	'''
	Create the tree for the kernelDensity
	'''
	def learn(self):
		self.kde = KernelDensity(kernel='gaussian', bandwidth=0.04).fit(self.data)

	'''
	samples rocks from kde one by one making sure there are no intersection
	returns a Texture
	'''
	def sample(self, n_rocks=None):
		length = n_rocks
		if length == None:
			length = len(self.data)

		mtexture = Texture3D(self.size)
		i=0
		while i < length:
			new_rock = rock.dataToRock3D(self.kde.sample(1, random_state=None)[0])

			if mtexture.add(new_rock):
				i = i+1

		return mtexture

	'''
	compute the distance between two points
	return float
	'''
	def __distance(self, center1, center2):
		center1 = np.array(center1)
		center2 = np.array(center2)

		sub = center1 - center2
		sub = sub**2

		return math.sqrt(np.sum(sub))

	'''
	returns a string defining the texture. (for saving)
	format:
	size
	c1,c2,c3#rad1,rad2,rad3#col1,col2,col3#rot1,rot2,rot3
	c1,c2,c3#rad1,rad2,rad3#col1,col2,col3#rot1,rot2,rot3
	'''
	def toString(self):
		result = str(self.size) + '\n'
		for rock in self.rocks:
			center = '' + str(rock.center[0]) + ',' + str(rock.center[1]) + ',' + str(rock.center[2])
			radius = '' + str(rock.radius[0]) + ',' + str(rock.radius[1]) + ',' + str(rock.radius[2])
			color = '' + str(rock.color[0]) + ',' + str(rock.color[1]) + ',' + str(rock.color[2] + ',' + str(rock.color[3]))
			rotation = '' + str(rock.rotation[0]) + ',' + str(rock.rotation[1]) + ',' + str(rock.rotation[2])

			result = result + center + '#' + radius + '#' + color + '#' + rotation + '\n'
		return result

	'''
	Test if two rocks intersect. 
	returns bool
	'''
	def __intersect(self, rock1, rock2):
		return self.__distance(rock1.center, rock2.center) < max(rock1.radius) + max(rock2.radius)

	'''
	Test if a rock intersects another rock in self.rocks
	'''
	def intersect(self, rock):
		for r in self.rocks:
			if self.__intersect(rock, r):
				return True
		
		return False

'''
returns a new texture of size size with n_rocks rocks. 
'''
def createRandomTexture(size, n_rocks):
	newTexture = Texture3D(size)
	while len(newTexture.rocks) <= n_rocks:
		newTexture.add(rock.randomRock3D(size))
	return newTexture
 
'''
returns a texture defined in the file file.
'''
def load(file):
	text = ''
	with open(file, 'r') as myfile:
		text=myfile.read()
	splitRocks = text.split('\n')
	texture = Texture3D(splitRocks[0])
	for rockTxt in splitRocks[1:-1]:
		split = rockTxt.split('#')
		center = [float(i) for i in split[0].split(',')]
		radius = [float(i) for i in split[1].split(',')]
		color = [float(i) for i in split[2].split(',')]
		rotation = [float(i) for i in split[3].split(',')]

		newRock = rock.Rock3D(center, radius, color, rotation)
		texture.add(newRock)
	return texture








