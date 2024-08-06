class Test:
    def __new__(cls , *args , **kwargs):
        print('Создаем экземпляр класса')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self , name):
        print('Инициализация атрибутов')
        self.name = name

a = Test.__new__(Test)

    

