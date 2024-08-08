# read first n lines of files
with open('F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt','r') as f:
    n = int(input('Enter number of lines'))
    f.seek(0)
    for i in range(0,n):
        line = f.readline()
        if line == '':
            break
        print(line.strip())
    f.close()