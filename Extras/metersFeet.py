import conversion_module

def menu():
    print("This program converts between feet and meters\n")
    print("Select from the two options below:\na. Feet to Meters\nb. Meters to Feet")

def convert(choice):
    # Feet to meters
    if choice == "a":
        num = float(input("Enter feet: "))
        print(str(round(float(conversion_module.to_meter(num)), 2)) + " meter")
    elif choice == "b":
        num = float(input("Enter meters: "))
        print(str(round(float(conversion_module.to_feet(num)), 2)) + " feet")
    else:
        choice = "loop"

def main():
    menu()
    option = input("\nWhich convertion would you like? (a/b): ")

    while convert(option) != "loop":
        convert(option)

        if convert(option.lower()) != "a" or convert(option.lower()) != "b":
            print("\nInvalid option")
            break

    
if __name__ == "__main__":
    main()
