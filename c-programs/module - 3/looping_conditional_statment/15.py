# calculate sum of 10 numbers using while loop
n = 10
i=0
list_of_number = []
sum_of_number = 0
while n!=0:
    i = i + 1
    n1 = int(input(f'Enter Number {i}: '))
    list_of_number.append(n1)
    sum_of_number = sum(list_of_number)
    n = n -1
print(f'sum of all numbers = {sum_of_number}')    

