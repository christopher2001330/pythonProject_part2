def personal_sum(numbers):
    result = 0  # Сумма чисел
    incorrect_data = 0  # Счётчик некорректных данных

    for item in numbers:
        try:
            # Пробуем прибавить к результату текущее значение
            result += item
        except TypeError:
            # Если тип данных некорректен
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {item}")

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Вызываем personal_sum для подсчёта суммы чисел
        total_sum, incorrect_count = personal_sum(numbers)
        # Рассчитываем среднее арифметическое
        return total_sum / (len(numbers) - incorrect_count)
    except ZeroDivisionError:
        # Если происходит деление на 0, возвращаем 0
        return 0
    except TypeError:
        # Если передан некорректный тип данных
        print("В numbers записан некорректный тип данных")
        return None


# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка передана
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанные типы данных
print(f'Результат 3: {calculate_average(567)}')  # Передано одно число
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Только числа
