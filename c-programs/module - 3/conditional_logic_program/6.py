# find character wovel or not 

def check_vowel(character):
    char_vowel_list = ['a','e','i','u','o']
    if character in char_vowel_list:
        print('Entered Character Is vowel')
    else: 
        print('Not vowel')


character = input('Enter Character: ')
check_vowel(character.lower())     
