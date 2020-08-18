
firstname = input('Enter your firstname : ')
lastname = input('Enter your lastname : ')
idnum = (input('Enter your student ID number : '))
codeis = firstname[:3] + lastname[:3] + idnum[-3:]
print ('Your system login name is : ',codeis)

