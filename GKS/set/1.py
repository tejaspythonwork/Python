# find size of set in python
import sys as s
set1 = {'a','c',1,2,4,3,5,11.11}

# two ways
# 1.
print(set1.__sizeof__())


# 2.
set2 = {1,2,3,4,5,6,5,4,3,2,1}
print(s.getsizeof(set2))