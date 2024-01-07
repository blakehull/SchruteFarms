import numbers


class SensorBoundary:
    def __init__(self, lower_bound: numbers.Number, upper_bound: numbers.Number):
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
