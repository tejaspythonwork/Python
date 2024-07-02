# find repeated items in tuple

tuple1 = (1,2,4,5,2,1,3,78,9,64,48,9,45,1)
repeated_item = {}
for i in tuple1:
    if i in repeated_item:
        repeated_item[i] = repeated_item[i] + 1
    else:
        repeated_item[i] = 1

print(f'Repeated Items = {repeated_item}')            
convert_repeated_item  = repeated_item.items()
print('repeated items in tuple format')
print(tuple(convert_repeated_item))