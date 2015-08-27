from Block import *

class Food(Block):
    def __init__(self, world, color, x=0, y=0):
        super(Food, self).__init__(world, color, x, y)