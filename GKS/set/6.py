set1 = {1,2,3,55,44,19,6,66,456}
set2 = {11,456,22,55,44,123,66,7}
set3 = {0,11,22,66,456,655,0,-99,56,55}

def find_common_set(s1,s2,s3):
  common = set()
  for element in s1:
    if element in s2 and element in s3:
        common.add(element) 

  return common 

result = find_common_set(set1,set2,set3) 
print(result)