class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Пpивет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f"У меня день рождения, мне теперь {self.age}")

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __str__(self):
        return f"{self.name}"

    def __del__(self):
        print(f'{self.name} ушёл')



den = Human("Денис", 22)
max = Human("Макс", 22)
# if den:
#     den.say_info()
# print(len(den))
# max.birthday()
# print(den == max)
a = 6
print(den)