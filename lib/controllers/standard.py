#
#
#

class Proportional:

    def __init__(self, kp):
        self.kp = kp

    def evaluate(self, target, current):
        error = target - current
        return self.kp * error

