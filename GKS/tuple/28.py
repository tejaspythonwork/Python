# flatten tuple list to string 

def defination28():
    test_list = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
    res_list = []

    [res_list.extend(ele) for ele in test_list ]
    print(res_list)
    string_text = ','.join(res_list)
    print(string_text)


defination28()