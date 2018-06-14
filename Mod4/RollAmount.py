import random

def diceRoll(num):
    low = 1
    high = 10
    count = 0
    
    for i in range (0, 601):
        dice = random.randint(low, high)

        if dice == 1:
            count += 1

            # Check each roll amount
            #print("\t" + str(num) + " was rolled: " + str(count) + " times")
    return count
    
def rollAmount(trialNum):
    count = 1
    print("="*41)
    print("Trial number " + str(trialNum))
    print("\nUsing the randint() function")
    
    for i in range (1, 7):
        roll = diceRoll(count)
        print("\t" + str(i) + " was rolled " + str(roll) + " times")
        count += 1
    
    

def main():
    print("Rolling a die\n")
    for i in range (1, 5):
        rollAmount(i)
    
if __name__ == "__main__":
    main()
