# remove character from string except alphabets

text_str = '12345ABC54321'
new_str = ''
for i in text_str:
    if i.isalpha():
        new_str = new_str + i

print(f'Original String = {text_str}')        
print(f'New String = {new_str}')