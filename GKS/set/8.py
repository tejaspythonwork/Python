# find lost element from list of an array

def defination8_1():
    list1 = [1, 2, 3, 4, 5, 6,] 
    list2 = [4, 5, 6, 7, 8] 
    A = set(list1)
    B = set(list2)

    if len(A) < len(B):
        print(list(A-B))
    elif len(A) > len(B):
        print(list(B-A)) 


defination8_1()           

