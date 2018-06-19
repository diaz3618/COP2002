#!/usr/bin/env python3

"""
Project Statement
The following program contains one syntax error, one runtime error, and
one logic error. Find and correct all three so that the application functions correctly. 
"""

TAX = 0.06

def sales_tax(amt):
    sale = amt + (amt * TAX)
    return sale

def main():
    print("Welcome to the 6% tax calculator!\n")
    total = int(input("Please enter the total amount: "))
    print("The total amount after tax is: ", str(sales_tax(total)))
    
if __name__ == "__main__":
    main()
