# convert list of list to tuple of tuple

def defination4():
    test_list = [['Best'], ['Gfg'], ['Gfg']] 
    test_tup = tuple(tuple(s) for s in test_list)
    print(test_tup)


defination4()    