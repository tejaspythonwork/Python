# maximum and minimum elements from tuple


def defi2(t1):
   result1 = max(t1)
    

   result2 = min(t1)
   return result1,result2


res1,res2 = defi2((1,4,2,77,5,4,0,-50))
print(f'max = {res1}')
print(f'min = {res2}')