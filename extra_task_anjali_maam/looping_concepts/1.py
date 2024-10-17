# sum of n numbers

def defination1():
    n = int(input('Please enter element number: '))
    list_for_num = []
    sum_of_num = 0
    for i in range(1,n+1):
       num = int(input(f'please enter {i} number: '))
       list_for_num.append(num)

    sum_of_num = sum(list_for_num)
    print(sum_of_num) 

defination1()      