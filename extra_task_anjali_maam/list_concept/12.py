# flatten nested list to single list

def defination12():
    nested_list = [[1, 2], [3, 4], [5, 6]]
    flat_list = []
    for sub_list in nested_list:
        for i in sub_list:
            flat_list.append(i)


    print(flat_list)
    
defination12()    