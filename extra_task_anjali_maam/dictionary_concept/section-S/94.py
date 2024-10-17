# extract and sort based on values

def defination94():
     data = {'a': 5, 'b': 10, 'c': 2}
     res = lambda x : x[1]

     result = sorted(data.items(),key=res)
     print(result)

defination94()     