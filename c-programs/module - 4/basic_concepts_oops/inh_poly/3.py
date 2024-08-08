class Person:
    def __init__(self):
        self.name = 'ABC'
        self.age = 25


class Student(Person):
    def __init__(self):
        self.percentage = '70 %'

    def input_data(self):
        self.name = input('Enter Student name: ')
        self.percentage = input('Enter Student Percentage: ')    

    def disp(self):
        print('Student')
        print(f'{self.name}')
        print(f'{self.percentage}')

class Teacher(Person):
    def __init__(self):
        self.salary = 16700
    
    def input_data(self):
        self.name = input('Enter Name - Teacher : ')
        self.salary = input('Enter Salary - Teacher : ')

    def disp(self):
        print('Teacher')
        print(f'{self.name}')
        print(f'{self.salary}')





obj = Student()
obj.input_data()
obj.disp()


# ====

obj1 = Teacher()
obj1.input_data()
obj1.disp()