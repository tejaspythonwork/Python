# transform values based on keys

def defination85():
     data = {
          'x1': 10, 
          'x2': 20, 
          'y1': 30,
          'y2': 40
          }
     dict1 = {}
     dict2 = {}
     
     for k,v in data.items():   
          if k.startswith('x') :
               dict1[k] = v * 2
          else:
               dict2[k] = v // 2
     print(dict1)
     print(dict2)
     dict1.update(dict2)
     print(dict1)
defination85()

