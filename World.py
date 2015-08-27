import pygame
from Snake import *
from random import randint, random
from math import *
from Particle import Particle


class World:
    RED = 255, 0, 0
    GREEN = 0, 255, 0

    def __init__(self, loc, width, height):
        self.loc = loc  # Location and size of the world

        self.width = width  # Width of grid in cells
        self.height = height  # Height of grid in cells

        self.cellWidth = 0  # Width of individual cell
        self.cellHeight = 0  # Height of individual cell

        self.updateSize()

        self.snake = Snake(self, World.RED, 1, 0, 0)
        self.blocks = [[None for x in range(width)] for y in range(height)]
        self.newFood()

        self.particles = []

    def updateSize(self):
        self.cellWidth = round(self.loc.width / self.width)
        self.cellHeight = round(self.loc.height / self.height)

    def update(self):
        self.snake.update()

    def newFood(self):
        x = y = -1
        while x < 0 or y < 0 or self.getBlock(x, y):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
        self.setBlock(x, y, Food(self, World.GREEN))

    def spawnParticles(self, n, gridX, gridY):
        for i in range(n):
            col = randint(0, 255), randint(0, 255), randint(0, 255)
            size = randint(1, 3)
            speed = random() * 4.0 + 1.0
            angle = random() * 2.0 * pi
            self.particles.append(Particle([gridX * self.cellWidth + self.cellWidth // 2 + self.loc.x, gridY * self.cellHeight + self.cellHeight // 2 + self.loc.y], size, [speed * cos(angle), speed * sin(angle)], col))

    def draw(self, surface):
        for y, row in enumerate(self.blocks):
            for x, block in enumerate(row):
                if block:
                    drawRect = pygame.Rect(self.loc.x + x * self.cellWidth, self.loc.y + y * self.cellHeight,
                                           self.cellWidth, self.cellHeight)
                    block.draw(surface, drawRect)
                    # self.snake.draw(surface)

    def setBlock(self, x, y, block):
        self.blocks[y][x] = block;
        if block:
            block.x = x
            block.y = y

    def getBlock(self, x, y):
        return self.blocks[y][x]
