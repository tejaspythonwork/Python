# reverse of string using recursion

text_str = 'hello'
text_str_1 = text_str[-1]
print(text_str_1)


def defination_recursion(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + defination_recursion(s[:-1])
    
input_str = '1234567890' 
print(defination_recursion(input_str))   
