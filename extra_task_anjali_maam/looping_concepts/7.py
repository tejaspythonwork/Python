# find prime numbers in range
def is_prime(n):
    if n <=1:
       return False
    for i in range(2,int(n**0.5) + 1 ):
        print(f'i1 = {i}')
        if n % i == 0:
            print(f'---i2--- = {i}')
            return False 
    return True            


    

def defination7(start,end):
    primes = [num for num in range(start,end + 1) if is_prime(num) ]
    print(primes)


res = defination7(1,10)

