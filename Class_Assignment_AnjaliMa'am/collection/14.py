l1 = []
status = True
while status:
    val = input('Enter Value')
    l1.append(val)
    
    choice = input('Do you want to continue? Enter y for yes and n for no')    
    if choice == 'y' or choice == 'yes':
        status = True
    elif choice == 'n' or choice == 'no':
        status = False
        print('You have entered following')
        print('--------------------------')
        print(l1)
    