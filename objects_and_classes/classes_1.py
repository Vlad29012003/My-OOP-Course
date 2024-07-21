# class TestClass:
#     def get_name(self):
        # print('Test')

class Users:
    name = "Jon"
    last_name = "Jonson"
    genre = "female"
    age = 13

    def get_name(self):
        print(self.name)
    
    def get_age(self):
        return f'{self.age}'
    
    def get_genre(self):
        return f'{self.genre}'
    
    def  get_last_name(self):
        return f'{self.last_name}'





class MyClass:
    class_attribute = 10
    def __init__(self , instance_attribute):
        self.instance_attribute = instance_attribute

my_instance_attribute = MyClass(20)
print(MyClass.__dict__)
print(my_instance_attribute.__dict__)


a = 10
b = 10

print(id(a))
print(id(b))