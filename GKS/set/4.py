# remove an item from set
s1 = {1,'a','2',1.6,32,23,56,66,23}

for i in range(len(s1)):
    s1.remove(next(iter(s1)))
    print(s1)