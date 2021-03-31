import pygame, random, time

# config var
WIDTH = 800
clock = pygame.time.Clock()

# display
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Pathfinding Algorithms')

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,165,0)
GREY = (100,100,100)

# fonts
pygame.font.init()
font = pygame.font.SysFont("comicsans", 50)

# settings
gridSize = 16
gameSpeed = 30
gridDimensions = WIDTH // gridSize
blinkTime = 0.5
milliseconds = int(round(time.time() * 1000))

class Firefly():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * gridSize
        self.y = col * gridSize
        self.period = random.uniform(1.5,2)
        self.active = False
        self.countdown = random.uniform(0,self.period)
        self.lastUpdateTime = milliseconds

    def update(self):
        self.countdown -= (milliseconds - self.lastUpdateTime)/1000
        self.lastUpdateTime = milliseconds
        if self.countdown <= 0:
            if self.active:
                self.active = False
                self.countdown = self.period
            else:
                self.active = True
                self.countdown = blinkTime

def drawGrid():
    for i in range(gridDimensions):
        pygame.draw.line(screen, GREY, (0, i * gridSize), (WIDTH, i * gridSize))
    for j in range(gridDimensions):
        pygame.draw.line(screen, GREY, (j * gridSize, 0), (j * gridSize, WIDTH))

def drawFireflies(grid):
    for row in grid:
        for item in row:
            if item.active:
                pygame.draw.rect(screen,ORANGE,(item.y,item.x,gridSize,gridSize),2)

def drawScreen(grid):
    screen.fill(BLACK)
    drawGrid()
    drawFireflies(grid)
    pygame.display.update()

def makeGrid():
    grid = []
    for i in range(gridDimensions):
        grid.append([])
        for j in range(gridDimensions):
            grid[i].append(Firefly(i, j))
    return(grid)

def main():
    grid = makeGrid()
    x = Firefly(12,4)
    running = True
    while running:
        global milliseconds
        milliseconds = int(round(time.time() * 1000))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        for row in grid:
            for firefly in row:
                firefly.update()

        drawScreen(grid)



if __name__ == "__main__":
    main()    