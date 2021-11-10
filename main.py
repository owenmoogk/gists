# INIT
import pygame
from Mass import *
from settings import *
from updateNodes import *

masses = []
masses.append(StationaryMass())

def drawWindow(masses):
	screen.fill(backgroundColor)
	for mass in masses:
		mass.draw()
	pygame.display.update()

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