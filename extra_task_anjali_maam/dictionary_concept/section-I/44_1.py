# remove state from this dictionaries

def defination44_1():
    profile = {'user': 
               {'name': 'Jane', 'age': 28, 
                'address': {'city': 'Seattle', 'state': 'WA'}}}
    
    removed_state = profile['user']['address'].pop('state')
    print(removed_state)
    print(f'After Removing = {profile}')

defination44_1()