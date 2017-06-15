"""
CP1404/CP5632 Practical
Car class
"""

class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):

        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):

        return "{}".format(super().__str__())

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        if distance < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(self.reliability)

        return distance_driven
