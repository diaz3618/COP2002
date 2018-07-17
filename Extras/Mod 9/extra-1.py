from locale import *
setlocale(LC_ALL, '')

def _input():
    print("Interest Calculator\n")

    while True:
        try:
            amount = float(input("Enter loan amount: "))
            rate = float(input("Enter interest rate: "))
            rate = rate / 100
            interest_amount = 

            print("{:10} {:>15}".format("Loan amount:", currency(amount)))
            print("{:10} {:13.3%}".format("Interest rate:", rate))
            print("{:10} {:>15}".format("Interest amount:", currency(amount)))

        except ValueError:
            print("Value error")
def main():
    _input()

main()
