from .vector import vector2

class camera:

    def __init__(self, x, y):

        self.position = vector2(x,y)
        self.zoom = 1
        self.offset = vector2(0,0)