# list of names and convert it into capatalize

l1 = ['asd','qwe','rty','uio','cvb']

def conert_into_capatialize(x):
    l2 = x.capitalize()
    return l2


result = list(map(conert_into_capatialize,l1))
print(result)