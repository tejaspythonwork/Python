# Purpose of continue statment in python
'''-------------------------------------------------
Continue statment in python skip current iteration and after that it will 
iterates continue through defined Sequence
-------------------------------------------------'''

for i in range(0,6):
    if i==2:
        print('when value is 2 i have used continue so it skip that value')
        
        continue
    print(i)