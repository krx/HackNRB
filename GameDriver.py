import sys, pygame, time
from World import *
from Block import Block
current_milli_time = lambda: int(round(time.time() * 1000))

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

world = World(pygame.Rect(210,10,580,580), 50, 50)
snake = world.snake
snake.headX = 47

baseInterval = 600
updateInterval = baseInterval // snake.length
lastUpdate = current_milli_time()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.turnLeft()
            if event.key == pygame.K_RIGHT:
                snake.turnRight()

    if current_milli_time() - lastUpdate >= updateInterval:
        screen.fill(black)
        world.draw(screen)
        world.update()
        pygame.display.flip()
        lastUpdate = current_milli_time()
        updateInterval = baseInterval // snake.length
