#!/usr/bin/env python3

import csv

FILENAME = "monthly_sales.csv"

def write_sales(sales):
    pass

def read_sales():
    pass

def view_monthly_sales(sales):
    pass

def view_yearly_summary(sales):
    pass

def edit(sales):
    pass

def display_menu():
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly  - View yearly sumary")
    print("edit    - Edit sales for a month")
    print("exit    - Exit program")
    print()  

def display_title():
    print("Monthly Sales program")
    print()

def main():
    display_title()
    display_menu()
    sales = read_sales()
    while True:
        command = input("Command: ")
        if command == "monthly":
            view_monthly_sales(sales)
        elif command == "yearly":
            view_yearly_summary(sales)
        elif command == "edit":
            edit(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
