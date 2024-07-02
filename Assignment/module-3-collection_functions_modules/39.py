# merge 2 python dictionaries
dict1 = {'a':1,'b' : 2,'c': 3,'d' : 4,'e' : 5}
dict2 = {'f':6,'g' : 7,'h': 8,'i' : 9,'j' : 10}
dict3 = {'k':11,'l' : 12,'m': 13,'n' : 14,'o' : 15}

dict4 = dict1
dict4.update(dict2)
dict4.update(dict3)
print(dict4)