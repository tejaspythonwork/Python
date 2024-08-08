# remove tuple based on length k

def defination12():
    test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

    k = int(input('Please enter length of tuple to remove: '))

    res = [ele for ele in test_list if len(ele) !=k ]
    print(res)


defination12()