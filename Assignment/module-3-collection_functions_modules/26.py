# replace last value of tuple in a  list
list_of_tuple = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
new_val = 10001
modified_list_of_tuple = []

for t in list_of_tuple:
    modified_tuple = t[:-1] + (new_val,)

    modified_list_of_tuple.append(modified_tuple)

print(modified_list_of_tuple)    