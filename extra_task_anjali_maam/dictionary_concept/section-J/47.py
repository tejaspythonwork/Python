# find key with max value

def defination47():
    scores = {'math': 85, 'science': 90, 'history': 88,'A' : 110,'B' : 155}
    highest_val = max(scores.items(),key= lambda x:x[1])
    print(highest_val)


defination47()    