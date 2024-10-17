# find most frequent value

from collections import Counter

def defination88():
    data = {'a': 'apple', 
            'b': 'banana',
            'c': 'apple', 
            'd': 'cherry',
            'axz': 'apple'
            }
    
    new_dict = {}
    for k,v in data.items():
        if v not in new_dict:
            new_dict[v] = [k]
        else:
            new_dict[v].append(k)

    print(new_dict)

defination88()    
