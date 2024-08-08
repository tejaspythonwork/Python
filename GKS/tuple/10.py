# join tuple if first simmilar element found

def defination10():
    test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
    for e,i in enumerate(test_list):
        print(f'{e} {i}')


    res = []
    for ind,sub in enumerate(test_list):
        print(f'{ind} {sub}')
        for index, i in enumerate( sub):
            print(f'{index} {i}')    

    print('===================')

    for s in test_list:
        if res and res[-1][0] == s[0]:
            res[-1].extend(s[1:])
        else:
            res.append([ele for ele in s])  

    res = list(map(tuple,res))
    print(res)           

defination10()        