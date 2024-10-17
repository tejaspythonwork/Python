# create dictionaries from list of tuple 

def defiantion77():
    tuples = [
        ('a', 1), 
        ('b', 2), 
        ('c', 3)
        ]
    
    dict1 = {k:v for k,v in tuples}
    print(dict1)


defiantion77()    