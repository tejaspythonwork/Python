# find top frequent n values

def defination98():
    data = {
        'a': 3, 
        'b': 1, 
        'c': 3, 
        'd': 2,
        'e': 3
        }
    for k,v in data.items():
        print(f'{k} occures for {v} times')

    res = lambda x : x[1]
    result = sorted(data.items(),key=res,reverse=True)
    print(result)

    for k,v in dict(result).items():
        print(f"{k} occures for {v} times")

defination98()