 # generate dictionaries with key-value pairs from function

def defination59():
  
  keys = get_dict_keys()
  vals = get_dict_vals()

  res = {k:v for k,v in zip(keys,vals)} 
  print(res) 




def get_dict_keys():
    dict_keys = []
    for i in range(1,6):
        ip_key = input('please enter key: ')
        dict_keys.append(ip_key)

    return dict_keys


def get_dict_vals():
    dict_vals = []
    for i in range(1,6):
        ip_val = input('please enter val: ')
        dict_vals.append(ip_val)
    return dict_vals    


defination59()


 