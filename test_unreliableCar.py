from random import randint

from prac8.unreliableCar import UnreliableCar


def main():
    random_distance = randint(0, 100)
    test_car = UnreliableCar("Prius 1", 100, 100)
    test_car.drive(random_distance)
    print(test_car)
    test_car.drive(random_distance)
    print(test_car)
main()
