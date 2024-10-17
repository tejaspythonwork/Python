# add key-value pair to nested dictionaries

def defination43():
     val = {'phone': '555-1234' }
     profile = {'user': {'name': 'Jane', 'age': 28}}
     profile['user'].update(val)

     print(profile)



defination43()     