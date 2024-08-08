# Extract substring from given string

text_main_string = 'I am Learning Python'
text_substring = 'Python'
ind = 0
if text_substring in text_main_string:
    ind = text_main_string.index(text_substring)

    print(f'Substring Found at position = {ind + 1}')
else:
    print('Substring not found')