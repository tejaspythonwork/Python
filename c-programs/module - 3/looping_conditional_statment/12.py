# find armstrong number


number = 153
sum = 0
temp = number
while temp > 0:
   dgt = temp % 10
   sum = dgt ** 3 + sum
   temp = temp.__floordiv__(10)

if number == sum:   
   print(f'Armstrong Number =  {number}')
else:
   print(f'Not Armstrong Number = {number}')