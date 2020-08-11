keep_going = 'y'

# calculate a series of commission.
while (keep_going == 'y' or keep_going == 'Y'):
    wholesale_cost = int(input("Enter the item's wholesale cost: "))
    retail = wholesale_cost * 2.5
    print('Retail price: $',retail)
    keep_going = input('Do you have another item? (Enter y for yes) : ')