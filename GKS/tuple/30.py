# combination of sum with tuples in tuple list

from itertools import combinations

def defination30():
    test_list = [(2, 4), (5, 1), (1,1), (2,2)]

    res = [(b1 + a1 , b2 + a2) for (a1,a2) , (b1,b2) in combinations(test_list,2)]
    print(res)

defination30()    