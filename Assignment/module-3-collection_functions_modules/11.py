# takes list 
# returns new list with unique elements

list = ['A','B','C','A','B','C','A','B','C','D','E','F']
unique_list = []

for i in list:
    if i  not in unique_list:
        unique_list.append(i)

print(unique_list)        