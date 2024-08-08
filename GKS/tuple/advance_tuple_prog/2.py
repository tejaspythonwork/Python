# extract symmetric tuple 

def defination2():
    test_list = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]
    print(f'original list = {str(test_list)}')

    temp = set(test_list) & {(b,a) for a,b in test_list}
    res =  {(a,b) for a,b in temp if a < b}

    print(f'Symmetric tuple = {res}')


defination2()
