# Accept 5 nummbers and check even/odd

list_int = []
for i in range(1,6):
    number = int(input('Please enter number: '))
    list_int.append(number)




def find_even(num):
    if num % 2 == 0:
        return True
    

def find_odd(num):
    if num % 2 !=0:
        return True  

odd_list = list(filter(find_odd,list_int))
even_list = list(filter(find_even,list_int))

print(odd_list)
print(even_list)