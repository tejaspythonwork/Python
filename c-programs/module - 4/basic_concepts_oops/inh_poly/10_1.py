class OverloadOp():
    def __init__(self,val):
        self.value = val


    def __lt__(self,other):
        return self.value < other.value 

    def __str__(self):
        return str(self.value) 



num1 = OverloadOp(100)
num2 = OverloadOp(20)

if num1 < num2 :
    print('num2 is large')
else:
    print('num1 is large')