import pygame
from Sprite import Sprite

class Block(Sprite):
    def __init__(self, world, rect, color):
        self.rect = rect
        self.color = color

    def draw(self, surface, rect):
        pygame.draw.rect(surface, self.color, self.rect)