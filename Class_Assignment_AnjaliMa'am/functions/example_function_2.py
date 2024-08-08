# accept number and check palindrom

def check_number_palindrom(number):
    converted_number = str(number)
    converted_number_reverse = converted_number[::-1]
     
    if str(number) == converted_number_reverse:
        return 'Number is palindrom'
    else:
        return 'Number is not palindrom'



 
n = int(input('Enter Number'))
result =  check_number_palindrom(n)        
print(result)