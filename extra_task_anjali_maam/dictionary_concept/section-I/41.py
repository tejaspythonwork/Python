# access nested dictionary values

def defination41():
    profile = {
        'user': {'name': 'Jane','age': 28, 'address': {'city': 'Seattle', 'state': 'WA'}}}
    
    print(profile['user']['address']['city'])


defination41()