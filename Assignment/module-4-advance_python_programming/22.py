# how to define a class in python? what is self     
# give an example of python class
# Ans. class is a combination of data members - variables and 
# member function - 
# it consist of properties and behaviour
# properties means variables and behaviour are methods which 
# acts on properties 
# properties can changed means modifiable and method acts on properties
# ------------------------------------
# self = means it is a reference to particular elements of a class
# which is used to access member variables and member function
# ----- Python Class -----

class Student:
    def __init__(self,roll_number,name,age,total_marks):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.total_marks = total_marks
        self.avg = self.total_marks/3

    def display(self):
        print(f'Roll number = {self.roll_number}')
        print(f'Roll name = {self.name}')
        print(f'Roll Age = {self.age}')
        print(f'Roll Total Marks = {self.total_marks}')
        print(f'Roll Average = {self.avg}')

obj1 = Student(1,'ABC',25,300)
obj2 = Student(2,'DEF',22,160)
obj1.display()
print('------------------')
obj2.display()