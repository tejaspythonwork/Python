# date - 06-06-2024
# display menu in for 1.addition 2.substraction 3.division 4.multiplication 5.exit
# every time asks for do you want to enter value or not means exit 

status = True
print('Enter 2 numbers')
#num1 = int(input('Enter First Number'))
#num2 = int(input('Enter Second Number'))
while status:
    num1 = int(input('Enter First Number'))
    num2 = int(input('Enter Second Number'))
    print("""
                    Menu
                 1.Addition
                 2.Substraction
                 3.Division
                 4.Multiplication    
                 5.Exit 
          """)
    choice = int(input('Enter Your Choice'))

    if choice == 1: 
        print('Addition')
        print(num1 + num2)
    if choice == 2: 
        print('Substraction')
        print(num1 - num2)    
    if choice == 3: 
        print('Division')
        print(num1 / num2)
    if choice == 4: 
        print('Multiplication')
        print(num1 * num2)
    if choice == 5: 
        print('Exit')    

    my_status = input(f"Do you want to continue press '{{y}}' for yes and '{{n}}' for no")
    if my_status == 'y' or my_status == 'yes':
        status = True
    else:
        status = False    
