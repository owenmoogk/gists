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

		if distance <= 1:
			# collided
			totalMass = mass1.mass + mass2.mass
			mass1.xVel = (mass1.xVel*mass1.mass + mass2.xVel*mass2.mass) / (totalMass)
			mass1.yVel = (mass1.yVel*mass1.mass + mass2.yVel*mass2.mass) / (totalMass)
			mass1.mass += mass2.mass

			masses.remove(mass2)


		# force between two objects, acceleration adjusts depending on masses and then needs to be seperated by vectors
		gravitationalAcceleration = gravitationalConstant * mass2.mass * mass1.mass / distance**2

		if gravitationalAcceleration > 0.5:
			gravitationalAcceleration = 0.5

		totalMass = mass1.mass + mass2.mass
		movementRatio = mass2.mass / totalMass
		gravitationalAcceleration *= movementRatio

		# now have to split up into vectors
		# step 1, find angle
		angle = math.atan2(deltaX, deltaY)
		angle = math.radians(math.degrees(angle) - 90)
		# print("Distance: ", distance, "Angle: ", math.degrees(angle))

		# now split into vectors for each, and add to current accel
		mass1.xAccel += gravitationalAcceleration * math.cos(angle)
		mass1.yAccel += gravitationalAcceleration * math.sin(angle)
