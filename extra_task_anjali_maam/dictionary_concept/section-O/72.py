# update dictionaries with function

def defination72():
     data = {'a': 1, 'b': 2, 'c': 3}
     status = True
     menu = '''
        1.Increment Dictionaries Values by 1
        2.Exit
        '''
     while status:
        print(menu)
        try:
            choice = int(input('Please Enter Your Choice: '))
            match(choice):
                case 1: 
                    data = {k:int(v) + 1 for k,v in data.items()}
                    print(data)
                    
                case 2:
                    status = False
        except ValueError:
            print('Please enter valid choice')


defination72()     