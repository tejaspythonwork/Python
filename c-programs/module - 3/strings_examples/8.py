# count total number of vowels and consonent in string

def defination8():
    vowels = 'aeiou'
    vowel_count = 0
    consonent_count = 0
    text_str = 'Hi, how are you, I am fine too'

    for c in text_str:
        if c.isalpha():
            if c in vowels:
                vowel_count = vowel_count + 1 
            else:
                consonent_count = consonent_count + 1

    return vowel_count,consonent_count 

v,c = defination8()

print(f'Vowel Count - {v}')
print(f'Consonent Count - {c}')