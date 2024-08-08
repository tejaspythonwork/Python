# cross - pairing - of tuples

def defination24_1():
    test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
    test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

    res = []
    for a in test_list1:
        for b in test_list2:
            if a[0] == b[0]:
                res.append((a[1],b[1]))


    print(res)

defination24_1()    