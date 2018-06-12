import temperature

def convert(choice = 3):
    # Fahrenheit to celsius
    if choice == 1:
        num = float(input("Enter degrees in Fahrenheit: "))
        print("Degrees in Celsius: " + str(round(temperature.to_celsius(num), 1)))

    # Celsius to fahrenheit
    elif choice == 2:
        num = float(input("Enter degrees in Celsius: "))
        print("Degrees in Fahrenheit: " + str(round(temperature.to_fahrenheit(num), 1)))

    # Invalid option
    elif choice > 2:
        print("\n\nInvalid choice.")

def main():
    print("MENU")
    print("1. Fahrenheit to celsius\n2. Celsius to Fahrenheit")

    choice = "y"
    while choice.lower() == "y":
        menuChoice = int(input("\nEnter a menu option: "))

        # Convertion function
        convert(menuChoice)

        # Continue loop, or break
        print()
        while choice.lower() != "n" or choice.lower() != "y":
            choice = input("Convert another temperature? (y/n): ")
            
            if choice.lower() == "n":
                print("\nBye!")
                break
            
            elif choice.lower() == "y":
                break
            elif choice.lower() != "n" or choice.lower() != "y":
                print("please enter y or n")
    


if __name__ == "__main__":
    main()
