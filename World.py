import pygame

class World:
    def __init__(self, loc, width, height):
        self.loc = loc #Location and size of the world

        self.width = width #Width of grid in cells
        self.height = height #Height of grid in cells

        self.cellWidth = 0 #Width of individual cell
        self.cellHeight = 0 #Height of individual cell

        self.updateSize()
        self.sprites = []

    def updateSize(self):
        self.cellWidth = self.loc.width // self.width
        self.cellHeight = self.loc.height // self.height

    def draw(self, surface):
        for sprite in self.sprites:
            drawRect = pygame.Rect(self.loc.x + sprite.x * self.cellWidth, self.loc.y + sprite.y * self.cellHeight, sprite.get
            sprite.draw(surface)
