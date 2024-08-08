# convert tuple to tuple pair

def defination3():
    test_tuple = ('A','B','C')
    pair_tupple = tuple(zip(test_tuple[:-1],test_tuple[1:]))
    print(list(pair_tupple))


defination3()    