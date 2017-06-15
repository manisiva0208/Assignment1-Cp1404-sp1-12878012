def main():

    name = input("Enter name: ")
    valid_choice = False
    while not valid_choice:
        display_menu()
        choice = input(">>> ")
        if choice == 'H':
            print("Hello", name)
        elif choice == 'G':
            print("Goodbye", name)
        elif choice == "Q":
            print("Finished.")
            valid_choice = True
        else:
            print("Invalid choice")


def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
main()
