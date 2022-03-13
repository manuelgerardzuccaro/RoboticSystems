#
# arm.py
#

import math

G = 9.81

class Arm:

    def __init__(self, _mass, _friction, _length):
        self.M = _mass
        self.b = _friction
        self.r = _length
        self.omega = 0
        self.theta = 0

    def evaluate(self, delta_t, _torque):
        new_omega = self.omega - ((self.b * self.r) / self.M) * delta_t * self.omega \
          - G * delta_t * self.theta + delta_t/(self.M * self.r) * _torque
        new_theta = self.theta + self.omega * delta_t
        self.omega = new_omega
        self.theta = new_theta

    def evaluate_no_approx(self, delta_t, _torque):
        new_omega = self.omega - ((self.b * self.r) / self.M) * delta_t * self.omega \
          - G * delta_t * math.sin(self.theta) + delta_t/(self.M * self.r) * _torque
        new_theta = self.theta + self.omega * delta_t
        self.omega = new_omega
        self.theta = new_theta

