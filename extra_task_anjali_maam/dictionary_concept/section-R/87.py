# convert nested dictionaries to flattened dictionaries

def defination87(d,parent_key = '',sep = '.'):
    itm = {}
    for k,v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k  
        if isinstance(v,dict):
            itm.update(defination87(v,new_key,sep=sep))
        else:
            itm[new_key] = v

    return itm            


data = {'a': {'b': {'c': 1}}, 'd': 2}
res = defination87(data)
print(res)