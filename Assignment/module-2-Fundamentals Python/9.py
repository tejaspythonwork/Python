# sum of 3 given integers if 
# 2 values are equal sum will be 0

num1 = int(input('Enter 1st number'))
num2 = int(input('Enter 2nd number'))
num3 = int(input('Enter 3rd number'))

if num1 == num2 or num2 == num3:
    sum = 0
    print('Two numbers are equal so sum is zero')
else: 
    sum = num1 + num2 + num3
    print(f'sum = {num1} + {num2} + {num3} = {sum}')
