# create dictionaries with object attributes

class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def print_details(self):
        print(self.name)
        print(self.age)
        print(self.city)

    def print_dict(self):
        return {'name' : self.name, 'age' : self.age ,'city' : self.city}


p1 = Person('Tejas',33,'Gandhinagar')    
p1.print_details()
print('========')
p2 = Person('ABC 1',34,'G1')
p2.print_details()
print('========')
print(p2.print_dict())
print('========')
print(p1.print_dict())