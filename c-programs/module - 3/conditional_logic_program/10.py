# wap to check positive/negative/zero

number = int(input('Please enter digit'))

def check_number(num):
    if num == 0:
        print('Number is Zero')
    elif num > 0:
        print('Greater Than Zero - Positive')
    else:
        print('Less Than Zero - Negative')
        

check_number(number)        