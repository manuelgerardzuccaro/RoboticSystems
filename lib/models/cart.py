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
        speed_prime = (1 - self.b * delta_t / self.M) * self.speed + delta_t * _force / self.M
        position_prime = self.position + self.speed * delta_t
        self.speed = speed_prime
        self.position = position_prime


