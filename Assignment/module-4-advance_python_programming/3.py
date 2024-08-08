# Append text to a file and display text in file

with open('F:/Python/Python/Assignment/module-4-advance_python_programming/files/file_1.txt','a+') as f:
   f.seek(0)
   content = f.read()
   print(content)
   print('****************************************************')
   print('====================================================') 
   new_content = input('type content do you want to append: ')
   f.write(f'\n{new_content}')
   print('====================================================') 
   print('After Appending')
   f.seek(0)
   content = f.read()
   print(content)
   f.close()