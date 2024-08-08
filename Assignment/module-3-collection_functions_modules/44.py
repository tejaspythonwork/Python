# python code for combination of latters
# {'1': ['a','b'], '2': ['c','d']}
# o/p => ac ad bc bd

dict1 = {'1': ['a','b'], '2': ['c','d']}
result_list = []
v1 = ''

v1 = dict1['1']
v2 = dict1['2']
print(v1)    
print(v2)


print((v1) * (v2))