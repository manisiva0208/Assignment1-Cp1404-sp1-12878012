
def main():
    quantity = 0
    total = 0
    valid_number = False
    while not valid_number:
        quantity = int(input("Number of items: "))
        if quantity < 0:
            valid_number = False
        else:
            valid_number = True
    for i in range(0, quantity, 1):
        price = float(input("Price of item: "))
        total += price

    if total > 100:
        discount = total * 0.10
        total -= discount
    print("Total price for", quantity, "items is $", total)


main()
