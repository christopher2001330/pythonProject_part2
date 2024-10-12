import time  # Для измерения времени и пауз
from threading import Thread  # Для создания потоков
from time import sleep  # Для приостановки записи


# Функция записи слов в файл с паузами
def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")


# Функция для замера времени выполнения
def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return end_time - start_time


# Последовательные вызовы функций
def sequential_execution():
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")


# Многопоточные вызовы функций
def threaded_execution():
    threads = [
        Thread(target=write_words, args=(10, "example5.txt")),
        Thread(target=write_words, args=(30, "example6.txt")),
        Thread(target=write_words, args=(200, "example7.txt")),
        Thread(target=write_words, args=(100, "example8.txt")),
    ]

    # Запуск потоков
    for thread in threads:
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()


# Измерение времени последовательного выполнения
print("Запуск последовательного выполнения:")
sequential_time = measure_time(sequential_execution)
print(f"Работа функций: {sequential_time:.6f} секунд")

# Измерение времени многопоточного выполнения
print("\nЗапуск многопоточного выполнения:")
threaded_time = measure_time(threaded_execution)
print(f"Работа потоков: {threaded_time:.6f} секунд")
