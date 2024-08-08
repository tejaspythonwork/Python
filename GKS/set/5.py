# check 2 lists have atleast one common elements

s1 = [1,2,3,5,7]
s2 = [5,6,99,0,8]

def common_member(a,b):
    return any(i in a for i in b)

print(common_member(s1,s2))