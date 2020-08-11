import random

keep_going = 'y'

# calculate a series of commission.
while (keep_going == 'y' or keep_going == 'Y'):

    print("What is my magic number ( 1 to 100) ?")
    mynumber = random.randint(1, 100)
    ntries = 1
    yourguess = -1
    while (ntries < 7 and yourguess != mynumber):
        msg = str(ntries) + ">>"
        if (ntries == 6) :
            print('This is your last chance!!')
        yourguess = int(input(msg))
        if (yourguess > mynumber) :
            print("--> too high")
        if (yourguess < mynumber) :
            print("--> too low")
        ntries += 1

    if yourguess == mynumber :
        print("Yes! it's",mynumber)
    else :
        print("Sorry! my number is",mynumber)

    keep_going = input('Do you want to calculate another' + \
                    'commission (Enter y for yes): ')