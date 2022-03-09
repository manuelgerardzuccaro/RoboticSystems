#
#
#

class Proportional:

    def __init__(self, kp):
        self.kp = kp

    def evaluate(self, target, current):
        error = target - current
        return self.kp * error


class Integral:

    def __init__(self, ki):
        self.ki = ki
        self.output = 0

    def evaluate(self, delta_t, target, current):
        error = target - current
        self.output = self.output + self.ki * error * delta_t
        return self.output



class ProportionalIntegral:

    def __init__(self, kp, ki):
        self.p = Proportional(kp)
        self.i = Integral(ki)

    def evaluate(self, delta_t, target, current):
        return self.p.evaluate(target, current) + self.i.evaluate(delta_t, target, current)

