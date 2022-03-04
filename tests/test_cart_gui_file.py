#
# test_cart_gui.py
#

import sys
sys.path.insert(0, '../lib')

from models.cart import *
from gui.gui_1d import *
from data.readers import *

from PyQt5.QtWidgets import QApplication, QWidget

class CartSystem:

    def __init__(self, filename):
        # Mass = 1kg
        # friction = 0.8
        self.cart = Cart(1, 0.8)
        self.datafile = FileReader(filename)
        self.datafile.load()
        self.delta_t = 1e-3 # 1ms
        self.t = 0

    def run(self):
        [ F ] = self.datafile.get_vars(self.t, [ 'F' ])
        self.cart.evaluate(self.delta_t, F)
        self.t = self.t + self.delta_t
        return True

    def get_pose(self):
        return self.cart.position

    def get_speed(self):
        return self.cart.speed


if __name__ == '__main__':
    cart_sys = CartSystem(sys.argv[1])
    app = QApplication(sys.argv)
    ex = MainWindow(cart_sys)
    sys.exit(app.exec_())
