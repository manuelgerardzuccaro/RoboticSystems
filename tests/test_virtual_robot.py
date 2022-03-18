#
#
#

import sys
sys.path.insert(0, '../lib')

from models.virtual_robot import *
from data.plot import *

rob =   VirtualRobot(   1, # distance 1 m
                        1.5, # max speed 1.5 m/s
                        2.0, # accel 2 m/s2
                        2.0) # decel 2 m/s2

t = 0           # beginning of events
delta_t = 1e-3  # sampling interval = 1ms

plotter = DataPlotter()

while rob.phase != rob.TARGET:
    plotter.add('t', t)
    plotter.add('v', rob.v)
    plotter.add('p', rob.p)
    rob.evaluate(delta_t)
    t = t + delta_t

plotter.plot( ['t', 'time'] , [ [ 'v', 'Speed' ],
                                [ 'p', 'Position' ] ])
plotter.show()
