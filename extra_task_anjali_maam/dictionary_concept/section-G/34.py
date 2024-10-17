# filter dictionaries based on keys

def defination34():
    dict1 = {}
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    l_func = lambda x: x[0].startswith('a')
    res = list(filter(l_func,data.items()))
    print(res)
    dict1 = dict(res)
    print(dict1)



defination34()