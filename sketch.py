import pygame, sys
from pygame.locals import *
import numpy as np
import math
import texture
import rock

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

	radius = 1
	color = (0,0,255)
	

	new_texture = texture.Texture()

	while True: #main game loop

	    for event in pygame.event.get():
	        if event.type == pygame.MOUSEBUTTONDOWN: #This checks for the mouse press event
	            center = pygame.mouse.get_pos() #Gets the mouse position

	            new_rock = rock.Rock(center, radius, color)

	            if new_texture.add(new_rock):
	            	pygame.draw.circle(pywindow, color, new_rock.center, radius) #Draws a circle at the mouse position

	        if event.type == pygame.KEYDOWN:
	        	if int(event.key) == ord('b'):
					color = (0,0,255)

	        	if int(event.key) == ord('r'):
	        		color = (255,0,0)

	        	if int(event.key) == ord('g'):
	        		color = (0,255,0)

	        	if 48<int(event.key)<=57:
	        		radius = (int(event.key)-48)*5

	        if event.type == QUIT:
	            pygame.quit()
	            return new_texture
	    pygame.display.update()

def paint(mtexture):
	print 'painting'
	pygame.init()

	pywindow = pygame.display.set_mode((int(width), int(height)))
	WHITE = (255, 255, 255)
	pywindow.fill(WHITE)

	for rock in mtexture.rocks:
		pygame.draw.circle(pywindow, rock.color, rock.center, rock.radius)

	pygame.display.update()

	while True: #main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				return