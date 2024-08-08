# simple calculator using class

class Calculator:
    def __init__(self):
        self.num1 = int(input('Please enter 1st number'))       
        self.num2 = int(input('Please enter 2nd number'))       

    def addition(self):    
        return self.num1 + self.num2
    
    def substraction(self):
        return self.num1 - self.num2 
    

    def calc(self):
        self.status = True
        menu = '''
        1.Addition
        2.Substraction
        '''
        while self.status:
            print(menu)
            choice = int(input('please enter your choice'))

            match choice:
                case 1:
                   res = self.addition()
                   print(res)
                case 2:
                   res = self.substraction()
                   print(res)
                case 3:
                    self.status = False
                case default:
                    print('please enter choice between 1 - 2')        

obj = Calculator()   
obj.calc()                 