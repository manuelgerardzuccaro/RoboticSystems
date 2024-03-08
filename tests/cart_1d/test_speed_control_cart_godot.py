import sys

from pathlib import Path
from matplotlib import pylab

CURRENT_POSITION = Path(__file__).parent
sys.path.append(f"{CURRENT_POSITION}/../../")

from lib.godot.interface import *
from lib.controllers.standard import *

cart = GodotCart1D()
controller = ProportionalIntegral(10,20)

t = 0  # beginning of events

target_speed = 500
_input = 0

time_array = []
speed_array = []
input_array = []

while t < 5:  # let's simulate 5 seconds
    (delta_t, position, speed) = cart.process(_input)
    _input = controller.evaluate(delta_t, target_speed, speed)

    time_array.append(t)
    speed_array.append(speed)
    input_array.append(_input)
    t = t + delta_t

pylab.figure(1)
pylab.plot(time_array, speed_array, 'r-+', label='speed, v(t)')
pylab.xlabel('time')
pylab.legend()

pylab.figure(3)
pylab.plot(time_array, input_array, 'r-+', label='force, f(t)')
pylab.xlabel('time')
pylab.legend()

pylab.show()
