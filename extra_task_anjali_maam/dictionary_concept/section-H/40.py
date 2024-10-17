# group dictionary by values

def defination40():
    items = {
             'apple': 'fruit', 
             'banana':'fruit', 
             'carrot': 'vegetable'
             }
    
    group_dict = {}

    for key,val in items.items():
        if val in group_dict:
            group_dict[val].append(key)
        else:
            group_dict[val] = [key]           


    print(group_dict)
    
defination40()        