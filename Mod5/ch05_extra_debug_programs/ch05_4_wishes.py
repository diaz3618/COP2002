#!/usr/bin/env python3

"""
Project Statement
The application shown has four errors. Create a hierarchy chart to
begin the debugging process. Then find and fix the four errors so
that the program allows the user to input as many items and their
costs as desired and outputs a subtotal of the items and a total
cost including 6% sales tax.
"""
def validate(item_cost):
    while item_cost <= 0:
        item_cost = float(input("Enter a valid cost for this item: "))
    return item_cost

def display_welcome():
    print("This program will create a wish list for the user.")
    print("Enter as many items as you like, with their costs")
    print("and the program will calculate your total, before and")
    print("after 6% tax.")

def goodbye():
    print("Hope you get everything you wish for!")
    print("Goodbye!")

def get_tax(sub):
    total_cost = sub * 1.06
    print("Your total cost, including 6% tax, is $" + str(round(total_cost,2)))

def get_item():
    sub = 0
    repeat = "y"
    while repeat.lower() == "y":
        item_name = input("\nEnter the name of your item: ")
        item_cost = float(input("Enter the cost of this item: "))
        item_cost = validate(item_cost)
        
        print("\nItem: " + str(item_name) + " for $" + str(round(item_cost, 2)))
        sub = sub + item_cost
        print("\nYour subtotal is $" + str(round(sub, 2)))
        get_tax(sub)
        
        if repeat.lower() == "n":
            goodbye()
            break
        repeat = input("\nEnter an item? y/n ")

def main():
    display_welcome()
    sub = 0
    get_item()
    
# if started as the main module, call the main function
if __name__ == "__main__":
    main()

