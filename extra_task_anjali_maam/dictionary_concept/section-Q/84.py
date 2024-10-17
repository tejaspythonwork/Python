# create dictionaries with sequential keys

def defination84():
    tuple1 = ('a', 'b', 'c', 'd', 'e') 
    tuple2 =  (1, 2, 3, 4, 5)

    dict1 = {k:v for k,v in zip(tuple1,tuple2) }
    print(dict1)

defination84()     