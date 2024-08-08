# update list using for loop


def defination8():
    test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
    ind = 1
    val = 5 
    new_list = []
    for tup in test_list:
        temp_list = list(tup)
        temp_list[ind] = val
        new_tuple = tuple(temp_list)
        new_list.append(new_tuple)
    print(new_list)



defination8()        