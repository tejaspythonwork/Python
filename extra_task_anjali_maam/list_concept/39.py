# group element into sublist

def subset(num):
    if num == []:
        return [[]]
    
    x = subset(num[1:])
    return x + [[num[0]] + y for y in x ]


def defination39(number,n):
    return [x for x in subset(number) if len(x) == n ]


num = [1,2,3,4,5,6,7,8,9]
res = defination39(num,2)
print(res)