# convert matrix to custom tuple matrix

def defination5():
    test_list = [[4, 5, 6], [6, 7, 3], [1, 3, 4]]
    add_list = ['Gfg', 'is', 'best']

    res = []
    for idx,ele in zip(add_list,test_list):
        for e in ele:
            res.append((idx,e))

    print(res)

defination5()    