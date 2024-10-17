# fibonnanci 

def fibonnanci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fib_seq = [0,1]
    for i in range(2,n+1):
        fib_seq.append(fib_seq[-1] + fib_seq[-2]) 

    return fib_seq


n = 10
fib = fibonnanci(n)
print(f'{fib}')