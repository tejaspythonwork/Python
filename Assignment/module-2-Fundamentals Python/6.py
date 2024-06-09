# swap two numbers with and without 3rd variable

print('Interchange numbers with 3rd variable')
num1 = int(input('Enter First Number'))
num2 = int(input('Enter Second Number'))

print(f'Before swap number 1 = {num1} number 2 = {num2}')
# with third variable

temp = num1
num1 = num2
num2 = temp
print('with 3rd variable')
print(f'After swap number 1 = {num1} number 2 = {num2}')

# without third variable
print('-------------------------------------------')
print('Interchange numbers without 3rd variable')
num1 = int(input('Enter First Number'))
num2 = int(input('Enter Second Number'))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2 

print('without 3rd variable')
print(f'After swap number 1 = {num1} number 2 = {num2}')
