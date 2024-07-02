# takes 2 list and return true if they have one 
# common member

list1 = ['A','B','C','D']
list2 = ['A','D','E','F']
list3 = []

def prg9():
    for i in list1: 
        for j in list2:
            if i == j:
                # print('Common Element found')
                # list3.append(i)
                return True 

#print(list3)


if prg9() == True:
    print('Common Element Found')