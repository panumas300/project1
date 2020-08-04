score1 = int(input('Enter the score for test 1: '))
score2 = int(input('Enter the score for test 2: '))
score3 = int(input('Enter the score for test 3: '))
average = (score1 + score2 + score3) / 3
print('\nThe average score is ',average)

if average >= 95:
    print('Congratulations ! \n That is a great average!')
    