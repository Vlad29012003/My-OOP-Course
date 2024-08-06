class User:
    version = 1

    def __init__(self ,name ='name1'):
        self.name = name

    @classmethod
    def set_name(cls , value):
        # cls.version = value
        return cls(value)

