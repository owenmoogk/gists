import pygame

pygame.font.init()  # init font
windowWidth = 1200
windowHeight = 675
myFont = pygame.font.SysFont("comicsans", 50)
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Gravity Simulation")

# SETTINGS
simSpeed = 60 # 60 ticks / frames per second
numOfMasses = 20
dampening = 0.98
gravitationalConstant = 30
maxSpeed = 50 # pixels per second

# COLORS
white = (255,255,255)
grey = (150,150,150)
blue = (51,153,255)
red = (255,0,0)
pink = (254,127,156)
green = (0,255,0)
backgroundColor = (30,30,30)