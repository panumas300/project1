print('KPH\tMPH')
for num in range(60, 131, 10):
    MPH = (num*0.62137)
    print(num,'\t','%.1f'%MPH)