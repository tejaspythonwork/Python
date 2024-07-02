# create dictionary from string
# track count of letters from string


def function47():   
    dict1 = {}
    str1 = 'w3resource'

    for st in str1:
        if st in dict1:
           dict1[st] = dict1[st] + 1
        else:
            dict1[st] = 1    
    
    print(dict1)
function47()        