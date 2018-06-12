#!/usr/bin/env python3

def validate(a):
    if a <= 0:
        print("\n\n[-] Amount must be more than 0\n")
        main()
    
def shippingCost(a):
    shipping_cost = 0
    
    if a < 30.00:
        shipping_cost = 5.95
        
    elif a > 30 and a < 49.99:
        shipping_cost = 7.95
        
    elif a > 50.00 and a < 74.99:
        shipping_cost = 9.95
        
    elif a > 75.00:
        return shipping_cost

    return shipping_cost

def main():
    tax = 0.625
    print("Total cost", "\n" + "=" * 45)
    totalCost = float(input("Enter the total cost of your order: $ "))

    # Validate
    validate(totalCost)

    # Spacer
    print("=" * 45)
    
    print("Cost of items ordered:\t$ " + str(round(totalCost, 2)))
    print("Subtotal (with tax):\t$ " + str(round(totalCost + (totalCost * tax), 2)))

    # Shipping cost
    shipping_cost = shippingCost(totalCost + (totalCost * tax))
    print("Shipping cost:\t\t$ " + str(shipping_cost))

    # Total owed
    print("\nTotal owed:\t\t$ " + str(round((totalCost + (totalCost * tax)) + shipping_cost, 2)))

if __name__ == "__main__":
    main()
