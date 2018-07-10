#!/usr/bin/env python3

import random

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

def main():
    display_title()
    display_menu()

    inventory = _read(INVENTORY_FILENAME)
    while True:        
        command = input("Command: ")        
        if command == "walk":
            walk(inventory)
        elif command == "show":
            show(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
    
"""
read_inventory() and read_items() do the same thing,
why not make one function that can read either one?
"""
def _read(filename):
    items = []
    with open(filename) as file:  ## **Using "with" automatically closes the file.
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
    return items


# COMMENTED OUT
"""
def read_inventory():
    items = []
    with open(INVENTORY_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
    return items

def read_items():
    items = []
    with open(ITEMS_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
    return items
"""
## COMMENTED OUT


def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for inv in inventory:
            file.write(inv + "\n")  
 
def walk(inventory):
    items = _read(ITEMS_FILENAME)
    randItem = random.randint(0, len(items) - 1)
    invSize = len(inventory)
    max = 4
    
    while True:
        print("While walking down a path, you see a " + items[randItem])
        grab = str(input("Do you want to grab it? (y/n): "))

        if grab.lower() == "y":
            if invSize < max:
                inventory.append(items[randItem])
                print("You picked up " + items[randItem] + "\n")
                break
            else:
                print("You can't carry any more items. Drop something first.\n")
                break
            
        elif grab.lower() == "n":
            break
        else:
            print("\nInvalid option")
            break
 
def show(inventory):
    for i in range(len(inventory)):
        inv = inventory[i]
        print(str(i+1) + ". " + inv)
    print()

def drop_item(inventory):
    index = int(input("Number: "))   
    inv = inventory.pop(index - 1)
    write_inventory(inventory)
    print(inv + " was deleted.\n")

def display_title():
    print("The Wizard Inventory program\n")

def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")       # Walk to find items
    print("show - Show all items")          # Show items
    print("drop - Drop an item")            # Remove item
    print("exit - Exit program\n")          # Exit

if __name__ == "__main__":
    main()
