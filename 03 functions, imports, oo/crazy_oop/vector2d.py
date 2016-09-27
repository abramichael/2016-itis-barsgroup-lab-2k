class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

    def __add__(self, v2):
        return Vector2D(self.x + v2.x, self.y + v2.y)
