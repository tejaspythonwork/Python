# extract subset of dictionaries

def defination65():
    data = {
        'a': 1, 
        'b': 2, 
        'c': 3, 
        'd': 4,
        }
    
    subset = {(k,v) for k,v in data.items() if k == 'b' or k == 'd'}
    print(subset)


defination65()
