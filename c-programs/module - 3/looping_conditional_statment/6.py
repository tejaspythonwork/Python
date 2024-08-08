# fibonnanci upto given numbers
def find_fibo():
 fibo_list = [0,1]

 for i in range(2,11):
    next_fibo = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(next_fibo)

 return fibo_list

res = find_fibo()
print(res)