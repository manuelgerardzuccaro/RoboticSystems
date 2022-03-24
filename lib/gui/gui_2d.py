#
#
#

import sys
import math
import pathlib

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget

class CartWindow(QWidget):

    def __init__(self, _compound_sys):
        super(CartWindow, self).__init__()
        self.compound_system = _compound_sys
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('Robot 2D Simulator')
        self.show()

        current_path = pathlib.Path(__file__).parent.resolve()
        image = str(current_path) + '/../icons/mobile_robot_2d.png'

        self.robot_pic = QtGui.QPixmap(image)

        self.delta_t = 1e-4 # 0.1ms of time-tick

        self._timer_painter = QtCore.QTimer(self)
        self._timer_painter.start(self.delta_t * 1000)
        self._timer_painter.timeout.connect(self.go)


    def go(self):
        if not(self.compound_system.step()):
            self._timer_painter.stop()
        self.update() # repaint window


    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor(255,255,255))
        qp.setBrush(QtGui.QColor(255,255,255))
        qp.drawRect(event.rect())

        (x, y, theta) = self.compound_system.get_pose()

        qp.setPen(QtCore.Qt.black)
        qp.drawLine(50, 500, 900, 500)
        qp.drawLine(50, 500, 50, 50)
        qp.drawLine(50, 50, 900, 50)
        qp.drawLine(900, 50, 900, 500)

        qp.drawText(910, 20, "X  = %6.3f m" % (x))
        qp.drawText(910, 40, "Y  = %6.3f m" % (y))
        qp.drawText(910, 60, "Th = %6.3f deg" % (math.degrees(theta)))
        qp.drawText(910, 80, "T  = %6.3f s" % (self.compound_system.t))

        s = self.robot_pic.size()

        x_pos = 50 + x*1000 - s.width() / 2
        y_pos = 500 - y*1000 - s.height() / 2

        t = QtGui.QTransform()
        t.translate(x_pos + s.width()/2, y_pos + s.height()/2)
        t.rotate(-math.degrees(theta))
        t.translate(-(x_pos + s.width()/2), - (y_pos + s.height()/2))

        qp.setTransform(t)
        qp.drawPixmap(x_pos,y_pos,self.robot_pic)

        qp.end()



def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
