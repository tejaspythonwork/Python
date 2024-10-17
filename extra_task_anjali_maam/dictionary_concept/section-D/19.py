# extract key and values into list 
def defination19():
     data = {'apple': 10, 'banana': 20,'cherry': 30}
     key_list = []
     val_list = []

     for k,v in data.items():
        key_list.append(k)
        val_list.append(v) 

     print(f'keys = {key_list}')
     print(f'values = {val_list}') 


defination19()