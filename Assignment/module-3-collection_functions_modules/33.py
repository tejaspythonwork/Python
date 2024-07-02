# concatenate 3 dictionary
dict1 = {'a' : 1, 'A' : 2, 19: 113,11.1 : 4,0:111}
dict2 = {'b' : 1, 'E' : 2, 18: 13,19.1 : 41,1:111}
dict3 = {'c' : 1, 'd' : 2, 17: 35,65.1 : 4,2:111}

concatenated_dictionaries = {**dict1,**dict2,**dict3}
print(f'-------')
print('Concatenated Dictionary')
print(concatenated_dictionaries)
print(f'-------')