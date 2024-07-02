# split a list into diffrent variables

list1 = [['a','b','c'],1,1,2,4,24,[3424,35,1],1.3,4.6]
variable_name = 'variable'


# for i,item in enumerate(list1):
#     exec(f'var_{i} = {item}')
    
    

for i in range(0,len(list1)):    
    print(f'var_{i} = {list1[i]}')
    