# unzip a list of tuple into individual list 
# removed blank tuple from list
list_of_tuple = [(1,2,3),(4,5,6),(),(7,8,9),(10,11,12),(),()]



for index,t in enumerate(list_of_tuple):
    if t:
        var_name = f'var_{index}'
        print(f'{var_name} = {list(t)}')
    