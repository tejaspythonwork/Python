# compare 2 strings without using library function

text_str_1 = 'Hello, how are you'
text_str_2 = 'Hello, how are you'
text_str_3 = ''

def defination5(text_1,text_2):

 for i in text_1.split():
    for j in text_2.split():
        if i == j:
            # print('String id matched')
            return True
        else:
            # print('String not matched')    
            return False
        
result = defination5(text_str_1,text_str_2)

def print_result(res):
 if res == True:
    print('String is matched') 
 else:
   print('String not match')       

print_result(result)
print('=======================')
print('Another Parameters:')
result2 = defination5(text_str_1,text_str_3)
print_result(result2)

