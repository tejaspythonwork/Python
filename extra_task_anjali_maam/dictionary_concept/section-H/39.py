# find missing key in dictionary

def defination39():
    required = {'a': 1, 'b': 2, 'c': 3}
    present =  {'a': 1, 'c': 3}
    res_dict = { k:v for k,v in required.items() if k not in present or present[k]!=v }
    

    
    print(res_dict)

defination39()    