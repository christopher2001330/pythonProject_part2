import random
import threading
from queue import Queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом (по умолчанию None)


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        time_to_eat = random.randint(3, 10)  # Случайное время еды
        sleep(time_to_eat)  # Гость ест
        print(f"{self.name} закончил(-а) есть за {time_to_eat} секунд")


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = list(tables)  # Список столов в кафе

    def guest_arrival(self, *guests):
        """Размещение гостей за столами или в очереди."""
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()  # Запускаем поток гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)  # Если столов нет, добавляем в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """Обслуживание гостей и освобождение столов."""
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():  # Проверяем, закончил ли гость есть
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    # Если есть гости в очереди, садим их за стол
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()  # Запускаем поток нового гостя
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            sleep(1)  # Имитируем проверку раз в 1 секунду


# Создаём столы
tables = [Table(number) for number in range(1, 6)]

# Создаём гостей
guest_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guest_names]

# Создаём кафе с указанными столами
cafe = Cafe(*tables)

# Принимаем гостей
cafe.guest_arrival(*guests)

# Обслуживаем гостей
cafe.discuss_guests()
