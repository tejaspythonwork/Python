# convert school name into abbreviated form
'''def convert_to_abbreviated(school_name):
    for e in school_name:
        print(e)
    else:
        print('School Name Has Been Converted')
name = input('Enter School Name')
s_name = convert_to_abbreviated(name)'''
#print(s_name)       
def abbreviate_school_name(school_name):
    # Split the school name into words
    words = school_name.split()
    
    # Take the first letter of each word and join them together
    abbreviation = ''.join(word[0].upper() for word in words)
    
    return abbreviation

school_name = "Massachusetts Institute of Technology"
abbreviation = abbreviate_school_name(school_name)
print(f"The abbreviation of '{school_name}' is '{abbreviation}'")
