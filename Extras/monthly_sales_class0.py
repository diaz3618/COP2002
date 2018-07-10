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
    # [i][0] == Months
    sales = read_sales()
    for i in range(0, len(sales)):
        print(sales[i][0] + " - " + str(sales[i][1]))
    print()

def view_yearly_summary(sales):
    # [i][1] == Monthly # amount
    total = 0
    for i in range(0, len(sales)):
        total += int(sales[i][1])

    print("Yearly total:\t\t" + str(total))
    print("Monthly average:\t" + str(total / len(sales)))
    print()

def edit(sales):
    i = 0
    month = str(input("Three-letter Month: "))
    sales_amount = str(input("Sales Amount: "))

    
    while True:
        if  sales[i][0] == month:
            print(sales[i][0] + "\tFound it!")
            sales.remove(sales[i][1])
            sales.insert(i, sales_amount)
            if sales[i][1] == sales_amount:
                print("Sales amount for " + str(sales[i][0]) + " was modified.")
            else:
                print("Value was not changed\n")
            break
        else:
            print(sales[i][0] + "\tNot that one!")
            i += 1

## WORK IN PROGESS
def edit2(sales):
    sales_list = []
    i = 0
    month = str(input("Three-letter Month: "))
    sales_amount = str(input("Sales Amount: "))

    while True:
        if sales[i][0].lower() == month.lower():
            print(sales[i][0] + "\tFound it!")
            sales.remove(sales[i])
            sales.insert(i, month)
            sales.insert(i, sales_amount)
            
        if sales[i][1] == sales_amount:
                print("Sales amount for " + str(sales[i][0]) + " was modified.")
            else:
                print("Value was not changed\n")
            break
        else:
            print(sales[i][0] + "\tNot that one!")
            i += 1
            

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
            edit2(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
