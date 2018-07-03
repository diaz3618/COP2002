#!/usr/bin/env python3
'''
Daniel Diaz Santiago
COP2002.002
Module 6 Homework - Wizard Inventory program
'''

def main():
    print("The Wizard Inventory program\n")
    menu()

    # Initial list
    items = ["wooden staff", "wizard hat", "cloth shoes"]
    
    while True:
        cmd = str(input("Command: "))

        if cmd.lower() == "show":
            show(items)
        elif cmd.lower() == "grab":
            grab(items)
        elif cmd.lower() == "edit":
            edit(items)
        elif cmd.lower() == "drop":
            drop(items)
        elif cmd.lower() == "exit":
            print("Bye!")
            return False
        else:
            print("\nCommand is invalid.")
            
def menu():
    print("COMMAND MENU")
    print("show - Show all items")  # Show items
    print("grab - Grab an item")    # Add items
    print("edit - Edit an item")    # Update item name
    print("drop - Drop an item")    # Remove item
    print("exit - Exit program\n")  # Exit

def show(items):
    i = 1
    for j in items:
        print(str(i) + ". " + j)
        i += 1  # number counter (1. 2. etc...)
    print()

def grab(items):
    # User can only carry 4 items
    if len(items) < 4:
        item_name = str(input("Name: "))
        items.append(item_name)
        print(item_name + " was added.\n")
    else:
        print("You can't carry any more items. Drop something first.\n")

def edit(items):
    item_num = int(input("Number: "))
    update_name = str(input("Updated name: "))
    if item_num != 0:   # Set to prevent program to attempt to remove x element in index -1 if 0 is entered.
        index = item_num - 1                # ei. Number 1 is index 0: "|0|1|2|3|..."
        items.remove(items[index])          # Remove element in index x
        items.insert(index, update_name)    # Insert element in index x

        print("Item number " + str(item_num) + " was updated.\n")

def drop(items):
    max = len(items)    
    item_num = int(input("Number: "))
    
    if item_num < 1 or item_num > max:
        print("Item is not being carried.\n")
    else:
        item = items.pop(item_num - 1)  # ei. Number 1 is index 0: "|0|1|2|3|..."
        print(item + " was dropped.\n")



if __name__ == "__main__":
    main()
