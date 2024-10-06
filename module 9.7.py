# Функция для проверки простого числа
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Декоратор
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем функцию и получаем результат
        if check_prime(result):  # Проверяем, простое ли число
            print("Простое")
        else:
            print("Составное")
        return result  # Возвращаем результат функции

    return wrapper


# Функция сложения трёх чисел
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
