#!/usr/bin/env python3

import random

ITEMS_FILENAME = "wizard_all_items.txt"
INVENTORY_FILENAME = "wizard_inventory.txt"

def read_inventory():
    pass

def read_items():
    pass
 
def write_inventory(inventory):
    pass
 
def walk(inventory):
    print("While walking down a path, you see a ")
 
def show(inventory):
    pass

def drop_item(inventory):
    pass


















def main():
    display_title()
    display_menu()

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

def display_title():
    print("The Wizard Inventory program\n")

def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")  # Show items
    print("grab - Grab an item")    # Add items
    print("edit - Edit an item")    # Update item name
    print("drop - Drop an item")    # Remove item
    print("exit - Exit program\n")  # Exit

if __name__ == "__main__":
    main()
