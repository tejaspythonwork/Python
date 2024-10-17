# find min value

def defination61():
    data = {'a': 5, 'b': 3, 'c': 9,'d' : -111999}
    min_val = min(data.items(),key= lambda x : x[1])
    print(min_val)

defination61()