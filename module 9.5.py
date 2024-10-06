# Пользовательское исключение
class StepValueError(ValueError):
    pass  # Наследуемся от ValueError, оставляем пустым


# Класс итератора
class Iterator:
    def __init__(self, start, stop, step=1):
        # Проверяем шаг на равенство 0, если 0 — выбрасываем исключение
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")

        self.start = start  # Начало диапазона
        self.stop = stop  # Конец диапазона
        self.step = step  # Шаг итерации
        self.pointer = start  # Текущая позиция (указатель)

    def __iter__(self):
        # Сбрасываем указатель на начало и возвращаем сам итератор
        self.pointer = self.start
        return self

    def __next__(self):
        # Логика для положительного шага
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration  # Останавливаем итерацию
            else:
                current_value = self.pointer
                self.pointer += self.step  # Увеличиваем на шаг
                return current_value

        # Логика для отрицательного шага
        else:
            if self.pointer < self.stop:
                raise StopIteration  # Останавливаем итерацию
            else:
                current_value = self.pointer
                self.pointer += self.step  # Уменьшаем на шаг
                return current_value


# Пример использования
try:
    # Попробуем создать итератор с шагом 0
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print(e)  # Выводим сообщение об ошибке: "Шаг не может быть равен 0"

# Примеры с другими итераторами
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Циклы для проверки итераций
for i in iter2:
    print(i, end=' ')  # Выводит: -5 -4 -3 -2 -1 0 1
print()

for i in iter3:
    print(i, end=' ')  # Выводит: 6 8 10 12 14
print()

for i in iter4:
    print(i, end=' ')  # Выводит: 5 4 3 2 1
print()

for i in iter5:
    print(i, end=' ')  # Выводит: 10 9 8 7 6 5 4 3 2 1
print()
