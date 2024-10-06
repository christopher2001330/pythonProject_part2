# Заданные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка с использованием zip для разницы длин строк
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для сравнения длин строк без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример вывода
print(list(first_result))  # Преобразуем генератор в список для вывода
print(list(second_result))  # Преобразуем генератор в список для вывода
