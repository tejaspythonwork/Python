# combine multiple dictionaries into one

from collections import defaultdict


def defination76():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4} 
    dict3 = {'d': 5}

    dict4 = defaultdict(int)

    for d in (dict1,dict2,dict3):
        for k,v in d.items():
            dict4[k] = dict4[k] + v

    print(dict(dict4))

defination76()            