# handles missing key gracefully

from collections import defaultdict

def get_val_with_default(data,key,default_val = None):
    return data.get(key,default_val)


data = {'name' :'Alice','age' : 30}
try_first = get_val_with_default(data,'name','unknown')
try_second = get_val_with_default(data,'Gender','unknown')

print(try_first)
print(try_second)

