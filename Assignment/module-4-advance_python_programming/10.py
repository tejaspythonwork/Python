# write a program to count frequency of a word in file

from collections import OrderedDict

filename = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt'

with open(filename,'r') as f:
    content = f.read()
    # dict1 = OrderedDict(list)
   # dict1 = OrderedDict(content.split())
    print(content.split())

    frequency = OrderedDict()

    for item in content.split():
        if item in frequency:
            frequency[item] = frequency[item] + 1
        else:    
            frequency[item] = 1


    for k,v in frequency.items():
        print(f'{k} = {v}')         


    f.close()    