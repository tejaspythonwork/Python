# Accept 2 numbers check it's size and find sum

num1 = int(input('Enter First Number'))
num2 = int(input('Enter Second Number'))

num1size = len(str(num1))
num2size = len(str(num2))
sum = num1 + num2
print(f'size of {num1} is {num1size}')
print(f'size of {num2} is {num2size}')
print(f'sum of {num1} + {num2} is {sum}')