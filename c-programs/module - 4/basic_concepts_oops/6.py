# class Person with fields like
# name-age-country
# with setter and getter

class Person:
    
    def __init__(self):
        self.__name = 'ABC'
        self.__age = 15
        self.__country = 'India'


    def set_name(self,name_1):
        self.__name = name_1

    def set_age(self,age_1):
        self.__age = age_1

    def set_country(self,cnt_1):
        self.__country = cnt_1

    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country

    def get_age(self):
        return self.__age
    



obj = Person()
print(f'=====Without Using Setter=====')
print(f'name = {obj.get_name()}')
print(f'age = {obj.get_age()}')
print(f'country = {obj.get_country()}')

print(f'=====With Using Setter=====')
obj.set_name('New Name With Setter')
obj.set_age(20)
obj.set_country('New India')

print(f'============================')
print(f'name = {obj.get_name()}')
print(f'age = {obj.get_age()}')
print(f'country = {obj.get_country()}')
