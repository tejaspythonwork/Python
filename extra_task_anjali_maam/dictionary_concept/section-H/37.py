# nested dictionary values extraction

def defination37():
    data = {'user1': 
            {'name': 'Alice', 'age': 30}, 
            'user2': 
            {'name': 'Bob', 'age': 25}
            }
    
    for i in data.values():
        print(i['age'])


defination37()