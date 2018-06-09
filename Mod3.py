#!/usr/bin/env python3

def change(a):
    # Turn overall amount into cents
    totalCents = int(a * 100)
    
    # Initialize variables
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    
    # Calculate change
    for i in range (0, 3):
        count = 0  # 0 = quarters, 1 = dimes, 2 = nickels, 3 = pennies
        while totalCents != 0:
            if count == 0:
                quarter = int(totalCents // 25)
                totalCents = int(totalCents - (quarter * 25))
                count += 1
                
            elif count == 1:
                dime = int(totalCents // 10)
                totalCents = int( totalCents - (dime * 10))
                count += 1
                
            elif count == 2:
                nickel = int(totalCents // 5)
                totalCents = int(totalCents- (nickel * 5))
                count += 1
                
            elif count == 3:
                penny = int(totalCents // 1)
                totalCents = int(totalCents - (penny * 1))
                count +=1
                
            elif count >= 4:
                break
            
    # Print results
    print("\nQuarters:\t" + str(quarter))
    print("Dimes:\t\t" + str(dime))
    print("Nickels:\t" + str(nickel))
    print("Pennies:\t" + str(penny))
    
def main():
    print("Change Calculator")
 
    choice = "y"
    while choice.lower() == "y":
        amount = float(input("\nEnter dollar amount (for example, .56, 7.85): "))
 
        # Change function
        change(amount)
 
        # Continue loop, or break
        while choice != "n" or choice != "y":
            choice = input("\nContinue? (y/n): ")
            if choice.lower() == "n":
                print("\nBye!")
                break
            print("please enter y or n")
            if choice.lower() == "y":
                break
 
if __name__ == "__main__":
    main()
