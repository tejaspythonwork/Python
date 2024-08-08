# custom sort in list of tuples

def defination31():
    test_list = [(7, (8, 4)), (5, (6, 1)), (7, (5, 3)), (10, (5, 4)), (10, (1, 3))]
    res = sorted(test_list,key=lambda sub: (-sub[0],sum(sub[1])))
    print(res)

defination31()    