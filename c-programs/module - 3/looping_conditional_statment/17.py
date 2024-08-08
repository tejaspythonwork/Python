# calculate even and odd using while loop

l1 = [1,3,4,2,100]

def number_odd(n):
    if n % 2!= 0:
        return n
    

def number_even(n):
    if n % 2 == 0:
        return n

print('Even Numbers: ')
res_even = list(filter(number_even,l1))
print(res_even)


print('Odd Numbers: ')
res_odd = list(filter(number_odd,l1))
print(res_odd)

result = ''.join([str(num) for num in res_even])
print(result)

split_numbers = result.split()
print(split_numbers)

str_list = [str(num) for num in split_numbers]
print(''.join(str_list))

int_list = [int(n) for n in str_list]
print(int_list)

