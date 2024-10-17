# list comprehension nested list to flatten list

def defination29():
    nested = [[1, 2],[3, 4], [5, 6]]
    res = [i for x in nested for i in x]
    print(res)

defination29()    