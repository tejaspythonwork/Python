# sum of all divisors of a number


def sum_of_all_divisors(n):
    total_sum = 0
    
    
    for i in range(1,n + 1):
        if n % i == 0:
            total_sum = i+ total_sum


    return total_sum


number = int(input('Enter Number To Sum Of all its divisors'))
res63 = sum_of_all_divisors(number)
print(res63)
