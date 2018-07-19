from locale import *
from decimal import Decimal
import sys
setlocale(LC_ALL, '')

def _input():
    while True:
        try:
            amount = Decimal(input("Enter loan amount: "))
            rate = Decimal(input("Enter interest rate: "))
            rate = rate / 100
            interest_amount = amount * rate
            line = "{:16} {:>16}"

            print(line.format("Loan amount:", currency(amount)))
            print("{:16} {:16.3%}".format("Interest rate:", rate))
            print(line.format("Interest amount:", currency(interest_amount)))
            print()
            break

        except ValueError:
            print("Value error")
        except Exception as e:
            print(type(e), e)
            print("\nEncountered error, terminating program...")
            sys.exit()
def main():
    try:
        print("Interest Calculator\n")

        choice = "y"
        while choice.lower() == "y":
            _input()

            choice = str(input("Continue? (y/n): "))
            if choice.lower() == "n":
                break
            elif choice.lower() == "y":
                pass
            else:
                return False
    except Exception as e:
        print(type(e), e)
        print("\nEncountered error, terminating program...")
        sys.exit()

if __name__ == "__main__":
    main()
