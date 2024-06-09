# returns true if 2 integer values are equal 
# or their sum or diffrences is 5 

num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))

def number_operations():
    if num1 == num2 or num1 - num2 == 5 or num1 + num2 == 5:
        return True
    else: 
        return False