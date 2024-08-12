class User:
    version = 1

    def __init__(self ,name ='name1'):
        self.name = name

    @classmethod
    def set_name(cls , value):
        # cls.version = value
        return cls(value)

import datetime

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls , name , birth_year):
        age = datetime.date.today( ).year - birth_year
        return cls(name, age)

person = Person.from_birth_year('John' , 1990)



# Зачем нужен @classmethod?

# Атрибут class_var лежит в области самого класса , в то время как self.class_var обьявляется внутри конструктора , следовательно он лежит в области экземпляра 
# . Поэтому обращаясь к class_var через обьект класса , используя @classmethod и cls мы получаем "hello" , в то время как обращение к self.class_var даст "world" 
# в виде результата

class MyClass:
        class_var = 'hello'

        def __init__(self):
                self.class_var = "world"

        @classmethod
        def get_value(cls):
            print(cls.class_var)
 
        def get_instance_value(self):
            print(self.class_var)

my_obj = MyClass()
my_obj.get_value() # hello
my_obj.get_instance_value() # world


# еще несколько примеров 


# как работает @classmethod ?

# В данном примере мы используеми метод для определения хеша , и метод , который изменяем результат возврата на уровне класса . 
# Так как экземпляр лишь ссылаются на все методы класса , то изменение метода глобально , приведет к тому , что все экземпляры получат новую ркализацию метода get_hash_sum()


class MyClass:
    def __init__(self):
        pass

    @classmethod
    def set_hash_sum(cls):
        cls.get_hash_sum = lambda self: "modify"

    def get_hash_sum(self):
        return "default"

a = MyClass()
b = MyClass()
c = MyClass()

print(a.set_hash_sum())
a.set_hash_sum() # Переопределяем метод на уровне класса
print(c.get_hash_sum()) # modify
print(a.get_hash_sum()) # modify


# Фабричные методы с @clasmethod ?

# Если вы хотите создать обьекты подклассов на основе некоторых критериев , вы можете использовать @classmethod для реализации такого функционала:

class Vehicle:
    def __init__(self , color , model):
        self.color = color
        self.model = model

    @classmethod
    def from_color(cls , color):
         if color == 'red':
              return cls(color , "Ferrari")
         elif color == 'blue':
              return cls(color , "Lamborhini")
         else:
              raise ValueError("uncnown car")
         
    def __str__(self):
        return f"{self.model} , {self.color}"
    
car1 = Vehicle.from_color('red')
car2 = Vehicle.from_color('blue')
print(car1)
print(car2)


# Наследование с @clasmethod ?
# Подкласс может использовать @classmethod для создания экземпляров самого себя:

class Animal:
    def __init__(self , name):
        self.name = name

    @classmethod
    def from_name(cls , name):
         return cls(name)
    
class Dog(Animal):
     def back(self):
          print('Woof')

dog = Dog.from_name('Fido')
dog.back()

    
          
# Реализация счетчика с @classmethod ?

class Counter:
    count = 0

    def __init__(self):
         Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
obj1 = Counter()
obj2 = Counter()

print(Counter.get_count())

# Так как @classmethod обращяется к пространству класса , а не экземпляра , то атрибут 
# count будет меняться глобально доя всех экземпляров