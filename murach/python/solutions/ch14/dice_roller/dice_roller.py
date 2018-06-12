from dice import Dice, Die

def main():
    print("The Dice Roller program")
    for i in range(1, 7):
        die = Die()
        die.value = i
        print(die.image)    
    print()

    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Die objects and add to Dice object
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    while True:        
        # roll the dice
        dice.rollAll()
        print("YOUR ROLL: ")
        for die in dice.list:
            print(die.image)
        print()
        print("TOTAL:", dice.getTotal())
        print()

        choice = input("Roll again? (y/n): ")
        if choice != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
