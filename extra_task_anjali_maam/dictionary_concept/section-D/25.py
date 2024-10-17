# created dictionaries from list

def defination25():
    keys = ['name', 'age', 'city'] 
    values = ['John', 25, 'New York']

    dict1 = {k:v for k,v in zip(keys,values)}
    print(dict1)

defination25()    