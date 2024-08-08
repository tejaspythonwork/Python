# sort tuple based on second element

t1 = [('for', 24), ('Geeks', 8), ('Geeks', 30)] 


# def sort_based_digit(list(t1)):
#     return t1[1]


t2 = sorted(list(t1),key= lambda x:x[1])
print(t2) 