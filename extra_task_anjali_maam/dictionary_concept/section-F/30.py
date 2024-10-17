# remove duplicates dictionaries

def defination30():
    new_list = []
    entries = [
        {'name': 'Alice','age': 30}, 
        {'name': 'Bob', 'age': 25}, 
        {'name': 'Alice', 'age': 30}
        
    ]
    for i in entries:
        if i not in new_list:
            new_list.append(i)
    

    print(new_list)

defination30()    