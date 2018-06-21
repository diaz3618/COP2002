import random as r
MAX = 10

def game():
    print("I\'m thinking of a number from 1 to " + str(MAX) + "\n")
    num = r.randint(1, MAX)
    count = 0
    
    while True:
        guess = int(input("Your guess: "))

        if num > guess:
            print("Too low.")
            count += 1
        elif num < guess:
            print("Too high.")
            count += 1
        else:
            count += 1
            print("You guessed it in " + str(count) + " times")
            return False
    
def main():
    print("Guess the number!\n")
    choice = "y"
    while choice.lower() == "y":
        game()

        while choice.lower() != "n" or choice.lower() != "y":
            choice = input("\nWould you like to play again? (y/n): ")
            print()
            if choice.lower() == "n":
                print("\nBye!")
                break
            elif choice.lower() == "y":
                break
            print("please enter y or n")    

if __name__ == "__main__":
    main()
