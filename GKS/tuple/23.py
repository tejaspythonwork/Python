# extract digits from tuple list 

def defination23():
    lst = []
    test_list = [(15, 3)] 
    for i in test_list:
        for ele in i:
            for digit in str(ele):
                 lst.append(int(digit))

    print(lst)
    print(digit)

defination23()        