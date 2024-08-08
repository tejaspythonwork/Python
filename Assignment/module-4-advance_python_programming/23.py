# construct area of rectangle by length and width
class Rectangle():

    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.area_of_rect = self.width * self.length

    def disp(self):
        print(f'Area of rectangle = {self.area_of_rect.__round__(2)}')


rect1 = Rectangle(100,100) 
rect1.disp()            
print('------------')
rect2 = Rectangle(1.9,4.2)
rect2.disp()