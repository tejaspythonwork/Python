# count number of times --- 'is' --- occured in String

def defination12():
 text_str = 'is is is a a a is is'.split()
 count_is = 0
 for i in text_str:
    if i == 'is':
      count_is = count_is + 1
 return count_is    

print(f'is occured = {defination12()} times')
