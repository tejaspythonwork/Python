# maximum number of characters in string

from collections import Counter

text = 'Hello! how are you'

dict1 = Counter(text)
print(dict1)

max_key = max(dict1,key=dict1.get)
print(max_key)
max_val = max(dict1.values())
print(f'{max_key} occures for {max_val} times')