# reverse a string if length is multiple of 4

def twenty(string_input):
    if len(string_input) % 4 == 0:
        print('string is multiple of 4')
        reverse_string = string_input[::-1]
        return reverse_string
    
    
str1 = input('enter string')
twenty_multiple_four = twenty(str1)        
print(twenty_multiple_four)