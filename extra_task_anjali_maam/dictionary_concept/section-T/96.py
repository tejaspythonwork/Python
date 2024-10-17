# create dictionaries with 
# default Factory function

from collections import defaultdict

example_default_dict = defaultdict(list)


example_default_dict['fruits'].append('Apple'),
example_default_dict['fruits'].append('Banana'),
example_default_dict['fruits'].append('Cherry')


example_default_dict['veg'].append('Carrot'),
example_default_dict['veg'].append('Spinach'),


for k,v in example_default_dict.items():  
    print(f'{k} are = {v}')