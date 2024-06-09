# code for first 2 and last 2 character from single String 
# if length <=2 return String

str1 = input('Enter String')


def  twenty_one(string1):

    if len(string1) <=2:
     print(f'You have entered = {string1}')
     return string1
    elif len(string1) > 2:
     print('morethan 2 chars')
     # first 2 character
     first_two = string1[0:2]
     print('First 2 characters')
     print(first_two)   
     # last 2 character
     last_two = string1[len(string1) - 2 : len(string1)]
     print('Last 2 characters')
     print(last_two)
     return string1
       

str2 = twenty_one(str1)
print(str2)