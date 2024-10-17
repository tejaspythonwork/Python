# remove dup values

def defination69():
    data = {'a': 1, 'b': 2, 'c': 1}
    new_dict = {}

    for k,v in data.items():
        if v not in new_dict.values():
            new_dict[k] = v
        else:    
            continue

    print(new_dict)

defination69()    