# find largest/smallest and sum of all items from list
max = 0
min = 10
sum = 0
list1 = [1,2,4,63,14,456,55,7643,454,3665,-1,10]
for i in list1:
    if i > max:
       max = i

for i in list1:
    if i < min:
      min = i   

# find sum of all items in list
for i in list1:
    sum = sum + i


print(f'Maximum Value = {max}')     
print(f'Minimum Value = {min}')   
print(f'Summation = {sum}')