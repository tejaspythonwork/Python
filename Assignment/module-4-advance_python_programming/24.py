# calculate area and perimeter of circle

import math 

class Circle:

    def __init__(self,radius) :
        self.radius = radius


    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius        
    
    def disp_all_values(self):
        print(f'Perimeter = {self.perimeter().__round__(2)}')
        print(f'Area = {self.area().__round__(2)}')


c1 = Circle(100) 
c1.disp_all_values()       