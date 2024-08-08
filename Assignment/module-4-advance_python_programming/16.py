# Q: can one block of except statment handle 
# multiple exception
# Ans.Yes one except statment can handle multiple exception
# example

try:
    b = 'a'
    a = 1/0
    c = b/'a'
    int('abc')
except(ZeroDivisionError,TypeError,ValueError):
    print('Error : either zero division error\nor invalid type\nor Invalid Value')
