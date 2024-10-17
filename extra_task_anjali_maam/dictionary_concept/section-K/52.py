# find keys with values greater than a threshold

def defination52():
     grades = {'math': 75, 'english': 82, 'science': 90}
     threshold = 76
     result = []
     for k,v in grades.items():
          if v > threshold:
               result.append(k)


     print(result)

defination52()               