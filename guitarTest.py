from prac7.guitar import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Gibson L-3 CES", 2012, 1603.40)

    print("Expected 95. Got ", my_guitar.get_age())
    print("Expected 5. Got ", second_guitar.get_age())

    print("Expected True. Got ", my_guitar.is_vintage())
    print("Expected False. Got ", second_guitar.is_vintage())

main()

