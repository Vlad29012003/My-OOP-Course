# Задание 1.1

# Изменится ли Test.version при редактировании экземпляра используя a.version = 22

class Test:
    version = 1

a = Test()
a.version = 22

print(Test.version)

# a) Да так как он является ссылкой на обьект класса 

# Correct answer
# b) Нет так как мы обновляем значение внутри пространства имен экземпляра 

# Задание 1.2

# Какое значение будет выводится после вызова print(a.version) и почему?


class Test:
    version = 1

a = Test()
Test.version = 22
print(a.version)

# Варианты ответа 
# a) 1 так как значение экземпляра сохраняется отлельно от класса 
# b) 22 так как мы изменили значение используя адрес в памяти , на который ссылается экземпляры 


# Задание 1.3
# Вопрос: Чем экземпляр отличается от класса?
# Варианты ответа 

# a) Класс создается из экземпляра
# б) Ничем
# в) Экземпляр создается из класса

# Задание 1.4
#Напишите класс, который будет содержать атрибут version, значение которого 100.
#После чего используя getattr необходимо получить атрибут version и вывести его на экран.

# class Test:
#     version = 100
# print(getattr(Test , 'version'))


# Задание 1.5 
# Создайте пустой класс без атрибутов.
# Используя setattr добавьте атрибут version с значением 100, после чего выведите его на экран
# любым способом.


# class Mazafaka:
#     pass

# b = Mazafaka()
# a = setattr(b , 'version' , 100)
# print(b.version)


# Задание 1.6
# Создайте класс, который содержит атрибут version, значение которого 100.
# Используя delattr удалите этот атрибут и выведите список всех атрибутов класса на экран.
# До удаления атрибут должен быть в списке, а после удаления его быть не должно.


class Deleter:
    version = 100

a = delattr(Deleter ,'version')
print(dir(a))


# Задание 1.7
# Вопрос: Что выводит __dict__ когда мы вызываем его обращаясь к объекту?
# Варианты ответа:

# а) Используемые функции
# б) Словарь атрибутов объекта
# в) Аргументы объекта


# Задание 1.8

# вопрос: Что если создать экземпляр из класса где используется __init__ и изменить
# значение в самом классе. Отразится ли это на данных всех экземпляров?
# Варианты ответа:

# а) Нет, так как __init__ и аргумент self создает объекты внутри своего пространства имен
# б) Да, так как они будут ссылаться на одинаковую ячейку в памяти


# Задание 1.9
# Вопрос: Для чего нужен self?
# Варианты ответа:
# а) Чтобы создать экземпляры класса
# б) Чтобы привязать данные к конкретному экземпляру класса
# в) Чтобы обращаться к глобальным атрибутам



# Задание 2.0
# Вопрос: Возможно ли использовать getter для записи данных?
# Варианты ответа:
# а) Да
# б) Нет


# Задание 2.1
# Вопрос: Чем отличается getter и setter?
# Варианты ответа:
# а) getter доступен только для чтения, setter позволяет записывать данные
# б) getter позволяет записывать данные, setter используется только для чтения


# Задание 2.2
# Вопрос: Зачем использовать Dunder методы __get__, __set__?
# Варианты ответа:
# а) Это позволяет реализовать свойства (property) более удобно
# б) С помощью __get__, __set__ мы можем обращаться к спискам используя индексы
# в) Это необходимо для сериализации данных