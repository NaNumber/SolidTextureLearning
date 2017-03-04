import pygame, sys
from pygame.locals import *
import numpy as np
import math

width = 500.0
height = 500.0
rayon_max = 100.0
color_max = 255.

def sketch():
	pygame.init()

	pywindow = pygame.display.set_mode((int(width), int(height)))
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)
	pywindow.fill(WHITE)

	rayon = 1
	color = (0,0,255)

	min_circles = []
	max_circles = []

	while True: #main game loop

	    for event in pygame.event.get():
	        if event.type == pygame.MOUSEBUTTONDOWN: #This checks for the mouse press event
	            circ = pygame.mouse.get_pos() #Gets the mouse position
	            circ_list = list(circ)
	            circ_list.append(rayon)
	            circ_list = circ_list + list(color)
	            print circ_list
	            if not isIntersected(circ_list, max_circles):
	            	max_circles.append(np.array(circ_list))
	            	circ_list = minimize(circ_list)
	            	min_circles.append(np.array(circ_list))
	            	pygame.draw.circle(pywindow, (color), (circ), rayon) #Draws a circle at the mouse position!
	        if event.type == pygame.KEYDOWN:
	        	if int(event.key) == ord('b'):
					color = (0,0,255)

	        	if int(event.key) == ord('r'):
	        		color = (255,0,0)

	        	if int(event.key) == ord('g'):
	        		color = (0,255,0)

	        	if 48<int(event.key)<=57:
	        		rayon = (int(event.key)-48)*5

	        if event.type == QUIT:
	            pygame.quit()
	            return min_circles
	    pygame.display.update()

def paint(circles):

	print 'painting'

	circles = np.array(circles)

	for i in range(len(circles)):
		circles[i] = maximize(circles[i])

	pygame.init()

	pywindow = pygame.display.set_mode((int(width), int(height)))
	WHITE = (255, 255, 255)
	pywindow.fill(WHITE)

	for circ in circles:
		pygame.draw.circle(pywindow, (int(circ[3]),int(circ[4]),int(circ[5])), (int(circ[0]),int(circ[1])), int(circ[2]))

	pygame.display.update()

	while True: #main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				return

def minimize(circ):
	min_circ = np.copy(circ)
	min_circ = min_circ*1.
	min_circ[0] = circ[0]/width
	min_circ[1] = circ[1]/height
	min_circ[2] = circ[2]/rayon_max
	min_circ[3] = circ[3]/color_max
	min_circ[4] = circ[4]/color_max
	min_circ[5] = circ[5]/color_max
	return min_circ

def maximize(circ):	
	max_circ = np.copy(circ)
	max_circ = max_circ*1.
	max_circ[0] = max(0, circ[0]*width)
	max_circ[1] = max(0, circ[1]*height)
	max_circ[2] = max(0, circ[2]*rayon_max)
	max_circ[3] = max(0, min(circ[3]*color_max, 255))
	max_circ[4] = max(0, min(circ[4]*color_max, 255))
	max_circ[5] = max(0, min(circ[5]*color_max, 255))
	return max_circ

def distance(p1, p2):
	p1 = np.array(p1)
	p2 = np.array(p2)

	sub = p1 - p2
	sub = sub**2
	#import pdb; pdb.set_trace()
	return math.sqrt(np.sum(sub))

def intersect(circ1, circ2):
	circ1 = np.array(circ1)
	circ2 = np.array(circ2)
	return distance(circ1[:2], circ2[:2]) < circ1[2] + circ2[2]

def isIntersected(circle, circles_list):
	circle = np.array(circle)
	circles_list = np.array(circles_list)
	for circ in circles_list:
		#import pdb; pdb.set_trace()
		if intersect(circle, circ):
			return True
	return False