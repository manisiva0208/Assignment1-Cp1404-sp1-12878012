LOWER_NUMBER = 33
UPPER_NUMBER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))

    number = get_number(LOWER_NUMBER, UPPER_NUMBER)
    print("The character for {} is {}".format(number, chr(number)))


def get_number(lower, upper):
    valid_number = False
    number = 0
    while not valid_number:
        number = int(input("Enter a number between " + str(lower) + " and " + str(upper) + ": "))
        if number < lower or number > upper:
            print("invalid number")

        else:
            valid_number = True

    return number
main()
