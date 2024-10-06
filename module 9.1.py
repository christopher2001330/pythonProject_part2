def apply_all_func(int_list, *functions):
    results = {}  # создаём пустой словарь для хранения результатов
    for func in functions:  # перебираем переданные функции
        results[func.__name__] = func(int_list)  # вызываем функцию и сохраняем результат в словарь
    return results  # возвращаем словарь с результатами


# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))  # {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))  # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
