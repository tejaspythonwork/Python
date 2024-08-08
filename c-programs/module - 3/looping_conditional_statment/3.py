# finding even and odd
# finding sum of even and odd


numbers = []
print(f'Please enter 10 numbers:')
for i in range(10):
    num = int(input(f'Please enter number {i+1}: '))
    numbers.append(num)

print(f'You have entered this numbers = {numbers}') 

# finding even numbers 
even_list = [ e for e in numbers if e % 2 == 0 ]
print('Even Numbers: ')
print(even_list)   

# finding odd numbers
odd_list = [o for o in numbers if o % 2 != 0]
print('Odd Numbers: ')
print(odd_list)


# sum of even numbers
sum_even_numbers = sum(even_list)
# sum of odd numbers
sum_odd_numbers = sum(odd_list)

print(f'Sum Even Numbers = {sum_even_numbers}')
print(f'Sum Odd Numbers  = {sum_odd_numbers}')