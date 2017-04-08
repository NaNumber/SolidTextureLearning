import rock
import numpy as np 
from sklearn.neighbors.kde import KernelDensity
import math

class Texture:
	def __init__(self):
		self.rocks = []
		self.data = []

	def add(self, rock):
		if not self.intersect(rock):
			self.rocks.append(rock)
			self.data.append(rock.data())
			return True
		return False

	def learn(self):
		self.kde = KernelDensity(kernel='gaussian', bandwidth=0.02).fit(self.data)

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

	def __distance(self, center1, center2):
		center1 = np.array(center1)
		center2 = np.array(center2)

		sub = center1 - center2
		sub = sub**2

		return math.sqrt(np.sum(sub))

	def __intersect(self, rock1, rock2):
		return self.__distance(rock1.center, rock2.center) < rock1.radius + rock2.radius

	def intersect(self, rock):
		for r in self.rocks:
			if self.__intersect(rock, r):
				return True
		return False

class Texture3D:
	def __init__(self):
		self.rocks = []
		self.data = []

	def add(self, rock):
		if not self.intersect(rock):
			self.rocks.append(rock)
			self.data.append(rock.data())
			return True
		return False

	def learn(self):
		self.kde = KernelDensity(kernel='gaussian', bandwidth=0.04).fit(self.data)

	def sample(self, n_rocks=None):
		length = n_rocks
		if length == None:
			length = len(self.data)

		mtexture = Texture3D()
		i=0
		while i < length:
			new_rock = rock.dataToRock3D(self.kde.sample(1, random_state=None)[0])

			if mtexture.add(new_rock):
				i = i+1

		return mtexture

	def __distance(self, center1, center2):
		center1 = np.array(center1)
		center2 = np.array(center2)

		sub = center1 - center2
		sub = sub**2

		return math.sqrt(np.sum(sub))

	def __intersect(self, rock1, rock2):
		return self.__distance(rock1.center, rock2.center) < max(rock1.radius) + max(rock2.radius)

	def intersect(self, rock):
		for r in self.rocks:
			if self.__intersect(rock, r):
				return True
		
		return False


def createRandomTexture(size, n_rocks):
	newTexture = Texture3D()
	while len(newTexture.rocks) <= n_rocks:
		newTexture.add(rock.randomRock3D(size))
	return newTexture
 









