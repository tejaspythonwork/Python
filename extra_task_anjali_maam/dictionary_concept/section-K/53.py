# sort dictionaries by key

def defination53():
    data = {'b': 2, 'a': 1, 'c': 3}
    s_lambda = lambda x : (x[0],x[1])
    result = list(sorted(data.items(),key=s_lambda))
    print(dict(result))

    

defination53()    