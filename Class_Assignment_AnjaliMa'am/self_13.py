# this code demonstrate use of Function

def level1():
    print('Level - 1')

def level2():
    print('Level - 2')    

def level3():
    print('Level - 3')    

status = True
while status:
    print('3 levels')
    print('1ST')    
    print('2ND')
    print('3rd')

    choice = int(input('Enter Level'))

    if choice == 1:
        level1()
    if choice == 2:
        level2()
    if choice == 3:
        level3()
        status = False       