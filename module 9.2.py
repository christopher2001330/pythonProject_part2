# Даны списки строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, если длина строки >= 5 символов
first_result = [len(word) for word in first_strings if len(word) >= 5]

# 2. Список пар слов (кортежей) одинаковой длины, из first_strings и second_strings
second_result = [(f_word, s_word) for f_word in first_strings for s_word in second_strings if
                 len(f_word) == len(s_word)]

# 3. Словарь, где ключ - строка, значение - длина строки, только для строк чётной длины
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Пример вывода
print(first_result)
print(second_result)
print(third_result)
