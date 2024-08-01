class User():
    __slots__ = ['name' , 'age' , 'hh']
    def __init__(self , name = 'john' , age = 20):
        self.name = name
        self.age = age

    def get_data(self):
        print(self.name)
        print(self.age)

    @staticmethod
    def get_sum(x , y):
        print(x + y)
