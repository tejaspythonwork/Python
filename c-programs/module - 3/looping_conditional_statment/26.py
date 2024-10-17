# series
# 3.
# (1)+ (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)

def defination26(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i):
            print(f'i = {i} j = {j}')
            sum = sum + j
    print(sum)    



n = int(input('please enter digit: '))
defination26(n)            