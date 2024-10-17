# sort dictionary values

def defination38():
    scores = {'Alice': 90, 'Bob': 80, 'Charlie': 85}
    new_dict = sorted(scores.items(),key = lambda x:x[1],reverse=True)
    print(new_dict)


defination38()