# python program to get uniquely value from ilist
list = [1,2,-1,-5,5324,32,13,77,1,3,2,5324,2]

unique_numbers = []

for n in list:
    if n not in  unique_numbers:
        unique_numbers.append(n)


print(f'Unique Numbers - {unique_numbers}')