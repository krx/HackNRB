import pygame
from Snake import Snake

class World:
    def __init__(self, loc, width, height):
        self.loc = loc #Location and size of the world

        self.width = width #Width of grid in cells
        self.height = height #Height of grid in cells

        self.cellWidth = 0 #Width of individual cell
        self.cellHeight = 0 #Height of individual cell

        self.updateSize()

        self.snake = Snake((255,0,0), 3, 0, 0)

        self.blocks = [[0 for x in range(width)] for y in range(height)]

    def updateSize(self):
        self.cellWidth = self.loc.width // self.width
        self.cellHeight = self.loc.height // self.height

    def update(self):
        self.snake.update()

    def draw(self, surface):
        for block in self.blocks:
            drawRect = pygame.Rect(self.loc.x + block.x * self.cellWidth, self.loc.y + block.y * self.cellHeight, self.cellWidth, self.cellHeight)
            block.draw(surface, drawRect)
        self.snake.draw(surface)

    def setBlock(self, x, y, block):
        self.blocks[x][y] = block;