#
# test_z_theta_control.py
#

import sys
sys.path.insert(0, '../../lib')

from models.multirotor import *
from models.robot import *
from controllers.standard import *
from gui.multirotor_gui import *
from data.plot import *

from PyQt5.QtWidgets import QApplication

class MultirotorRobot(RoboticSystem):

    def __init__(self):
        super().__init__(1e-3) # delta_t = 1e-3
        self.MR = Multirotor2D(1.0, 0.25) # 1.0kg, L = 25cm

        self.vz_control = PIDSat(10.0, 50.0, 0.0,
                                 15, True)   # 15 N saturation + antiwindup
        self.z_control = PIDSat(2.0, 0.0, 0.0, 2)   # 2 m/s

        self.omega_control = PIDSat(1.0, 5.0, 0.0,
                                    15, True)   # 15 N saturation + antiwindup
        self.theta_control = PIDSat(2.0, 0.0, 0.0, 1.57)   # 1.57 m/s

        self.z_target = 0.4
        self.theta_target = math.radians(-10)

        self.plot = DataPlotter()

    def run(self):
        (_, z, theta) = self.get_pose()
        (_, vz, omega) = self.get_speed()

        omega_target = self.theta_control.evaluate(self.delta_t, self.theta_target, theta)

        vz_target = self.z_control.evaluate(self.delta_t, self.z_target, z)

        f = self.vz_control.evaluate(self.delta_t, vz_target, vz)

        diff = self.omega_control.evaluate(self.delta_t, omega_target, omega)

        self.MR.evaluate(self.delta_t, f - diff, f + diff)

        self.plot.add( 't', self.t)
        self.plot.add( 'omega', omega)
        self.plot.add( 'omega_target', omega_target)
        self.plot.add( 'theta', theta)
        self.plot.add('f', f)

        if self.t >= 4:
            self.plot.plot( [ 't', 'time' ],
                            [ [ 'omega', 'omega' ] , [ 'omega_target', 'omega_target' ] ])
            self.plot.plot( [ 't', 'time' ],
                            [ [ 'f', 'F' ]  ])
            self.plot.plot( [ 't', 'time' ],
                            [ [ 'theta', 'theta' ]  ])
            self.plot.show()
            return False
        else:
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
