def main():
    boss = 'Y'
    
    print('Choose the menu')
    print('1.show file')
    print('2.write name')

    menu = int(input(': '))
    while boss == 'Y' or boss == 'y' :
        if menu == 1:
           choose_one()
        elif menu == 2:
           choose_two()
        else:
           print('Wrong!')
        bosss = input('Want to do this again ?:(press Y or N) ')
        if boss == 'Y' or boss == 'y' :
            print('Choose the menu')
            print('1.show file')
            print('2.write name')
            menu = int(input(': '))

 
def choose_one():
    infile = open('september 15/myfriends.txt','r')

    file_contents = infile.read()
dfhd
    infile.close()

    print(file_contents)
    
    


def choose_two():
    infile = open('september 15/myfriends.txt','a')

    name = input('Enter your name : ')
    infile.write(name + '\n')

    infile.close()

main()