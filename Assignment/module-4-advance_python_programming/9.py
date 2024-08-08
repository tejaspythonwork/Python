# count number of lines in textfile

file_name = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt'

with open(file_name,'r') as f:
    content = f.readlines()
    print(len(content))
    f.close()