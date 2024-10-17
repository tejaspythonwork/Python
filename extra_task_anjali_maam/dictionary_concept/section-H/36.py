# dictionary key frequency

def defination36():
    items = [
            {'type': 'fruit','name': 'apple'}, 
            {'type': 'fruit', 'name': 'banana'},
            {'type': 'vegetable', 'name': 'carrot'}
            ]
    
    combined_items = {}

    for i in items:
        i_type = i['type']
        i_name = i['name']

        if i_type in combined_items:
            combined_items[i_type].append(i_name)
        else:
            combined_items[i_type] = [i_name]       


    for item_type,item_name in combined_items.items():
        print(f'{item_type} = {item_name}')        

defination36()        