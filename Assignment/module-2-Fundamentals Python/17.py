# add "ing" at the end of given string - length should atleast 3
# if string already ends with "ing" add "ly" 
# if string length is less than 3 make it return and unchanged


def one_seven(str1):
    if len(str1) >= 3:
        if str1.endswith('ing'):
            print('Ends with ing')
            str2 = str1 + 'ly'
            return str2 
        else: 
            str3 = str1 + 'ing'
            return str3
    else:
        return str1

print(one_seven('str'))