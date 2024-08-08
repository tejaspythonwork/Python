# create class named car with private members
# like company model and year
# getters and setters
# 

class Car:

    def __init__(self):
        self.__company = 'Toyota'
        self.__model = 2015
        self.__year = 2020


    def set_company(self,cmpny):
        self.__company = cmpny

    def set_model(self,mdl):
        self.__model = mdl
      
    def set_year(self,yr):
        self.__year = yr
  
    def get_company(self):
        return self.__company
    
    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year    


obj = Car()
print('Without Using Setters')
print(obj.get_company())
print(obj.get_model())
print(obj.get_year())
print('==================================')
print('With using setters')
print('==================================')
obj.set_company('New Cmpny')
obj.set_model(1010)
obj.set_year(2020)
print('----------------------------------')
print(obj.get_company())
print(obj.get_model())
print(obj.get_year())
