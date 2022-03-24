#
# virtual_robot.py
#

import math

class A_VirtualRobot:

    ACCEL = 0
    CRUISE = 1
    DECEL = 2
    TARGET = 3
    def __init__(self, _p_target, _vmax, _acc, _dec):
        self.p_target = _p_target
        self.vmax = _vmax
        self.accel = _acc
        self.decel = _dec
        self.v = 0 # current speed
        self.p = 0 # current position
        self.phase = A_VirtualRobot.ACCEL
        self.decel_distance = 0.5 * _vmax * _vmax / _dec

    def evaluate(self, delta_t):
        if self.phase == A_VirtualRobot.ACCEL:
            self.p = self.p + self.v * delta_t \
                     + self.accel * delta_t * delta_t / 2
            self.v = self.v + self.accel * delta_t
            if self.v >= self.vmax:
                self.v = self.vmax
                self.phase = A_VirtualRobot.CRUISE
            elif self.p_target - self.p <= self.decel_distance:
                self.phase = A_VirtualRobot.DECEL

        elif self.phase == A_VirtualRobot.CRUISE:
            self.p = self.p + self.vmax * delta_t
            if self.p_target - self.p <= self.decel_distance:
                self.phase = A_VirtualRobot.DECEL

        elif self.phase == A_VirtualRobot.DECEL:
            self.p = self.p + self.v * delta_t \
                     - self.decel * delta_t * delta_t / 2
            self.v = self.v - self.decel * delta_t
            if self.p >= self.p_target:
                self.v = 0
                self.p = self.p_target
                self.phase = A_VirtualRobot.TARGET

# ------------------------------------------------------------

class VirtualRobot:

    ACCEL = 0
    CRUISE = 1
    DECEL = 2
    TARGET = 3
    def __init__(self, _p_target, _vmax, _acc, _dec):
        self.p_target = _p_target
        self.vmax = _vmax
        self.accel = _acc
        self.decel = _dec
        self.v = 0 # current speed
        self.p = 0 # current position
        self.phase = VirtualRobot.ACCEL
        self.decel_distance = 0.5 * _vmax * _vmax / _dec

    def evaluate(self, delta_t):
        if self.phase == VirtualRobot.ACCEL:
            self.p = self.p + self.v * delta_t \
                     + self.accel * delta_t * delta_t / 2
            self.v = self.v + self.accel * delta_t
            distance = self.p_target - self.p
            if self.v >= self.vmax:
                self.v = self.vmax
                self.phase = VirtualRobot.CRUISE
            elif distance <= self.decel_distance:
                v_exp = math.sqrt(2 * self.decel * distance)
                if v_exp < self.v:
                    self.phase = VirtualRobot.DECEL

        elif self.phase == VirtualRobot.CRUISE:
            self.p = self.p + self.vmax * delta_t
            distance = self.p_target - self.p
            if distance <= self.decel_distance:
                self.phase = VirtualRobot.DECEL

        elif self.phase == VirtualRobot.DECEL:
            self.p = self.p + self.v * delta_t \
                     - self.decel * delta_t * delta_t / 2
            self.v = self.v - self.decel * delta_t
            if self.p >= self.p_target:
                self.v = 0
                self.p = self.p_target
                self.phase = VirtualRobot.TARGET


# ------------------------------------------------------------

class SpeedProfileGenerator:

    ACCEL = 0
    CRUISE = 1
    DECEL = 2
    TARGET = 3
    def __init__(self, _p_target, _vmax, _acc, _dec):
        self.p_target = _p_target
        self.vmax = _vmax
        self.accel = _acc
        self.decel = _dec
        self.v = 0 # current speed
        self.phase = SpeedProfileGenerator.ACCEL
        self.decel_distance = 0.5 * _vmax * _vmax / _dec

    def evaluate(self, delta_t, current_pos):
        # Indeed this is not correct!!
        # We should consider that, if the target is overcome, we must go back!!
        if current_pos >= self.p_target:
            self.v = 0	
            self.phase = SpeedProfileGenerator.TARGET
            return

        distance = self.p_target - current_pos
        if self.phase == SpeedProfileGenerator.ACCEL:
            self.v = self.v + self.accel * delta_t
            if self.v >= self.vmax:
                self.v = self.vmax
                self.phase = SpeedProfileGenerator.CRUISE
            elif distance <= self.decel_distance:
                v_exp = math.sqrt(2 * self.decel * distance)
                if v_exp < self.v:
                    self.phase = SpeedProfileGenerator.DECEL

        elif self.phase == SpeedProfileGenerator.CRUISE:
            if distance <= self.decel_distance:
                self.phase = SpeedProfileGenerator.DECEL

        elif self.phase == SpeedProfileGenerator.DECEL:
            self.v = math.sqrt(2 * self.decel * distance)
