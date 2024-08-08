# how to check that variable is an object of class named A

class A:
    pass


ob1 = A()
if isinstance(ob1,A):
    print('ob1 is an instance of class A')