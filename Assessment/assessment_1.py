# Python e-notebook console based application
from my_package import generate_note,write_to_file,use_date_time,read_all_files


import os
import glob


class Assessment1:
  
  menu = '''
        welcome to python E-Note

        press 1.Generate Note
        press 2.View Note
        press 3.exit
    '''
  def __init__(self):
    self.status = True
    self.generateor_name = ''
    self.e_note_title = ''
    self.e_note_content = ''

  def display_menu(self):
        while self.status:
            print(self.menu)
            try:
                choice = int(input('Enter Your Choice: '))
                
                if choice == 1:
                    print('Generate Note')
                    write_to_file.write_to_file(self)
                elif choice == 2:
                     read_all_files.read_all_files(self)
                     print('View Note') 
                elif choice == 3:
                    self.status = False 
                else:
                    print('Please enter a valid choice between 1 to 3.')
            except ValueError:
                print('Invalid input. Please enter a valid integer.')





  
obj = Assessment1()
obj.display_menu()
# obj.date_and_time()
# obj.write_to_file()
# obj.read_all_files()