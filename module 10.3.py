import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Объект блокировки

    def deposit(self):
        for _ in range(100):
            amount = randint(50, 500)  # Случайная сумма для пополнения
            with self.lock:  # Автоматическая блокировка на время операции
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                # Разблокируем поток, если баланс >= 500
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            sleep(0.001)  # Имитация времени выполнения

    def take(self):
        for _ in range(100):
            amount = randint(50, 500)  # Случайная сумма для снятия
            print(f"Запрос на {amount}")
            with self.lock:  # Автоматическая блокировка на время операции
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    # Блокируем поток, если баланс недостаточен
                    self.lock.acquire()


# Создание объекта банка
bank = Bank()

# Создание потоков для пополнения и снятия
th1 = threading.Thread(target=bank.deposit)
th2 = threading.Thread(target=bank.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Итоговый вывод
print(f"Итоговый баланс: {bank.balance}")
