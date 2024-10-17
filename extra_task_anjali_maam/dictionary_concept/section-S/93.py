# update dictionary based on condition

def defination93():
     data = {
          'apple': 10, 
          'banana': 20,
          'cherry': 30
          }

     for k,v in data.items():
         if v > 15:
              data[k] = v + 15     

     print(data)

defination93()              