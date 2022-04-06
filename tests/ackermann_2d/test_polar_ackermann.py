#
# test_robot_2d_gui.py
#

import sys
sys.path.insert(0, '../../lib')

from models.cart2d import *
from models.robot import *
from controllers.standard import *
from controllers.control2d import *
from data.plot import *
from gui.gui_2d import *

from PyQt5.QtWidgets import QApplication

class AckermannRobot(RoboticSystem):

    def __init__(self):
        super().__init__(1e-3) # delta_t = 1e-3
        # Mass = 10kg
        # side = 15cm
        # wheels radius = 2cm
        # friction = 0.8
        self.car = AckermannSteering(10, 0.8, 0.02, 0.15)
        # 5 Nm max, antiwindup
        self.speed_controller = PIDSat(2.0, 2.0, 0, 5, True)
        self.polar_controller = Polar2DController(1.0, 2.0, #kp = 1, vmax = 2 m/s
                                                  1.0, math.pi/4)  # kp = 1, steering max = 45 deg

    def run(self):
        (vref, steering) = self.polar_controller.evaluate(self.delta_t,
                                                          0.5, 0.5,
                                                          self.get_pose())
        (v, w) = self.get_speed()

        torque = self.speed_controller.evaluate(self.delta_t, vref, v)

        self.car.evaluate(self.delta_t, torque, steering)

        return True

    def get_pose(self):
        return self.car.get_pose()

    def get_speed(self):
        return (self.car.v, self.car.w)


if __name__ == '__main__':
    cart_robot = AckermannRobot()
    app = QApplication(sys.argv)
    ex = CartWindow(cart_robot, 'ackermann_robot_2d.png')
    sys.exit(app.exec_())
