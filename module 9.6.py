def all_variants(text):
    length = len(text)
    # Внешний цикл: начинаем с каждого символа строки
    for i in range(length):
        # Внутренний цикл: строим подпоследовательности, начиная с i-го символа
        for j in range(i + 1, length + 1):
            # Возвращаем текущую подпоследовательность
            yield text[i:j]


# Пример использования:
a = all_variants("abc")
for i in a:
    print(i)
