#!/usr/bin/env python3
'''
Daniel Diaz Santiago
COP2002.002
This program checks whether the given number is prime or not, and shows its factors.
'''


def validate(num):
    if num <= 0:
        print("\nNumber must be bigger than 0.\n\n")
        main()


def isPrime(num):
    if num <= 2:
        return True

    for i in range(2, num):
        if num % i * i == 0:
            return False
    return True


def factor(num):
    print("The factor of your numbers are:")

    # Factor number
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            print(str(i))

    # Check if variable "a" is prime
    if isPrime(num) == True:
        print(str(num) + " is a prime number.")
    else:
        print(str(num) + " is not a prime number.")
        print("It has " + str(count) + " factors.")


def main():
    print("Prime Number Checker\n")

    choice = "y"
    while choice.lower() == "y":
        # Ask for a number to factor
        num = int(input("Please enter a integer between 1 and 5,000: "))
        validate(num)

        # Factor function
        factor(num)

        while choice.lower() != "n" or choice.lower() != "y":
            choice = input("\nTry again? (y/n): ")
            print()
            if choice.lower() == "n":
                print("\nBye!")
                break
            elif choice.lower() == "y":
                break
            print("please enter y or n")


if __name__ == "__main__":
    main()
