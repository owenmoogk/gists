# INIT
import pygame, random, time, math
from Mass import *
from settings import *
from drawScreen import *
from updateNodes import *

masses = []
masses.append(StationaryMass())

for i in range(numOfMasses):
	masses.append(Mass())

clock = pygame.time.Clock()
while True:
	clock.tick(simSpeed)

	# quit function
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	for index, mass in enumerate(masses):
		update(mass, masses)
		mass.move()

	drawWindow(masses)