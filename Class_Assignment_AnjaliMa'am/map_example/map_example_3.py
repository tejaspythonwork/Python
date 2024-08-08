# list of name and convert it into upper case

l1 = ['dsdf','aasf','qweq','zgadg','afat']

def convert_upper_case(list_l1):
    l2 = list_l1.upper()
    return l2



result = list(map(convert_upper_case,l1))
print(result)