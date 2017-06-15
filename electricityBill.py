TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    total = 0
    price = int(input("Which tariff? 11 or 31: "))
    usage = float(input("Enter daily use in kWh: "))
    days = int(input("Enter number of billing days: "))
    if price == 11:
        total = (TARIFF_11 * usage) * days
    elif price == 31:
        total = (TARIFF_31 * usage) * days

    print("Estimated bill: $", total)


main()
