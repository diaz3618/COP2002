import conversion_module

def welcome():
    print("This program converts between feet and meters\n")

def menu():
    print("Select from the two options below:\na. Feet to Meters\nb. Meters to Feet")

def convert(choice):
    # Feet to meters
    if choice == "a":
        num = float(input("Enter feet: "))
        print(str(round(float(conversion_module.to_meter(num)), 2)) + " meters")
    elif choice == "b":
        num = float(input("Enter meters: "))
        print(str(round(float(conversion_module.to_feet(num)), 2)) + " feet")

def main():
    welcome()
    
    again = "y"
    while again.lower() == "y":
        menu()
        option = input("\nWould you like to convert another number? (a/b): ")
        convert(option)


        while again.lower() != "n" or again.lower() != "y":
            again = input("\nRun again? (y/n): ")
            if again.lower() == "n":
                print("\nThanks, bye!")
                break

            elif again.lower() == "y":
                print()
                break
            elif again.lower() != "n" or again.lower() != "y":
                print("please enter y or n")


    
if __name__ == "__main__":
    main()
