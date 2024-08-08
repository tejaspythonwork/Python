# student marksheet using multiple inheritance

class student:

    def __init__(self):
        self.name = input('Enter Your Name: ')


class marks:
    def __init__(self):
        self.marks = 100
        self.subject1 = 50        
        self.subject2 = 51
        self.subject3 = 98        

class Marksheet(student,marks):
    
    def __init__(self):
        student.__init__(self)
        marks.__init__(self)



    def disp_data(self):
        print(f'Marksheet of {self.name}')
        print(f'{self.name}')
        print(f'subject-1 {self.subject1}')
        print(f'subject-2 {self.subject2}')
        print(f'subject-3 {self.subject3}')
        print(f'Total =  {self.subject1 + self.subject2 + self.subject3}')
        total = self.subject1 + self.subject2 + self.subject3
        avg = total//3
        print(f'Average = {avg}')






obj = Marksheet() 
obj.disp_data()               