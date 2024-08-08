# palindrom number using function

def palindrom_10(text_str1):


    text_reverse_str1 = text_str1[::-1]
    if text_reverse_str1 == text_str1:
        print('Palindrom')
    else:
        print('Not Palindrom')



palindrom_10('ABCDCBA')
palindrom_10('BCDAASF')