from Food import *

class Snake:

    def __init__(self, world, color, length, headX, headY):
        self.world = world
        self.color = color
        self.length = length
        self.blocks = []
        self.headX = headX
        self.headY = headY
        self.speed = Dir.RIGHT

    def update(self):
        # Update location
        self.headX = (self.headX + self.speed[0]) % self.world.width
        self.headY = (self.headY + self.speed[1]) % self.world.height

        # Update blocks
        if len(self.blocks) >= self.length:
            old = self.blocks[0]
            self.blocks.remove(old)
            self.world.setBlock(old.x, old.y, None)

        head = Block(self.world, self.color, self.headX, self.headY)
        self.blocks.append(head)

        #Before setting the next block, check for collisions
        next = self.world.getBlock(self.headX, self.headY)
        if next: #we hit something
            if isinstance(next, Food):
                #eat food
                self.length += 1
                self.world.newFood()
            elif isinstance(next, Block):
                #collided with itself
                print("DEAD")

        self.world.setBlock(self.headX, self.headY, head)

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
