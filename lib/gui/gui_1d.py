#
# gui_1d.py
#

import sys
import math
import pathlib

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):

    def __init__(self, delta_t, _sys):
        super(MainWindow, self).__init__()
        self.delta_t = delta_t
        self.t = 0
        self._system = _sys
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1000, 400)
        self.setWindowTitle('Robot 1D Simulator')
        self.show()

        current_path = pathlib.Path(__file__).parent.resolve()
        image = str(current_path) + '/../icons/cart.png'

        self.robot_pic = QtGui.QPixmap(image)

        self._timer_painter = QtCore.QTimer(self)
        self._timer_painter.start(self.delta_t * 1000)
        self._timer_painter.timeout.connect(self.go)


    def go(self):
        if not(self._system.run(self.t, self.delta_t)):
            self._timer_painter.stop()
        self.t += self.delta_t
        self.update() # repaint window


    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor(255,255,255))
        qp.setBrush(QtGui.QColor(255,255,255))
        qp.drawRect(event.rect())

        x_pos = 50 + (self._system.get_pose() * 100)
        y_pos = 236

        qp.drawPixmap(x_pos,y_pos,self.robot_pic)

        qp.setPen(QtCore.Qt.black)
        qp.drawLine(0, 281, 990, 281)
        qp.drawLine(0, 282, 990, 282)
        qp.drawLine(990, 281, 990 - 10, 281 - 10)
        qp.drawLine(990, 282, 990 - 10, 282 + 10)

        qp.drawText(850, 20, "t = %6.3f s" % (self.t))
        qp.drawText(850, 40, "P = %6.3f m" % (self._system.get_pose()))
        qp.drawText(850, 60, "V = %6.3f m/s" % (self._system.get_speed()))

        qp.end()


