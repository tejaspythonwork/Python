# remove empty tuple from list of tuple
list_of_tuple = [(1,2,3),(4,5,6),(),(7,8,9),(10,11,12),(),()]
filtered_tuple = []
for t in list_of_tuple:
   if t:
      filtered_tuple.append(t)

print(tuple(filtered_tuple))        