# find second smallest number from list

list = [1,2,0,-1,-2,-5,5324,32,13,77]

sorted_numbers = sorted(list,reverse=False)
second_smallest = sorted_numbers[1]

print(F'Sorted List = {sorted_numbers}')

print('Second Smallest Number = ')
print(second_smallest)