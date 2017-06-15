numbers = []


def main():
    for i in range(0, 5, 1):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    avg = sum(numbers) / len(numbers)
    print("The average of the numbers is", avg)

main()
