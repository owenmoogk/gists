import pygame
from settings import *

def drawWindow(masses):
	screen.fill(backgroundColor)
	for mass in masses:
		mass.draw()
	pygame.display.update()