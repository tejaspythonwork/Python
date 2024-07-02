# check element exists within tuple
tuple_1 = ('I','am','learning','python','python','is','object','oriented','language')
def prg22():
    print('Below is a tuple ')
    print(tuple_1)
    find_element = input('Enter word to find ')
    
    if find_element in tuple_1:
        print('Element Present')
        return True
    else:
        print('Element Not Present')
        return False

        
        
str = prg22()
print(str)

