#!/usr/bin/env python3
from decimal import Decimal
import locale as lc

def main():
    print("Monthly Payment Calculator")
    IO()
    
def IO():
    line = "{:22}"
    again = "y"
    
    while again.lower() == "y":
        try:
            print("\nDATA ENTRY")

            ## Input
            loan_amount = Decimal(input(line.format("Loan amount:")))
            yearly_interest = Decimal(input(line.format("Yearly interest rate:")))
            years = Decimal(input(line.format("Years:")))

            ## Calculate monthly payments
            calculate(loan_amount, yearly_interest, years)

            ## Run again?
            while again.lower()!= "n" or again.lower() != "y":
                again = str(input("Continue? (y/n): "))
                
                if again.lower() == "n":
                    print("\nBye!")
                    break
                elif again.lower() == "y":
                    break
                else:
                    print("Invalid choice.\n")
                    
        except Exception as e:
            print(type(e), e)
            print("Invalid input")
        except KeyboardInterrupt:
            print("\nBye!")
            break

def calculate(loan_amount, yearly_interest, years):
    ## Set USD
    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")

    """
    Loan amount, yearly interest,
    and amount of years validation.
    """
    if loan_amount >= 0 and yearly_interest > 0 and years >= 1:
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
                    
    else:
        print("Invalid input.\n")
        
def results(loan_amount, yearly_interest, years, payment):
    line = "{:18} {:>18}"

    print("\nFORMATTED RESULTS")
    
    print(line.format("Loan amount:", lc.currency(loan_amount, grouping = True)))
    print("{:18} {:>15%}".format("Yearly interest rate:", yearly_interest/100))
    print(line.format("Number of years:", years))
    print(line.format("Monthly payment:", lc.currency(payment, grouping = True)) + "\n")

if __name__ == "__main__":
    main()
