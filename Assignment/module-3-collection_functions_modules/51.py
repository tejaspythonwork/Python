# check that string is palindrom or not
def def51():
    str1 = input('Enter String To Check Palindrom Or Not')
    
    str2 = str1[::-1]
    print(f'Reverse String = {str2}')
    if str1 == str2:
        print('Palindrom')
    else:
        print('Not Palindrom')
    

def51()    