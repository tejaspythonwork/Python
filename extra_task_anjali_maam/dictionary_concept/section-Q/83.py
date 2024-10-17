# remove dictionaries with null values

def defination83():
    data = {'a': 1, 
            'b': None, 
            'c': 2, 
            'd': None}
    

    for k,v in list(data.items()):
        if v == None:
            data.pop(k)

    print(f'without null values = {data}')        

defination83()    