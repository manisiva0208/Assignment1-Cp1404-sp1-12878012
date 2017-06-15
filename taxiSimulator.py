from prac8.taxi import Taxi
from prac8.silverServiceTaxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
fares = []


def main():
    taxi_choice = 0
    print("Lets drive!")

    valid_input = False
    while not valid_input:
        display_menu()
        choice = input(">>>: ").upper()
        if choice == 'C':
            taxi_choice = choose_taxi()
        elif choice == 'D':
            drive_taxi(taxi_choice)
        elif choice == 'Q':
            print("Taxis are now:")
            count = 0
            for taxi in taxis:
                print("{} - {}".format(count, taxi))
                count += 1
            valid_input = True
        else:
            print("Invalid input")


def choose_taxi():

    print("Taxis Available")
    count = 0
    taxi_choice = 0
    for taxi in taxis:
        print("{} - {}".format(count, taxi))
        count += 1
    valid_choice = False
    while not valid_choice:
        taxi_choice = int(input("Choose Taxi: "))
        if taxi_choice > len(taxis):
            print("Enter valid taxi")
        else:
            total = 0
            for fare in fares:
                total += fare
            print("Bill to date: $", total)
            valid_choice = True
    return taxi_choice


def drive_taxi(taxi_choice):
    drive = int(input("Drive how far? "))
    taxis[taxi_choice].drive(drive)
    fares.append(taxis[taxi_choice].get_fare())
    total = 0
    for fare in fares:
        total += fare
    print("Your {} trip cost you ${}".format(taxis[taxi_choice].name, taxis[taxi_choice].get_fare()))
    print("Bill to date: $", total)


def display_menu():
    print("q)uit, c)hoose taxi, d)rive")

main()
