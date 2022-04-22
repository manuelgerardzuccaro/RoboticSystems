#
# test_manipulator_pos.py
#

import sys
sys.path.insert(0, '../../lib')

from models.manipulator import *
from models.robot import *
from models.inputs import *
from models.virtual_robot import *
from controllers.standard import *
from data.plot import *
from gui.three_joints_gui import *

from PyQt5.QtWidgets import QApplication

class ManipulatorRobot(RoboticSystem):

    def __init__(self):
        super().__init__(1e-3) # delta_t = 1e-3
        self.arm = ThreeJointsPlanarArm(0.2, 0.2, 0.02,
                                        0.5, 0.5, 0.5,
                                        0.8)

        # joint 1
        self.speed_control_1 = PIDSat(400, 100, 0,
                                        20, True) # 20Nm max torque, antiwindup

        # joint 2
        self.speed_control_2 = PIDSat(400, 100, 0,
                                        20, True) # 20Nm max torque, antiwindup

        # joint 3
        self.speed_control_3 = PIDSat(10, 4, 0,
                                        20, True) # 20Nm max torque, antiwindup

        self.pos_control_1 = PIDSat(50, 0, 0, 2) # 2 rad/s max speed
        self.pos_control_2 = PIDSat(50, 0, 0, 2) # 2 rad/s max speed
        self.pos_control_3 = PIDSat(50, 0, 0, 2) # 2 rad/s max speed

        self.trajectory = VirtualRobot2D( 1, 0.5, 0.5)

        (x, y, a) = self.arm.get_pose()
        self.target_x = 0.1
        self.target_y = 0.0
        self.target_alpha = math.radians(-90)

        self.trajectory.set_target( (x,y), (self.target_x, self.target_y) )

        self.plotter = DataPlotter()


    def run(self):

        (x, y) = self.trajectory.evaluate(self.delta_t)

        (self.theta1, self.theta2, self.theta3) = self.arm.inverse_kinematics(x, y, self.target_alpha)

        wref_1 = self.pos_control_1.evaluate(self.delta_t, self.theta1, self.arm.element_1.theta)
        wref_2 = self.pos_control_2.evaluate(self.delta_t, self.theta2, self.arm.element_2.theta)
        wref_3 = self.pos_control_3.evaluate(self.delta_t, self.theta3, self.arm.element_3.theta)

        torque1 = self.speed_control_1.evaluate(self.delta_t, wref_1, self.arm.element_1.w)
        torque2 = self.speed_control_1.evaluate(self.delta_t, wref_2, self.arm.element_2.w)
        torque3 = self.speed_control_1.evaluate(self.delta_t, wref_3, self.arm.element_3.w)

        self.arm.evaluate(self.delta_t, torque1, torque2, torque3)

        self.plotter.add('Theta_ref', self.theta1)
        self.plotter.add('Theta', self.arm.element_1.theta)
        self.plotter.add('w', wref_1)
        self.plotter.add('t', self.t)

        if self.t > 4:
            self.plotter.plot( [ 't', 'Time' ],
                               [ [ 'Theta_ref', 'Theta Ref'] , [ 'Theta', 'Theta' ] ])
            self.plotter.plot( [ 't', 'Time' ],
                               [ [ 'w', 'W']  ])
            self.plotter.show()
            return False
        else:
            return True

    def get_joint_positions(self):
        return self.arm.get_joint_positions()

    def get_pose_degrees(self):
        return self.arm.get_pose_degrees()



if __name__ == '__main__':
    robot = ManipulatorRobot()
    app = QApplication(sys.argv)
    ex = ManipulatorWindow(robot)
    sys.exit(app.exec_())
