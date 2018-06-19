#!/usr/bin/env python3

"""
Project Statement
The application has a logic error. It returns and displays an inappropriate result.
Analyze the code, set an appropriate breakpoint, and utilize the debugger to watch
the progression of the local variables. Isolate the error and correct the code.
"""

TAX = 0.06

def sales_tax(amt):
    amt = amt + (amt * 0.06)
    return amt

def purchases():
    go = 1
    total = 0
    go = int(input("Please enter an amount followed by enter, or 0 (zero) to quit: "))
    
    while go != 0:
        total += go
        go = int(input("Next: "))
    total = sales_tax(total)
    
    return total

def main():
    print("Welcome to the 6% tax calculator!\n")
    print("The total amount after tax is: ", purchases(), "\n")

    more = "y"
    while more == "y":
        print("The total amount after tax is: ", purchases(), "\n")
        more = input("Would you like to calculate another? (y/n): ")
    print("Thanks, bye!")    
    
if __name__ == "__main__":
    main()
