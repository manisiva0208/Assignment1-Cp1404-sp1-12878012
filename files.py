def main():
    write_file = open("name.txt", "w")
    name = input("Your name? ")
    write_file.write(name)
    write_file.close()

    read_file = open("name.txt", "r")
    name = read_file.read().strip()
    print("Your name is", name)
    read_file.close()

    read_file2 = open("numbers.txt", "r")
    num1 = int(read_file2.readline())
    num2 = int(read_file2.readline())
    total = num1 + num2
    print(total)
    read_file2.close()

main()