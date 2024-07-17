# class TestClass:
#     def get_name(self):
#         print('Test')

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
