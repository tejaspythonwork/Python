# create list which contain only even numbers

def is_even(n):
    if n % 2 == 0:
       return n  

def defination10():
    num = [1,2,3,4,5,6]
    even_number = list(filter(is_even,num))
    print(even_number)

    
defination10()


