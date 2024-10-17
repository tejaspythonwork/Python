'''
fifth pattern
A 
A B 
A B C 
A B C D
A B C D E 

'''

def defination19_5():
    a = 65
    for i in range(1,6):
        a = 65
        for j in range(i):
            ch = chr(a)
            a = a + 1
            print(f'{ch} ',end = ' ')
        print('')        




defination19_5()    