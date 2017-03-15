
import numpy as np

width = 500.0
height = 500.0
radius_max = 100.0
color_max = 255.

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

