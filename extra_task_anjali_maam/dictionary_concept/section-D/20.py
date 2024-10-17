# filter dictionary by value

def defination20():
     scores = {'math': 85, 'english': 78,'science': 92}
     filter_func = lambda x:x[1] > 80
     filter_dict = dict(filter(filter_func,scores.items()))
     print(filter_dict)


defination20()