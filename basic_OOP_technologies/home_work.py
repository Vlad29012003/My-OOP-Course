# Вопрос: Есть ли возможность обратиться к классу напрямую, без создания экземпляра, и
# вызвать метод, который использует @staticmethod?
# Варианты ответа:

# а) да
# б) нет


# Ответ а

class MyClass:
    @staticmethod
    def my_method():
        print("Hello from static method")

MyClass.my_method() 



# Задание 1.2
# Вопрос: Позволяет ли slots ускорить выполнение программы?
# Варианты ответа:
# а) Да
# б) Нет

# Ответ а)


# Использование __slots__ в Python может ускорить выполнение программы. Это происходит потому, что __slots__ ограничивает атрибуты, которые экземпляры класса могут иметь, 
# и устраняет использование словаря (__dict__) для хранения атрибутов, что снижает накладные расходы на память и ускоряет доступ к атрибутам.


# Вопрос: Что запускается первым при создании экземпляра?
#Варианты ответа:
# а) __new__
# б) __init__
# в) __mul__

# Ответ а 



# Метод __new__ запускается первым при создании экземпляра класса. Он отвечает за создание нового объекта и возвращает его. 
# После того как объект создан, вызывается метод __init__, который инициализирует объект (например, устанавливает его атрибуты).



# Вопрос: Возможно ли с помощью __new__ создать экземпляр класса?
# Варианты ответа:
# а) Да
# б) Нет


# Метод __new__ предназначен именно для создания нового экземпляра класса. 
# Он отвечает за создание и возвращение нового объекта. Вы можете переопределить __new__, 
# чтобы изменить процесс создания экземпляра, например, возвращать экземпляр другого класса или даже предотвращать создание экземпляра.

class MyClass:
    def __new__(cls):
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("Instance initialized")

obj = MyClass()



# Вопрос: Возможно ли создать экземпляр из @classmethod
# Варианты ответа:
# а) Нет, с помощью @classmethod мы можем только создавать методы на уровне класса
# б) Да, так как он принимает объект класса

# Ответ б 

# С помощью @classmethod действительно можно создать экземпляр класса, потому что метод, помеченный как @classmethod, принимает первым аргументом сам класс (обычно обозначаемый как cls).
#  Вы можете использовать этот аргумент для создания нового экземпляра.


class MyClass:
    def __init__(self, value):
        self.value = value

    @classmethod
    def create_instance(cls, value):
        return cls(value)

obj = MyClass.create_instance(10)
print(obj.value)  # Выведет 10



class Test:
    version = 1

    def __init__(self , name):
        self.name = name

    @classmethod
    def rewrite(cls):
        cls.version = 2

a = Test(1)
b = Test(2)

a.rewrite()

print(b.version)

# б) Это возможно, в данном случае выводится 2



# Вопрос: Можно ли хранить важные данные в приватных атрибутах? Вроде логинов,
# паролей, API-токенов
# Варианты ответа:
# а) Да
# б) Нет

# ответ нет 

# Хотя приватные атрибуты в Python (обозначаемые как __attribute) делают доступ к данным сложнее,
# они не обеспечивают полной безопасности. Приватные атрибуты всё ещё могут быть доступны через обходные пути, такие как использование именования класса.



# Вопрос: Предоставляет ли инкапсуляция полное сокрытие данных, которые невозможно
# прочитать?
# Варианты ответа:
# а) Да
# б) Нет

# ответ б 

# Инкапсуляция в Python не обеспечивает полного сокрытия данных.
# Даже если атрибуты помечены как приватные (с использованием двойного подчёркивания, например, __attribute), их всё ещё можно прочитать с помощью определённых методов,
#  таких как обход через манипуляции с именами.


# Вопрос: Инкапсуляция - это ...
# Варианты ответа:
# а) Технология, которая позволяет переопределять атрибуты
# б) Технология для защиты и шифрования данных
# в) Сокрытие данных

# ответ в

# Инкапсуляция — это концепция в объектно-ориентированном программировании, которая относится к сокрытию данных и деталей реализации внутри класса.
# Она позволяет управлять доступом к данным, защищая внутреннее состояние объекта от внешнего вмешательства и нежелательных изменений.



# Вопрос: Почему при изменении любого экземпляра все данные редактируются глобально?
# Варианты ответа:
# а) Так как при создании экземпляра данные изначально ссылаются на один адрес
# б) Потому что мы используем __init__
# в) Так как они все ссылаются на одинаковую ячейку в памяти и содержат прямую ссылку на
# объект

# ответ в 

# Если несколько экземпляров класса ссылаются на один и тот же объект или изменяемую структуру данных (например, список или словарь),
# изменение одного экземпляра может повлиять на другие, потому что все они ссылаются на одну и ту же область памяти.



# Вопрос: Что позволяет сделать декоратор @singledispatch?
# Варианты ответа:
# а) Реализовать разное поведение того же метода
# б) Использовать перегрузку операторов

# Ответ а 

