# group data by multiple keys

from collections import defaultdict


data = [
        {'category': 'fruit',
             'type': 'citrus', 
             'item': 'orange'}, 
         
        {'category': 'fruit',
             'type': 'berry', 
             'item': 'strawberry'},
        
        {'category': 'vegetable', 
             'type': 'root', 
             'item': 'carrot'},

        {'category': 'fruit',
             'type': 'berry', 
             'item': 'rasberry'},

        
        {'category': 'fruit',
             'type': 'citrus', 
             'item': 'mango'}, 
       ]


grouped_data = defaultdict(lambda:defaultdict(list))

for entry in data:
    cat = entry['category']
    typ = entry['type']
    itm = entry['item']


    grouped_data[cat][typ].append(itm)

    

grouped_data = {k:dict(v) for k,v in grouped_data.items() }
print(grouped_data)    

