# how to read entire text file in python

with open('F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt','r') as f:
    content = f.read()
    print(content)
    f.close()