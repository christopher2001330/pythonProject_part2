from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            self.days += 1
            self.enemies = max(0, self.enemies - self.power)
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
            sleep(1)  # Задержка на 1 секунду

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание объектов-рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод сообщения об окончании битв
print("Все битвы закончились!")
