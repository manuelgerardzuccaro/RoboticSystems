#
# test_position_control_cart_gui.py
#

import sys
sys.path.insert(0, '../../lib')

from models.cart import *
from models.robot import *
from controllers.standard import *
from gui.gui_1d import *

from PyQt5.QtWidgets import QApplication

class CartRobot(RoboticSystem):

    def __init__(self):
        super().__init__(1e-3) # delta_t = 1e-3
        # Mass = 1kg
        # friction = 0.8
        self.cart = Cart(1, 0.8)
        self.controller = Proportional(0.2) # Kp = 0.2
        self.target_position = 4 # 4 meters

    def run(self):
    	# F = 0.2 * (self.target_position - self.get_pose)
        F = self.controller.evaluate(self.target_position, self.get_pose())
        # F = -1 al target
        if (self.t >= 20.0):
        	F = F + 1
        	
        # se posizione corrente == target --> F = 0
        self.cart.evaluate(self.delta_t, F)
        return True

    def get_pose(self):
        return self.cart.position

    def get_speed(self):
        return self.cart.speed


if __name__ == '__main__':
    cart_robot = CartRobot()
    app = QApplication(sys.argv)
    ex = CartWindow(cart_robot)
    sys.exit(app.exec_())
