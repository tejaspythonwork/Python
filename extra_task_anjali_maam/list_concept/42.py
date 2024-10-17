# each tuple consist elements from both lists

def defination42():
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]

    list_compr = [(i,j)for i in list1 for j in list2]
    print(list_compr)

defination42()    