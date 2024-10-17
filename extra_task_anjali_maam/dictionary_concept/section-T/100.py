# compute average values of dictionaries

def defination100():
    data = {
            'a': 10, 
            'b': 20, 
            'c': 30
            }
    sum = 0
    avg = 0
    len_data = len(data.values())    
    for k,v in data.items():
        sum = sum + v


    avg = sum//len_data
    print(f'sum = {sum}')
    print(f'avg = {avg}')    

defination100()