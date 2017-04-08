
import numpy as np
from random import randint
from random import uniform

width = 500.0
height = 500.0
depth = 500.0
radius_max = 100.0
color_max = 255.
rotation_max = 360.

class Rock:
	def __init__(self, center, radius, color):
		self.center = np.array(center)
		self.radius = radius
		self.color	= np.array(color)

		min_center = np.copy(center)
		min_center = min_center*1.
		min_center[0] = center[0]/width
		min_center[1] = center[1]/height

		min_color = np.copy(color)
		min_color = min_color*1.
		min_color[0] = color[0]/color_max
		min_color[1] = color[1]/color_max
		min_color[2] = color[2]/color_max

		self.min_center = min_center
		self.min_radius = radius / radius_max
		self.min_color = min_color

	def data(self):
		return np.array(self.min_center.tolist() + [self.min_radius] + self.min_color.tolist())

def dataToRock(data):
	center = []
	color = []
	center.append(int(max(0, data[0]*width)))
	center.append(int(max(0, data[1]*height)))
	radius = int(max(0, data[2]*radius_max))
	color.append(max(0, min(int(data[3]*color_max), 255)))
	color.append(max(0, min(int(data[4]*color_max), 255)))
	color.append(max(0, min(int(data[5]*color_max), 255)))

	return Rock(center, radius, color)

class Rock3D:
	def __init__(self, center, radius, color, rotation):
		self.center = np.array(center)
		self.radius = np.array(radius)
		self.color	= np.array(color) 
		self.rotation = np.array(rotation)

		min_center = np.copy(center)
		min_center = min_center*1.
		min_center[0] = center[0]/width
		min_center[1] = center[1]/height
		min_center[2] = center[2]/depth

		min_radius = np.copy(center)
		min_radius = min_radius*1.
		min_radius[0] = radius[0]/radius_max
		min_radius[1] = radius[1]/radius_max
		min_radius[2] = radius[2]/radius_max

		min_color = np.copy(color)
		min_color = min_color*1.
		min_color[0] = color[0]
		min_color[1] = color[1]
		min_color[2] = color[2]

		min_rotation = np.copy(rotation)
		min_rotation = min_rotation*1.
		min_rotation[0] = rotation[0]/rotation_max
		min_rotation[1] = rotation[1]/rotation_max
		min_rotation[2] = rotation[2]/rotation_max


		self.min_center = min_center
		self.min_radius = min_radius
		self.min_color = min_color
		self.min_rotation = min_rotation

	def data(self):
		print self.min_rotation
		return np.array(self.min_center.tolist() + self.min_radius.tolist() + self.min_color.tolist() + self.min_rotation.tolist())

def dataToRock3D(data):
	center = []
	color = []
	radius = []
	rotation = []
	center.append(data[0]*width)
	center.append(data[1]*height)
	center.append(data[2]*depth)
	radius.append(max(0, data[3]*radius_max))
	radius.append(max(0, data[4]*radius_max))
	radius.append(max(0, data[5]*radius_max))
	color.append(max(0, data[6]))
	color.append(max(0, data[7]))
	color.append(max(0, data[8]))
	color.append(1.)
	rotation.append(data[9]*rotation_max % 360)
	rotation.append(data[10]*rotation_max % 360)
	rotation.append(data[11]*rotation_max % 360)

	return Rock3D(center, radius, color, rotation)

def randomRock3D(size_texture):
	radius = [randint(10,90), randint(10,90), randint(10,90)]
	color = [uniform(0,1),uniform(0,1),uniform(0,1),1.]
	center = [randint(-size_texture/2,size_texture/2), randint(-size_texture/2,size_texture/2), randint(-size_texture/2,size_texture/2)]
	rotation = [randint(0,360), randint(0,360), randint(0,360)]

	return Rock3D(center, radius, color, rotation)