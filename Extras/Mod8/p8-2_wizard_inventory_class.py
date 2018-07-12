#!/usr/bin/env python3

import random

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

def display_title():
    print("The Wizard Inventory program")
    print()    

def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def read_inventory():
    inventory = []
    with open(INVENTORY_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            inventory.append(line)
    return inventory


def read_items():
    items = []
    
    with open(ITEMS_FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
    return items

 
def write_inventory(inventory):
    with open(INVENTORY_FILENAME, "w") as file:
        for row in inventory:
            file.write(row + "\n")

 
def walk(inventory):
    randItems = read_items()
    items = random.choice(randItems)
    print("While walking down the path, you see " + items + ".")
    grab = input("Do you want to grab it? (y/n): ")
    if grab.lower() == "y":
        if len(inventory) >= 4:
            print("You can't carry any more items. Drop something first.")
        else:
            inventory.append(items)
            write_inventory(inventory)
            print("You picked up " + items + ".")

  
def show(inventory):
    for i in range(len(inventory)):
        inv = inventory[i]
        print(str(i+1) + ". " + inv)
    print()

        
def drop_item(inventory):
    index = int(input("Number: "))

    if index < 1 or index > len(inventory):
        print("Invalid number. Please try again.")
    else:
        item = inventory.pop(index-1)
        write_inventory(inventory)
        print("You dropped " + item + ". ")
        print()


def main():
    display_title()
    display_menu()

    #items = read_items()   # check this file right away
    inventory = read_inventory()
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

if __name__ == "__main__":
    main()
