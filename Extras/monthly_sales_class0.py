#!/usr/bin/env python3

import csv

FILENAME = "monthly_sales.csv"

def write_sales(sales):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)

def read_sales():
    sales = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)
    return sales

def view_monthly_sales(sales):
    sales = read_sales()
    for i in range(0, len(sales)):
        print(sales[i][0] + " - " + str(sales[i][1]))
    print()

def view_yearly_summary(sales):
    _sales = read_sales()
    count = 0
    total = 0
    for i in range(0, len(_sales)):
        total += int(_sales[i][1])

    print("Yearly total:\t\t" + str(total))
    print("Monthly average:\t" + str(total / len(sales)))
    print()

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
