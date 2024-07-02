# to map 2 lists into dictionary
key = ['1','2','3','4','5']
value = ['a','b','c','d','e']

dict1 = {k:v for k ,v in zip(key,value)}
print(dict1)