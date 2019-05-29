from Vector import Vector2
import random

class Body:

    mass = 0
    radius = 0
    force = Vector2(0,0)
    acceleration = Vector2(0,0)
    velocity = Vector2(0,0)
    position = Vector2(0,0)

    def __init__(this, x, y, radius = random.randint(1,3), mass = 1):

        this.mass = mass
        this.radius = radius
        this.position.x = x
        this.position.y = y
