# count unique value

def defination63():
     items = {
          'a': 1, 
          'b': 1, 
          'c': 2, 
          'd': 2, 
          'e': 3
          }
     unique_vals = set(items.values())
     unique_count = len(unique_vals)

     print(f'unique vals = {unique_vals}')
     print(f'unique count = {unique_count}')

defination63()     