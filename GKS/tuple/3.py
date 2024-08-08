# generate list as a way that has list of numbers 
# and 1st element as it is
# and last element as its cube

tuple_1 = (1,2,3,4,5)

res = [(val,pow(val,3)) for val in tuple_1]
print(res)