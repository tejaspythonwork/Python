# wap to find maximum among 3 numbers
print('Find Max Among 3 numbers')
num1 = int(input('Please enter first number'))
num2 = int(input('Please enter second number'))
num3 = int(input('Please enter third number'))

max_num = num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num1 and num2 > num3 else num3) 
print(f'Maximum number = {max_num}')
