# armstrong number using for loop

number = 153

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for dgt in num_str:
        sum = sum + int(dgt) ** n

    if sum == num:
        print('Number is armstrong')
        return True
        
    else:
        print('Numbre is not armstrong')
        return False
    
print(is_armstrong(153))