from ctypes import c_bool
from Food import *
from random import randint
from time import time

current_milli_time = lambda: int(round(time() * 1000))


class Snake:
    def __init__(self, world, color, length, headX, headY):
        self.world = world
        self.color = color
        self.length = length
        self.blocks = []
        self.headX = headX
        self.headY = headY
        self.speed = Dir.RIGHT
        self.dead = False
        self.hueShift = 0
        self.hueStep = 0.5
        self.moveDelay = 100
        self.lastMoveTime = current_milli_time()

        self.deathSequence = False
        self.deathTime = 0
        self.deathDelay = 4000

    def update(self):
        if not self.deathSequence:
            # Only move after a certin time interval
            if current_milli_time() - self.lastMoveTime >= self.moveDelay:
                self.lastMoveTime = current_milli_time()

                # Update location
                # self.headX = (self.headX + self.speed[0]) % self.world.width
                # self.headY = (self.headY + self.speed[1]) % self.world.height
                self.headX += self.speed[0]
                self.headY += self.speed[1]

                if self.headX < 0 or self.headX >= self.world.width or self.headY < 0 or self.headY >= self.world.height:
                    # collided with a wall
                    self.deathSequence = True
                    return
                # Update blocks
                if len(self.blocks) >= self.length:
                    block = self.blocks.pop(0)
                    self.world.setBlock(block.x, block.y, None)

                head = Block(self.world, self.color, self.headX, self.headY)
                self.blocks.append(head)

                # Before setting the next block, check for collisions
                next = self.world.getBlock(self.headX, self.headY)
                if next:  # we hit something
                    if isinstance(next, Food):
                        # eat food
                        self.length += 2
                        self.world.newFood()
                        self.world.spawnParticles(randint(150, 300), self.headX, self.headY)
                    elif isinstance(next, Block):
                        # collided with itself
                        self.deathSequence = True
                        return

                self.world.setBlock(self.headX, self.headY, head)

            # Recolor blocks to RAINBOW
            for i, block in enumerate(reversed(self.blocks)):
                col = pygame.Color(0)
                col.hsva = (float(i / len(self.blocks)) * 360.0 + self.hueShift) % 360.0, 100, 100, 100
                block.color = col
            self.hueShift = (self.hueShift + self.hueStep) % 360.0
        else:
            # Death sequence
            if len(self.blocks) > 0:
                # Time the explosions so they aren't all at once
                if current_milli_time() - self.lastMoveTime >= self.moveDelay * 2:
                    self.lastMoveTime = current_milli_time()
                    block = self.blocks.pop(-1)
                    self.world.setBlock(block.x, block.y, None)
                    self.world.spawnParticles(randint(150, 300), block.x, block.y)
                    self.deathTime = current_milli_time()
            elif current_milli_time() - self.deathTime >= self.deathDelay:
                self.dead = True

    def setDirection(self, dir):
        self.speed = dir;

    def turnRight(self):
        dir = self.speed
        if dir is Dir.UP:
            self.setDirection(Dir.RIGHT)
        elif dir is Dir.RIGHT:
            self.setDirection(Dir.DOWN)
        elif dir is Dir.DOWN:
            self.setDirection(Dir.LEFT)
        elif dir is Dir.LEFT:
            self.setDirection(Dir.UP)

    def turnLeft(self):
        dir = self.speed
        if dir is Dir.UP:
            self.setDirection(Dir.LEFT)
        elif dir is Dir.RIGHT:
            self.setDirection(Dir.UP)
        elif dir is Dir.DOWN:
            self.setDirection(Dir.RIGHT)
        elif dir is Dir.LEFT:
            self.setDirection(Dir.DOWN)


class Dir:
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]
