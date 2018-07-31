#!/usr/bin/env python3
from decimal import Decimal
import locale as lc

def main():
    print("Interest Calculator\n")

    again = "y"
    while again.lower() == "y":
        IO()
        again = str(input("\nContinue? (y/n): "))

        while again.lower() != "y" or again.lower() != "n":
            if again.lower() == "n":
                print("\nBye!")
                break
            elif again.lower() == "y":
                break
            else:
                print("Invalid option, enter y or n\n")
            again = str(input("\nContinue? (y/n): "))

def IO():
    line = "{:20} {:>}"

    ## Input
    loan_amount = Decimal(input(line.format("Enter loan amount:", "$")).replace(",",""))
    rate = Decimal(input(line.format("Enter interest rate:", "%")))
    result(loan_amount, rate)

def result(loan, rate):
    line = "{:<22} {:>}"
    payments = loan * (rate/100)
    
    ## Set USD
    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")

    ## Quantize
    loan = loan.quantize(Decimal("1.12"))
    rate = rate.quantize(Decimal("1.123"))
    payments = payments.quantize(Decimal("1.12"))

    ## Output
    print(line.format("\nLoan amount:", lc.currency(loan, grouping = True)))
    print("{:<22} {:>%}".format("Interest rate:", rate/100))
    print(line.format("Interest amount:", lc.currency(payments, grouping = True)))

if __name__ == "__main__":
    main()
