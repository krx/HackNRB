from Block import Block

class Food(Block):
    def __init__(self, world, x, y, color):
        super(Food, self).__init__(world, x, y, color)