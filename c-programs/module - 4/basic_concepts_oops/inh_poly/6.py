# private public and protected

class ExampleAccessSpecifier:
    def __init__(self):
        self.__name = 'ABC'
        self._age = 15
        self.address = 'India'

    def disp_data(self):             
        print(f'Name (privvte) = {self.__name}')
        print(f'Age (protected) = {self._age}')
        print(f'Address (public) = {self.address}')


class Inh(ExampleAccessSpecifier):
    def __init__(self):
        super().__init__()

    def child_disp_data(self):
        super().disp_data()

obj = ExampleAccessSpecifier()
obj.disp_data()        
print('===========================')
print('Accessing using child class')
# ===
obj_child = Inh()
obj_child.child_disp_data()
print('===========================')