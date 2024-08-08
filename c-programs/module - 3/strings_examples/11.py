# read a sentence and replace upper case with lower case and viceversa

text_str = 'Hi Happy To See YOu'
converted_str = ''


for i in text_str:
    if i.islower():
       converted_str = converted_str + i.upper()  
    else:
       converted_str = converted_str + i.lower()


print(converted_str)