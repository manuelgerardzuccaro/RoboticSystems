#
# test_cart_gui.py
#

import sys
sys.path.insert(0, '../lib')

from models.cart import *
from gui.gui_1d import *

from PyQt5.QtWidgets import QApplication, QWidget

class CartSystem:

    def __init__(self):
        # Mass = 1kg
        # friction = 0.8
        self.cart = Cart(1, 0.8)

    def run(self, t, delta_t):
        self.cart.evaluate(delta_t, 2) # 2 Newton
        return True

    def get_pose(self):
        return self.cart.position

    def get_speed(self):
        return self.cart.speed


if __name__ == '__main__':
    cart_sys = CartSystem()
    app = QApplication(sys.argv)
    delta_t = 1e-3 # 1ms
    ex = MainWindow(delta_t, cart_sys)
    sys.exit(app.exec_())
