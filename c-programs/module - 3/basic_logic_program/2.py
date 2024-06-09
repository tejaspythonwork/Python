# simple calculator using while loop

status = True

while status:
    num1 = int(input('Enter First Number:'))
    num2 = int(input('Enter Second Number: '))

    print('''
            Menu
      ----------------
      1.Addition
      2.Substraction
      3.Division
      4.Multiplication
      5.Exit    
     -----------------
     

    ''')
    choice = int(input('Please Enter Your Choice: '))
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
        status = False
        
    answer = input('Do you want to continue y for yes and n for no ')
    if answer == 'y' or answer == 'yes': 
        status = True
    elif answer == 'n' or answer == 'no': 
        status = False    