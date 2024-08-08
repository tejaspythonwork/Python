# area of rectangle using inheritance

class Shape:
    def __init__(self):
        self.width = int(input('please enter width: '))
        self.length = int(input('Please enter length: '))        

class Rectangle(Shape):        
    def area(self):
        return self.width * self.length
    

obj = Rectangle()
res = obj.area()    
print(res)