# write a python program to write a list to a file
list1 = [1,2,3,4,5,6,7,8,9,10]

file_name = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_list_11.txt'

with open(file_name,'w') as fl:
    for item in list1:
        fl.write(str(item))

    print('List has been written to file')    
    fl.close()