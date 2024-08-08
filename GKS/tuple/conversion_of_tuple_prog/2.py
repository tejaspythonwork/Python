# python prograam to convert 
# tuple matrix to tuple list

def defination2():
    res1 = ''
    res2 = ''
    list1 = []
    test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]] 

    list2 = [list(map(lambda x : x[i], [tup for sublist in test_list for tup in sublist])) for i in range(2) ]
    print(list2)

defination2()