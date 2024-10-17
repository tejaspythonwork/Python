# count occurences of each key in list of dictionaries

from collections import Counter


def defination75():
    records = [
        {'name': 'Alice'},
        {'name': 'Bob'}, 
        {'name': 'Alice'}, 
        {'name': 'Charlie'}
        ]
    
    result = Counter(i['name'] for i in records)
    print(result)    


defination75()    