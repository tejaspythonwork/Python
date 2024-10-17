'''
first_pattern

1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
'''

def defination19_1():
    for i in range(1,6):
        for j in range(1,i+1):
            if j % 2 == 0:
                print('0',end= ' ')
            else:
                print('1',end= ' ')    
        print('')        

defination19_1()        