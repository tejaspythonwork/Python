# check dictionaries equality

def defination33():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 2, 'a': 1}

    result = dict1 == dict2
    if result:
        print('Dictionaries Equal')
    else:
        print('Dictionaries are not equal')

defination33()