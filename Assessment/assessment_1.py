# Python e-notebook console based application
import datetime
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
    
  '''def display_menu(self):
     while self.status:
       try:  
        print(self.menu)
        choice = int(input('Enter Your Choice: '))
        while True:
          # try:
           
          #  break
          # except ValueError('Please enter valid integer') as e : 
            # print(e)
         
           if choice == 1:
            print('generate note')
         # self.generate_note()
            self.write_to_file()
           if choice == 2:
            self.read_all_files()
            print('View Note') 
           if choice == 3:
            self.status = False 
      
       except TypeError('Please enter valid choice:(1/2/3) ') as e:
          print(e) 
'''
  
  def display_menu(self):
        while self.status:
            print(self.menu)
            try:
                choice = int(input('Enter Your Choice: '))
                
                if choice == 1:
                    print('Generate Note')
                    self.write_to_file()
                elif choice == 2:
                    self.read_all_files()
                    print('View Note') 
                elif choice == 3:
                    self.status = False 
                else:
                    print('Please enter a valid choice between 1 to 3.')
            except ValueError:
                print('Invalid input. Please enter a valid integer.')





  def generate_note(self):

    while True:
        try:
                self.generateor_name = input('Please enter note Generator Name: ')
                if not all(char.isalpha() or char.isspace() or char == '-' for char in self.generateor_name):
                    raise ValueError("Please enter a valid string containing only letters, spaces, or hyphens.")
        except ValueError as e:
                print(e)
        else:
                break

    while True:
        try:
                self.e_note_title = input('Please enter e-note title: ')
                if not self.e_note_title.replace(" ","").isalpha():
                    raise ValueError("Please enter a valid string.")
        except ValueError as e:
                print(e)
        else:
                break

    while True:
        try:
                self.e_note_content = input('Please enter e-note Content: ')
                if not isinstance(self.e_note_content, str) or self.e_note_content.strip() == "":
                    raise ValueError("Please enter a valid content.")
        except ValueError as e:
                print(e)
        else:
                break   


    return self.generateor_name,self.e_note_title,self.e_note_content             

  def date_and_time(self):
   dt = datetime.date.today()
   tm = datetime.datetime.now()
   tm_format = tm.strftime('%H:%M:%S')        
   dt_format = dt.strftime('%d-%m-%Y')      
#    print(dt)
#    print(dt_format)
#    print(tm_format)
   return dt_format,tm_format 




  def write_to_file(self):
    date_1,time_1 = self.date_and_time()
    print(date_1)
    print(time_1)
    generator,title,content = self.generate_note()
    # print(generator)
    # print(title)
    # print(content)
    with open(rf'F:\Python\Python\Assessment\my_notes\{title}.txt','w+') as file:
        file.write(f'{date_1} \n{time_1} \n')
        file.write(f'\nE-Note Title = {title}')
        file.write(f'\nE-Note Description = {content}')
        file.write(f'\nE-Note Generator = {generator}')
        file.write(f'\n=================================================')
    

  def read_all_files(self):
     files = glob.glob(os.path.join('F:\Python\Python\Assessment\my_notes','*'))  
     for f in files:
          if os.path.isfile(f):
               with open(f,'r') as f: 
                    content = f.read()
                    print(content)
                    print('-' * 40)


obj = Assessment1()
obj.display_menu()
# obj.date_and_time()
# obj.write_to_file()
# obj.read_all_files()