# Декоратор @singledispatch из модуля functools позволяет реализовать одноимённый метод, который может по-разному обрабатывать аргументы в зависимости от их типа. 
# Это позволяет создавать функции с разным поведением в зависимости от типа входного аргумента, что напоминает перегрузку функций в других языках программирования.


# Напишите класс, который будет содержать методы get_number, которые принимают int и str.
# Из метода, который принимает int, необходимо вернуть значение 100.
# Далее обращаемся к нашему классу извне, вызываем метод который возвращает int и выводим
# результат на экран.

from functools import singledispatch

class Number:
    @singledispatch
    def get_number(value):
        pass

    @get_number.register(int)
    def get_number_int(arg):
        return f'hey dude your number is integer {arg}'

    @get_number.register(str)
    def get_number_srt(arg):
        return f"hey dude your number is string"


print(Number.get_number(12))



# Теоретические вопросы и задачи

# 1. Декоратор staticmethod
# Теория

# Что такое staticmethod в Python?

# staticmethod делает метод статичным, что означает, что такой метод:

# Не имеет доступа к атрибутам экземпляра класса (self).
# Не имеет доступа к атрибутам самого класса (cls).
# Ведет себя как обычная функция, но находится внутри класса, и может быть вызван напрямую через класс или его экземпляр.

class MyClass:
    @staticmethod
    def my_static_method():
        return "Это статический метод"
    
print(MyClass.my_static_method())

a = MyClass()

print(a.my_static_method())


# Когда и почему использовать staticmethod вместо обычного метода класса?

# Логически связан с классом, но не использует и не изменяет атрибуты или методы класса и его экземпляров.
# Выполняет какую-то функцию, которая имеет смысл в контексте класса, но при этом не зависит от состояния конкретного объекта или класса в целом.

# В чем отличие между staticmethod и classmethod?

# Таким образом, staticmethod используется для функций, связанных с классом по логике, но не требующих доступа к его структуре, 
# а classmethod — когда нужен доступ к самому классу, чтобы, например, модифицировать его состояние или поведение.


# выбирайте staticmethod, когда метод не зависит от класса и его экземпляров, 
# а classmethod — когда нужно работать с классом на уровне его структуры и состояния.

# Создайте класс Calculator с методом add, который будет статическим и складывать два числа. 
# Вызовите этот метод без создания экземпляра класса.


class Calculator:
    @staticmethod
    def add(x , y):
        return x + y
    
print(Calculator.add(10 , 10))


# Добавьте в класс Utility статический метод reverse_string, который принимает строку и возвращает её в обратном порядке.

class Utility:
    @staticmethod
    def reverse_string(string):
        return string[::-1]

print(Utility.reverse_string('arthur'))


# Реализуйте класс MathOperations, который содержит статический метод для вычисления факториала числа.
import math

class MathOperations:
    @staticmethod
    def math_factorial(number):
        return math.factorial(number)


print(MathOperations.math_factorial(4))
            

# Создайте класс, который содержит статический метод для проверки, является ли переданная строка палиндромом.


class Check:
    @staticmethod
    def check_string_palindrome(value):
        a = value.lower()
        return a == a[::-1]

print(Check.check_string_palindrome('Alla'))


# 2. __slots__

# Что такое __slots__ в Python и зачем они используются?


# Обычно в Python каждый объект хранит свои атрибуты в специальном месте, называемом словарем (__dict__). 
# Этот словарь позволяет добавлять и изменять атрибуты на лету. Но за это приходится платить дополнительной памятью, так как словарь занимает много места.

# Когда ты используешь __slots__, Python не создает словарь для каждого объекта.
# Вместо этого, он резервирует фиксированное место для тех атрибутов, которые ты указал в __slots__. 
# Это экономит память, но взамен объект теряет возможность добавлять новые атрибуты, которых нет в __slots__.


# Экономия памяти: Если у тебя много объектов одного класса, и ты точно знаешь, что каждому объекту нужно всего несколько атрибутов,
#  __slots__ позволяет сэкономить память.

# Быстрее доступ к атрибутам: Из-за того, что Python не нужно управлять словарем, доступ к атрибутам происходит быстрее.



# Создайте класс Person, используя __slots__ для определения атрибутов name и age. 
# Проверьте, что попытка добавления нового атрибута вызовет ошибку.


class Person:
    __slots__ = ['name' , 'age']

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def get_data(self):
        print(self.name)
        print(self.age)


person = Person(name='jach' , age=12)

person.get_data()

try:
    person.male = 'male'
except AttributeError as e:
    print(f"ошибка {e}")
        

# Модифицируйте класс Car, чтобы он использовал __slots__ и ограничивался атрибутами make и model. 
# Попробуйте добавить атрибут color и объясните результат.


class Car:
    __slots__ = ['make' , 'model']

    def __init__(self , make , model):
        self.make = make
        self.model = model

    def get_value(self):
        print(self.make)
        print(self.model)


cars = Car(make = 'Tesla' , model= 'gtr')
cars.get_value()

try:
    cars.author = 'Author'
