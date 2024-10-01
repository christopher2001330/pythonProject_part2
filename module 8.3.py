# Класс исключения для VIN номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


# Класс исключения для номера автомобиля
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


# Класс автомобиля
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # Название модели автомобиля
        if self.__is_valid_vin(vin):  # Проверка корректности VIN номера
            self.__vin = vin  # Присвоение VIN номера, если он корректен
        if self.__is_valid_numbers(numbers):  # Проверка корректности номера автомобиля
            self.__numbers = numbers  # Присвоение номера, если он корректен

    # Приватный метод для проверки корректности VIN номера
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")  # Проверка на тип
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")  # Проверка на диапазон
        return True

    # Приватный метод для проверки корректности номера автомобиля
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")  # Проверка на тип
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")  # Проверка на длину строки
        return True


# Пример использования
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
