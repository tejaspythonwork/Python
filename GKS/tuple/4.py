# adding tuple to list and list to tuple

# adding tuple to list

list1 = ['a','b','c','d','e']
tuple1 = ('a','b',['5',5.5,100])

index = 3
list1.insert(3,tuple1)
print(list1)


# adding list to tuple

l1 = ['a','b','c','d','e']
t1 = (1,2,3,4,5,6,7,8,9,10)

t1 = list(t1)
t1.extend(l1)
t1 = tuple(t1)
print(t1)