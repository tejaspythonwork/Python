# accept 5 names from user at run time

list_of_names = []
for i in range(1,6):
    name = input('Please enter name: ')
    list_of_names.append(name)


print(f'you have entered = {list_of_names}')  
res = ','.join(list_of_names)  
print(f'Name without list {res}')
