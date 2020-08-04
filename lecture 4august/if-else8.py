print ('Please select operation -')
print ('1.Add')
print ('2.Subtract')
print ('3.Multiply')
print ('4.Divide')
choice = int(input('Select operations form 1, 2, 3, 4, : '))
num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
if choice == 1:
    num3 = num1 + num2
    print (num1,'+',num2,'=',num3)
elif choice == 2:
    num3 = num1 - num2
    print (num1,'-',num2,'=',num3)
elif choice == 3:
    num3 = num1 * num2
    print (num1,'*',num2,'=',num3)
else :
    num3 = num1 / num2
    print (num1,'/',num2,'=',num3)