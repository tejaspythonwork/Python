# pairs of complete string in two sets

def defination15(str1,str2):
    count = 0
    result = ''
    for s1 in str1:
        for s2 in str2:
            result = s1 + s2

            tmp_set = set([ch for ch in result if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]) 
            if len(tmp_set) == 26:
                return True

    print(count)
    
set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc'] 
set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz'] 
# result = defination15(set1,set2)
# if result == True:
#     print('String Contains Complete Alphabets')



def def15(set1,set2):
    pairs = [(st1,st2) for st1 in set1 for st2 in set2]
    return pairs




set1 = {"apple", "banana", "cherry"}
set2 = {"dog", "elephant", "frog"}
res = def15(set1,set2)
for pair in res:
    print(pair)