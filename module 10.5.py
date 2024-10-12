import time
from multiprocessing import Pool


def read_info(name):
    """Считывает строки из файла и добавляет их в локальный список."""
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break  # Прекращаем чтение, если строк больше нет
            all_data.append(line)


if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.perf_counter()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.perf_counter() - start_time
    print(f'Линейный вызов: {linear_duration:.6f} секунд')

    # Многопроцессный вызов
    start_time = time.perf_counter()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.perf_counter() - start_time
    print(f'Многопроцессный вызов: {parallel_duration:.6f} секунд')
