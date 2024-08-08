# class - rectangle
# private members like length and width
# find perimeter and area

class Rectangle:

   def __init__(self):
       self.length = int(input('Enter Length: '))
       self.width = int(input('Enter Width: ')) 


   def area(self):
       self.area = self.length * self.width       
       return self.area           


   def perimeter(self):                    
       self.perimeter = 2 * (self.length + self.width)
       return self.perimeter 

obj = Rectangle()
print(obj.area()) 
print(obj.perimeter())      