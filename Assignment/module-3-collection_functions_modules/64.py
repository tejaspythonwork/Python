# write program to find max and min for
# specific decimal numbers
min = 1.0
max = 0

list_numbers = [1.1,0.5,11.4,0.10,10.0,55.9,11.5,-100,-200]

for i in list_numbers:
    if i > max:
        max = i
print('Maximum Value')        
print(max)        


for i in list_numbers:
    if i < min:
        min = i
print('Minimum Value')
print(min)
