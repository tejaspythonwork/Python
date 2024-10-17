# filter dictionaries using 
# so that values and
# between 5 to 10


def defination79():
    res = []
    data = {'a': 5, 'b': 10, 'c': 15}
    for k,v in data.items():
        if v in range(5,11):
            res.append({k:v })
    print(res)

defination79()