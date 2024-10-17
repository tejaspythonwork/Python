def defination(d):
   for val in d.values():
      if isinstance(val,dict):     
          defination(val)
      else:
          print(val)  
             

dict1 = {'a': {'b': {'c': 1}}, 'd': 2}
defination(dict1)
