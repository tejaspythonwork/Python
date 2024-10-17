# remove key from nested dictionaries
# remove address from nested dictionaries
def defination44():
    profile = {'user': 
               {'name': 'Jane', 'age': 28, 
                'address': {'city': 'Seattle', 'state': 'WA'}}}
    

    removed_address = profile['user'].pop('address')
    print(f'Address which are removed = {removed_address}')
    print(f'After removing address dictionary will be {profile}')


defination44()    