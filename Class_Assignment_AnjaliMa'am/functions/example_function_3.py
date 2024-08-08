# check string is palindrom or not

def check_string_palindrom(text):
    reverse_string = text[::-1]

    if text == reverse_string:
        return 'String is palindrom'
    else:
        return 'String is not palindrom'
    

text = input('Please enter String')
result = check_string_palindrom(text)
print(result)