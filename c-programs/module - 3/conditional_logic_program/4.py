# make simple calculator (operation include Addition, Subtraction, 
# Multiplication, Division, modulo) using conditional statement

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2 

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1/num2

def modulo(num1,num2):
    return num1 % num2


def simple_calculator():
   status = True
   

   while status: 
        number1 = int(input('Enter First Number')) 
        number2 = int(input('Enter Second Number'))  
        
        print('''
                =============
               Simple Calculator 
        --------------------------------   
                1.Addition
                2.Multiplication
                3.Division
                4.Substraction 
                5.Modulo
                ==============
              
              ''')

        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            op1 = add(number1,number2)
            print(op1)
        if choice == 2:
            op2 = mul(number1,number2)
            print(op2)
        if choice == 3:
            op3 = div(number1,number2)
            print(op3)
        if choice == 4:
            op4 = sub(number1,number2)     
            print(op4)
        if choice == 5:
            op5 = modulo(number1,number2)     
            print(op5)    

        choice_input = input('Do you want to continue press y for yes and n for no')
        if choice_input == 'y' or choice_input == 'Y':
            status = True
        elif choice_input == 'n' or choice_input == 'N':
            status = False    


simple_calculator()