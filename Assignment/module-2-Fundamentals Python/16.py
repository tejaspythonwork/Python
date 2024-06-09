# Single String From 2 given string with seperated space
# swap first 2 character of each String

str1 = 'Learning python'
str2 = 'Python is object oriented programming language'
str3 = str1 + ' ' + str2

print(str3)

# def swap_2_chars(str):
#     if len(str) >= 2:
#         return str[2] + ' ' + str[0] + str[3:len(str)]   
#     return str 


def swap1(st1):
    if len(st1) >=2:
        return st1[1] + st1[0] + st1[2:len(st1)]
    return st1        


def swap2(st2):
    if len(st2) >=2:
        return st2[1] + st2[0] + st2[2:len(st2)]
    return st2

first_swap1 = swap1(str1)
second_swap2 = swap2(str2)

print(first_swap1)
print(second_swap2)
print('---------------------')
print('combined string')
print(first_swap1 + " - " + second_swap2)