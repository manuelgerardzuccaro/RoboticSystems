#
# geometry.py
#

import math

def normalize_angle(a):
    while a > math.pi:
        a = a - 2*math.pi
    while a < - math.pi:
        a = a + 2*math.pi
    return a

