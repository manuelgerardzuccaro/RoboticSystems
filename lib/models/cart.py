class Cart:
    def __init__(self, _mass, _friction):
        """
        Defines a cart robot of a 1D environment with the given mass and friction
        :param _mass: The mass of the cart, expressed in Kg
        :param _friction: The force of friction present in the system
        """
        self.M = _mass
        self.b = _friction
        self.speed = 0
        self.position = 0

    def evaluate(self, delta_t, _force):
        """
        Evaluates the linear speed and position at the given time with the applied force
        :param delta_t: The delta time
        :param _force: The applied force
        """
        new_speed = (1 - self.b * delta_t / self.M) * self.speed + delta_t * _force / self.M
        new_position = self.position + self.speed * delta_t
        self.speed = new_speed
        self.position = new_position


