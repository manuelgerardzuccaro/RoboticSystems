import sys

from pathlib import Path
from matplotlib import pylab

CURRENT_POSITION = Path(__file__).parent
sys.path.append(f"{CURRENT_POSITION}/../../")

from lib.godot.interface import *

cart = GodotCart1D()

t = 0  # beginning of events

_input = 1000  # constant input of 1000 kg

time_array = []
speed_array = []
position_array = []

while t < 3:  # let's simulate 3 seconds
    (delta_t, position, speed) = cart.process(_input)
    time_array.append(t)
    speed_array.append(speed)
    position_array.append(position)
    t = t + delta_t

pylab.figure(1)
pylab.plot(time_array, speed_array, 'r-+', label='speed, v(t)')
pylab.xlabel('time')
pylab.legend()

pylab.figure(2)
pylab.plot(time_array, position_array, 'r-+', label='position, p(t)')
pylab.xlabel('time')
pylab.legend()

pylab.show()
