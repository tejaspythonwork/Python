# how to compare 2 lists
list1 = ['A','B','C','D','E']
list2 = ['E','D','C','B','A']


mismatched_items = [(item1,item2) for item1,item2 in zip(list1,list2) if item1!=item2 ]
print('Mismatched Items')
for itm1,itm2 in mismatched_items:
    print(f'{itm1}!={itm2}')