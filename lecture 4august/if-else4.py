hours = int(input('Enter the number of hours worked: '))
hourly = int(input('Enter the hourly pay rate: '))
hoursover = (hours-40)*1.5
alltime = hourly * 40

if hours > 40:
    print ('The gross pay is $',hoursover*hourly+alltime)
else:
    print ('The gross pay is $',hours*hourly)