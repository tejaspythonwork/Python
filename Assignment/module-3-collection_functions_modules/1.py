''' what is list how will you reverse a list
Ans: List is a collection of simmilar and dis-simmilar elements
it is mutable
It is orderable
Below example demonstarate that to reverse a list
'''  
list1 = ['A','B','C','D','E',1,2,4,5,3,6,9,3]
reverse_list = []
for i in range(len(list1)-1,-1,-1):
    reverse_list.append(list1[i])
    
    
print(reverse_list)    