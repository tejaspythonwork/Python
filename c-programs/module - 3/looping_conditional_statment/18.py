# multiplication table for n

def print_multiplication_table(n):
    for i in range(1,11):
        # for  n in range(1,11):
            print(f'{n} x {i} = {n * i}')


result = print_multiplication_table(10)            