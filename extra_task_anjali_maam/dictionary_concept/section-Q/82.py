# merge dictionaries with list values

def defination82():
    dict1 = {'a': [1, 2], 'b': [3, 4]}
    dict2 = {'a': [5], 'c': [6]}

    merged = {k: dict1.get(k,[]) + dict2.get(k,[])  for k in dict1 | dict2  }
    print(merged)

defination82()    
