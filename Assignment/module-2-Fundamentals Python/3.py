# fibonacci series

def fibonancci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a + b

input_number = int(input('Please enter number')) 
print(f'Fibonancii Series of nummber {input_number} is below')
int_series = fibonancci(input_number)
      
for fib_number in fibonancci(input_number):
    print(fib_number,end= ' ')