# read last n lines of file
filename = 'F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt'
n = 5


with open(filename, 'r') as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]
    
    for line in reversed(last_n_lines):
        print(line.strip())
    
    file.close()