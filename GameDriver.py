import sys, pygame
from World import World

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

world = World(pygame.Rect(5,5,400,400), 50, 50)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        ballrect = pygame.Rect(50,50,10,10)

        screen.fill(black)
        pygame.draw.ellipse(screen, white, ballrect)
        pygame.display.flip()