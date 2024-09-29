import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2  # Полупериметр
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Проверка кода

# Создание объектов
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Изменение цвета
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)
print(cube1.get_color())  # [222, 35, 130]

# Изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)
print(circle1.get_sides())  # [15]

# Периметр (круг)
print(len(circle1))  # 15

# Объём куба
print(cube1.get_volume())  # 216
