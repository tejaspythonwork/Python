# write python function to insert a string inside middle of String

def insert_at_middle(original_string,insert_string):
    middle_index = len(original_string)//2 
    print(middle_index)
    new_string = original_string[:middle_index] + insert_string + original_string[middle_index:]
    return new_string


insert_str = 'really '
str1 = '    Python is great language'

main_str = insert_at_middle(str1,insert_str)
print(main_str)