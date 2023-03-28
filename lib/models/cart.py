#
# cart.py
#

class Cart:
    def __init__(self, _mass, _friction):
        self.M = _mass
        self.b = _friction
        self.speed = 0
        self.position = 0

    def evaluate(self, delta_t, _force):
        new_speed = (1 - self.b * delta_t / self.M) * self.speed + delta_t * _force / self.M
        new_position = self.position + self.speed * delta_t
        self.speed = new_speed
        self.position = new_position


