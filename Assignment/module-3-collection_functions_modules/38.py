# to check that multiple keys exist in dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

keys_to_check = ['a','b','d']
all_eexists = all(key11 in my_dict for key11 in keys_to_check)

if all_eexists == True:
    print('All Keys Are Exists')
else:
    print('Not all keys are exists')