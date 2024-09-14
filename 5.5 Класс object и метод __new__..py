# print(int.__mro__)
# print(object)
class User:
    __instance = None

    def __new__(cls, *args, **kwards):
        print("Я в нью")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print("Я в ините")
        self.args = args
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")
        for key, values in kwargs.items():
            setattr(self, key, values)


other = [1, 2, 3]
user = {"name": "Den", "age": 25}

user1 = User(other, user)
print(user1.args)
print(user1.name)
