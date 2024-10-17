# program to reverse number using for loop

text_number = 12345678901011
text_str = str(text_number)
for i in range(len(text_str)-1,-1,-1):
    print(text_str[i],end = ' ')
print()    