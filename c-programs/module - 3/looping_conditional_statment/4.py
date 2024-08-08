# wap to print table up to given numbers

def print_multiplication_table(n):
    for i in range(1,n+1):
        print(f'Multiplication Table  For {i}')
        for j in range(1,11):
            print(f'{i} x {j} = {i * j}')
        print() 



num = int(input('Enter A Multiplication digit:'))
print_multiplication_table(num)           