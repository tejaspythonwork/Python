# find largest smallest word in string
text_str = 'Hi! there how are you I am Happy'

text_str_spllited = text_str.split()
print(text_str_spllited)
# find max length

smallest_word = text_str_spllited[0]
largest_word = text_str_spllited[0]

for i in text_str_spllited:
    if len(i) < len(smallest_word):
      smallest_word = i
    elif len(i) > len(largest_word):
       largest_word = i
 
print('Smallest Word = '+smallest_word)
print('Largest Word ='+largest_word)
