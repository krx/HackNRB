class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, rect):
        raise NotImplementedError()

    def getX(self):
        return self.x

    def getY(self):
        return self.y