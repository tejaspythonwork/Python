# extract subdictionaries

def defination81():
    data = {'a': 1, 
            'b': 2, 
            'c': 3, 
            'd': 4
            }
    print('Extracted dictionaries with keys and values')
    for key,val in data.items():
        if key == 'b' or key == 'c':
            print(f'key = {key} and val = {val}')

defination81()            