# find the key with longest value

def defination95():
    data = {
    'a': 'apple', 
    'b': 'banana',
    'c': 'cherry12345'
    }

    res = lambda x : len(x[1])
    result = max(data.items(),key=res)
    print(result)

defination95()    