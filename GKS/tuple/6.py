# modulo of tuple elements 

test_tuple1 = (10, 4, 5, 6)
test_tuple2 = (5, 6, 7, 5)

res = [ele1 % ele2 for ele1,ele2 in zip(test_tuple1,test_tuple2)]
print(res)