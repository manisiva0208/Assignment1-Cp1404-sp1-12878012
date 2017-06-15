from prac8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel, fanciness):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${}".format(super(Taxi, self).__str__(),
                                                                                  self.current_fare_distance,
                                                                                  (self.fanciness * Taxi.price_per_km),
                                                                                  self.flag_fall)

    def get_fare(self):
        """ get the price for the taxi trip """
        return ((self.fanciness * Taxi.price_per_km) * self.current_fare_distance) + self.flag_fall

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance = distance_driven
        return distance_driven
