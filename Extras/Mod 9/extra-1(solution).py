#!/usr/bin/env python3

from decimal import Decimal     # import the Decimal class from the decimal module
import locale as lc             # import the locale module into the lc namespace
                                # a namespace is an area in main memory that holds a module 
def main():
    print("Interest Calculator")
    print()
    
    choice = "y"
    while choice.lower() == "y":
        # get user input
        # Use the constructor of the Decimal class to construct Decimal objects
        # from string values
        # a backslash to show that a line is continued
        loan_amount = \
            Decimal(input("Enter loan amount:   "))
        interest_rate = \
            Decimal(input("Enter interest rate: "))
        print()

        # quantize the entries
        # a method to round decimal values to the specific number
        # of decimal places
        # 1.12 specify two decimal places
        # the argument can be any value that has the right number of decimal places
        # by default, quantize() method use the ROUND_HALF_EVEN
        # ex) 10.005 -> 10.00 (5 is preceded by even)
        # ex) 10.015 -> 10.01 (5 is preceded by odd)

        loan_amount = loan_amount.quantize(Decimal("1.12"))
        interest_rate = interest_rate.quantize(Decimal("1.123"))

        # calculate and quantize the interest amount
        interest_amount = loan_amount * (interest_rate / 100)
        interest_amount = interest_amount.quantize(Decimal("1.12"))        

        # format and display the results
        # formatting for currency
        # Before calling currency() or format()
        # need to set the locale using setlocale()
        # LC_ALL to apply this locale to all categories
        # with an empty string, Python attemps to use the default locale
        # for the user's computer 
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C": # fails
            lc.setlocale(lc.LC_ALL, "en_US") # English/United States
        # The format specificaiton - a string
        line = "{:16} {:>16}"
        # followed by a period and the format() method of a string
        # currency() to format specific value
        # first argument specifies the monetary value
        # optional grouping argument to Ture to separate the thousands 
        print(line.format("Loan amount:",
            lc.currency(loan_amount, grouping=True)))
        print(line.format("Interest rate:",
            str(interest_rate) + "%"))
        print(line.format("Interest amount:",
            lc.currency(interest_amount, grouping=True)), "\n")

        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
