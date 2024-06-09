# read value of an integer
# if value is < integer => value is greater than zero
# if value is > integer and valiue == 0 => value is less than zero

m = int(input('Enter Integer: '))
if m < 0:
    n=1
elif m>0 or m ==0:
    n=0

if n == 1:
    print('m is larger than zero')
else:   
    print('m is less than zero')