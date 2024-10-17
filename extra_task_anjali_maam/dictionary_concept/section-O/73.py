# sort dictionaries by ascending order by values

def defination73():
    data = {'a': 3, 'b': 1, 'c': 2}
    res = sorted(data.items(),key= lambda x:x[1])
    print(res)

defination73()    