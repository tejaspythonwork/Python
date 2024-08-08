# check that tuple is distinct 

def defination18():
    test_tup = (1, 4, 5, 6, 1, 4)

    for i in range(len(test_tup)):
        if test_tup[i] in test_tup[i + 1:]:
            distinct = False
            break

    print(f'is tuple distinct = {distinct}')    


defination18()
