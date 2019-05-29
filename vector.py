class vector2:

    x = 0
    y = 0
    
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, vector):
        new_vector = Vector2(self.x + vector.x, self.y + vector.y)
        return new_vector

    def __mul__(self, scalar):
        new_vector = Vector2(self.x * scalar, self.y * scalar)
        return new_vector

    def dot(self, vector):
        dot = self.x * vector.x + self.y * vector.y
        return dot
