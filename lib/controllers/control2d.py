#
# control2d.py
#

import math
from standard import *

def normalize_angle(a):
    while a > math.pi:
        a = a - 2*math.pi
    while a < math.pi:
        a = a + 2*math.pi
    return a


class Polar2DController:

    def __init__(self, KP_linear, v_max, KP_heading, w_max):
        self.linear = PIDSat(KP_linear, 0, 0, 0, v_max)
        self.angular =PIDSat(KP_heading, 0, 0, 0, w_max)

    def evaluate(self, delta_t, xt, yt, current_pose):
        (x, y, theta) = current_pose

        dx = xt - x
        dy = yt - y

        target_heading = math.atan2(dy, dx)

        distance = math.sqrt(dx*dx + dy*dy)
        heading_error = normalize_angle(target_heading - theta)

        if (heading_error > math.pi/2)or(heading_error < -math.pi/2):
            distance = -distance
            heading_error = normalize_angle(heading_error + math.pi)

        v_target = self.linear.evaluate(delta_t, heading_error)
        w_target = self.angular.evaluate(delta_t, heading_error)
