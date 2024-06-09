# get factorial of given number

def factorial(n): 
    if n == 1 or n==0:
        return 1
    else: 
        return n * factorial(n-1)


n = int(input('Enter Number'))
result = factorial(n)
print(f'Factorial of {n} is {result}')
