# python code for check uppercase - lowercase - digit - special character

character = input('Enter Single Character')

def check_character(char):
   if char.islower():
      print('Lower Case')
   elif char.isupper():
      print('Upper Case')
   elif char.isdigit():
      print('Digit') 
   elif not char.islower() or not char.isupper() or not char.isdigit():
      print('Special Character')      

check_character(character)

