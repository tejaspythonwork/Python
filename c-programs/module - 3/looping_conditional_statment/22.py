# Accept 3 numbers and check each number is 
# palindrom or not

def check_palindrom(number_ip):
    num1 = str(number_ip)
    num2 = num1[::-1]
    if num1 == num2:
        return f'{num1} is palindrom'
    else:
        return f'{num1} is not palindrom'

def defination21():
    i=1
    while i <= 3:
        num = input(f'please enter number {i}: ')

        print(num)
        res = check_palindrom(num)
        print(res)
        i = i + 1    


defination21()