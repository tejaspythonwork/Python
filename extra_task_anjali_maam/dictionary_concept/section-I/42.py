# update nested dictionary values
# update state to 'OR'

def defination42():
    profile = {'user': 
               {'name': 'Jane', 'age': 28, 
                'address': {'city':'Seattle', 'state': 'WA'}}}
    

    val = profile['user']['address']['state']
    print(f'old val = {val}')
    profile['user']['address']['state'] = 'OR'
    new_val = profile['user']['address']['state'] 
    print(f'new val = {new_val}')

defination42()    