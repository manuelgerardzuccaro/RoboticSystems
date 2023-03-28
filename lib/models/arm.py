import math

# Standard Acceleration of Gravity
G = 9.81


class Arm:

    def __init__(self, _mass, _friction, _length):
        """
        Defines an arm robot with the given mass, friction and bar length
        :param _mass: The mass attached at the end of the bar, expressed in Kg
        :param _friction: The force of friction present in the system
        :param _length: The bar's length
        """
        self.M = _mass
        self.b = _friction
        self.r = _length
        self.omega = 0
        self.theta = 0

    def evaluate(self, delta_t, _torque) -> None:
        """
        Evaluates the angular speed and angular position at the given time with the applied torque
        :param delta_t: The delta time
        :param _torque: The Applied torque
        """
        new_omega = self.omega - ((self.b * self.r) / self.M) * delta_t * self.omega \
                    - G * delta_t * self.theta + delta_t / (self.M * self.r) * _torque
        new_theta = self.theta + self.omega * delta_t
        self.omega = new_omega
        self.theta = new_theta

    def evaluate_no_approx(self, delta_t, _torque) -> None:
        """
        Evaluates without approximation the angular speed and angular position at the given time with the applied torque
        :param delta_t: The delta time
        :param _torque: The applied torque
        """
        new_omega = self.omega - ((self.b * self.r) / self.M) * delta_t * self.omega \
                    - G * delta_t * math.sin(self.theta) + delta_t / (self.M * self.r) * _torque
        new_theta = self.theta + self.omega * delta_t
        self.omega = new_omega
        self.theta = new_theta
