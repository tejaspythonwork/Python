# concatinate 2 strings using operator overloading in python

class A:
   def __init__(self):
      self.str1 = 'Hi'
      self.str2 = 'Tejas'
      self.concated_str = ''


   def __add__(self):   
      self.concated_str = self.str1 + ' ' + self.str2 + '!'
   
   def __str__(self):
      return self.concated_str


a = A()
a.__add__()
print(a.__str__())
