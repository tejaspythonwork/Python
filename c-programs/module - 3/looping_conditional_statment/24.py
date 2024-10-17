# series programs - 1.
# 1 + 2 + 3 + 4 + 5 + ..... + n


def defination24(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum + i

    print(sum)



n = int(input('please enter digit: '))
defination24(n)        