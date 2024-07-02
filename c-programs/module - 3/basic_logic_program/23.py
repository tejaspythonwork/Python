# swap number using multiplication and division
num1 = int(input('Enter 1st number'))
num2 = int(input('Enter 2nd number'))

print(f'Before Swapping = {num1} and {num2}')


num1 = num1 * num2
num2 = num1//num2
num1 = num1//num2

print(f'After Swapping = {num1} and {num2}')
