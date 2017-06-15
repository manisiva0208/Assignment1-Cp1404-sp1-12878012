from prac7.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")

    valid_input = True
    while valid_input:

        name = input("Name: ")
        if name == "":
            valid_input = False
            continue
        else:
            valid_input = True
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitars.append(Guitar(name, year, cost))
        print(Guitar(name, year, cost), "added.")

    print("These are my guitars:")
    count = 0
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>5} ({}), worth ${:5,.2f} {}".format(count + 1, guitar.name, guitar.year, guitar.cost,
                                                                 vintage_string))


main()
