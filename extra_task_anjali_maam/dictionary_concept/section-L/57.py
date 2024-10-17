# find common values in dictionaries

def defination57():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'x': 2, 'y': 3}

    for k,v in dict1.items():
        for k1,v1 in dict2.items():
         if v == v1:
            print(f'Common values in both dictionaries: ')
            print(f'{k} = {v}')
            print(f'{k1} = {v1}')


defination57()
