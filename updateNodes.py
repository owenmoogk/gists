import math, random
from settings import *

def update(mass1, masses):

	for mass2 in masses:
		if mass2 == mass1:
			continue

		deltaY = mass1.y - mass2.y
		deltaX = mass2.x - mass1.x

		# distance between two masses
		distance = math.sqrt(deltaY**2 + deltaX**2)

		# force between two objects, acceleration adjusts depending on masses and then needs to be seperated by vectors
		gravitationalAcceleration = gravitationalConstant * mass2.mass * mass1.mass / distance**2

		# now have to split up into vectors
		# step 1, find angle
		angle = math.atan2(deltaX, deltaY)
		angle = math.radians(math.degrees(angle) - 90)
		print("Distance: ", distance, "Angle: ", math.degrees(angle))

		# now split into vectors for each, and add to current accel
		mass1.xAccel += gravitationalAcceleration * math.cos(angle)
		mass1.yAccel += gravitationalAcceleration * math.sin(angle)
