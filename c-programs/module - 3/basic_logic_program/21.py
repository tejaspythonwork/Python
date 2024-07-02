# swap 2 numbers using with and without variable

num1 = int(input('ENter 1st number'))
num2 = int(input('ENter 2nd number'))
# without 3rd variable
print(f'Before Swapping number = {num1} and {num2}')
num1 = num1 + num2 
num2 = num1 - num2 
num1 = num1 - num2 
print(f'After Swapping number = {num1} and {num2}')
print('===========================================')
print(f'Before Swapping number = {num1} and {num2}')
# with 3rd variable
temp = num1 
num1 = num2
num2 = temp

print(f'After Swapping number = {num1} and {num2}')