#!/usr/bin/env python3

"""
Project Statement
The following program should display the cost of an item in an
end-of-year sale. An item that was initially on sale for 20%
is now discounted further. But the program doesn't work in the
store owner's favor. Find the logic error and fix it.
"""

def main():
    cost = float(input("enter original cost: "))
    discount1 = 0.20
    
    discount2 = float(input("enter the deep discount: "))
    discount2 = discount2 / 100
    sale_price1 = cost - (cost*discount1)
    
    print("\nOriginal cost: $", cost)
    print("\nAfter a discount of " + str(discount1 * 100) + "%, the item costs $" + str(sale_price1))

    sale_price2 = sale_price1 - (sale_price1 * discount2)

    print("After a discount of " + str(discount1 * 100) + "% and then an additional")
    print("discount of " + str(discount2 * 100) + "%, the item costs $" + str(sale_price2))
    
# if started as the main module, call the main function
if __name__ == "__main__":
    main()

