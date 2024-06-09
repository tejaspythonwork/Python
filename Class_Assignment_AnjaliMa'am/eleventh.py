# enter 5 numbers from user and check either positive or negative

for i in range(1,6):
    i = int(input(f'Enter Number {i}:'))
    if i < 0:
        
        print('Number is negative ')
    else: 
        print('Number is positive ') 
