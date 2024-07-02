# to check list contains sublist
list_of_elements = [1, 2, [3, 4], 5, [6, 7], 8, "string"]
contains_sublist = False
sub_list = [3, 4]


for e in list_of_elements:
    if isinstance(e,list):
        contains_sublist = True   
        break

if contains_sublist:
    print('List Contains Sublist')
else:
    print('List Not Contains Sublist')

