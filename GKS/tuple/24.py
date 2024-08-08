# cross pairing of tuple 

def defination24():
    test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
    test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

    res = [(a[1],b[1]) for b in test_list2  for a in test_list1 if a[0] == b[0]]
    print(res)

defination24()    