# accept 5 numbers from user and check odd/even

for i in range(1,6):
    num1 = int(input('Enter number'))
    if num1 % 2 ==0:
        print(f'{num1} is even')
    else:
        print(f'{num1} is odd')