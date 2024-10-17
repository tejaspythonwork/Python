# find common keys

def defination17():
     dict1 = {'a': 1, 'b': 2}
     dict2 = {'b': 3, 'c': 2}
     dict3 = {}

     for i in dict1:
        if i in dict2:
          dict3 = {i:dict1[i] + dict2[i]}


     print('common dictionary key found')   
     print(dict3)   


defination17()            