class Date:

    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year


    def set_day(self):
      while True:      
        day = int(input('Please enter day: '))
        try:
         if day > 30:
            raise ValueError('Day Should Not Greater Than 30') 
         else:
          self.day = day 
          break   
        except ValueError as e :
            print(e)




    def set_month(self):
       while True: 
        month = int(input('Please enter month: '))  
        try:
           if month > 12:
              raise ValueError('Month should between 1 - 12')
           else:
              self.month = month        
              break
        except ValueError as e :
           print(e)       
    
    
    def set_year(self):
        while True:
          year = int(input('Please enter year: '))  
          try:
             if not 1000 < year < 2050:
                raise ValueError('Year should between 1000 - 2050')
             else:
                self.year = year 
                break 
          except ValueError as e: 
             print(e)
                    

    def get_day(self):
        return self.day    

    def get_month(self):
        return self.month 

    def get_year(self):
        return self.year    
   

obj = Date(1,1,1)
obj.set_day()
obj.set_month()
obj.set_year()
print('You have entered following')
print(f'Day = {obj.get_day()}')
print(f'month = {obj.get_month()}')
print(f'year = {obj.get_year()}')
print('Date = ')
print(f'{obj.get_day()}-{obj.get_month()}-{obj.get_year()}')