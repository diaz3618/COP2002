#!/usr/bin/env python3

def main():
        menu()
        
        # Continue loop, or break
        again = "y"
        print()
        while again.lower() != "n" or again.lower() != "y":
            again = str(input("\nAdd another SKU? (y/n): "))
            print()
            if again.lower() == "n":
                print("\nBye!")
                break
            elif again.lower() == "y":
                inv()
                write("", True)
            print("[-] Invalid choice...\n")

def menu():
        print("Inventory app\n\nChoose an option")
        
        option = str(input("(r)Read file, (a)Add to file: "))
        while option.lower() != "r" or option.lower() != "a":
            print()
            if option.lower() == "r":
                openFile()
                option = str(input("(r)Read file, (a)Add to file: "))
            elif option.lower() == "a":
                w_or_a()
                inv()
            print("[-] Invalid choice...\n")
            
def inv():
        # Initialize
        total = 0
        length = 1
        lf = "n"

        # Ask once
        sku  = str((input("SKU: ")))
        lf = input("LF? (y/default = n): ")

        while True:
                # Linear Feet?
                if lf.lower() == "y":
                        length = int(input("Length: "))

                # Amount input
                amount = int(input("Amount: "))
                if amount == 0:
                        write("SKU: " + str(sku) + "\tQty. " + str(total) + "\n")
                        return False

                total += mult(length, amount)
                print("\tSKU: " + sku)
                print("\tTotal: " + str(total))
                

def write(info, writeNew = True):
        if writeNew == False:
                f = open("list.txt", "w+")
        f = open("list.txt", "a+")
        f.write(info)
        f.close()

def openFile():
        f = open("list.txt", "r")

        if f.mode == "r":
                listFile = f.read()
                print(listFile)
        
        

def w_or_a():
        # Write new or append to file
        fileOption = input("(w)Write new file, (a)Append to file?: ")

        while fileOption.lower() != "w" or fileOption.lower() != "a":
                if fileOption.lower() == "w":
                        write("",False)
                        break
                elif fileOption.lower() == "a":
                        write("")
                        break
                elif fileOption.lower() == "b":
                        menu()
                        break
                else:
                        print("[-] Invalid choice...\n")
                        fileOption = input("(w)Write new file, (a)Append to file?: ")

def mult(length, amnt):
        total = length * amnt
        return total
	
if __name__ == "__main__":
  main()
