import pygame, random
from settings import *

class StationaryMass:
	def __init__(self):
		self.mass = 60

		self.x = random.randint(self.mass,windowWidth-self.mass)
		self.y = random.randint(self.mass,windowHeight-self.mass)
		self.xVel = 0
		self.yVel = 0
		self.xAccel = 0
		self.yAccel = 0
		

	def move(self):
		
		pass

	def draw(self):
		pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.mass)

	

class Mass:

	def __init__(self):
		self.mass = random.randint(5,10)

		self.x = random.randint(self.mass,windowWidth-self.mass)
		self.y = random.randint(self.mass,windowHeight-self.mass)
		self.xVel = 0
		self.yVel = 0
		self.xAccel = 0
		self.yAccel = 0
		

	def move(self):
		
		self.xVel += self.xAccel
		self.yVel += self.yAccel

		self.xVel *= dampening
		self.yVel *= dampening

		if abs(self.xVel) > maxSpeed:
			if self.xVel < 0:
				self.xVel = -maxSpeed
			else:
				self.xVel = maxSpeed
		if abs(self.yVel) > maxSpeed:
			if self.yVel < 0:
				self.yVel = -maxSpeed
			else:
				self.yVel = maxSpeed


		# resetting bc they get updated int the
		self.xAccel = 0
		self.yAccel = 0

		self.y += self.yVel
		self.x += self.xVel

		# relationships need boundaries
		if self.y <= self.mass:
			self.y = self.mass
			self.yVel = abs(self.yVel)
		if self.y >= windowHeight - self.mass:
			self.yVel = -abs(self.yVel)
			self.y = windowHeight - self.mass
		if self.x <= self.mass:
			self.x = self.mass
			self.xVel = abs(self.xVel)
		if self.x >= windowWidth - self.mass:
			self.xVel = -abs(self.xVel)
			self.x = windowWidth - self.mass

	def draw(self):
		pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.mass)

	