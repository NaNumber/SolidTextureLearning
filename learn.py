import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sketch


from sklearn.neighbors.kde import KernelDensity

data = sketch.sketch()

print data
kde = KernelDensity(kernel='gaussian', bandwidth=0.02).fit(data)

'''
sample1 = kde.sample(len(data), random_state=None)
sample2 = kde.sample(len(data), random_state=None)
sample3 = kde.sample(len(data), random_state=None)

'''
sample = []
i=0
while i < len(data):
	new_sample = kde.sample(1, random_state=None)
	new_sample = new_sample[0]

	max_new_sample = sketch.maximize(new_sample)
	max_sample = []

	for s in sample:
		max_sample.append(sketch.maximize(s))

	#import pdb; pdb.set_trace()

	if not sketch.isIntersected(max_new_sample, max_sample):
		sample.append(new_sample)
		print new_sample
		i = i+1


sketch.paint(sample)


'''
xy_sample= sample.transpose(1,0)
xy_data = data.transpose(1,0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xy_data[0], xy_data[1], xy_data[2], s=50)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xy_sample[0], xy_sample[1], xy_sample[2],s=50)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
'''
'''
plt.plot(xy_data[0],xy_data[1],'ro')
plt.axis([0,3,0,3])
plt.show()

plt.plot(xy_sample[0],xy_sample[1],'ro')
plt.axis([0,3,0,3])
plt.show()
'''

