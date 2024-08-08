# get all subset of given size of set

import itertools

def find_sub_sets(s,n):
    return list(itertools.combinations(s,n))



s = {1,2,3,4}
res = find_sub_sets(s,2)
print(res)