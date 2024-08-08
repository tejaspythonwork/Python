# multi level inheritance

class A:
    def __init__(self):
        print('Constructor of class A is called')
        

class B(A):
    def __init__(self):
        print('Constructor of class B is called')
        super().__init__()        

class C(B):
    def __init__(self):
        print('Constructor of class C is called')
        super().__init__()


c = C()