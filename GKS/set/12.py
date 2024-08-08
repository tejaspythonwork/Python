# Accept String which contains all Vowels

def definatin12():
    count = 0
    vowels = 'aeiou'
    absent_vowel = []
    present_vowel = []
    # text_str = input('Enter String: ')
    while True:
     try:
      text_str = input('Please Enter String: ')
      for char in text_str:
        if char in vowels:
            present_vowel.append(char)
            count = count + 1

      text_present_vowels = set(''.join(present_vowel))
      print(count)
      print(text_present_vowels)
      if len(text_present_vowels) == len(vowels):
          print('String Accepted')
      else:
          print('String not accepted')
          raise ValueError('Please enter correct string')

      for absnt in vowels:    
         if absnt not in present_vowel:
             absent_vowel.append(absnt)
      print(present_vowel)    
      print(absent_vowel)
     except ValueError as e:
        print(e) 
     else:
        break    


definatin12()