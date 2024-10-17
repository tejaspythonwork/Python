# create summary dictionaries from list of dictionaries

def defination60():
    summary_dict = {}
    records = [
        {
        'name': 'John',
        'sales': 100
        },
        {
        'name': 'Jane', 
        'sales': 150
        }, 
        {
         'name':'Joe', 
         'sales': 200
        }
    ]
    

    for k1 in records:
        for k,v in k1.items():
            if k in summary_dict:
                summary_dict[k].append(v)
            else:
                summary_dict[k] = [v]
    # print(summary_dict)


    for kv1,kv2 in summary_dict.items():
        if kv1 == 'sales':
            summary_dict[kv1] = sum(kv2)
    print(f'summary dict = {summary_dict}')         

defination60()