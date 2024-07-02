# to check number is perfect or not
# defination = positive integer that is equal to the sum 
# of its divisors - excluding number itself

def def50(n):
    if n < 1:
        return False
    
    sum_of_divisors = 0
    for i in range(1,n):
        if n % i == 0:
            sum_of_divisors = sum_of_divisors + i

    return sum_of_divisors == n

number = 28
check_perfect_number = def50(number)       
if check_perfect_number:
    print('Perfect')
else:
    print('Not Perfect')