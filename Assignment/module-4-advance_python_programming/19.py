# how do you handle exception with try/except/finally in python
# explain with code

try:
    b:int = 'a'+1
    a = 1/0
    
    
except ZeroDivisionError:
    print('Can not divide by zero')
except TypeError:
    print('Type Error Occured')

finally:
    print('Finally Block Executed Always')    