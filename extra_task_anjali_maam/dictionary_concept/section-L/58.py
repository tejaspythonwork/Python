# extract keys with specific items

def defination58():
    data = {
        'item1': 10, 
        'item2': 20,
        'other1': 30,
        'item3': 45
        }
    
    for k,v in data.items():
        if k.startswith('item'):
            print(f'{k} = {v}')

defination58()            