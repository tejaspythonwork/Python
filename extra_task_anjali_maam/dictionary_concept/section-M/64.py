# remove key-val pair with specific vals

def defination64():
     inventory =  {
          'apple': 10, 
          'banana': 5,
          'orange': 10
    }
     
     for k,v in inventory.items():
          if v == 10:
               continue
          else:
               print(f'remaining item key = {k} and val = {v}')


defination64()
