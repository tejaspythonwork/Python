# find first appearance of substring not and poor from given string
# if not follows poor replace whole not...poor sub string with good 
# return resulting string



def eighteenth(string1):
    index_not = string1.find('not')
    index_poor = string1.find('poor')
    
    if index_not !=-1 and index_poor!=-1 and index_not< index_poor:
        return string1[:index_not] + 'good' + string1[index_poor + len('poor'):]
    else:
        return string1
         

str1 = 'The movie is not that poor, its actually quite good.'
function_18 = eighteenth(str1)
print(f'After Execution string = {function_18}')


