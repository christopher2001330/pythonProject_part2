class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_info(self):
        print(f'Пpивет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age +=1
        print(f"У меня день рождения, мне теперь {self.age}")

den = Human("Денис", 22)
max = Human("Макс",22)

print(den.name, den.age)
print(max.name, max.age)
den.say_info()
max.say_info()
max.birthday()