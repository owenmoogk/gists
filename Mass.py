import pygame, random
from settings import *

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

		# resetting bc they get updated int the
		self.xAccel = 0
		self.yAccel = 0

		self.y += self.yVel
		self.x += self.xVel

		# if they crash into the edge
		if self.y <= self.mass or self.y >= windowHeight - self.mass:
			self.yVel = -self.yVel
		if self.x <= self.mass or self.x >= windowWidth - self.mass:
			self.xVel = -self.xVel

	def draw(self):
		pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.mass)

	