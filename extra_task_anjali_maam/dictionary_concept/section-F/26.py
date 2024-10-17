# advance dictionary operation

def defination26():
     dict1 = {'a': 1, 'b': 2}
     dict2 = {'b': 3, 'c': 4}

     s1_k = set(dict1.keys())
     s2_k = set(dict2.keys())

     s1_v = set(dict1.values())
     s2_v = set(dict2.values())

     print('same keys in both dictionaries')
     s3_k = s1_k & s2_k
     print(s3_k)


     print('same values in both dictionaries')
     s3_v = s1_v & s2_v
     print(s3_v)
     if not s3_v:
          print('no common values in dictionaries')


defination26()