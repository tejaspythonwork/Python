'''
fourth pattern
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

'''

def defination19_4():
    dgt = 0
    for i in range(1,6):
        for j in range(i):
            dgt = dgt + 1
            print(f'{dgt} ',end= ' ')
        print('') 


defination19_4()           