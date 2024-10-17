# series 
# 2.
# (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n)


def defination25(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum + (i*i)

    print(sum)


n = int(input('please enter digit: '))
defination25(n)        