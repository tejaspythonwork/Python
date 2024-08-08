# remove duplicate list from tuple

def defination22():
    test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3]) 
    x = []
    for tup in test_tup:
        if tup not in x:
            x.append(tup)

    print(tuple(x))
    
defination22()            