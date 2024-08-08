import math as m

class def11():
    def __init__(self):
        # rectangle
        self.w = 100
        self.l = 20
        self.area_of_rect = self.w * self.l

        # triangle
        self.h = 10
        self.b = 10
        self.area_of_triangle = (self.h * self.b) // 2
        # circle
        self.r = 100
        self.area_of_circle = m.pi * self.r * self.r



    def disp(self):
        print(f'Area of rectangke = {self.area_of_rect}')
        print(f'Area of triangle = {self.area_of_triangle}')
        print(f'Area of circle = {self.area_of_circle}')




obj = def11()
obj.disp()