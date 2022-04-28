#
# test_multirotor.py
#

import sys
sys.path.insert(0, '../../lib')

from models.multirotor import *
from models.robot import *
from gui.multirotor_gui import *

from PyQt5.QtWidgets import QApplication

class MultirotorRobot(RoboticSystem):

    def __init__(self):
        super().__init__(1e-3) # delta_t = 1e-3
        self.MR = Multirotor2D(0.5, 0.2) # 0.5kg, L = 20cm

    def run(self):
        f1 = 4.0
        f2 = 3.0
        self.MR.evaluate(self.delta_t, f1, f2)
        return True

    def get_pose(self):
        return (self.MR.x, self.MR.z, self.MR.theta)

    def get_speed(self):
        return (self.MR.vx, self.MR.vz, self.MR.omega)


if __name__ == '__main__':
    robot = MultirotorRobot()
    app = QApplication(sys.argv)
    ex = MultirotorWindow(robot)
    sys.exit(app.exec_())
