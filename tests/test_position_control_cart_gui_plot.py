#
# test_position_control_cart_gui_plot.py
#

import sys
sys.path.insert(0, '../lib')

from models.cart import *
from models.robot import *
from controllers.standard import *
from data.plot import *
from gui.gui_1d import *

from PyQt5.QtWidgets import QApplication

class CartRobot(RoboticSystem):

    def __init__(self):
        super().__init__(1e-3) # delta_t = 1e-3
        # Mass = 1kg
        # friction = 0.8
        self.cart = Cart(1, 0.8)
        self.plotter = DataPlotter()
        self.controller = Proportional(0.2) # Kp = 0.2
        self.target_position = 4 # 4 meters

    def run(self):
        F = self.controller.evaluate(self.target_position, self.get_pose())
        self.cart.evaluate(self.delta_t, F)
        self.plotter.add('t', self.t)
        self.plotter.add('target', self.target_position)
        self.plotter.add('position', self.get_pose())
        if self.t >= 15:
            self.plotter.plot( [ 't', 'time'], [ [ 'target', 'Target' ],
                                                 [ 'position', 'Current Position' ] ])
            self.plotter.show()
            return False
        else:
            return True

    def get_pose(self):
        return self.cart.position

    def get_speed(self):
        return self.cart.speed


if __name__ == '__main__':
    cart_robot = CartRobot()
    app = QApplication(sys.argv)
    ex = MainWindow(cart_robot)
    sys.exit(app.exec_())
