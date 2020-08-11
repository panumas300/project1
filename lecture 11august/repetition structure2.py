#This program calculates sales commissions.
# Create a variable to control the loop.
keep_going = 'y'

# calculate a series of commission.
while (keep_going == 'y' or keep_going == 'Y'):
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comn_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comn_rate

    # Display the commission.
    print('The commission is $', \
    format(commission, ',.2f'), sep='')

    #See if the user wants to do another one.
    keep_going = input('Do you want to calculate another' + \
                    'commission (Enter y for yes): ')