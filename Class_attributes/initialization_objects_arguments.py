class User:
    def __init__(self, name):
        self.name = name



class Users:
    def __init__(self , *args , **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(self.args)
        print(self.kwargs)

# In [3]: a = User(*[1,2,3], **{"name":"name1"})



class User:
    def __init__(self , name):
        self.name = name
        self.get_name()

    def get_name(self):
        print(self.name)
        


class Person:
    def __init__(self , name , age):
        self.name = name # Сохраняем эти переменные внутри экземпляра 
        self.age = age
        # Можете воспринимать это как глобальные переменные экземпляра которые вы создаете из класса 

    def get_data(self): # В каждом методе 1й аргумент это self
        # Мы можем обращяться к этим переменным откуда угодно 
        print (f'name {self.name} , age {self.age}')
        
a = Person("Alex" , 10) 
b = Person("su" , 123)