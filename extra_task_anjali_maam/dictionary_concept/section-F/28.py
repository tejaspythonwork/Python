# merge dictionaries with conflicts resolved 


 
def defination28():
    dict1 = {'x': 1, 'y': 2}
    dict2 = {'y': 3, 'z': 4}
    dict3 = (dict)
    dict3 = dict1.copy()


    for k,v in dict2.items():
        dict3[k] = dict3.get(k,0)  + v

    


    print(dict3)

defination28()           