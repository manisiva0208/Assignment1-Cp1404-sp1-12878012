

from prac8.taxi import Taxi


def main():

    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    print(my_taxi)
main()
