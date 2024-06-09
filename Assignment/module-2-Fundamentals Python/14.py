# find occurences of sub String in a String

count_occurences = 0
str_input = input('Enter String')
str_sub_input = input('Enter Substring')

count_occurences = str_input.count(str_sub_input)
print(f"The character '{str_sub_input}' appears {count_occurences} times in '{str_input}'.")