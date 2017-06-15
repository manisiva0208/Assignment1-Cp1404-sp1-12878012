from prac8.silverServiceTaxi import SilverServiceTaxi


def main():

    my_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_taxi.drive(10)
    print(my_taxi)
    print(my_taxi.get_fare())

main()
