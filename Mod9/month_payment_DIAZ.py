#!/usr/bin/env python3

from decimal import Decimal
import locale as lc

def main():
    print("Monthly Payment Calculator")
    menu()

def menu():
    again = "y"
    line = "{:30}"

    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")

    while True:
        try:
            if again.lower() == "y":
                print("\nDATA ENTRY")
                
                loan_amount = Decimal(input(line.format("Loan amount:")))
                yearly_interest = Decimal(input(line.format("Yearly interest rate:")))
                years = Decimal(input(line.format("Years")))
                if loan_amount >= 0 or yealy_interest >= 0 or years >= 0:
                    ## Months
                    months = years * 12

                    ## Calculate and quantize
                    loan_amount = loan_amount.quantize(Decimal("1.12"))
                    yearly_interest = yearly_interest.quantize(Decimal("1.123"))

                    ## Payment formula
                    monthly_interest_rate = yearly_interest / 1200
                
                    payment = loan_amount * monthly_interest_rate / (1 -1 / \
                                (1 + monthly_interest_rate) ** months)
                    payment = payment.quantize(Decimal("1.12"))


                    ## Print results
                    results(loan_amount, yearly_interest, years, payment)

                    ## Continue while loop?
                    again = str(input("Continue? (y/n): "))
                else:
                    print("Invalid input.\n")
                
                
            elif again.lower() == "n":
                print("\nBye!")
                return False
            
            else:
                print("Invalid option\n")
                again = str(input("Continue? (y/n): "))

        except Exception as e:
            print("Invalid input.\n")

def results(loan_amount, yearly_interest, years, payment):
    line = "{:16} {:>16}"

    print("\nFORMATTED RESULTS")
    
    print(line.format("Loan amount:", lc.currency(loan_amount, grouping = True)))
    print("{:16} {:>11%}".format("Yearly interest rate:", yearly_interest/100))
    print(line.format("Years:", years))
    print(line.format("Monthly payment:", lc.currency(payment, grouping = True)))
    print()
    
def payment(loan_amount, months, monthly_interest_rate):
    pass

if __name__ == "__main__":
    main()
