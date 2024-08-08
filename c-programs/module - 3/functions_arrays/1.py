# find max number from list using function

def find_max():
    l1 = [1,34565,34,222,11,0,-1]
    large_number = l1[0]
    for i in l1:
        if len(str(i)) > len(str(large_number)):
            large_number = i
    
    print(large_number)


find_max()    