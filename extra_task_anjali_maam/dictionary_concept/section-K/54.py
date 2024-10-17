# count dictionary values how much time 3 occures

def defination54():
     items = {'apple': 3, 
              'banana': 2,
              'cherry': 3}
     cnt = 0
     
     for k,v in items.items():
          if v == 3:
               cnt = cnt + 1
               print(f'{k} {v}')
     print(f'Total occurence for count 3 is = {cnt}')         
     
defination54()    
