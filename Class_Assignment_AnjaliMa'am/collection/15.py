'''
    Menu
  1.insert element
  2.remove element value wise
  3.search element
  4.fetch specific element index
  5.remove specific element index wise

'''

def one_five():
    l1 = [1,3,5,7,9,22,55,66]
    status = True
    while status:
        print('''
                  Menu
  ---------------------------------------
            1.insert element
            2.remove element value wise
            3.search element
            4.fetch specific element index
            5.remove specific element index wise
              
''')    
        
        input_choice = int(input('Enter Your Choice'))
        if input_choice == 1:
            print('insert element')
            element_to_add = int(input('Enter Element'))
            l1.append(element_to_add)
            print(f'new list = {l1}')
        elif input_choice == 2:
            print('remove element')
            element_to_remove = int(input('Enter element to remove'))
            indexed_element = l1.index(element_to_remove)
            l1.pop(indexed_element) 
            print(f'new list {l1}')   
        elif input_choice == 3:
            print('Search an element')
            search_element = int(input('Enter element to search'))
            if search_element in l1:
                print('Element Present')
            else:
                print('Element Not Present')
        elif input_choice == 4:
            print('Fetch Specific Element')
            ind = int(input('Enter Element')) 
            index_val = l1.index(ind) 
            print(index_val) 
            print(f'element index = {index_val} and element = {ind}') 
        elif input_choice == 5:    
            print('remove specific element index wise')          
            remove_element = int(input('Enter element to remove'))
            l1.remove(remove_element)
            print(l1)
        else:
            print('Please enter valid choice between 1 - 5')
 
        choice_exit = input('Do you want to continue press y for yes and n for no')
        if choice_exit == 'y' or choice_exit == 'yes':
            status = True
        elif choice_exit == 'n' or choice_exit == 'no':
            status = False


one_five()        