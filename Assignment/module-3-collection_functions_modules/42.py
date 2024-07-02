# python program to print all unique values in dictionaris

dict1 = {'a' : 111,'b' : 221,'c':101,'D' : 1,1:234,3:111,4:221}
unique_dict = set(dict1.values())
unique_val_dict = {}
value_count = {}

for val in dict1.values():
    if val in value_count:  
        value_count[val] = value_count[val] + 1
    else:
        value_count[val] = 1

print(value_count)

for k,v in dict1.items():
    if value_count[v] == 1:
       unique_val_dict[k] = v 



print('Unique Value In Dictionary Format: ')
print(unique_val_dict)        
print('Unique Value in set format: ')
print(unique_dict)