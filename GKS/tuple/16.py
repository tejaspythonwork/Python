# filter tuple based on length 

def defination16():
    test_list = [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

    i1 = 2
    j1 = 3

    res = [i for i in test_list if len(i) >= i1 and len(i) <=j1 ]
    print(res)



defination16()    