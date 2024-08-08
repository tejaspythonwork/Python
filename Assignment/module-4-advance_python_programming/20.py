# program that can write only odd numbers
# else generate an error

def example20():
    try:
     number_ip = int(input('enter number: '))
     if number_ip % 2 !=0:
        raise EvenNumberException(num=number_ip,msg='Even Numbers Are Not Allowed')
    except EvenNumberException as e:
       print(f'Error = {e.msg} , you have entered = {e.num}')



class EvenNumberException(Exception):    
    def __init__(self,num,msg):
        self.num = num
        self.msg = msg
        super().__init__(self.num,self.msg)    

example20()        