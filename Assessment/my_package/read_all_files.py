import glob
import os


def read_all_files(self):
     files = glob.glob(os.path.join('F:\Python\Python\Assessment\my_notes','*'))  
     for f in files:
          if os.path.isfile(f):
               with open(f,'r') as f: 
                    content = f.read()
                    print(content)
                    print('-' * 40)