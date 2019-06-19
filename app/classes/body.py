from .vector import vector2
import random

class body:

    def __init__(self, x, y, radius = random.randint(20,50), mass = 1, xSpeed = 0, ySpeed = 0):

        self.mass = mass
        self.radius = radius
        self.position = vector2(x, y)
        self.speed = vector2(xSpeed, ySpeed)
