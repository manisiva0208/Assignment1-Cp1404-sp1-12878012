from random import randint
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number = int(input("How many quick picks?"))
    while number <= 0:
        print("please enter number > 0")
        number = int(input("How many quick picks?"))

    for i in range(number):
        numbers = []
        for j in range(6):
            random_number = randint(MIN_NUMBER, MAX_NUMBER)
            while random_number in numbers:
                random_number = randint(MIN_NUMBER, MAX_NUMBER)
            numbers.append(random_number)
            print(format(random_number, "2d"), end=" ")

        print()

    print()


main()
