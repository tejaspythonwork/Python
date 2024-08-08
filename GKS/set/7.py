# find missing and additional values in 2 lists


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

def find_missing_additional(s1,s2):
    missing_in_list1 = []
    additional_in_list1 = []

    for elem in s2:
        if elem not in s1:
            missing_in_list1.append(elem)


    for elem in s1:
        if elem not in s2:
            additional_in_list1.append(elem) 

    print(additional_in_list1)
    print(missing_in_list1)


find_missing_additional(list1,list2)