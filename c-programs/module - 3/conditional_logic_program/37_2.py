# consonent or vowel using switch case

def consonent_vowel():
    input_char = input('please enter single character').lower()

    match input_char:
        case 'a': 
           return 'vowel'
        case 'e': 
           return 'vowel'
        case 'i': 
           return 'vowel'
        case 'o': 
           return 'vowel'
        case 'u': 
           return 'vowel'
        case default:
          return 'Consonent'
       
word_checker = consonent_vowel()
print(word_checker)
