class Student:
    
    def __init__(self):
        self.roll_number = 1

class Test:
    def __init__(self):
        self.subject_1 = 50 
        self.subject_2 = 50

class Result(Student,Test):
    def __init__(self):
        self.total_marks = 100
        Student.__init__(self)
        Test.__init__(self)

    def disp(self):
        print(self.roll_number)
        print(self.subject_1) 
        print(self.subject_2)
        print(self.total_marks) 


obj = Result()
obj.disp()        

                    
