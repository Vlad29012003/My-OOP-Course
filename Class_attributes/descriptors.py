# class Data:
#     def __init__(self):
#         self.value = ""

    
#     def __get__(self , instance , owner):
#         print('__get__')
#         return self.value
    
#     def __set__(self , instance , value):
#         print('__set__')
#         self.value = value

# class User:
#     name = Data()
#     surname = Data()



# test = User()



# Пример с __get__  / __set__

# class Temperature:
#     def __init__(self , celsius):
#         self._celsius = celsius

#     def __get__(self , instance , owner):
#         return self._celsius
    
#     def __set__(self , instance , value):
#         if value < -273.15:
#             raise ValueError('damn this is a bad dude')
#         self._celsius = value


# class Celsius:
#     temperature = Temperature(0)

#     def __init__(self , temperature):
#         self.temperature = temperature 

# Temperature = это дескрипторы который используется для реализации обьекта температуры .
# Celsius - это коасс ь котоый содержит атрибут temperature Когда создается экземпляр Celsius , он устанавливает temperature атриьут к значению , переданному в конструкторе

# a = Celsius(25)

# print(a.temperature)

# a.temperature = 30
# print(a.temperature)

# a.temperature = -300



# class Point:
#     def __init__(self , x , y):
#         self.y = y
#         self.x = x

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __add__(self , other):
#         return Point(self.x + other.x , self.y + other.y)

#     def __eq__(self , other):
#         return self.x == other.x and self.y == other.y