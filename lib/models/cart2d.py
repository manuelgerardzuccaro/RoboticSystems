#
# cart2d.py
#

import math

class Cart2D:

    def __init__(self, _mass, _radius, _lin_friction, _ang_friction):
        self.M = _mass
        self.b = _lin_friction
        self.beta = _ang_friction
        self.Iz = 0.5 * _mass * _radius * _radius
        # Iz = moment of inertia (the robot is a cylinder)
        self.v = 0
        self.w = 0
        self.x = 0
        self.y = 0
        self.theta = 0

    def evaluate(self, delta_t, _force, _torque):
        new_v = self.v * (1 - self.b * delta_t / self.M) + delta_t * _force / self.M
        new_w = self.w * (1 - self.beta * delta_t / self.Iz) + delta_t * _torque / self.Iz
        self.x = self.x + self.v * delta_t * math.cos(self.theta)
        self.y = self.y + self.v * delta_t * math.sin(self.theta)
        self.theta = self.theta + delta_t * self.w
        self.v = new_v
        self.w = new_w


class TwoWheelsCart2D(Cart2D):

    def __init__(self, _mass, _radius, _lin_friction, _ang_friction, _traction_wheelbase):
        super().__init__(_mass, _radius, _lin_friction, _ang_friction)
        self.traction_wheelbase = _traction_wheelbase

    def evaluate(self, delta_t, f_left, f_right):
        f = f_left + f_right
        t = self.traction_wheelbase * (f_right - f_left)
        super().evaluate(delta_t, f, t)


