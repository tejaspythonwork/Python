# python code to find tuple elements which are all positive

def defination20():
  tuple_1 =  [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6, 0)] 
  res = []
  for (x,y,z) in tuple_1:
    if x > 0 and y > 0 and z > 0:
       res.append((x,y,z)) 

  print(res)      

defination20()
