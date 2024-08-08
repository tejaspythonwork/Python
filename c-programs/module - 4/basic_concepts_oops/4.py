# class - named - circle
# private - radius
# calculate area 
# and circumference

import math as m

class Circle:
    
    def __init__(self):
        self.__radius = 0

    def area(self):
       self.__radius = 50
       return m.pi * self.__radius

    def circumference(self):
        self.__radius = 50
        return 2 * m.pi * self.__radius 



obj = Circle()
print(obj.area().__round__(2))
print(obj.circumference().__ceil__())       