# Способ зарегистрировать @singledispath только для класса , если мы добавим __init__ и создадим экземпляр в таком случае будет вызываться стандартный get_value
# с NotImplementerdError() Снизу реализация @singledispath  c классом напрямую

from functools import singledispatch

class Validator:
    @singledispatch
    def get_value(self , value):
        raise NotImplementedError()
    
    @get_value.register(int)
    def _(value: int):
        print(f'{value} - int')

    @get_value.register(str)
    def _(value: str):
        print(f'{value} - str')

if __name__ == '__main__':
    Validator.get_value(10)
    Validator.get_value('10')


# Применение для экземпляров Решение предыдущей ошибки
# class Validator:
#     def __init__(self):
#         pass

#     @singledispatch
#     def get_value(self , value):
#         raise NotImplementedError()
    
#     @get_value.register(int)
#     def _(value: int):
#         print(f'{value} - int')


#     @get_value.register(str)
#     def _(value: str):
#         print(f'{value} --- str')


# if __name__ == '__main__':
#     a = Validator()
#     a.get_value(10)
#     a.get_value('123')


# Как исправить предыдущую ошибку?

# Если нужно использовать технологию вместе с экземпляром класса , тогда данная реализация будет выглядеть следующим образом

from functools import singledispatchmethod

class Validator:
    def __init__(self):
        pass

    @singledispatchmethod
    def get_value(self , value):
        raise NotImplementedError
    
    @get_value.register
    def _(self , value:str):
        print(f'{value} -- str')

    @get_value.register
    def _(self , value: int):
        print(f"{value} -- int")


if __name__ == '__main__':
    a = Validator()
    a.get_value(10)
    a.get_value('2323')
    

# Для методов нужно применять @singledispathmethod Когда же нам не нужны экземпляры а нужно использовать статические методы без привязки к self
# тогда применяем @singledispath как в прошлом примере.