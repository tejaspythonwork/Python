'''
second pattern:

A
B C
D E F
G H I J 
K L M N O    
'''

def defination19_2():
    a = 65
    ind = 0
    ch = chr(a)
    for i in range(1,6):
        row = []
        for j in range(i):
            row.append(chr(65 + ind))
            ind = ind + 1
        print(' '.join(row))    
        # print(f'{row}')

defination19_2()