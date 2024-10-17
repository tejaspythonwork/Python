# find max value for each key 
def defination31():
     max_ele = 0
     data = {'Jan': [1, 2, 3], 'Feb': [4, 5, 6], 'Mar': [7, 8, 9]}
     for k,v in data.items():
          max_ele = max(v)
          key = k

     print(key)
     print(max_ele)




defination31()     