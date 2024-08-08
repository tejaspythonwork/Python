# extract tuple having k number of digits

def defination1():
    test_tup = [(54, 20), (34, 55), (222, 23), (12, 45), (7, ), (11,22,33)]
    res = list(t for t in test_tup if len(t) == 2)
    print(res)



defination1()    