# remove duplicate from list 
list1 = ['A','B','A','T','Q','F','E','C','Q']
unique_list1 = []
equal_count=0
for item in list1:
    if item not in unique_list1:
        unique_list1.append(item)

print(f'After removing duplicates = {unique_list1}')    