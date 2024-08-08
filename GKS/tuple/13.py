# remove tuple which has 2 None element in tupe list

def defination13():
    test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, ),(None,None)]

    for i,item in enumerate(test_list):
        if item == (None,None):
            test_list.remove(item)

    print(test_list)


defination13()        