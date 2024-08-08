# what are oops concept? is multiple inheritance supported in python
'''
Ans:
OOPs concept consist of following:
1.class:
class is a blueprint,

class is a wrapper around data and behaviour
in other words we can say class is a datatype

class is declared with class keyword


2.object:
variable of class type is known as object
with the help of object we can access variables and methods of
class
when we create object of class it occupies space in memory called 
RAM
# =========
3.inheritance:
to use properties and methods of one class in another class is
known as inheritance

the benifit of inheritance is one class can access properties and methods of 
another class

Types:
1.single level inheritance:
when one class named A - acts as parent class 
and class named B acts as child class 

example:
class A:
  pass
  

class B(A):
  pass


2.multi-level-inheritance:
when one class named A acts as parent class for class B and 
class B acts as parent class for class C this kind of inheritance 
is termed as multi-level-inheritance


class A:
  pass
  
class B(A):
  pass
    
class C(B):
  pass

  
the benifits of multilevel inheritance is that class c can access properties
and behaviour of class B and class A

3.multiple - inheritance:
when there is morethan 2 parent classes and one child class 
this kind of inheritance is known as multiple inheritance

class A:
  pass
  
class B:
  pass
  
class C(A,B):
  pass  

4.hybrid - inheritance:
when there is one parent class and 2 or more child class
and this 2 or more child class be parent class of 
child class again

class Parent1:
    pass
    
class Child1(Parent1):
    pass


class Child2(Parent1):
    pass


class Child(Child1,Child2):
    pass    


here Child1 and Child2 is parent class for Child


5.hierarchical inheritance:
when there is one parent class and it has morethan one child class

class Parent:
    pass
    

class Child1(Parent):
    pass


class Child2(Parent):
    pass        

# =======
 
4.Polymorphism:
poly - means many
and
morph - means form
means one method with multiple and diffrent parameters
2 types
1.Method Overloading:
method with same name but diffrent parameters
partially supported by python such as
A.with the help of *args and **kwargs
B.default value should be passed when function defination

2.method overriding:
same method found in child and parent class


5.Encapsulation:
capsulate data and methods into single unit is known as 
Encapsulation
example: class

6.Abstraction:
we can not create an object of an abstract class
to create an abstract class you have to use abc library and 
import ABC - built-in module

whatever method we declare in abstract class and when abstract
class inherited by other child class 
the particular child class have to initiate all methods of
parent class

abstrction means hinding unnecessasary details and showing 
only functionality

7.Constructor:
the main function of constructor is to initialize elements/variables 
of class 
to define constructor we can use double underscore init method with 
def keyword
every method has a keyword named self - which reference to variable of
class type
# =====

yes multiple inheritance is supported by python

'''