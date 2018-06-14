import conversion_module as cm

def welcome():
    print("This program converts between feet and meters\n")

def menu():
    print("Select from the two options below:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def convert(choice):
    # Feet to meters
    if choice == "a":
        num = float(input("Enter feet: "))
        print(str(round(float(cm.to_meter(num)), 2)) + " meters")

    elif choice == "b":
        num = float(input("Enter meters: "))
        print(str(round(float(cm.to_feet(num)), 2)) + " feet")

    else:
        print("\nInvalid option, try again\n\n")
        main()

def main():
    welcome()
    
    again = "y"
    while again.lower() == "y":
        menu()
        option = str(input("\nWhich conversion would you like? (a/b): "))
        convert(option)

        while again.lower() != "n" or again.lower() != "y":
            again = input("\nWould you like to convert another number? Enter (y/n): ")
            if again.lower() == "n":
                print("\nThanks, bye!")
                break

            elif again.lower() == "y":
                print()
                break
            print("please enter y or n")

    
if __name__ == "__main__":
    main()
