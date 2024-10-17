# transform keys to upper case 

def defination68():
    data = {'name': 'Alice', 'city': 'New York'}
    new_dict = {k.upper():v for k,v in data.items()}
    print(new_dict)



defination68()