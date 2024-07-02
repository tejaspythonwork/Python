# sort dictionary by value
dictionary1 = {1:1232,2:11,3:78,4:10,5:100,2:19,0:100}
dictionary2 = sorted(dictionary1.values())
dictionary3 = sorted(dictionary1.values(),reverse=True)
print('Ascending Order - values')
print(dictionary2)

print('Descending Order - values')
print(dictionary3)

