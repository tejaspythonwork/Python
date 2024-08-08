# convert tuple into list by adding given string 
# after every element

def defination1():
    test_tup = [5, 6, 7]
    k = "Gfg" 
    res = [ele for sub in test_tup for ele in (sub,k)]
    print(tuple(res))

defination1()