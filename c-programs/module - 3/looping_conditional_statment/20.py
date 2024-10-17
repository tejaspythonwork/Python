'''
print o/p like:
01 02 03 04 05 06 07 08 09 10 
11 12 13 14 15 16 17 18 19 20
'''

def defination20():
    num = 1
    for i in range(2):
        for j in range(10):
            print(f'{num:02}',end = ' ')
            num = num + 1
        print() 


defination20()           