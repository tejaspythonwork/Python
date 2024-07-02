# combine 2 dictionary and if key are same then
# perform sum of its 2 values

dict1 = {'a':100,'b':200,'c':300}
dict2 = {'a':300,'b':200,'d':400}
result_dict = {}
all_keys = set(dict1).union(set(dict2))

print('All Keys')
print(all_keys)

for k in all_keys:
    value1 = dict1.get(k)
    value2 = dict2.get(k)
    print(f'v1 = {value1} key = {k}')
    print(f'v2 = {value2} key = {k}')
    if isinstance(value1,(int,float)) and isinstance(value2,(int,float)):
        result_dict[k] = value1 + value2
    elif isinstance(value1,(str)) and isinstance(value2,(str)):
        result_dict[k] = value1 + value2
    elif value1 is None and value2 is not None:
        result_dict[k] = value2
    elif value1 is not None and value2 is None:
        result_dict[k] = value1              
    else:
        result_dict[k] = f'{value1 or ''} {value2 or ''}' 

print('After Addition of dictionaries new Dictionaries = ')
print(f'{result_dict}')           