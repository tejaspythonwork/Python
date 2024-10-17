# deep merge dictionaries

def defination86(dict1,dict2):
     
     for k,v in dict2.items():
          if k in dict1:
               if isinstance(dict1[k],dict) and isinstance(v,dict):
                    defination86(dict1[k],v)         
               else:
                    dict1[k] = v + dict1[k]
                
          else:
               dict1[k] = v

     return dict1                         



dict1 = {'a': {'x': 1, 'y': 12},
              'b': {'z': 3}}
dict2 = {'a': {'y': 10, 'z': 20}, 
              'c': {'w': 30}}
result = defination86(dict1,dict2)
print(result)