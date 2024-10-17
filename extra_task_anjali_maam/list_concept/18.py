# concate this 2 lists

def defination18():
    i=''
    res = []
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    for item in list2:
        list1.append(item)

    print(f'Concated List - {list1}')

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    concated_list = list1 + list2

    print(concated_list)

defination18()            