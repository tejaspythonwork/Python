# write file line - by - line and store it into list
# 6 and 7 - both programs

filename = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt'
# list_of_lines = []
with open(filename,'r') as f:
    lines = f.readlines()
    list_of_lines = lines
    list_of_lines_var = ''.join(list_of_lines)
    total_length = len(lines)
    
    print(total_length)
    print(list_of_lines)
    print('========')
    print(list_of_lines_var,end = '')
    f.close()