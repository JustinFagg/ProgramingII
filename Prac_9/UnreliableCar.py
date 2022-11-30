"""
CP1404/CP5632 Practical
UnreliableCar class
"""
import random

from Prac_9.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that doesn't always drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.reliability:.2f}% reliable"

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = 0
        if random.randrange(100)<self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
