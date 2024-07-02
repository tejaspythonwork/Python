# calculate factorial of number

def prg48(num):
    if num < 0:
      return 'Invalid Input'
    res = 1            
    for i in range(2,num  + 1):
            res = res * i

    return res


n = int(input('Enter integer to calculate factorial : '))
fact = prg48(n)
print(f'Factorial = {fact}')