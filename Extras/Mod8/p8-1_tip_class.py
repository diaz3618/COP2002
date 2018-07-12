#!/usr/bin/env python3

def get_cost():
    while True:
        try:
            cost = float(input("Cost of meal: "))
            if cost >= 0:
                return cost
            else:
                print("Must be greater than 0. Please try again.")
        except ValueError:
            print("Must be valid decimal number. Please try again.")

def get_tip_percent():
    while True:
        try:
            tip = int(input("Tip percent: "))
            if tip >= 0:
                return tip
            else:
                print("Must be greater than 0. Please try again.")
        except ValueError:
            print("Must be valid integer. Please try again.")
            

def main():
    # display a welcome message
    print("Tip Calculator")
    print()

    print("INPUT")
    meal_cost = get_cost()
    tip_percent = get_tip_percent()
    print()

    # calculate tip and total amount
    tip_amount = round(meal_cost * (tip_percent / 100), 2)
    total = round(meal_cost + tip_amount, 2)

    print("OUTPUT")
    print("Cost of meal:", meal_cost)
    print("Tip percent: ", tip_percent)
    print("Tip amount:  ", tip_amount)
    print("Total amount:", total)

if __name__ == "__main__":
    main()
