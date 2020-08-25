def main():
  print('The sum of num1 and num2 is')
  num1 = int(input('Enter num1 : '))
  num2 = int(input('Enter num2 : '))
  show_sum(num1, num2)

def show_sum(number1, number2):
  result = number1 + number2
  print('result is : ',result)

main()