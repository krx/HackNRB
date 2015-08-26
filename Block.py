import pygame

class Block:
    def __init__(self, world, color, x=0, y=0):
        self.world = world
        self.color = color
        self.x = x
        self.y = y

    def draw(self, surface, rect):
        pygame.draw.rect(surface, self.color, rect)