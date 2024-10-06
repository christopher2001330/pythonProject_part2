# Метод Lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения символов на одинаковых позициях
result = list(map(lambda f, s: f == s, first, second))

# Выводим результат
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# Метод Замыкание

def get_advanced_writer(file_name):
    # Функция для записи данных в файл
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:  # Открываем файл для добавления ('a')
            for item in data_set:
                file.write(str(item) + '\n')  # Записываем каждый элемент с новой строки

    return write_everything


# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод Call
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words  # Атрибут для хранения переданных слов

    def __call__(self):
        return choice(self.words)  # Выбираем случайное слово


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Вывод: случайное слово из списка
print(first_ball())
print(first_ball())
