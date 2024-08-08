# seperate even and odd using map() 
even_list = []
odd_list = []
def even_odd(num):

    
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)    

    res = list(map(even_odd,l1))
    print(res)
    return even_list,odd_list
   




l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  
even,odd = even_odd(l1)
print(even)
print(odd)