# addition sub mult div

class Operation:
    def __init__(self):
        self.num1 = 10
        self.num2 = 50 

        print(f'Addition = {self.num1 + self.num2}')
        print(f'Substraction = {self.num1 - self.num2}') 
        print(f'Multiplication = {self.num1 * self.num2}')
        print(f'Division = {self.num1.__floordiv__(self.num2)}')  

obj = Operation()        
