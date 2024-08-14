from functools import singledispatch

class User:
    @singledispatch
    def get_children_location(value):
        print("default" , value)

    @get_children_location.register(int)
    def _(value):
        print("int", value)

    @get_children_location.register(str)
    def _(value):
        print('str' , value)


# Полиморфизм в Python - это способность объекта принимать различные формы в зависимости от контекста, в котором он используется.
# Это достигается за счет использования наследования и переопределения методов.
# Наследование позволяет переиспользовать уже готовый функционал из другого класса, а уже существующий класс, тем самым наследуя уже реализованное поведение,
# которым мы можем пользоваться из только что созданного класса. 
# Новый класс, известный как производный класс, наследует все атрибуты и методы базового класса. 
# Переопределение метода - это способность производного класса предоставить собственную реализацию метода, который уже определен в базовом классе.


# Полиморфизм позволяет рассматривать разные объекты так, как если бы они были объектами одного типа. Например, в Python вы можете использовать один и тот же метод для разных объектов, 
# даже если эти объекты имеют разные типы, если они реализуют этот метод.


class Animal:
    def __init__(self , name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Wooof"
    
class Cat(Animal):
    
    def speak(self):
        return "May May"
    

def animal_speak(animal):
    print(animal.speak())

dog = Dog('Rufus')
cat = Cat("katty")

animal_speak(dog)
animal_speak(cat)


# Полиморфизм - это мощный инструмент для создания гибкого и многократно используемого кода. 
# Его следует использовать, когда вам нужно написать код, который может работать с различными типами объектов общим способом. 
# Однако не следует злоупотреблять, так как чрезмерное использование может затруднить понимание и сопровождение кода.



# Утиная типизация - это форма динамической типизации в Python при которой тип обьекта определяется не его классом ,
# а его поведением . Это обеспечивает большую гибкость и полиморфизм вашего кода:

class Car:
    def drive(self):
        print("Driving a car")


class Bike:
    def drive(self):
        print('Riding a bike')

class Driver:
    def drive_vehicle(self , vehicle):
        vehicle.drive()


car = Car()

bike = Bike()

driver = Driver()

driver.drive_vehicle(car)
driver.drive_vehicle(bike)


# Перезагрузка операторов позволяет вам переопределить поведение встроенных операторов Python таких как  + , - , * и тд Это полезно при создании пользовательских классов
# которые ведут себя как встроенные типы :

class Vector:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def __add__(self , other):
        return Vector(self.x + other.x , self.y + other.y)
    
    def __sub__(self , other):
        return Vector(self.x - other.x , self.y - other.y)
    
    
    def __mul__(self , scalar):
        return Vector(self.x * scalar , self.y * scalar)
    
a = Vector(1 , 2)
b = Vector(2 , 2)

c = a + b
d = a - b
e = a * 2

print(c)
print(d)
print(e)


# Полиморфные функции - это функции которые могут принимать обьекты разных типов в качестве аргументов и вести себя по разному в зависимости от типа :

def get_area(shape):
    if isinstance(shape , Rectangle):
        return shape.width * shape.height
    elif isinstance(shape , Circle):
        return 3.14 * shape.radius ** 2
    else:
        raise TypeError("Unfortunatle shape type")
    
class Rectangle:
    def __init__(self ,width ,  height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self , radius):
        self.radius = radius

rect = Rectangle(2, 2)

circ = Circle(2)

get_area(rect)
get_area(circ)

        

# Пример полиморфизма с @singledispatch

from functools import singledispatch

class Rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self , radius):
        self.radius = radius

@singledispatch
def area(shape):
    raise NotImplementedError("Unsupported shape type")

@area.register

def _(rectangle: Rectangle):
    return rectangle.width * rectangle.height


@area.register
def _(circle: Circle):
    return 3.14 * (circle.radius ** 2)

rect = Rectangle(5 , 10)
print(f"The area of the rectangle is {area(rect)}")

circ = Circle(5)

print(f'The area of the circle is {area(circ)}')

# При определении @area.register , в сигнатуре функции обязательно нужно задать тип данных так как без него мы получим ошибку . 
# Поэтому мы явно указываем rectangle : Rectangle и circke: Circle.


# Используем @singledispathmethod

from functools import singledispatchmethod

# Классы для использования внутри draw который определяется в зависимости от переданного типа 

class VectoRenderer():
    def draw_circle(self , radius):
        print(f'drawing a vector circle with radius {radius}')

class RasterRenderer():
    def draw_pixelated_circle(self , radius):
        print(f'drawing a pixwlated circle with radius {radius}')


class Circle():
    def __init__(self , radius):
        self.radius = radius

    @singledispatchmethod
    def draw(self , renderer):
        raise NotImplementedError('cannot draw this shape')
    
    @draw.register
    def _(self , renderer: VectoRenderer):
        renderer.draw_circle(self.radius)

    @draw.register
    def _(self , renderer: RasterRenderer):
        renderer.draw_pixelated_circle(self.radius)


if __name__ == '__main__':
    circle = Circle(10)
    Vecto_renderer = VectoRenderer()
    raster_render = RasterRenderer()


circle.draw(Vecto_renderer)
circle.draw(raster_render)

