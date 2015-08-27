import pygame


class Particle:
    def __init__(self, pos, size, vel, col):
        self.pos = pos
        self.size = size
        self.vel = vel
        self.col = col

    def draw(self, surface):
        pygame.draw.circle(surface, self.col, [int(round(self.pos[0])), int(round(self.pos[1]))], self.size)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
