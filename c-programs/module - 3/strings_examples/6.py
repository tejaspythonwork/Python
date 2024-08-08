# count total number of alphabets,digits and special characters

text_str_1 = 'Hi! how are you, your mobile number is 8460512281'

alpha_count = 0
digit_count = 0
special_count = 0
alpha_list = []
for txt in text_str_1:
    if txt.isalpha():
        alpha_list.append(txt)
        alpha_count = alpha_count + 1
    if txt.isdigit():
        digit_count = digit_count + 1
    if not (txt.isalpha() or txt.isdigit() or txt.isspace()):
        print(txt)
        special_count = special_count + 1   


print(f'In above string there are \nAlphabets = {alpha_count}\ndigits = {digit_count}\nspecial characters = {special_count}')        
print(alpha_list)     
print('Converted to string = ')
print(''.join(alpha_list))