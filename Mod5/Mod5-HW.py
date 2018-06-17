import random

def IO():
	max = int(input(("Enter the upper limit for the range of numbers: ")))
	print("I\'m thinking of a number between 1 and " + str(max) + "\n")
	
	return max

def guess(max):
	# Keep track of the amount of tries
	count = 0
	# Generate a random number
	num = random.randint(1, max)
	
	while True:
		guess = int(input("Your guess: "))
		# Guessed correctly
		if guess == num:
			count += 1
			print("You guessed it in " + str(count) + " tries.")
			return
		# Guessed num is too low
		elif guess < num:
			print("Too low.")
			count += 1
		# Guessed num is too high
		elif guess > num:
			print("Too high.")
			count += 1

def game():
	print("Guess the number!\n")
	choice = "y"
	while choice.lower() == "y":
		max = IO()  # Max number (1, max)
		guess(max)
		
		# Continue loop, or break
		print()
		while choice.lower() != "n" or choice.lower() != "y":
			choice = input("Play again? (y/n): ")
			
			if choice.lower() == "n":
				print("\nBye!")
				break
				
			elif choice.lower() == "y":
				print()
				break
			
			print("please enter y or n\n")

def main():
	game()
	
if __name__ == "__main__":
	main()
