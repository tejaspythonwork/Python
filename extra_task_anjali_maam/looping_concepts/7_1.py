# find range of prime numbers

def is_prime(n):
    if n <=1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False

    return True 


def defination_7_1(start,end):
    primes = [ n for n in range(start,end + 1) if is_prime(n) ]
    return primes


res = defination_7_1(1,15)
print(res)