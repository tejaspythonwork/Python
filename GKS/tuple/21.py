# removes duplicates from tuple

def defination21():
    test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
    x = []
    for i in test_tup:
        if i not in x:
            x.append(i) 
    res = tuple(x) 
    print(res) 

defination21()    
