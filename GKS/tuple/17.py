# records with value at k index


def defination17():
    test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
    res = []
    for x,y,z in test_list:
        if y == 3:
           res.append((x,y,z))


    print(f'Tuple at kth position = {res}')       

defination17()    