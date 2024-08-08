# addition - substraction - multiplication - division
# using switch case

def addition():
    num1 = int(input('Enter 1st number'))
    num2 = int(input('Enter 2nd number'))
    return num1 + num2

def substraction():
    num1 = int(input('Enter 1st number'))
    num2 = int(input('Enter 2nd number'))
    return num1 - num2

def multiplication():
    num1 = int(input('Enter 1st number'))
    num2 = int(input('Enter 2nd number'))
    return num1 * num2

def division():
    num1 = int(input('Enter 1st number'))
    num2 = int(input('Enter 2nd number'))
    return num1.__floordiv__(num2)


def match_case_for_value():
    status = True
    menu = '''
    1.Addition
    2.substraction
    3.multiplication
    4.division
    5.exit    

    '''
    while status:
     print(menu)
     value = int(input('Please enter your choice: '))
     match value:
      case 1:
       res = addition()
       print(res) 
      case 2:
       res = substraction()
       print(res)  
      case 4:
       res = division()
       print(res)  
      case 3:
       res = multiplication() 
       print(res) 

      case 5:
        status = False
      case default:
        print('please enter choice between 1 - 4')           


match_case_for_value()        