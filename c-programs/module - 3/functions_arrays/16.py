# accept 5 numbers from user and perform sum

int_list = []
for i in range(1,6):
    i = int(input('Please enter value: '))
    int_list.append(i)

int_list_sum = sum(int_list)
print('summation')
print(int_list_sum)