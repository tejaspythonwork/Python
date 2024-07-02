# write a code to count number of string where string length is 2 or more
# and also check first and last characters are same from
# given list of string
matched_string = []
list1 = ['string1','string2','string3','string4','string5','strrts','1s1']
length_list1 = len(list1)
print(length_list1)

for i in list1:
    substring_length = len(i)
    print(f'list item = {i} length = {substring_length}')

#print(substring_length)    
for str in list1:
    if len(str) > 0 and str[0] == str[-1]:
       matched_string.append(str)   
    
print(f'matched_string {matched_string}')    