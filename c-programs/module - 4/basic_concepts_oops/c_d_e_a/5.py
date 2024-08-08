# check triangle is Equilateral
# or Isosceles => x == y or x == z or y == z
# or Scalene => none of its side are equal

class triangle():
    
    def __init__(self):
        self.side1 = int(input('Please enter length for side 1: '))
        self.side2 = int(input('Please enter length for side 2: '))
        self.side3 = int(input('Please enter length for side 3: '))


    def equilateral(self):     
        if self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return 'Equilateral'
        else:
            return 'Not Equilateral'
        

    def isosceles(self):     
        if self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return 'Isosceles'
        else:
            return 'Not Isosceles'    
        

    def scalene(self):     
        if self.side1 != self.side2 or self.side1 != self.side3 or self.side2 != self.side3:
            return 'Scalene'
        else:
            return 'Not Scalene'    
        


obj = triangle()
print('==========================')
print(obj.equilateral())
print(obj.isosceles())
print(obj.scalene())