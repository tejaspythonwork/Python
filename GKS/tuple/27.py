# flatten tuple of list to tuple

def defination27():
    res = []
    test_tuple = ([5, 6], [6, 7, 8, 9], [3])
    for i in test_tuple:
        for j in i:
          res.append(j)
         
    print(tuple(res))

defination27()