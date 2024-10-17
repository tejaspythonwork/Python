# find unique element from nested tuple

def defination6():
    temp_list = []
    res = []
    test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]
    for i in test_list:
        for ele in i:
           if ele not in temp_list:
               temp_list.append(ele)
           else:
               res.append(ele)     
    print(res)
    print(temp_list)


defination6()        