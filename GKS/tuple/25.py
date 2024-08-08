# consecutive kth column diffrence in tuple list

def defination25():
   test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
   res = []
   for i in range(0,len(test_list)-1):
      res.append(abs(test_list[i][1] - test_list[i+1][1] ))

   print(res)

defination25()   