except AttributeError as e:
    print(e)
    




# Создайте класс Rectangle с использованием __slots__, 
# который вычисляет площадь прямоугольника. Определите атрибуты width и height и метод area.

class Rectangle:
    __slots__ = ['width' , 'height']

    def __init__(self , width ,height ):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

result = Rectangle(width= 3 , height= 2)
print(result.area())


# Реализуйте класс LibraryBook с атрибутами title, author, year, 
# используя __slots__. Напишите методы для получения информации о книге.


class LibraryBook:
    __slots__ = ['title' ,'author', 'year']

    def __init__(self ,title , author , year):
        self.title = title
        self.author = author
        self.year = year


    def get_book(self):
        return self.title , self.author , self.year
    

result = LibraryBook(title='The tru history' , author='grothery' , year=1943)

print(result.get_book())
class LibraryBook:
    __slots__ = ['title' ,'author', 'year']

    def __init__(self ,title , author , year):
        self.title = title
        self.author = author
        self.year = year


    def get_book(self):
        return self.title , self.author , self.year
    

result = LibraryBook(title='The tru history' , author='grothery' , year=1943)

print(result.get_book())



# Магический метод __new__
# Теория:
# Что делает магический метод __new__ и как он отличается от __init__?

# магический метод __new__  нужен для создание нового экземпляра класса
# Он вызывается перед __init__ и фактически создает объект, который затем передается в __init__ для инициализации.

# В каких случаях нужно переопределять __new__?


# Переопределять метод __new__ нужно в случаях, когда вам требуется особый контроль над созданием экземпляра класса. 
# Вот несколько сценариев, когда это может быть необходимо:



# Если вы работаете с неизменяемыми типами данных, такими как кортежи, строки или числа,
# и вам нужно изменить процесс создания объекта, __new__ — это единственный способ это сделать. 
# Это связано с тем, что после создания экземпляра неизменяемого объекта его атрибуты нельзя изменить через __init__.


# Синглтоны (одиночки):
# Когда вы хотите ограничить класс одним единственным экземпляром (например, класс настроек приложения),
#  __new__ используется для проверки наличия существующего экземпляра и возвращения его вместо создания нового.


# Как правильно использовать __new__ при создании синглтонов?

# Создание синглтона с помощью __new__ позволяет ограничить класс одним единственным экземпляром. 
# Это полезно, когда тебе нужно, чтобы от класса существовал только один объект, например, для хранения глобальных настроек или управления ресурсами.


class Singleton:
    _instance = None  # Статическая переменная для хранения единственного экземпляра

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Проверяем, существует ли уже экземпляр
            cls._instance = super().__new__(cls)  # Создаем новый экземпляр
        return cls._instance  # Возвращаем единственный экземпляр

    def __init__(self, value):
        self.value = value  # Инициализируем значение

# Пример использования
s1 = Singleton(10)
s2 = Singleton(20)

print(s1.value)  # 10 - значение первого созданного экземпляра
print(s2.value)  # 10 - оба экземпляра ссылаются на один и тот же объект
print(s1 is s2)  # True - оба переменных ссылаются на один и тот же объект


# Создайте класс Singleton, используя метод __new__, чтобы ограничить создание только одного экземпляра.

class Singleton:
    _instance = None

    def __new__(cls , *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self , value):
        self.value = value

object = Singleton('wdwd')
print(object.value)


# Реализуйте класс ImmutablePoint, который будет создавать неизменяемые точки (x, y).
#  Используйте метод __new__, чтобы заблокировать изменение значений после создания.

# class ImmutablePoint:
#     __slots__ = ['x' , 'y']

#     def __new__(cls ,*args, **kwargs):
#         instance = super().__new__(cls)
#         return instance

#     def __init__(self , x , y):
#         self.x = x
#         self.y = y



#     @property
#     def x(self):
#         return self._x

#     @property
#     def y(self):
#         return self._y

#     def __setattr__(self, name, value):
#         if hasattr(self, '_x') and hasattr(self, '_y'):
#             raise AttributeError("Cannot modify attributes of ImmutablePoint")
#         super().__setattr__(name, value)

#     def __delattr__(self, name):
#         raise AttributeError("Cannot delete attributes of ImmutablePoint")

# point = ImmutablePoint(10, 20)
# print(point.x)  # 10
# print(point.y)  # 20


# Создайте класс CustomObject, который при создании экземпляра возвращает строку вместо объекта.

class CustomObject:

    def __new__(cls ,attribute , *args, **kwargs):
        return str(attribute)

object = CustomObject(attribute='efefsfsfsf')
print(object)


# Реализуйте класс, который использует __new__, чтобы изменить поведение наследования от другого класса.

class BaseClass:
    def __new__(cls, *args, **kwargs):
        print(f"Creating instance of {cls.__name__}")
        return super().__new__(cls)


class DerivedClass(BaseClass):
    def __new__(cls, *args, **kwargs):
        print(f'creating instance pf {cls.__name__} from DerivedClass')
        return super().__new__(cls)
    
