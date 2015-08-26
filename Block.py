import pygame

class Block():
    def __init__(self, world, x, y, color):
        super(Block, self).__init__(x, y)
        self.color = color

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def draw(self, surface, rect):
        pygame.draw.rect(surface, self.color, rect)