# count total number of words in a string

from collections import Counter

text_str = 'Today is holiday'

text_str_list = text_str.split()

count_words = Counter(text_str_list)

print(text_str_list)
print(dict(count_words))
print('==================')
for k,v in count_words.items():
    print(f'{k} occures for {v} time(s)')