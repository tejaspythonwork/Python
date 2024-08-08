# Accept 5 numbers from user and find factorial of it

def find_fact(n):
    res = 1
    while n > 0:
      res = res * n
      n = n -1
    print(res)
    return res

result = find_fact(5)

res_map = list(map(find_fact,[10,8,7,6,5]))
print(res_map)