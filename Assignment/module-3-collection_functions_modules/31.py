# how you will create dictionary using tuples in python
# complex Structure

tuple1 = [(1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15)]
dictionary = {t[0]:(t[1],t[2]) for t in tuple1}
print(dictionary)

# simple structure
dictionary2 = {t[0]:t[1] for t in tuple1}
print(dictionary2)