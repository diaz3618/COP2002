#!/usr/bin/env python3

def isPrime(a):
	if a <= 2:
		return True
	
	for i in range(2, a):
		if a % i * i == 0:
			return False
	return True

def factor(a):
	print("The factor of your numbers are:")
	
	# Factor number
	for i in range(1, a+1):
		if a % i == 0:
			print(str(i))
	
	# Check if variable "a" is prime
	if isPrime(a) == True:
		print(str(a) + " is a prime number.")
	else:
		print(str(a) + " is not a prime number.")

def main():
	print("Prime Number Checker\n")
	
	choice = "y"
	while choice.lower() == "y":
		# Ask for a number to factor
		num = int(input("Please enter a integer between 1 and 5,000: "))
		
		# Factor function
		factor(num)
		
		while choice.lower() != "n" or choice.lower() != "y":
			choice = input("Try again? (y/n): ")
			print()
			if choice.lower() == "n":
				print("\nBye!")
				break
			print("please enter y or n")
			if choice.lower() == "y":
				break
	
if __name__ == "__main__":
	main()
