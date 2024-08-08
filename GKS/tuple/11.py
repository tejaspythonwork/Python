# all pair combination of 2 tuples

def defination11():
    test_tuple1 = (7, 2)
    test_tuple2 = (7, 8) 

    res1 = [(a,b) for a in test_tuple1 for b in test_tuple2]
    print(res1)

    res2 = [(a,b) for a in test_tuple2 for b in test_tuple1]
    print(res2)

    print(tuple(res1 + res2))

defination11()
