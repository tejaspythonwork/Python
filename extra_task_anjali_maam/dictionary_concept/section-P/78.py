# group values by their type

def defination78():
    data = {
        'a': 1, 
        'b': 'text', 
        'c': 2.5,
        'd': 3
        }
    grouped_data = {}

    for k,value in data.items():
        val_type = type(value).__name__

        if  val_type not in grouped_data:
            grouped_data[val_type] = [value]

        else:
            grouped_data[val_type].append(value)    



    print(grouped_data) 

defination78()               