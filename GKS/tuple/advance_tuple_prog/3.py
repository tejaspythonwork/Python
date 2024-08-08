# convert to sort tuple using maximum elements

def defination3():
    test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
    sorted_list = sorted(test_list,key=lambda x:max(x),reverse=True)
    print(sorted_list)



defination3()    