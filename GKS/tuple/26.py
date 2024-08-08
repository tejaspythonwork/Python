# kth column multiplication 

def defination26():
    test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
    result = 1
    res = [ test_list[i][2] * test_list[i+1][2] for i in range(0,len(test_list)-1)   ]
    for i in res:
        result = result * i
    
    
    print(result)



defination26()    