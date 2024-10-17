# convert sublist to single list 
def defination27():
    result = []
    list_of_lists = [[1, 2], [3, 4], [5, 6]]
    for i in list_of_lists:
        for j in i:
            result.append(j)

    print(result) 

defination27()           