# python tuple which divisible by k 

def defination19():
    test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
    test_l = []
    for x,y,z in test_list:
        if x % 6 == 0 and y % 6 == 0 and z % 6 == 0:
            test_l.append((x,y,z))


    print(test_l)        

defination19()    